from colorama import init, Fore  # Import for colored text output
import random  # For randomizing question order

# Initialize colorama for automatic reset after each print
init(autoreset=True)

class QuizGame:
    def __init__(self):
        self.result = 0              # To store the number of correct answers
        self.data = []              # To store raw question data from file
        self.username = ""          # To store user's name
        self.questions_dict = {}    # Dictionary to store questions and options

    def start(self):
        """Main entry point to start the quiz."""
        self.get_user_info()
        self.load_questions()
        self.ask_questions()
        self.show_scoreboard()
        self.save_result()

    def get_user_info(self):
        """Takes username input from user."""
        self.username = input(Fore.CYAN + "Enter your name: \n")

    def load_questions(self):
        """Loads and processes questions from a text file."""
        with open(r"C:\Users\Paramjeet\OneDrive\Desktop\Quiz_app\question.txt", "r") as f:
            lines = f.read().strip().split("\n")
            lines = list(filter(None, lines))  # Remove any blank lines

        # Group every 6 lines as one question block (5 lines for question + 1 for answer)
        for i in range(len(lines) // 6):
            self.questions_dict[i] = lines[i * 6:(i + 1) * 6]

    def ask_questions(self):
        """Asks questions to the user in randomized order."""
        q_indices = list(self.questions_dict.keys())
        random.shuffle(q_indices)  # Shuffle the question indices for randomness

        for q_no in q_indices:
            for line in self.questions_dict[q_no][:5]:
                print(Fore.CYAN + line)  # Print question and options

            # Extract correct answer from last line (format: Answer: A)
            correct_ans = self.questions_dict[q_no][5].split(":")[1].strip().upper()

            # Take user input
            user_ans = input(Fore.YELLOW + "Enter your option (A/B/C/D): ").strip().upper()

            # Validate user input
            while user_ans not in ['A', 'B', 'C', 'D']:
                user_ans = input(Fore.RED + "Invalid input. Enter A, B, C, or D: ").strip().upper()

            # Check the answer
            self.check_answer(user_ans, correct_ans)

    def check_answer(self, user_ans, correct_ans):
        """Compares user input to the correct answer and updates score."""
        if user_ans == correct_ans:
            print(Fore.GREEN + "Correct!\n")
            self.result += 1
        else:
            print(Fore.RED + f"Wrong Answer: {user_ans}")
            print(Fore.CYAN + f"Correct Answer: {correct_ans}\n")

    def show_scoreboard(self):
        """Displays the final score after the quiz ends."""
        total = len(self.questions_dict)
        print(Fore.MAGENTA + "\n*************** Score Board ***************")
        print("User:", Fore.CYAN + self.username)
        print("Total Questions:", total)
        print("Total Correct:", Fore.GREEN + str(self.result))
        print("Total Wrong:", Fore.RED + str(total - self.result))

    def save_result(self):
        """Appends the username and result to a file."""
        with open(r"C:\Users\Paramjeet\OneDrive\Desktop\Quiz_app\result.txt", "a") as wr:
            wr.write(f"User Name: {self.username}\n")
            wr.write(f"Score: {self.result} / {len(self.questions_dict)}\n")
            wr.write("-" * 40 + "\n")  # Separator for readability

# Run the quiz game when script is executed directly
if __name__ == "__main__":
    QuizGame().start()
