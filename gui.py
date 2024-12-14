from tkinter import *
import csv

class Gui:
    def __init__(self, window):
        """
        method to set up GUI layout
        """
        self.window = window

        self.frame_title = Frame(self.window)
        self.label_title = Label(self.window, text='Grades')
        self.label_title.pack()
        self.frame_title.pack()

        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Student Name')
        self.input_name = Entry(self.frame_name)
        self.label_name.pack(side='left')
        self.input_name.pack(padx=5, side='left')
        self.frame_name.pack(anchor='w', padx=10, pady=10)

        self.frame_attempts = Frame(self.window)
        self.label_attempts = Label(self.frame_attempts, text='Attempts')
        self.input_attempts = Entry(self.frame_attempts)
        self.label_attempts.pack(side='left')
        self.input_attempts.pack(padx=5, side='left')
        self.frame_attempts.pack(anchor='w', padx=40, pady=10)

        self.frame_text = Frame(self.window)
        self.label_text = Label(self.window, text='Please state name and number of attempts')
        self.label_text.pack()
        self.frame_text.pack()

        self.frame_score1 = Frame(self.window)
        self.label_score1 = Label(self.frame_score1, text='Score 1')
        self.input_score1 = Entry(self.frame_score1)
        self.label_score1.pack(side='left')
        self.input_score1.pack(padx=5, side='left')
        self.frame_score1.pack(anchor='w', padx=10, pady=10)

        self.frame_score2 = Frame(self.window)
        self.label_score2 = Label(self.frame_score2, text='Score 2')
        self.input_score2 = Entry(self.frame_score2)
        self.label_score2.pack(side='left')
        self.input_score2.pack(padx=5, side='left')
        self.frame_score2.pack(anchor='w', padx=10, pady=10)

        self.frame_score3 = Frame(self.window)
        self.label_score3 = Label(self.frame_score3, text='Score 3')
        self.input_score3 = Entry(self.frame_score3)
        self.label_score3.pack(side='left')
        self.input_score3.pack(padx=5, side='left')
        self.frame_score3.pack(anchor='w', padx=10, pady=10)

        self.frame_score4 = Frame(self.window)
        self.label_score4 = Label(self.frame_score4, text='Score 4')
        self.input_score4= Entry(self.frame_score4)
        self.label_score4.pack(side='left')
        self.input_score4.pack(padx=5, side='left')
        self.frame_score4.pack(anchor='w', padx=10, pady=10)

        self.label_text.config(text='Please fill out scores')
        self.input_name.delete(0, END)
        self.input_attempts.delete(0, END)

        self.frame_enter2 = Frame(self.window)
        self.button_enter2 = Button(text='Enter', command=self.submit)
        self.button_enter2.pack(pady=10)
        self.button_enter2.pack()

    def submit(self):
        """
        method to check attempts and send scores to file
        """
        name = self.input_name.get()
        attempt = self.input_attempts.get()
        score_1 = self.input_score1.get()
        score_2 = self.input_score2.get()
        score_3 = self.input_score3.get()
        score_4 = self.input_score4.get()

        if name == '' and attempt == '1':
            self.input_score1.delete(0, END)
            self.input_attempts.delete(0, END)
            self.label_text.config(text='Please state name', bg='red')
        elif name == '' and attempt == '2':
            self.input_score1.delete(0, END)
            self.input_score2.delete(0, END)
            self.input_attempts.delete(0, END)
            self.label_text.config(text='Please state name', bg='red')
        elif name == '' and attempt == '3':
            self.input_score1.delete(0, END)
            self.input_score2.delete(0, END)
            self.input_score3.delete(0, END)
            self.input_attempts.delete(0, END)
            self.label_text.config(text='Please state name', bg='red')
        elif name == '' and attempt == '4':
            self.input_score1.delete(0, END)
            self.input_score2.delete(0, END)
            self.input_score3.delete(0, END)
            self.input_score4.delete(0, END)
            self.input_attempts.delete(0, END)
            self.label_text.config(text='Please state name', bg='red')
        elif (0 > (score_1.isdigit())) or (score_1.isdigit() > 100):
            self.input_name.delete(0, END)
            self.input_attempts.delete(0, END)
            self.frame_saved = Frame(self.window)
            self.label_saved = Label(self.window, text='Grades invalid. Please resubmit')
            self.label_saved.pack()
            self.frame_saved.pack()
        elif (0 >(score_2.isdigit())) and (score_2.isdigit() > 100):
            self.input_name.delete(0, END)
            self.input_attempts.delete(0, END)
            self.frame_saved = Frame(self.window)
            self.label_saved = Label(self.window, text='Grades invalid. Please resubmit')
            self.label_saved.pack()
            self.frame_saved.pack()
        elif (0 >(score_3.isdigit())) and (score_3.isdigit() > 100):
            self.input_name.delete(0, END)
            self.input_attempts.delete(0, END)
            self.frame_saved = Frame(self.window)
            self.label_saved = Label(self.window, text='Grades invalid. Please resubmit')
            self.label_saved.pack()
            self.frame_saved.pack()
        elif (0 >(score_4.isdigit())) and (score_4.isdigit() > 100):
            self.input_name.delete(0, END)
            self.input_attempts.delete(0, END)
            self.frame_saved = Frame(self.window)
            self.label_saved = Label(self.window, text='Grades invalid. Please resubmit')
            self.label_saved.pack()
            self.frame_saved.pack()
        elif attempt == '1' and (0 < (score_1.isdigit()) <= 100) :
            self.input_name.delete(0, END)
            self.input_attempts.delete(0,END)
            self.input_score1.delete(0, END)
            self.frame_saved = Frame(self.window)
            self.label_saved = Label(self.window, text='Grades submitted!')
            self.label_saved.pack()
            self.frame_saved.pack()
            csv_file = 'grades.csv'
            with open(csv_file, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Name', 'Attempts', 'Score 1', 'Score 2', 'Score 3', 'Score 4', 'Final Score'])
                writer.writerow([name, attempt, score_1, '0', '0', '0', score_1])
        elif attempt == '2' and (0 < int(score_2) <= 100) and (0 < int(score_1) <= 100):
            self.input_name.delete(0, END)
            self.input_attempts.delete(0, END)
            self.input_score1.delete(0, END)
            self.input_score2.delete(0, END)
            self.frame_saved = Frame(self.window)
            self.label_saved = Label(self.window, text='Grades Submitted!')
            self.label_saved.pack()
            self.frame_saved.pack()
            csv_file = 'grades.csv'
            with open(csv_file, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Name', 'Attempts', 'Score 1', 'Score 2', 'Score 3', 'Score 4', 'Final Score'])
                writer.writerow([name, attempt, score_1, score_2, '0', '0', (int((int(score_1)+int(score_2))/2))])
        elif attempt == '3' and (0 < int(score_1) <= 100) and (0 < int(score_2) <= 100) and (0 < int(score_3) <= 100):
            self.input_name.delete(0, END)
            self.input_attempts.delete(0, END)
            self.input_score1.delete(0, END)
            self.input_score2.delete(0, END)
            self.input_score3.delete(0, END)
            self.frame_saved = Frame(self.window)
            self.label_saved = Label(self.window, text='Grades submitted!')
            self.label_saved.pack()
            self.frame_saved.pack()
            csv_file = 'grades.csv'
            with open(csv_file, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Name', 'Attempts', 'Score 1', 'Score 2', 'Score 3', 'Score 4', 'Final Score'])
                writer.writerow([name, attempt, score_1, score_2, score_3, '0', (int((int(score_1)+int(score_2)+int(score_3))/3))])
        elif attempt == '4' and (0 < (score_1.isdigit()) <= 100) and (0 < int(score_2) <= 100) and (0 < int(score_3) <= 100) and (0 < int(score_4) <= 100):
            self.input_name.delete(0, END)
            self.input_attempts.delete(0, END)
            self.input_score1.delete(0, END)
            self.input_score2.delete(0, END)
            self.input_score3.delete(0, END)
            self.frame_saved = Frame(self.window)
            self.label_saved = Label(self.window, text='Grades submitted!')
            self.label_saved.pack()
            self.frame_saved.pack()
            csv_file = 'grades.csv'
            with open(csv_file, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Name', 'Attempts', 'Score 1', 'Score 2', 'Score 3', 'Score 4', 'Final Score'])
                writer.writerow([name, attempt, score_1, score_2, score_3, score_4, (int((int(score_1)+int(score_2)+int(score_3)+int(score_4))/4))])