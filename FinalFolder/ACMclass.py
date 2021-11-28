'''
ACM CLASS
Authors: Madeleine Sirok, Valentina Colorado
Course: CIS4367.01
Date Last Modified: 11/28/21
Description: The ACM-Class-Final consist of the LabelACM class and the ACM class. The LabelACM class will label objects. 
While the ACM class will initialize a grid and its rules are within its own class while the objects of the labels in the ACM are initialized within the LabelACM class. 
The LabelACM class creates an object which takes the name of the object, the text that will be printed on screen and row and column for the location of the object. 
The rules are not created upon initialization because subjects and objects themselves do not hold the rules; rules are its own type
'''


from tkinter import *
from tkinter import ttk
import operator

'''
LabelACM class is an object class for the objects, subjects, and rights to be instantiated.
This class is separated from the ACM class because that holds all the rules for the ACM.
Note: 'object' is used in terms of of class being an object, and "Object" is used in terms of Subjects/Objects/Rules.
'''
class LabelACM:

    def __init__(self, name, text, row, column):
        self.name = name #name of the object
        self.text = text #text that will be on label
        self.row = row #row for object to be placed
        self.column = column #column for object to be placed
        self.rights = [] #rights for a given object
        
'''
ACM class is a class for all the rules of the ACM. The rules include: create object, create subject, delete object,
delete subject, grant, remove rights, etc. All the rules that were given on the slides.
'''
class ACM:

    subjects = [] #list of subjects that are created
    objects = [] #list  of objects that are created
    rights = [] #list of rights that are created
    
    

    def createObj(objName):  #takes object name to create new LabelACM object
        ''' CHECK IF OBJECT ALREADY EXISTS'''
        newObject = LabelACM(objName, objName, 0, len(ACM.objects)+1) #creats a new object
        ACM.objects.append(newObject) #add object to object list
        
    def createSub(subName): #takes window and subject name to create new subject onto window
        ''' CHECK IF SUBJECT ALREADY EXISTS'''
        newSubject = LabelACM(subName, subName, len(ACM.subjects)+1, 0) #creates a new subject 
        ACM.subjects.append(newSubject) #add object to object list
        ACM.createObj(subName) 
                

    def initRules(): # initalize all the rules in ACM

        for i in range(len(ACM.subjects)): 
            for j in range(len(ACM.objects)):
                newRight = LabelACM(ACM.subjects[i].name + ACM.objects[j].name, ACM.subjects[i].name + ACM.objects[j].name, ACM.subjects[i].row, ACM.objects[j].column) 
                ACM.rights.append(newRight) #append the new right to ACM.rights
                ACM.grant(ACM.subjects[i].name,ACM.subjects[i].name,"control") #Grants the subject control
               # print(newRight.name + ": " + str(newRight.row) + " " + str(newRight.column)) #used for testing
        
    def grant(subName, objName, right): #Takes subject name, object name, and desired right and grants subject right.

        for i in range(len(ACM.subjects)): #finds name of subject
            if ACM.subjects[i].name == subName: #if subject name is found 
                subI = ACM.subjects[i].name #save it as subI
                break

        for j in range(len(ACM.objects)): #finds name of object
            if ACM.objects[j].name ==  objName: #if object name is found
                objI = ACM.objects[j].name #save it as objI
                break
   
        for k in range(len(ACM.rights)): #searches for right location within rights list
            if ACM.rights[k].name == subI + objI: #if name is found
                if right not in ACM.rights[k].rights: #if right does not already exist
                    ACM.rights[k].rights.append(right) #add right
                    #print("rights: " +  ACM.rights[k].text + " " + str(ACM.rights[k].rights))
                    break
            
                        
    def removeRight(subName, objName, right): #Takes subject name object name and right
        for i in range(len(ACM.subjects)): #finds name of subject
            if ACM.subjects[i].name == subName: #if subject name is found
                subI = ACM.subjects[i].name #save it as objI
                break

        for j in range(len(ACM.objects)): #finds name of object
            if ACM.objects[j].name ==  objName: #if obj name is found
                objI = ACM.objects[j].name #save it as objI
                break

        for k in range(len(ACM.rights)): #searches for right location within rights list
            if ACM.rights[k].name == subI + objI and ACM.authorize(subName,objName) == 1: #if name is found AND that right is authorized to remove the right
                if right in ACM.rights[k].rights: #if right does not already exist
                    ACM.rights[k].rights.remove(right) #removes the right 
                    #print("rights: " +  ACM.rights[k].text + " " + str(ACM.rights[k].rights))
                    break
            


    def transfer(subNameF, objNameF, right, subNameT, objNameT, rightT): #subject from, object from, right, subject to, object to
        possible = 0
        
        for i in range(len(ACM.subjects)): #finds name of subject
            if ACM.subjects[i].name == subNameF: # if subject name is in ACM.subjects
                subF = ACM.subjects[i].name # save as subF
                break

        for j in range(len(ACM.objects)): #finds name of object
            if ACM.objects[j].name ==  objNameF: #if object name is in ACM.objects
                objF = ACM.objects[j].name #save as objF
                break

        for i in range(len(ACM.subjects)): #finds name of subject
            if ACM.subjects[i].name == subNameT: #if subject name of desired transfer subject exsits in the ACM.subjects
                subT = ACM.subjects[i].name #save as subT
                break

        for j in range(len(ACM.objects)): #finds name of object
            if ACM.objects[j].name ==  objNameT: #if object name of desired transder object exsits in the ACM.objects
                objT = ACM.objects[j].name #save as objT
                break
        
        for k in range(len(ACM.rights)): #searches for right location within rights list
            if ACM.rights[k].name == subF + objF: #if name is found
                if right in ACM.rights[k].rights and operator.contains(right, "*"): #if right does exist
                    possible = 1 

        if possible == 1: #if it is possible to transfer rule
            for k in range(len(ACM.rights)):
                if ACM.rights[k].name == subT + objT: #if name is found
                    if rightT not in ACM.rights[k].rights: #if right does not already exist
                        ACM.rights[k].rights.append(rightT) #add right
                        print("rights: " +  ACM.rights[k].text + " " + str(ACM.rights[k].rights)) 
                        break

    def readAll(): #prints all rights for subjects and objects
        print("Rights are defined as 'subject name' concatinated with 'object name' and printed with their rights.")
        for i in range(len(ACM.rights)):
            print(ACM.rights[i].text + " " + str(ACM.rights[i].rights)) #print out the rights

    def read(subName, objName): #takes subject name and object name and reads the rights
        
        for i in range(len(ACM.subjects)): #finds name of subject
            if ACM.subjects[i].name == subName: # if subject name exist in ACM.subjects
                sub = ACM.subjects[i].name #save as sub
                break

        for j in range(len(ACM.objects)): #finds name of object
            if ACM.objects[j].name ==  objName: #if object name exist in ACM.objects
                obj = ACM.objects[j].name #save as objI
                break
            
        for k in range(len(ACM.rights)): #finds right
            if ACM.rights[k].name == subName + objName: #if name is found
                print("Reading:\nSubject: " + sub + ", Object: " + obj + " ==>\nRights: " + str(ACM.rights[k].rights))
                return str(ACM.rights[k].rights) #return rights 

    def authorize(subName, objName): #takes subject name and object name to see if they're authorized to perform task
        print("checking authorization...")
            
        for k in range(len(ACM.rights)):
            if ACM.rights[k].name == subName + objName: #if name is foun
                if ("control" in ACM.rights[k].rights) or ("own" in ACM.rights[k].rights): # checks to see if entity has authorization 
                    return 1
                    
            
   
    def delRecursive(name): #takes in subject OR object name, checks if that subject, or object exist and deletes it 
        for m in range(len(ACM.rights)):
            if name in ACM.rights[m].text: #if objname matches name in array 
                del ACM.rights[m]   #delete rights
                ACM.delRecursive(name) # check if there are any more rights 
                break
        
    def delObj(objName): #takes object name and delete object from ACM
        for i in range(len(ACM.rights)):
            if objName in ACM.rights[i].text: #objname exist in array 
                ACM.delRecursive(objName) #find any place that has this object name and delete it
                break                      
        
        for i in range(len(ACM.objects)):# delets the object in the array  
             if ACM.objects[i].text ==  objName: #if objname matches name in array 
                 del ACM.objects[i] #delete object column
                 break


    def delSub(subName): #takes subject name and deletes subject from ACM
        for i in range(len(ACM.rights)):
            print( ACM.rights[i].text) #
            if subName in ACM.rights[i].text: #if objname matches name in array 
                ACM.delRecursive(subName) #if subject has more than one rule sends it to delRecursive
                del ACM.objects[i]  #deletes subject from column

                break                      
        
        #  objects array 
        for k in range(len(ACM.subjects)):
             if ACM.subjects[k].text ==  subName: #if objname matches name in array 
                 del ACM.subjects[k]    #deletes subject from object
                 break

    
    def printWindow(window): #function to print out ACM
        for i in range(len(ACM.objects)): #print object
            printObj = Label(window, text = ACM.objects[i].text) 
            printObj.grid(row = ACM.objects[i].row, column = ACM.objects[i].column) #prints the object is in the right row and column

        for i in range(len(ACM.subjects)): #print subject
            printSub = Label(window, text = ACM.subjects[i].text) 
            printSub.grid(row = ACM.subjects[i].row, column = ACM.subjects[i].column)#prints the subject is in the right row and column
            
        for i in range(len(ACM.rights)): #print rights
            #print("\nPrinting: "+ACM.rights[i].text + " " + str(ACM.rights[i].rights))
            if len(ACM.rights[i].rights) == 0:
                printRight = Label(window, text = '[]', borderwidth = 2, relief = "ridge")
                printRight.grid(row = ACM.rights[i].row, column = ACM.rights[i].column) #prints the right is in the right row and column
            else:
                printRight = Label(window, text = '\n'.join(ACM.rights[i].rights), borderwidth = 2, relief = "ridge")
                printRight.grid(row = ACM.rights[i].row, column = ACM.rights[i].column) #prints the right is in the right row and column
            
        
