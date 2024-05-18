import tkinter as tk
from tkinter import filedialog, messagebox

# Color scheme
colors = {
    "text": "#FEE715",  # Yellow
    "background": "#101820",  # Charcoal
    "close_button": ("white", "red"),  # Text, Background for Close button
}

# Create the Tkinter window
window = tk.Tk()
window.title("Problem-Solving Questions - Tony Robbins")
window.configure(bg=colors["background"])
window.geometry("910x855")  # Fixed window size
window.resizable(False, False)  # Disable window resizing


# Define font style
font_style = ("Liberation", 14)

questions = [
    "1. What is great about this problem?",
    "2. What is not perfect yet?",
    "3. What am I willing to do to make it the way I want it?",
    "4. What am I willing to no longer do to make it the way I want it?",
    "5. How can I enjoy the process while I do what is necessary to make it the way I want it?",
]

# Problem entry
problem_label = tk.Label(
    window,
    text="What is the problem?",
    font=("Liberation", 16),
    fg="darkred",
    bg="white",
)
problem_label.grid(row=0, column=0, padx=5, pady=5, columnspan=1)
problem_entry = tk.Text(window, height=2, font=font_style)
problem_entry.grid(row=1, column=0, padx=5, pady=5, columnspan=1, sticky="ew")


# Questions entries
questions_text_entries = []
for i, question in enumerate(questions, 1):
    question_label = tk.Label(
        window,
        text=question,
        font=font_style,
        fg=colors["text"],
        bg=colors["background"],
    )
    question_label.grid(row=i * 2, column=0, padx=5, pady=5, sticky="w")
    question_text_entry = tk.Text(window, height=3, font=font_style)
    question_text_entry.grid(row=i * 2 + 1, column=0, padx=5, pady=5, sticky="ew")
    questions_text_entries.append(question_text_entry)


# Function to handle Save Responses button click
def save_responses():
    responses = {}
    responses["Problem"] = problem_entry.get("1.0", "end-1c")
    for i, question in enumerate(questions, 1):
        responses[f"Q{i}"] = questions_text_entries[i - 1].get("1.0", "end-1c")
    save_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")],
        title="Save Responses",
    )
    separator = "-" * 70
    if save_path:
        with open(save_path, "w") as file:
            file.write(f"What is the problem?\n{separator}\n{responses['Problem']}\n\n")
            for i, question in enumerate(questions, 1):
                response = responses.get(f"Q{i}", "").strip()
                file.write(f"{question}\n{separator}\n{response}\n\n")
        messagebox.showinfo("Info", f"Responses saved to {save_path}")


# Save Responses button
save_responses_button = tk.Button(
    window, text="Save Responses", font=font_style, command=save_responses
)
save_responses_button.grid(
    row=len(questions) * 2 + 2,
    column=0,
    padx=5,
    pady=5,
    columnspan=1,
)

# Close button
close_button = tk.Button(
    window,
    text="Close",
    font=font_style,
    fg=colors["close_button"][0],
    bg=colors["close_button"][1],
    command=window.quit,
)
close_button.grid(row=len(questions) * 2 + 3, column=0, padx=5, pady=5)

# Centering all widgets
for child in window.winfo_children():
    child.grid_configure(padx=10, pady=4)

window.mainloop()
