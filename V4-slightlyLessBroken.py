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
        self.rights = []
        

class ACM:

    subjects = [] #list of subjects that are created
    objects = [] #list  of objects that are created
    rights = [] #list of rights that are created


    grid = [] #stores subject,object, and roles together
    counter =0 # counts how many times function is run
    row =0
    column =0
    

    def createObj(objName):  #takes window and object name to create new object onto window
        ''' CHECK IF OBJECT ALREADY EXISTS'''
        newObject = LabelACM(objName, objName, 0, len(ACM.objects)+1)
        ACM.objects.append(newObject) #add object to object list
        
    def createSub(subName): #takes window and subject name to create new subject onto window
        newSubject = LabelACM(subName, subName, len(ACM.objects)+1, 0)
        ACM.subjects.append(newSubject) #add object to object list
        ACM.createObj(subName)

    def grant(subName, objName, right): #grants subject right to object based on subject, object, and desired right
        subI = 0 #subject index
        objI = 0 #object index
    
        for i in range(len(ACM.subjects)): #finds index of subject
            if ACM.subjects[i].name == subName:
                subI = ACM.subjects[i].row

                LabelACM.row =subI
                
                break

        for j in range(len(ACM.objects)): #finds index of object
            if ACM.objects[j].name ==  objName:
                objI = ACM.objects[j].column
                LabelACM.column = objI
                
                break
            
        print("current subI,obi: ",subI,objI) #prints current subject and object index
        row = str(subI)
        column = str(objI)
        role = right
        allThree = (subName,objName, role) # combines all three values 
        ACM.counter += 1  

      
        print("COUTER:",ACM.counter)
        for i in range (ACM.counter): 
            if (allThree not in ACM.grid):
                print(allThree,"All three values do not exist in ACM.grid:")
                ACM.grid.append(allThree)
                print("APPENDING ALL THREE TO ACM.grid[i]: ",ACM.grid)
                break

            else:
                 print(allThree,"ALREADY exist:")
                 break
          
          
    '''def delRight(window, subName, objName, right):
        subI = 0 #subject index
        objI = 0 #object index

        for i in range(len(ACM.subjects)): #finds index of subject
            if ACM.subjects[i] == subName:
                subI = i+2 #subject index is list index + 2

        for j in range(len(ACM.objects)): #finds index of object
            if ACM.objects[j] ==  objName:
                objI = j+2 #object index is list index + 2

        #print(str(subI) + " " + str(objI)) #prints location of deleted right

        #if first or middle right in list
        for k in range(len(ACM.rightsObj)):
            if ACM.rights[k].name == str(subName)+str(objName):
                for p in range(len(ACM.rightsObj)):
                    ACM.rightsObj[p].destroy()

                    #ACM.rightsObj[k].grid(row=subI, column=objI)
                    


    def delObj(window, objName): 
        for i in range(len(ACM.objects)):
            if objName == ACM.objects[i].name:
                ACM.objObj[i].destroy()'''
        
def main():
    
    def close():
        window.destroy()

    window = Tk()
    window.title("ACM")
    window.geometry('900x400')

    Button(window, text="Quit", command=close).grid(row=0, column=0)
    ACM.createObj("Obj1")
    ACM.createSub("Sub1")
    ACM.createObj("Obj2")
    ACM.createSub("Sub2")
    ACM.createSub("Sub3")
    ACM.createObj("Obj3")
    ACM.createObj("Obj4")
    
    #ACM.delObj(window, "Obj1")

    ACM.grant("Sub2", "Obj3", "view")
    ACM.grant("Sub1", "Obj1", "own")
    ACM.grant("Sub2", "Obj3", "view")
    ACM.grant("Sub1", "Obj1", "write")
    ACM.grant("Sub3", "Obj2", "own")
    ACM.grant("Sub3", "Obj4", "read")
    ACM.grant("Sub3", "Obj2", "control")
    ACM.grant("Sub3", "Obj4", "read")



    for i in range(len(ACM.objects)):
        printObj = Label(window, text = ACM.objects[i].text)
        printObj.grid(row = ACM.objects[i].row, column = ACM.objects[i].column)

    for i in range(len(ACM.subjects)):
        printSub = Label(window, text = ACM.subjects[i].text)
        printSub.grid(row = ACM.subjects[i].row, column = ACM.subjects[i].column)
   
    '''     
    for i in range(ACM.counter):
        print("ACM.GRID IN MAIN FUNCTION: ",ACM.grid)
        printRight = Label(window, text = ACM.grid)
        printRight.grid(row = ACM.rights[i].row, column = ACM.rights[i].column)
    '''
        
    #ACM.delRight(window, "Sub1", "Obj1", "control")
    #ACM.delRight(window, "Sub1", "Obj1", "write")
    #ACM.delRight(window, "Sub3", "Obj4", "read")'''
    

    window.mainloop()

main()
