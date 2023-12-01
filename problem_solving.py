import PySimpleGUI as sg

# Color scheme
colors = {
    "text": "#FEE715",  # Yellow
    "background": "#101820",  # Charcoal
    "close_button": ("white", "red"),  # Text, Background for Close button
}

# Define the layout with updated fonts and colors
sg.theme_background_color(colors["background"])
sg.theme_text_element_background_color(colors["background"])
sg.theme_button_color((colors["text"], colors["background"]))

font_style = ("Liberation", 14)  # Example font

questions = [
    "1. What is great about this problem?",
    "2. What is not perfect yet?",
    "3. What am I willing to do to make it the way I want it?",
    "4. What am I willing to no longer do to make it the way I want it?",
    "5. How can I enjoy the process while I do what is necessary to make it the way I want it?",
]

layout = [
    [
        sg.Text(
            "PROBLEM-SOLVING QUESTIONS from Tony Robbins",
            font=("Liberation", 20),
            text_color=colors["text"],
        ),
    ],
    [
        sg.Text(
            "What is the problem?",
            font=font_style,
            text_color=colors["text"],
        ),
        sg.Input(
            border_width=3,
            text_color="darkred",
            default_text="The problem is ...",
            size=(100, 1),
            key="Problem",
        ),
    ],
    [sg.HorizontalSeparator()],
]
for i, question in enumerate(questions, 1):
    layout += [
        [sg.Text(question, font=font_style, text_color=colors["text"])],
        [sg.Multiline(size=(None, 2), key=f"Q{i}", font=font_style)],
    ]
layout += [
    [
        sg.Column(
            [
                [
                    sg.Button("Submit", font=font_style),
                    sg.Button("Save Responses", font=font_style),
                    sg.Button(
                        "Close", font=font_style, button_color=colors["close_button"]
                    ),
                ]
            ],
            justification="right",
        )
    ]
]

# Create the Window
window = sg.Window("Problem-Solving Questions - Tony Robbins", layout)

# Event loop
while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Close"):
        break
    elif event == "Submit":
        responses = values
        sg.popup("Responses recorded!", font=font_style)
    elif event == "Save Responses":
        save_path = sg.popup_get_file(
            "Save Responses",
            save_as=True,
            no_window=True,
            file_types=(("Text Files", "*.txt"),),
            default_extension=".txt",
        )
        if save_path:
            with open(save_path, "w") as file:
                file.write(f"What is the problem?\n{values['Problem']}\n\n")
                for i, question in enumerate(questions, 1):
                    response = values.get(f"Q{i}", "").strip()
                    file.write(f"{question}\n{response}\n\n")
            sg.popup("Responses saved to " + save_path, font=font_style)

window.close()
