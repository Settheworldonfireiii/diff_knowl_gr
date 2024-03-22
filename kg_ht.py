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
        self.prev = self.node



    def insert(self,x):
       it = self.next
       while it:
           it = it.next
       it.node = x
       it.next = None


    def search(self, x):
       it = self.node
       found = False
       i = 0
       while it:
               if it == x:
                   found = True
                   break
               i += 1
               it = it.next
       return found, i


    def traverse(self):
        it = self.node
        print(it)
        while it:
            it = it.next
            print(it)


    def traverse_reverse(self):
        it = self.node
        print(it)
        while it.self != it.prev:
            it = it.prev
            print(it)



    #not memory safe, it does not delete, just switches off the chain
    def delete(self, x):
        it = self.node
        i = 0
        while it:
            if it == x:
                it.prev.next = it.next
                t = it.prev.prev
                it.node = it.prev
                it.prev = t
                break





class HashTable:
    def __init__(self, bucknum = 100):
        self.create_buckets(self,bucknum)
        pass

    def hash(self, key):
        #p = 37, m =6, a = 3, b =4
        return ((3*key + 4) % 37) % 6