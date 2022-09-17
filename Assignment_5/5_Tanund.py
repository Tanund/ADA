class Node(object):  #object is the primitive class, so I inherit
    def __init__(self, key):
        self.left  = None
        self.right = None
        self.parent = None
        self.key = key  #this is actually the root node

    #def insert
    def insert(self, key):
        #if we already have a root node,
        if(self.key):
            #then check left and right
            #cond1:  if less than: go left
            if(key < self.key):
                #cond1.1  if the left is NIL, yay! fill it!
                if(self.left == None):
                    self.left = Node(key)
                    self.left.parent = self
                #cond1.2  if the left is NOT NIL...oh no...
                else:
                    self.left.insert(key)
            
            #cond2:  if greater than or equal to: go right
            elif(key >= self.key):
                #cond1.2  if the right is NIL, yay! fill it!
                if(self.right == None):
                    self.right = Node(key)
                    self.parent = self
                #cond1.2  if the right is NOT NIL...consider right as the parent...
                else:
                    self.right.insert(key)
        #if we don't have the root node
        else:
            #this key is the root node
            self.key = key

    
    def printT(self):
        if self.left != None:
            self.left.printT()

        if self.right != None:
            self.right.printT()

        print(self.key)

    def delete(self,z: "Node"):
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = z.right.minimum()
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y


    def transplant(self, u: "Node", v: "Node"):
        if u.parent == None:
            self.key = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent



    def minimum(self):
        if self.left == None:
            return self

        return self.left.minimum()

    def search(self, k):
        if k == self.key:
            return self
        
        if k < self.key and self.left != None:
            return self.left.search(k)
        elif k >= self.key and self.right != None:
            return self.right.search(k)

    
#try our class
root = Node(10)
root.insert(13)
root.insert(5)
root.insert(3)
root.insert(12)
root.printT()

z = root.search(5)

root.delete(z)
root.printT()