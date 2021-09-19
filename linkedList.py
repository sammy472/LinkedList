class LinkedList:
    """This is a base class for creating and manipulating singly linked list.
        Comes with several methods that allow you to manipulate single linked lists.
        It can be a linked of any data.
    """
    def __swapValues(self,a,b):
        """A private method for swapping two variables. Returns a tuple of the swapped variables.
        """
        c = a
        a = b
        b = c
        return a,b
    def __init__(self):
        self.__wrapper = dict()
        self.__wrapper.update({"value":None,"next":None})
    def createNode(self,value):
        """Creates and returns a node.
        """
        return {"value":value,"next":None}
    def addNode(self,value):
        """This function adds a node at the end of a linked list created by the wrapper class.
        Args:
            value (Int,Float,Strings,Sets,Dictionaries): Node can be of only one of the these data types.
        Returns:
            Linked List: Returns a linked list reprensentd by nested dictionaries.
        """
        if self.__wrapper["value"] == None and self.__wrapper["next"] == None:
            self.__wrapper["value"] =value
            return self.__wrapper
        temp = self.__wrapper
        while temp != None:
            if temp["next"] == None:
                temp["next"] = self.createNode(value)
                return self.__wrapper
            temp = temp["next"]
    def listLength(self):
        """Returns the length of a linked list as an integer value.
        """
        N = 0
        temp = self.__wrapper
        while temp != None:
            N += 1
            temp = temp["next"]
        return N
    def showItems(self):
        """Prints the values or items of a linked list.
        """
        temp = self.__wrapper
        while temp != None:
            print(temp["value"],end="\n")
            temp = temp["next"]
    def sortItemsAscend(self):
        """Sorts elements of a linked list ascendingly.
        """
        N = self.listLength()
        for i in range(N):
            c = self.__wrapper
            while c != None:
                if c["next"] == None:
                    break
                a = c["value"]
                b = c["next"]["value"]
                if a > b:
                   (c["value"],c["next"]["value"]) = self.__swapValues(a,b)
                c = c["next"]
    def sortItemsDescend(self):
        """Sorts elements of a linked list descendingly.
        """
        N = self.listLength()
        for i in range(N):
            c = self.__wrapper
            while c != None:
                if c["next"] == None:
                     break
                a = c["value"]
                b = c["next"]["value"]
                if a < b:
                    (c["value"],c["next"]["value"]) = self.__swapValues(a,b)
                c = c["next"]
    def deleteNode(self,index = 1):
        """This method deletes a node in the linked list. Default node position is 1. Indexing starts from 1.
        """
        N = self.listLength()
        if index >=1 and index <= N:
            tmp = self.__wrapper
            if index == 1:
                tmp = self.__wrapper
                self.__wrapper = tmp["next"]
                del(tmp)
            else:
                for i in range(index-2):
                    tmp = tmp["next"]
                temp = tmp["next"]
                tmp["next"] = temp["next"]
    def insertNode(self,value,index=1):
        """Inserts a node at any index in the linked list. Indexing starts at 1.
           Returns None
        """
        N = self.listLength()
        node = self.createNode(value)
        temp = self.__wrapper
        if index == 1:
            node["next"] = self.__wrapper
            self.__wrapper = node
        elif index > N:
            for j in range(N-1):
                temp = temp["next"]
            temp["next"] = node
        else:
            for i in range(index-2):
                temp = temp["next"]
            c = temp["next"]
            b = c["next"]
            temp["next"] = node
            node["next"] = c
#Testing the module.            
if __name__ == "__main__":
    l = LinkedList()
    l.addNode(1)
    l.addNode(2)
    l.addNode(3)
    l.addNode(4)
    l.addNode(5)
    l.addNode(6)
    l.addNode(7)
    l.addNode(8)
    l.addNode(9)
    l.addNode(10)
    print("Before\n\n\n\n\n\n")
    l.showItems()
    print("After\n\n\n\n\n\n")
    l.insertNode(20,16)
    l.showItems()
    l.sortItemsDescend()
    l.showItems()
    
    
        
