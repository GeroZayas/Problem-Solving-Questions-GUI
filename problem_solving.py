import PySimpleGUI as sg

# Define the layout
layout = [
    [sg.Text("PROBLEM-SOLVING QUESTIONS from Tony Robbins")],
    [sg.Text("1. What is great about this problem?")],
    [sg.Multiline(size=(None, 2), key="Q1")],  # Two lines high input box
    [sg.Text("2. What is not perfect yet?")],
    [sg.Multiline(size=(None, 2), key="Q2")],
    [sg.Text("3. What am I willing to do to make it the way I want it?")],
    [sg.Multiline(size=(None, 2), key="Q3")],
    [sg.Text("4. What am I willing to no longer do to make it the way I want it?")],
    [sg.Multiline(size=(None, 2), key="Q4")],
    [
        sg.Text(
            "5. How can I enjoy the process while I do what is necessary to make it the way I want it?"
        )
    ],
    [sg.Multiline(size=(None, 2), key="Q5")],
    [sg.Button("Submit"), sg.Button("Save Responses")],
]

# Create the Window
window = sg.Window("Survey Application", layout)
responses = {}

# Event loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == "Submit":
        responses = values
        sg.popup("Responses recorded!")
    elif event == "Save Responses":
        with open("responses.txt", "w") as file:
            for question, response in responses.items():
                file.write(
                    f"{question}: {response.strip()}\n"
                )  # strip to remove extra newlines
        sg.popup("Responses saved to responses.txt!")

window.close()
