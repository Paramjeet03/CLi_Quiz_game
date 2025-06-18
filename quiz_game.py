from colorama import init, Fore, Style
import random

init(autoreset=True)

class quiz_game:
    
    def __init__(self):
        self.result = 0
        self.data = []
        self.__file()
        self.ques_ans()

    def __file(self):
        with open(r"C:\Users\Paramjeet\OneDrive\Desktop\Quiz_app\question.txt", "r") as f:
            self.data = f.read().strip().split("\n")
            self.data = list(filter(None, self.data))

    def ques_ans(self):
        dict_1 = {}
        j = 0
        t = 0
        for i in range(len(self.data) // 6):
            dict_1[j] = self.data[t:t+6]
            j += 1
            t += 6

        def q_list():
            return [i for i in range(len(self.data) // 6)]

        def User_answer(ans):
            u_ans = input(Fore.YELLOW + "Enter your option: ").strip().upper()
            if ans == u_ans:
                print(Fore.GREEN + "Correct!\n")
                self.result += 1
            else:
                print(Fore.RED + " Wrong Answer:", u_ans)
                print(Fore.CYAN + " Correct Answer:", ans + "\n")

        def Score_board():
            print(Fore.MAGENTA + "\n*************** Score Board ***************")
            print("Total Questions:", len(dict_1))
            print("Total Correct:", Fore.GREEN + str(self.result))
            print("Total Wrong:", Fore.RED + str(len(dict_1) - self.result))

        def questions():
            list_q = q_list()
            while list_q:
                q_no = random.choice(list_q)
                for line in dict_1[q_no][:5]:
                    print(Fore.CYAN + line)

                ans = dict_1[q_no][5].split(":")[1].strip().upper()
                User_answer(ans)
                list_q.remove(q_no)

            Score_board()

        questions()

if __name__ == "__main__":
    quiz_game()