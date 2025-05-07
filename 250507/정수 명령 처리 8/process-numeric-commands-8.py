

# Please write your code here.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head != None:
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None

        else:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
        
        self.node_num += 1

    def push_back(self, data):
        new_node = Node(data)
        new_node.prev = self.tail

        if self.tail != None:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
        
        else:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        
        self.node_num += 1
    
    def pop_front(self):
        if self.head == None:
            print("List is empty")

        elif self.head.next == None:
            temp = self.head
            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data
        
        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None

            self.node_num -= 1
            return temp.data
        
    def pop_back(self):
        if self.tail == None:
            print("List is empty")
        
        elif self.tail.prev == None:
            temp = self.tail
            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data
        
        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None

            self.node_num -= 1
            return temp.data

    def size(self):
        return self.node_num

    def empty(self):
        return int(self.node_num == 0)
    
    def front(self):
        if self.head == None:
            print("List is empty")
        else:
            return self.head.data

    def back(self):
        if self.tail == None:
            print("List is empty")
        else:
            return self.tail.data


N = int(input())
command = []
A = DLL()

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_front":
        A.push_front(line[1])
    elif line[0] == "push_back":
        A.push_back(line[1])
    elif line[0] == "pop_front":
        print(A.pop_front())
    elif line[0] == "pop_back":
        print(A.pop_back())
    elif line[0] == "size":
        print(A.size())
    elif line[0] == "empty":
        print(A.empty())
    elif line[0] == "front":
        print(A.front())
    elif line[0] == "back":
        print(A.back())