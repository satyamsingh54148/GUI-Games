from tkinter import *
from tkinter import messagebox as mb
from timeit import default_timer as timer
import random

base = Tk()
base.geometry("800x600+350+50")
base.configure(bg="Grey")
base.title("Welcome")
window1 = Tk()
window1.geometry("800x600+350+50")
window1.configure(bg="grey")
window1.title("Typing Speed Test")
window1.withdraw()
hs = open("hs.txt", "r")
score = 0


def game():
    global score
    if score == 0:
        base.withdraw()
        score += 1
    window1.deiconify()

    def check_result(event):
        j = 0
        answer = entry.get("1.0", "end-1c")
        p_name = name.get()
        if p_name:
            pass
        else:
            p_name = "User"
        end = timer()
        time_taken = end-start
        if len(question) >= len(answer):
            for i in range(len(answer)):
                if answer[i] == question[i]:
                    j += 1
        else:
            for i in range(len(question)):
                if answer[i] == question[i]:
                    j += 1
        # wpm = (len(question) / 5) / (time_taken/60)
        wpm = round(len(question) * 60 / (5 * time_taken))
        acc = round((j / len(question)) * 100)
        total = round((wpm * acc) / 100)
        hs=open("hs.txt","r")
        if wpm < 0:
            wpm = 0
        hs.seek(0)
        hs.readline()
        hs_val = int(hs.readline())
        if total >= hs_val:
            hs.close()
            hs=open("hs.txt","w")
            hs.write(f"{p_name}\n")
            hs.write(f"{total}")
            mb.showinfo("Result", f"Congratulations {p_name}! \nYour speed was {wpm} WPM with {acc}% accuracy.\n"
                                  f"Your Final Score of {total} is the new High Score.")
        else:
            mb.showinfo("Result", f"Alas! \nYou speed was {wpm} WPM with {acc}% accuracy.\n"
                                  f"Your Final Score is {total}. \nKeep Trying {p_name}.")

    def finish():
        mb.showinfo("Exit", "Thank you for Playing.")
        hs.close()
        base.destroy()
        window1.destroy()

    def reset():
        lbl2.configure(bg="grey", fg="grey")
        game()

    words = ["Kings of Sleep is the second solo album released by bassist Stuart Hamm. It was released on June 19, 1989 on Relativity Records.",
             "The three astronauts were originally designated for the second crewed Apollo flight, and then as backups for Apollo 1.",
             "Jonathan Davis and the SFA was an American alternative metal band, formed as a side project for Korn frontman Jonathan Davis.",
             "He was a reverend. His election was disputed and whether he met the qualifications to hold office challenged.",
             "The Security Council reaffirmed the need to combat threats to international peace and security caused by terrorist acts.",
             "The Four-Headed Dragon is the 69th title of the Hardy Boys Mystery Stories, written by Franklin W. Dixon.",
             "The 1984 Kansas City Royals season was their 16th in Major League Baseball. The Royals won the American League West.",
             "The Gotha G.I was a heavy bomber used by the Imperial German Air Service during World War I."]
    random.shuffle(words)
    question = words[0]
    lbl2 = Label(window1, text=question, bg="black", fg="white", font="times 24", wraplength="550")
    lbl2.place(x=150, y=50)
    entry = Text(window1, font="times 24", wrap="word")
    entry.focus_set()
    entry.place(x=150, y=230, height=150, width=500)
    btn2 = Button(window1, text="Quit", bg="blue", fg="black", font="times 24", command=finish)
    btn2.place(x=155, y=470)
    btn3 = Button(window1, text="New Game", bg="blue", fg="black", font="times 24", command=reset)
    btn3.place(x=365, y=470)
    lbl3 = Label(window1, text="Hit Enter to submit", bg="grey", fg="black", font="aerial 24")
    lbl3.place(x=250, y=400)
    # btn4 = Button(window1, text="Submit", bg="blue", fg="black", font="times 24", command=check_result)
    # btn4.place(x=600, y=225)
    window1.bind("<Return>", check_result)
    start = timer()
    window1.mainloop()


lbl1 = Label(base, text="Want to check your Typing Speed ?", fg="red", bg="grey", font="Times 36")
lbl1.place(x=50, y=100)
lbl_name = Label(base, text="Enter Your Name : ", bg="grey", fg="cyan", font="times 28")
lbl_name.place(x=50, y=175)
name = Entry(base, justify="center", fg="black", font="aerial 28")
name.place(x=350, y=175)
btn1 = Button(base, text="Let's Start", font="Times 28", bg="blue", width="20", height="2", command=game,
              activebackground="purple")
btn1.place(x=200, y=250)
hs_lbl = Label(base, text="High Score", bg="grey", fg="green", font="times 36")
hs_lbl.place(x=300, y=400)
hs_name = hs.readline().rstrip()
hs_value = int(hs.readline())
h_score = Label(base, text=f"{hs_name} : {hs_value} WPM", fg="black", bg="grey", font="times 26")
h_score.place(x=300, y=475)
base.mainloop()

"""
To DO


change the colour scheme after consultation"""