from tkinter import *
import numpy as np
import pickle
from movie_model import get_recommendations

model = pickle.load(open('trial_model.sav', 'rb'))

def chatbot_response(msg):
    res = model.predict([msg])
    if res[0] == 0:
        return 'We apologize for the inconvinience, you can contact customer support for further details at 20198198/customersupport@gmail.com'
    else:
        return 'Glad you liked it! You might also like: ' + ', '.join([recc for recc in movie_predictions.head(3)])

# Creating GUI with tkinter
movie_counter = 0
movie_predictions = ''

def send():
    global movie_counter
    global movie_predictions

    if movie_counter == 0:
        movie = EntryBox.get("1.0", 'end-1c').strip()
        EntryBox.delete("0.0", END)
        movie_predictions = get_recommendations(movie)

        if movie != '':
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "You: " + movie + '\n\n')
            ChatLog.config(foreground="#442265", font=("Verdana", 12))

            ChatLog.insert(END, 'Bot: Did you like ' + movie +
                           '? We would love to hear your thoughts!\n\n')
            movie_counter = movie_counter + 1

    else:
        msg = EntryBox.get("1.0", 'end-1c').strip()
        EntryBox.delete("0.0", END)

        if msg != '':
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "You: " + msg + '\n\n')
            ChatLog.config(foreground="#442265", font=("Verdana", 12))

            res = chatbot_response(msg)
            ChatLog.insert(END, "Bot: " + res + '\n\n')

            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)

base = Tk()
base.title("FeedbackBot")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

# Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)
ChatLog.config(state=NORMAL)
ChatLog.insert(END, 'Bot: Hi, What movie did you watch?\n\n')

ChatLog.config(state=DISABLED)

# Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="arrow")
ChatLog['yscrollcommand'] = scrollbar.set

# Create Button to send message
SendButton = Button(base, font=("Verdana", 12, 'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff',
                    command=send)

# Create the box to enter message
EntryBox = Text(base, bd=0, bg="white", width="29", height="5", font="Arial")

# Place all components on the screen
scrollbar.place(x=376, y=6, height=386)
ChatLog.place(x=5, y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=2, y=401, height=90)

base.mainloop()
