class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def InsertInBegining(self, data):
        node = Node(data, self.head)
        self.head = node

    def InsertAtTheEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def InsertValues(self, data_list):
        self.head = None
        for data in data_list:
            self.InsertAtTheEnd(data)

    
    def Print(self):
        if self.head is None:
            print("LinkedList is Empty")
            return
        
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        
        print(llstr)

    def GetLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def RemoveAt(self, index):
        if index < 0 or index >= self.GetLength():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1
    
    def InsertAt(self, index, data):
        if index < 0 or index >= self.GetLength():
            raise Exception("Invalid Index")
    
        if index ==0:
            self.InsertInBegining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count== index -1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count +=1

    def InsertAfterValue(self, dataafter, data):
        if dataafter is None:
            raise Exception("Invalid Value")

        if self.head.data==data:
            self.head.next = Node(data,self.head.next)
            return
            
        itr = self.head
        while itr:
            if itr.data == dataafter:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
    
    def RemoveByValue(self, data):
        if data is None:
            raise Exception("Invalid Data")

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next 

if __name__ == '__main__':
    ll = LinkedList()
    ll.InsertValues(["Apple", "Orange", "Banana", "Pineapple", "Grapes"])
    print(ll.GetLength())
    ll.Print()
    ll.InsertAt(0, "figs")
    ll.Print()
    ll.InsertAfterValue("Banana", "Jackfruit")
    ll.Print()
    ll.RemoveByValue("Banana")
    ll.Print()
