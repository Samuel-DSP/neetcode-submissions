# class LinkedList:
    
#     def __init__(self):

    
#     def get(self, index: int) -> int:
        

#     def insertHead(self, val: int) -> None:
        

#     def insertTail(self, val: int) -> None:
        

#     def remove(self, index: int) -> bool:
        

#     def getValues(self) -> List[int]:
        

class LinkedList:
    def __init__(self):
        self.values = []

    def get(self, index: int) -> int:
        if index >= len(self.values):
            return -1
        return self.values[index]

    def insertHead(self, val: int) -> None:
        self.values.insert(0, val)

    def insertTail(self, val: int) -> None:
        self.values.append(val)

    def remove(self, index: int) -> bool:
        if index >= len(self.values):
            return False
        self.values.pop(index)
        return True

    def getValues(self) -> List[int]:
        return self.values