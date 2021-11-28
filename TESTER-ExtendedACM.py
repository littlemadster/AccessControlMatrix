'''
TESTER-ACM-CLASS
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


    '''
    Create the DAC
    '''
    ACM.createObj("Manuscript1")

    ACM.createSub("ADMIN1")
    ACM.createSub("Author1")
    ACM.createSub("Editor1")
    ACM.createSub("AssocEditors1")
    ACM.createSub("GuestEditor1")
    ACM.createSub("Reviewers1")

    
    
    #initalize the rules
    ACM.initRules()

    #grant rights so some of the subjects and objects
    ACM.grant("Root", "Root", "own*")
    ACM.grant("Root", "Root", "control*")
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
    ACM.transfer("Root", "Root","own*","Author","Manuscript","own")
    ACM.transfer("Root","Root","control*", "Author","Manuscript","control")
    ACM.transfer("Root","Root","control*", "Editor","Recomendations","control")


    

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

    '''
    EXTENDED ACM CODE.
    
    '''

    ACM.grant("Author1", "Credentials","submit")
    ACM.grant("Author1", "Manuscript1","submit")
    ACM.grant("Author1", "Manuscript1","own")
   
    ACM.grant("Editor1","Manuscript1","accept")
    ACM.grant("Editor1","Manuscript1","review")
    ACM.grant("Editor1","Manuscript1","consider")
    ACM.grant("Editor1","Manuscript1","score")
    ACM.grant("Editor1","Manuscript1","reccomend")
    ACM.grant("Editor1","AssocEditors1","invites*")
    ACM.grant("Editor1","GuestEditor1","invites*")

    
    ACM.grant("AssocEditors1","Invitation","accept")
    ACM.grant("AssocEditors1","Manuscript1","review")
    ACM.grant("AssocEditors1","Manuscript1","consider")
    ACM.grant("AssocEditors1","Manuscript1","score")
    ACM.grant("AssocEditors1","Manuscript1","reccomend")
    ACM.grant("AssocEditors1","Reviewers","invite")


    ACM.grant("GuestEditor1","Reviewers","invite")
    ACM.grant("GuestEditor1","Invitation","accept")
    ACM.grant("GuestEditor1","Manuscript1","review")
    ACM.grant("GuestEditor1","Manuscript1","score")
    ACM.grant("GuestEditor1","Manuscript1","reccomend")

    '''
    REMOVING THE ROOT USER
    '''
    ACM.delSub("Root")



    #prints the window for the ACM
    ACM.printWindow(window)
    

    window.mainloop()

main()
