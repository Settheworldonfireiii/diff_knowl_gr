class DirAccTable:
    def __init__(self, bucksz):
        self.table = [None] * bucksz

    def insert(self,key, value):
        self.table[key] = value


    def search(self,key):
        return self.table[key]


    def delete(self, key):
        self.table[key] =  None



class HashTable:
    def __init__(self, bucknum = 100):
        self.create_buckets(self,bucknum)
        pass