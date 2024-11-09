import random
from tkinter import *
import pandas

# Load data from CSV
try:
    data = pandas.read_csv("data/french_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn= original_data.to_dict(orient="records")
else:
   to_learn = data.to_dict(orient="records")

    # Constants
BACKGROUND_COLOR = "#B1DDC6"

# Initialize global variables
current_card = {}

# Function to display the next flashcard
def next_card():
    global current_card
    current_card = random.choice(to_learn)
    # Update the canvas text items with the French word
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_image, image=card_front_img)
    window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(card_image, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index= False)
    next_card()

# Set up the main window
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(3000,func=flip_card)

# Create the canvas for card display
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
card_back_img = PhotoImage(file="images/card_back.png")

# Text on the flashcard
card_title = canvas.create_text(400, 150, text='Title', font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text='Word', font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Load images for buttons
cross_image = PhotoImage(file="images/wrong.png")
check_image = PhotoImage(file="images/right.png")

# Create buttons for wrong and right choices
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# Display the first card initially
next_card()

# Start the main loop
window.mainloop()
