'''
TESTER-ACM
Authors: Madeleine Sirok, Valentina Colorado
Course: CIS4367.01
Date Last Modified: 11/28/21
Description: This class is to test and create the base ACM for the given Editorial Management system
'''

from ACMclassFinal import *
def main():
     
    def close():
        window.destroy()

    window = Tk()
    window.title("ACM")
    window.geometry('900x400')

    Button(window, text="Quit", command=close).grid(row=0, column=0)

    #create objects
    ACM.createObj("Obj1")
    ACM.createObj("Obj2")
    ACM.createObj("Obj3")
    ACM.createObj("Obj4")
    
    #create subjects
    ACM.createSub("Sub1")
    ACM.createSub("Sub2")
    ACM.createSub("Sub3")
    ACM.createSub("Sub4")

    
    #initalize the rules
    ACM.initRules()

    #grant rights so some of the subjects and objects
    ACM.grant("Sub1", "Obj1", "own")
    ACM.grant("Sub1", "Obj1", "write")
  
    ACM.grant("Sub2", "Obj2", "write")
    ACM.grant("Sub2", "Obj2", "control")
    ACM.grant("Sub2", "Obj1", "write")


    ACM.grant("Sub3", "Sub1", "view")
    ACM.grant("Sub4", "Sub2", "control")

    #removes rights from certain subjects and objects
    ACM.removeRight("Sub1", "Obj1", "control")
    ACM.removeRight("Sub1", "Obj1", "own")
    ACM.removeRight("Sub3", "Sub1", "view")

    #transfers rights
    ACM.transfer("Sub3", "Obj4", "read*", "Sub1", "Obj2", "read")

    #read all rights
    ACM.readAll()

    #read specific rights from specified subject and object
    ACM.read("Sub1", "Obj1")

    #checks to see if inputed subject and object have "own" or "control" rights
    ACM.authorize("Sub1","Sub1")
    ACM.authorize("Sub1","Obj1")

    #deletes object from ACM
    ACM.delObj("Obj1")

    #deletes subject from ACM
    ACM.delSub("Sub3")

    #prints the window for the ACM
    ACM.printWindow(window)
    

    window.mainloop()

main()
