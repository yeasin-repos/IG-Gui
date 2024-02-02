from instabot import Bot
import tkinter as tk
from tkinter import ttk

class InstagramBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Instagram Bot")
        self.root.geometry("300x200")
        self.root.config(bg="#bb9cc0")

        # Style
        style = ttk.Style()
        style.configure("TLabel", background="#bb9cc0", font=("Arial", 12))
        style.configure("TEntry", background="#bb9cc0", font=("Arial", 12))
        style.configure("TButton", background="#bb9cc0", foreground="black", font=("Arial", 12))

        self.label_username = ttk.Label(root, text="Username:")
        self.label_username.pack(pady=5)

        self.entry_username = ttk.Entry(root)
        self.entry_username.pack(pady=5, padx=10, ipadx=10)

        self.label_password = ttk.Label(root, text="Password:")
        self.label_password.pack(pady=5)

        self.entry_password = ttk.Entry(root, show="*")
        self.entry_password.pack(pady=5, padx=10, ipadx=10)

        self.btn_login = ttk.Button(root, text="Login", command=self.login)
        self.btn_login.pack(pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.pack(pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        bot = Bot()
        bot.login(username=username, password=password)

        if bot.api.is_logged_in:
            followers = bot.get_user_followers(username)
            followings = bot.get_user_following(username)
            total_posts = bot.get_total_user_medias(username)

            result_text = f"Followers: {len(followers)}\n"
            result_text += f"Followings: {len(followings)}\n"
            result_text += f"Total Posts: {total_posts}"

            self.result_label.config(text=result_text)
        else:
            self.result_label.config(text="Login failed. Please check your credentials.")

if __name__ == "__main__":
    root = tk.Tk()
    app = InstagramBotGUI(root)
    root.mainloop()
