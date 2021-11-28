'''
TESTER-ACM
Authors: Madeleine Sirok, Valentina Colorado
Course: CIS4367.01
Date Last Modified: 11/28/21
Description: This class is to test the functions of the ACM to make sure they work. This is a generic ACM
** WHEN RUNNING WINDOW MIGHT NOT OPEN COMPLETELY. YOU NEED TO MAXIMIZE THE WINDOW

'''
from ACMclassFinal import *
from tkinter import *
import tkinter as tk
def main():
     
    def close():
        window.destroy()

    window = Tk()
    window.title("ACM")
    window.geometry('900x400')

    Button(window, text="Quit", command=close).grid(row=0, column=0)
    #createRoot
    ACM.createSub("Root")

    #create objects
    ACM.createObj("Manuscript")
    ACM.createObj("Scores")
    ACM.createObj("Reviews")
    ACM.createObj("Recomendations")
    ACM.createObj("Invitation")
    ACM.createObj("Credentials")    
    #create subjects
    ACM.createSub("ADMIN")
    ACM.createSub("Author")
    ACM.createSub("Editor")
    ACM.createSub("AssocEditors")
    ACM.createSub("GuestEditor")
    ACM.createSub("Reviewers")

    
    #initalize the rules
    ACM.initRules()

    #grant rights so some of the subjects and objects
    ACM.grant("Root", "Root", "control")
    ACM.grant("Root", "Root", "accept")
    ACM.grant("Root", "Root", "reject")
    ACM.grant("Root", "Root", "invite*")
    ACM.grant("Root", "Root", "submit")
    ACM.grant("Root", "Root", "view")
    ACM.grant("Root", "Root", "edit")
    ACM.grant("Root", "Root", "manage")
    ACM.grant("Root", "Root", "qualitycontrol")
    ACM.grant("Root", "Root", "receive")



    #grant rights so some of the subjects and objects
    ACM.grant("Root", "Author", "own")
    ACM.grant("Root", "Author", "control")
    ACM.grant("Root", "Editor", "own")
    ACM.grant("Root", "Editor", "control")
    ACM.grant("Root", "AssocEditors", "own")
    ACM.grant("Root", "AssocEditors", "control")
    ACM.grant("Root", "GuestEditor", "own")
    ACM.grant("Root", "GuestEditor", "control")
    ACM.grant("Root", "Reviewers", "own")
    ACM.grant("Root", "Reviewers", "control")
    ACM.grant("Root", "ADMIN", "own")
    ACM.grant("Root", "ADMIN", "control")
    ACM.grant("Root", "Manuscript", "own")
    ACM.grant("Root", "Scores", "own")
    ACM.grant("Root", "Reviews", "own")
    ACM.grant("Root", "Recomendations", "own")
    ACM.grant("Root", "Invitation", "own")
    ACM.grant("Root", "Credentials", "own")

    ACM.grant("Author","Manuscript","submit")
    ACM.grant("Author", "Credentials","submit")

    ACM.grant("Editor","AssocEditors","invite*")
    ACM.grant("Editor","GuestEditor","invite*")
    ACM.grant("Editor","Manuscript","receive")

    ACM.grant("AssocEditors","Reviewers","invite")
    ACM.grant("AssocEditors","Manuscript","review")
    ACM.grant("AssocEditors","Manuscript","accept")
    ACM.grant("AssocEditors","Manuscript","reject")
    ACM.grant("AssocEditors","Manuscript","manage")
    ACM.grant("AssocEditors","Manuscript","qualitycontrol")
    ACM.grant("AssocEditors","Scores","consider")
    ACM.grant("AssocEditors","Reviews","consider")
    ACM.grant("AssocEditors","Recomendations","consider")
    ACM.grant("AssocEditors","Invitation","accept")

    ACM.grant("GuestEditor","Reviewers","invite")
    ACM.grant("GuestEditor","Manuscript","manage")
    ACM.grant("GuestEditor","Manuscript","qualitycontrol")
    ACM.grant("GuestEditor","Invitation","accept")


    ACM.grant("Reviewers", "Manuscript", "review")
    ACM.grant("Reviewers", "Scores", "submit")
    ACM.grant("Reviewers", "Reviews", "submit")
    ACM.grant("Reviewers", "Recomendations", "submit")
    ACM.grant("Reviewers", "Invitation", "accept")

    ACM.grant("ADMIN", "Manuscript", "view")
    ACM.grant("ADMIN", "Scores", "view")
    ACM.grant("ADMIN", "Reviews", "view")
    ACM.grant("ADMIN", "Recomendations", "view")
    ACM.grant("ADMIN", "Invitation", "view")
    ACM.grant("ADMIN", "Credentials", "view")

    #prints the window for the ACM
    ACM.printWindow(window)
    

    window.mainloop()

main()
