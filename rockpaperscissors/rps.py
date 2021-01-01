import tkinter as tk

WIDTH = 600
HEIGHT = 700


def main():
    root = tk.Tk()
    root.geometry(f'{WIDTH}x{HEIGHT}')
    root.resizable(width=False, height=False)
    root.title("Rock Paper Scissors")

    # Label PLAYER
    lbl_player = tk.Label(root, text="PLAYER", font=("Arial Bold", 50))
    lbl_player.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    # Label COMPUTER
    lbl_computer = tk.Label(root, text="COMPUTER", font=("Arial Bold", 50))
    lbl_computer.place(relx=0.5, rely=0.1, anchor=tk.CENTER)


    root.mainloop()


if __name__ == '__main__':
    main()