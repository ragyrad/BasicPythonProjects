import tkinter as tk
from PIL import Image, ImageTk  # pip install pillow


WIDTH = 600
HEIGHT = 700
IMAGE_WIDTH = 180
IMAGE_HEIGHT = 180


def open_and_resize_image(image_path, width, height):
    """ Opens and resizes the picture. Returns the modified image

    :param image_path: image to be changed and opened
    :param width: final image width
    :param height: final image height
    :return: final image
    """
    image = Image.open(image_path)
    resized_image = image.resize((width, height))
    return ImageTk.PhotoImage(resized_image)


def make_choice(choice):
    """The function return the player choice and and highlights the pressed image

    :param choice:
    :return: player choice
    """
    # Disable all buttons
    for button in rock_button, paper_button, scissors_button:
        button.configure(state=tk.DISABLED)
    # FIXME add the images
    # if choice == "rock":
    #     rock_button.configure(image="")
    # elif choice == "paper":
    #     paper_button.configure(image="")
    # elif choice == "scissors":
    #     scissors_button.configure(image="")

    return choice


if __name__ == '__main__':
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

    # picture rock
    rock_image = open_and_resize_image("rock.png", IMAGE_WIDTH, IMAGE_HEIGHT)
    # picture paper
    paper_image = open_and_resize_image("paper.png", IMAGE_WIDTH, IMAGE_HEIGHT)  # FIXME change images
    # picture scissors
    scissors_image = open_and_resize_image("scissors.png", IMAGE_WIDTH, IMAGE_HEIGHT)
    # question mark image for computer choose
    question_mark_image = open_and_resize_image("question.png", IMAGE_WIDTH, IMAGE_HEIGHT)

    gaps_between_buttons = (WIDTH - (IMAGE_WIDTH * 3)) // 4
    # Rock button
    rock_button = tk.Button(root, text="rock", image=rock_image, state=tk.DISABLED,
                            command=lambda choice="rock": make_choice(choice))
    rock_button.place(x=gaps_between_buttons, y=HEIGHT - IMAGE_HEIGHT - 120)
    # Paper button
    paper_button = tk.Button(root, text="paper", image=paper_image, state=tk.DISABLED,
                             command=lambda choice="paper": make_choice(choice))
    paper_button.place(x=gaps_between_buttons * 2 + IMAGE_WIDTH, y=HEIGHT - IMAGE_HEIGHT - 120)
    # Scissors button
    scissors_button = tk.Button(root, text="scissors", image=scissors_image, state=tk.DISABLED,
                                command=lambda choice="scissors": make_choice(choice))
    scissors_button.place(x=WIDTH - IMAGE_WIDTH - gaps_between_buttons, y=HEIGHT - IMAGE_HEIGHT - 120)
    # Computer select image
    question_mark = tk.Label(root, image=question_mark_image, borderwidth=2, relief="solid")
    question_mark.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    # The inscription will offer to make a choice, as well as notify about victory or loss.
    main_lbl = tk.Label(root, text="Choose rock paper or scissors", font=("Arial Bold", 18))
    main_lbl.place(relx=0.5, rely=0.53, anchor=tk.CENTER)

    # Start game button
    play_button = tk.Button(root, text="START GAME", font=("Arial Bold", 16))
    play_button.place(relx=0.5, rely=0.47, anchor=tk.CENTER)
    play_button.bind('<Button-1>', start_game)

    root.mainloop()
