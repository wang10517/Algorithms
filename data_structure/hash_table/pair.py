"""
    Author: Shengkai Wang 
    Date: 7.21 2019
    Email: chriswangmiis@gmail.com
    License: MIT
"""

"""
    Pair modulue for uses in chained hashing table 
"""

class pair(object):
    def __init__(self, key, value, next_pair = None):
        self.key = key
        self.value = value
        self.next = next_pair

    def __str__(self):
        if self.next is None:
            next_key = "None"
            next_val = "None"
        else:
            next_key = self.next.key 
            next_val = self.next.value
        return "({0},{1}) -> ({2},{3})".format(self.key, self.value, next_key, next_val)

    def next(next_pair):
        self.next = next_pair
    
    def __eq__(self, other):
        return self.key == other.key
    
    def __bool__(self):
        return self is not None
    
    def __repr__(self):
        return "class: {0}, key: {1}, value: {2}".format(self.__class__, self.key, self.value)
    
    def __hash__(self):
        return self.key + self.value
    