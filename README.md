# Problem-Solving Questions Application

This application is designed to facilitate structured problem-solving sessions inspired by Tony Robbins' approach. It provides a simple interface where users can input problems and associated questions, then save their responses for later review.

<img width="600" title="app screenshot" alt="app screenshot" src="./assets/Screenshot Problem Solving Questions GUI.png">

## Features

- **Color Scheme**: The application uses a dark theme for better readability.
- **Fixed Window Size**: Ensures consistency across different devices.
- **Non-Resizable Window**: Prevents accidental resizing during use.
- **Question-Based Approach**: Guides users through a systematic problem-solving process.
- **Response Saving**: Allows users to save their responses to a text file for future reference.

## Installation and Setup

To get started with the Problem-Solving Questions Application, follow these steps:

### Prerequisites

Ensure you have Python installed on your system. You can download Python from the official website (https://www.python.org/downloads/).

### Installing Dependencies

This application does not require any external libraries beyond those included in the standard Python distribution. However, ensure you have the latest version of Python installed to avoid compatibility issues.

### Running the Application

1. Clone the repository to your local machine using Git. If you don't have Git installed, you can download it from https://git-scm.com/downloads.

```bash
git clone https://github.com/GeroZayas/Problem-Solving-Questions-GUI.git
```

2. Navigate to the cloned directory:

```bash
cd Problem-Solving-Questions-GUI
```

3. Run the application using Python:

```bash
python main_tkinter.py
```

The application should now launch, allowing you to start solving problems according to the Tony Robbins method.

### Troubleshooting

If you encounter any issues running the application, please check the following:

- Ensure Python is correctly installed and added to your PATH environment variable.
- Verify that you are running the latest version of Python.
- Check the console output for error messages, which may indicate missing dependencies or other issues.

## Usage

1. Open the application.
2. Enter the problem statement in the designated text field.
3. Answer the subsequent questions using the provided text fields.
4. Click the "Save Responses" button to save your answers to a `.txt` file.
5. Use the "Close" button to exit the application.

## Code Structure

The application is built using `tkinter`, Python's standard GUI library. Key components include:

- A main window configured with a specific color scheme and geometry.
- Labels and text fields for entering and displaying problem statements and questions.
- Buttons for saving responses and closing the application.
- Functions to handle button clicks and manage the application logic.

## Contributing

Contributions to improve the functionality, design, or documentation are welcome. Please submit pull requests or issues via GitHub.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
