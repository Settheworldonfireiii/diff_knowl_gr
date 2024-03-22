class DirAccTable:
    def __init__(self, bucksz):
        self.table = [None] * bucksz

    def insert(self,key, value):
        self.table[key] = value


    def search(self,key):
        return self.table[key]


    def delete(self, key):
        self.table[key] =  None


class DLL:


    def __init__(self, x):
        self.node = x
        self.next = None
        self.prev =self.node


   def insert(self,x):
       it = self.next
       while it:
           it = self.next
       self.prev = it.prev
       self.node = x
       self.next = None

   def search(self, x):
       it = self.node
       found = False
       i = 0
       while it:
               if it == x:
                   found = True
                   break
               i += 1
               it = self.next
       return found, i




class HashTable:
    def __init__(self, bucknum = 100):
        self.create_buckets(self,bucknum)
        pass

    def hash(self, key):
        #p = 37, m =6, a = 3, b =4
        return ((3*key + 4) % 37) % 6