'''
ACM CLASS

    transfer
    #grant
    read
    #create object
    #create subject
    delete object
    delete subject
    delete right

    ### UPDATE TO MAKE LABELS AN OBJECT THAT CAN BE MANIPULATED/CHANGED ###
    
'''


from tkinter import *
from tkinter import ttk

class LabelACM:

    def __init__(self, name, text, row, column):
        self.name = name
        self.text = text
        self.row = row
        self.column = column

class ACM:

    objObj = []
    subjects = [] #list of subjects that are created
    objects = [] #list  of objects that are created
    rightsDict = {} #dictionary of rights and locations

    def createObj(window, objName):  #takes window and object name to create new object onto window
        objNamed = LabelACM(objName, objName, 0, len(ACM.objects)+1)
        ACM.objects.append(objNamed) #add object to object list
        objNamed = Label(window, text=objName)
        objNamed.grid(row=0, column=len(ACM.objects)+1) #prints object to table
        ACM.objObj.append(objNamed)
        
    def createSub(window, subName): #takes window and subject name to create new subject onto window
        ACM.subjects.append(subName) #add subject to subject list
        ACM.createObj(window, subName) #makes subject an object
        subName = Label(window, text=subName)
        subName.grid(row=len(ACM.subjects)+1, column=0) #print subject to table
        

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
            addRight = Label(window, text=right)
            addRight.grid(row=subI, column=objI) #update table with right
          
    '''def delRight(window, subName, objName, right):
        subI = 0 #subject index
        objI = 0 #object index

        for i in range(len(ACM.subjects)): #finds index of subject
            if ACM.subjects[i] == subName:
                subI = i+2 #subject index is list index + 2

        for j in range(len(ACM.objects)): #finds index of object
            if ACM.objects[j] ==  objName:
                objI = j+2 #object index is list index + 2

        print(str(subI) + " " + str(objI)) #prints location of deleted right

        #if first or middle right in list
        if str(ACM.rightsDict[(str(str(subI)+str(objI)))]).__contains__(right+str("\n")): #checks if right exists
            updateRights = str(ACM.rightsDict[str(str(subI)+str(subI))]).replace(str(right+str("\n")), "")
            ACM.rightsDict[str(str(subI)+str(objI))] = updateRights #update rights in dictionary
            Label(window, text=updateRights).grid(row=subI, column=objI) #update table with rights

        #if last right in list
        elif str(ACM.rightsDict[(str(str(subI)+str(objI)))]).__contains__(str("\n")+right): #checks if right exists
            updateRights = str(ACM.rightsDict[str(str(subI)+str(subI))]).replace(str(str("\n")+right), "")
            ACM.rightsDict[str(subI)+str(objI)] = updateRights #update rights in dictionary
            Label(window, text=updateRights).grid(row=subI, column=objI) #update table with rights            
                
        #if only right
        elif str(ACM.rightsDict[(str(str(subI)+str(objI)))]).__contains__(right): #checks if right exists
            updateRights = str(ACM.rightsDict[str(str(subI)+str(subI))]).replace(str(right), "")
            ACM.rightsDict[str(str(subI)+str(objI))] = updateRights #update rights in dictionary
            Label(window, text="").grid(row=subI, column=objI) #update table with rights'''


    def delObj(window, objName):
        for i in range(len(ACM.objects)):
            if objName == ACM.objects[i].name:
                ACM.objObj[i].destroy()
        
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
    #ACM.delObj(window, "Obj1")
    '''
    ACM.grant(window, "Sub1", "Obj1", "own")
    ACM.grant(window, "Sub1", "Obj1", "control")
    ACM.grant(window, "Sub1", "Obj1", "write")
    ACM.grant(window, "Sub3", "Obj2", "own")
    ACM.grant(window, "Sub3", "Obj4", "read")
    ACM.grant(window, "Sub3", "Obj2", "control")
    #ACM.delRight(window, "Sub1", "Obj1", "control")
    ACM.delRight(window, "Sub3", "Obj4", "read")
    print(ACM.rightsDict)
    print(ACM.subjects)
    '''
    print(ACM.objects[0].text)
    print((ACM.objObj[0])["text"]) # trying to get text from label object

    window.mainloop()

main()
'''
def attempt():
    
    def close():
        window.destroy()

    window = Tk()
    window.title("ACM")
    window.geometry('500x500')
    Button(window, text="Quit", command=close).grid(row=0, column=0)

    list = []

    label1Obj = LabelACM("label1", "label1", 0, 1)
    label1 = Label(window, text=label1Obj.text)
    label1.grid(row=label1Obj.row, column=label1Obj.column)
    label1.cget("text")
    label2Obj = LabelACM("lab", "lab", 1, 1)
    label2 = Label(window, text=label2Obj.text)
    label2.grid(row=label2Obj.row, column=label2Obj.column)
    label1.destroy()

    window.mainloop()

attempt()'''
