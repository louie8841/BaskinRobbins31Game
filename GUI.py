import tkinter as tk
from tkinter import messagebox
from random import randint

class NumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("31 Game")
        self.root.geometry("800x600")
        self.current_number = 0
        self.username = ""
        self.player_turn = True

        self.create_start_screen()

    def create_start_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Who are you?", font=("Arial", 24)).pack(pady=40)
        self.name_entry = tk.Entry(self.root, font=("Arial", 22), width=20)
        self.name_entry.pack(pady=20)
        tk.Button(self.root, text="Start", font=("Arial", 22), width=10, command=self.get_username).pack(pady=20)

    def get_username(self):
        self.username = self.name_entry.get().strip()
        if self.username:
            self.choose_first_player()
        else:
            messagebox.showwarning("Warning", "Please enter your name.")

    def choose_first_player(self):
        self.clear_screen()

        tk.Label(self.root, text="Who will go first?", font=("Arial", 24)).pack(pady=40)
        tk.Button(self.root, text=f"{self.username} (You)", font=("Arial", 22),
                  width=15, command=lambda: self.start_game(True)).pack(pady=20)
        tk.Button(self.root, text="Computer", font=("Arial", 22),
                  width=15, command=lambda: self.start_game(False)).pack(pady=20)

    def start_game(self, user_first):
        self.current_number = 0
        self.player_turn = user_first
        self.create_game_screen()

        if not self.player_turn:
            self.root.after(1000, self.computer_turn)

    def create_game_screen(self):
        self.clear_screen()

        # 맨 위 버튼
        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.pack(side="top", pady=30)
        self.num_buttons = []
        for i in range(1, 4):
            btn = tk.Button(self.btn_frame, text=str(i), font=("Arial", 24),
                            width=6, height=2, command=lambda x=i: self.user_turn(x))
            btn.grid(row=0, column=i - 1, padx=30, pady=10)
            self.num_buttons.append(btn)

        # 사용자 외침 라벨
        self.user_said_label = tk.Label(self.root, text="", font=("Arial", 22), fg="blue")
        self.user_said_label.pack(pady=10)

        # 중앙 숫자
        self.info_label = tk.Label(self.root, text=f"Current number: {self.current_number}",
                                   font=("Arial", 32))
        self.info_label.pack(expand=True)

        # 컴퓨터 외침 라벨
        self.computer_choice_label = tk.Label(self.root, text="", font=("Arial", 22), fg="red")
        self.computer_choice_label.pack(side="bottom", pady=40)

        if not self.player_turn:
            self.disable_buttons()

    def user_turn(self, num):
        said_text = self.generate_said_text(num)
        self.user_said_label.config(text=said_text)
        self.add_number(num)
        if self.check_winner():
            return
        self.player_turn = False
        self.disable_buttons()
        self.root.after(1000, self.computer_turn)

    def computer_turn(self):
        num = randint(1, 3)
        said_text = self.generate_said_text(num)
        self.computer_choice_label.config(text=said_text)
        self.add_number(num)
        if self.check_winner():
            return
        self.player_turn = True
        self.enable_buttons()

    def generate_said_text(self, count):
        return ' '.join(f"{self.current_number + i}!" for i in range(1, count + 1))

    def add_number(self, n):
        self.current_number += n
        self.info_label.config(text=f"Current number: {self.current_number}")

    def check_winner(self):
        if self.current_number >= 31:
            if self.player_turn:
                messagebox.showinfo("Result", f"{self.username} lost")
            else:
                messagebox.showinfo("Result", f"{self.username} won!")
            self.ask_retry()
            return True
        return False

    def ask_retry(self):
        answer = messagebox.askyesno("Retry", "Do you want to play again?")
        if answer:
            self.choose_first_player()
        else:
            self.root.quit()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def disable_buttons(self):
        for btn in self.num_buttons:
            btn.config(state='disabled')

    def enable_buttons(self):
        for btn in self.num_buttons:
            btn.config(state='normal')


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    game = NumberGame(root)
    root.mainloop()
