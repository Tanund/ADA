'''
Here I gonna perform chaining method

Assignment:  Linear Probing
'''
class HashTable:
    
    def __init__(self, m):
        self.m = m
        self.hashtable = self.create_hash_table()
    
    def create_hash_table(self):
        return [None for _ in range(self.m)]
    
    def _prehash(self, key):
        #challenge: handle negative keys and string
        if (type(key) == str):
            key = hash(key)  #returns a number for you
            
        if ((type(key) == int) | (type(key) == float)):
            if (key < 0):
                key = hash(float(key)) * -1  #first convert to float, then hash it
        
        assert (key >= 0) & (type(key) == int)
    
        return key
    
    def _hash(self, key, i):
        #get the position using division method
        return (key + i) % self.m
    
    def insert(self, key, val):
        
        found, pos, _, flag, flag_pos = self.search(key)
        # found key, update value
        if found:
            self.hashtable[pos] = (key, val)
        else:
            # can't find key, but found flag
            if flag:
                self.hashtable[flag_pos] = (key, val)
            else:
                # empty slot
                if self.hashtable[pos] == None:
                    self.hashtable[pos] = (key, val)
                else:
                    print('Hashtable is full, key = ' + str(key) + ' cannot be filled' )
                    return

        print(self.hashtable)
    
    def search(self, key):

        key     = self._prehash(key)
        pos     = self._hash(key, 0)
        first_pos = pos
        data    = self.hashtable[pos]
        found   = False
        answer  = -9999
        flag = False
        flag_pos = -9999
        i = 1
        while data != None:
            # found key
            if data[0] == key: 
                found = True
                answer = data[1]
                break
            # found delete flag, then save the first delete flag position
            if data[0] == -9999 and flag == False: 
                flag = True
                flag_pos = pos
            # move to next slot
            pos = self._hash(key, i)
            data = self.hashtable[pos]
            i = i + 1
            # prevent infinite loop
            if first_pos == pos:
                break

        return found, pos, answer, flag, flag_pos
    
    def delete(self, key):
        found, pos, _, _, _ = self.search(key)
        if found:
            self.hashtable[pos] = (-9999, -9999)
            print(self.hashtable)
        else:
            print('Nothing to delete !!!')
    
ht = HashTable(7)
ht.insert(0, 'Chaky')
ht.insert(2, 'Peter')
ht.insert(2, 'Peterss') # update value for same key
ht.insert(3, 'John')
ht.insert(10, 'Matthew') # collision, Matthew is filled to the next empty slot

found, _, val, _, _ = ht.search(3)
print(found, val)

ht.delete(3)
ht.delete(10)
ht.insert(10, 'Matthew') # Matthew is filled in the old place of John
ht.insert(3, 'John')
ht.insert(17, 'Tod')
ht.insert(77, 'Max')
ht.insert(1, 'Walter')
ht.delete(77)
ht.insert(1, 'Waltersss')

found, _, val, _, _= ht.search(1)
print(found, val)

ht.insert(8, 'Ken')
ht.insert(7, 'Pond')
ht.delete(0)
ht.insert(7, 'Pond')
