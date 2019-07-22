"""
    Author: Shengkai Wang 
    Date: 7.21 2019
    Email: chriswangmiis@gmail.com
    License: MIT
"""
"""
    Pros: 
        1. simple to implement 
        2. The running time of the hashing process is good
        3. Quick access time (follow from 2)
    Cons: 
        1. Collision prone
        2. Cannot accomodate non-int keys
        3. essentially just array
        4. inefficent memory ussage

    When to use: 
        1. none
"""
def directAddress(key):
    return key; 
