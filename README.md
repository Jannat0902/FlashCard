# FlashCard
Flashy - French Vocabulary Flashcard App

Flashy is an interactive flashcard application designed to help you learn French vocabulary efficiently. The app features a graphical interface built using Python's tkinter and allows you to focus on learning unfamiliar words while tracking your progress.

**Features**
Flashcard Interface: Displays a French word, which flips to show the English translation after a few seconds.
Progress Tracking: Known words are removed from the learning list and saved, helping you focus on words you haven't mastered yet.
CSV File Integration: Easily manage and update vocabulary words through a CSV file.

**Prerequisites**
Python 3.x
Libraries: pandas, tkinter

**Project Structure**
main.py: The main Python script that runs the app.
data/french_words.csv: The default CSV file containing French-English word pairs.
images/: Folder containing images used for flashcards and buttons.

**Customization**
To customize the vocabulary, modify data/french_words.csv. Ensure the file has two columns: French and English.
The app creates a words_to_learn.csv file to keep track of words you haven't mastered yet.
