import PySimpleGUI as sg

# Define the questions
questions = [
    "1. What is great about this problem?",
    "2. What is not perfect yet?",
    "3. What am I willing to do to make it the way I want it?",
    "4. What am I willing to no longer do to make it the way I want it?",
    "5. How can I enjoy the process while I do what is necessary to make it the way I want it?",
]

# Define the layout
layout = [[sg.Text("PROBLEM-SOLVING QUESTIONS from Tony Robbins")]]
for i, question in enumerate(questions, 1):
    layout += [[sg.Text(question)], [sg.Multiline(size=(None, 2), key=f"Q{i}")]]
layout += [[sg.Button("Submit"), sg.Button("Save Responses")]]

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
            for i, question in enumerate(questions, 1):
                response = responses.get(f"Q{i}", "").strip()
                file.write(f"{question}\n{response}\n\n")
        sg.popup("Responses saved to responses.txt!")

window.close()
