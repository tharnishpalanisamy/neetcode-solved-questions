class Node:
    def __init__(self, key = -1 ,val = -1 ) :
        self.key = key 
        self.val = val 
        self.next = None
class MyHashMap:

    def __init__(self):
        self.map = [Node() for i in range(1000)]

    def put(self, key: int, value: int) -> None: 
        index = key % 1000 
        cur = self.map[index] 
        while cur.next :
            if cur.next.key == key :
                cur.next.val = value 
                return 
            cur = cur.next 
        cur.next = Node(key,value)
        

    def get(self, key: int) -> int: 
        index = key % 1000 
        cur = self.map[index] 
        while cur.next :
            if cur.next.key == key :
                return cur.next.val 
            cur = cur.next 
        return -1
        

    def remove(self, key: int) -> None: 
        index = key % 1000 
        cur = self.map[index] 
        while cur.next :
            if cur.next.key == key :
                cur.next.val = -1 
                return 
            cur = cur.next 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)