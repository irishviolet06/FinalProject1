from tkinter import *
from gui import *
import csv

def main():
    window = Tk()
    window.title('Final Project 1')
    window.geometry('539x434')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()