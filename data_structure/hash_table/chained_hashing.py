"""
    Author: Shengkai Wang 
    Date: 7.21 2019
    Email: chriswangmiis@gmail.com
    License: MIT
"""

"""
    Hashtable with chained(singly linked list)hashing implementation
    Performance (m elements in array of size n ):
        1. search: O(m/n) on average, O(n) on worst
        2. set: O(m/n) on average, O(n) on worst
        3. delete: O(m/n) on average, O(n) on worst
        4. get: O(m/n) on average, O(n) on worst
"""
from pair import pair

class chainedHashTable:
    def __init__(self, hashFunc = hash, size = 100):
        self.table = [None for i in range(size)]
        self.tableSize = size
        self.hashFunc = hashFunc
        

    def __setitem__(self, key, value):
        index = self.hashFunc(key) % self.tableSize
        cur_pairs = self.table[index]
        insert = pair(key, value)
        
        if cur_pairs is None:
            self.table[index] = insert
        else:
            prev = None
            while cur_pairs:
                if cur_pairs.key == key:
                    cur_pairs.value = insert.value
                    return
                prev = cur_pairs
                cur_pairs = cur_pairs.next
            prev.next = insert
        return
    
    def __getitem__(self, key):        
        index = self.hashFunc(key) % self.tableSize
        cur_pairs = self.table[index]

        if cur_pairs is None:
            print('No such element found')
            return 
        else:
            while cur_pairs:
                if cur_pairs.key == key:
                    return cur_pairs.value
                cur_pairs = cur_pairs.next
            print('No such element found')
            return 

    def __delitem__(self, key):
        index = self.hashFunc(key) % self.tableSize
        cur_pairs = self.table[index]

        if cur_pairs is None:
            print('no such element found!')
            return
        else:
            prev = None
            while cur_pairs:
                if cur_pairs.key == key:
                    if prev is not None:
                        prev.next = cur_pairs.next
                    else:
                        self.table[index] = cur_pairs.next 
                    return
                prev = cur_pairs
                cur_pairs = cur_pairs.next
            print('no such element found!')
            return 

    def __repr__(self):
        result = ["class: {0} with size {1}, using hash function {2}".format(self.__class__, self.tableSize, str(self.hashFunc))]
        for item in self.table:
            if item:
                list_info = ""
                while item:
                    list_info = list_info + str(item) + " "
                    item = item.next
                result.append(list_info)        
        return "\n".join(result)

    def __str__(self):
        return "Chained Hashing table"
    

        
        