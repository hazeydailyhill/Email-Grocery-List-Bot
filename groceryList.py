import os

class GroceryList:
    def createList(self):
        file = open("groceryList.txt", "x")
        file.close()

    def addItem(self):
        item = str(input("Item to add? "))
        file = open("groceryList.txt", "a")
        file.write(item+ "\n")
        file.close()

    def showList(self):
        with open("groceryList.txt", "r") as file:
            #print(file.read())
            returnStatement = str(file.read())
            return returnStatement

    def deleteList(self):
        os.remove("groceryList.txt")
