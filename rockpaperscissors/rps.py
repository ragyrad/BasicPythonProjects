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

    # picture rock
    rock_image = open_and_resize_image("rock.png", IMAGE_WIDTH, IMAGE_HEIGHT)
    # picture paper
    paper_image = open_and_resize_image("paper.png", IMAGE_WIDTH, IMAGE_HEIGHT)
    # picture scissors
    scissors_image = open_and_resize_image("scissors.png", IMAGE_WIDTH, IMAGE_HEIGHT)
    # question mark image for computer choose
    question_mark_image = open_and_resize_image("question.png")

    gaps_between_buttons = (WIDTH - (IMAGE_WIDTH * 3)) // 5
    # Rock button
    rock_button = tk.Button(root, image=rock_image, command=lambda: print("rock_click"))
    rock_button.place(x=gaps_between_buttons, y=HEIGHT - IMAGE_HEIGHT - 120)
    # Paper button
    paper_button = tk.Button(root, image=paper_image, command=lambda: print("paper click"))
    paper_button.place(x=gaps_between_buttons * 2 + IMAGE_WIDTH, y=HEIGHT - IMAGE_HEIGHT - 120)
    # # Scissors button
    rock_button = tk.Button(root, image=scissors_image, command=lambda: print("scissors click"))
    rock_button.place(x=gaps_between_buttons * 3 + IMAGE_WIDTH * 2, y=HEIGHT - IMAGE_HEIGHT - 120)

    root.mainloop()


if __name__ == '__main__':
    main()
