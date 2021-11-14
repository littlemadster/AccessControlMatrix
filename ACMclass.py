'''
ACM CLASS

    transfer
    grant
    read
    create object
    create subject
    delete object
    delete subject
    delete right
    
'''

from tkinter import *
from tkinter import ttk

class ACM:

    subjects = [] #list of subjects that are created
    objects = [] #list  of objects that are created
    rightsDict = {} #dictionary of rights and locations

    def createObj(window, objName):  #takes window and object name to create new object onto window
        ACM.objects.append(objName) #add object to object list
        objName = Label(window, text=objName).grid(row=0, column=len(ACM.objects)+1) #prints object to table
        
    def createSub(window, subName): #takes window and subject name to create new subject onto window
        ACM.subjects.append(subName) #add subject to subject list
        ACM.createObj(window, subName) #makes subject an object
        subName = Label(window, text=subName).grid(row=len(ACM.subjects)+1, column=0) #print subject to table
        

    def grant(window, subName, objName, right): #grants subject right to object based on subject, object, and desired right
        subI = 0 #subject index
        objI = 0 #object index

        for i in range(len(ACM.subjects)): #finds index of subject
            if ACM.subjects[i] == subName:
                subI = i+2 #subject index is list index + 2

        for j in range(len(ACM.objects)): #finds index of object
            if ACM.objects[j] ==  objName:
                objI = j+2 #object index is list index + 2

        print(str(subI) + " " + str(objI)) #prints location of granted right
        
        if (str(str(subI)+str(objI))) in ACM.rightsDict: #checks if subject already has rights on object
            newRight = str(ACM.rightsDict[str(str(subI)+str(objI))]) + '\n' + str(right) #if yes, add new right
            ACM.rightsDict[str(str(subI)+str(objI))] = newRight #update rights in dictionary
            Label(window, text=newRight).grid(row=subI, column=objI) #update table with rights
        else: #if no existing rights
            ACM.rightsDict[str(str(subI)+str(objI))] = right #add right to dictionary at location
            Label(window, text=right).grid(row=subI, column=objI) #update table with right
                
                
                

def main():
    
    def close():
        window.destroy()

    window = Tk()
    window.title("ACM")
    window.geometry('500x500')

    Button(window, text="Quit", command=close).grid(row=0, column=0)
    ACM.createObj(window, "Obj1")
    ACM.createSub(window, "Sub1")
    ACM.createObj(window, "Obj2")
    ACM.createSub(window, "Sub2")
    ACM.createSub(window, "Sub3")
    ACM.createObj(window, "Obj3")
    ACM.createObj(window, "Obj4")
    ACM.grant(window, "Sub1", "Obj1", "own")
    ACM.grant(window, "Sub1", "Obj1", "control")
    ACM.grant(window, "Sub1", "Obj1", "write")
    ACM.grant(window, "Sub3", "Obj2", "own")
    ACM.grant(window, "Sub3", "Obj4", "read")
    print(ACM.rightsDict)
    print(ACM.subjects)
    print(ACM.objects)

    window.mainloop()

main()
