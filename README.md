# CLI Quiz Game

A simple command-line based quiz application developed in Python. This interactive game presents multiple-choice questions from a text file, accepts user input, provides immediate feedback, and displays the final score. It uses object-oriented programming and includes colored terminal output for enhanced user experience.

## Features

- Reads questions and answers from a structured text file
- Displays multiple-choice questions in the command line
- Validates user input (A/B/C/D only)
- Colored output using `colorama` to indicate correctness and errors
- Tracks and displays user score at the end
- Appends score to an external file for future reference

## Question Format

Each question in the input `.txt` file must follow this format:

```
Q: What is the capital of India?
A) Mumbai
B) Kolkata
C) New Delhi
D) Chennai
Answer: C
```

## How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/Paramjeet03/CLi_Quiz_game.git
cd CLi_Quiz_game
```

### 2. Install Dependencies
Ensure Python is installed on your system. Then install `colorama`:
```bash
pip install colorama
```

### 3. Prepare the Question File

Ensure your question file (e.g., `questions.txt`) follows the format above. Place it in the same directory or update the script path accordingly.

### 4. Run the Program

```bash
python Quiz_game.py
```

### 5. View Score Record

The score is saved in a file (e.g., `score.txt`) after the quiz ends:
```
User Name: suraj
Score: 6 / 10
```


## Code Structure

- `Quiz_game.py` - Main script that handles quiz flow
- `questions.txt` - Input file containing all the quiz questions
- `score.txt` - Output file where the user's score is logged

## Requirements

- Python 3.x
- colorama (for colored terminal output)

## License

This project is open-source and available under the [MIT License](LICENSE).
