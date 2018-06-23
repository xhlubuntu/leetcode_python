
#wa
class LinkeNode:
    def __init__(self,value):
        self._value = value
        self._pre = self._next = None

class LinkeList:
    def __init__(self,listvalues):
        self._size = 0
        for x in listvalues:
            self.insertTail(x)
    def insertTail(self,x):
        newNode = LinkeNode(x)
        if(self._size ==0):
            self._head = self._tail = newNode
        else:
            newNode._pre = self._tail
            self._tail._next = newNode
            self._tail = newNode
        self._size += 1
    def delete(self,node):
        assert(node != None)
        if(node == self._head and node == self._tail):
            self._head = self._tail = None
            del node
            self._size -=1
        elif(node == self._head):
            cur = self._head
            self._head = cur._next
            self._size -= 1
            del cur
        elif(node == self._tail):
            cur = self._tail
            self._tail = cur._pre
            self._size -= 1
            del cur
        else:
            cur = node
            cur._pre._next = cur._next
            cur._next._pre = cur._pre
            self._size -= 1
            del cur
    def lastRemaining(self):
        i = 0
        while(self._size>1):
            if(i%2==0):
                startnode = self._head
                p = startnode
                while (p is not None and p._next is not None and p._next._next is not None):
                    q = p._next._next
                    self.delete(p)
                    p = q
                if (self._size == 1):
                    return p._value
                else:
                    self.delete(p)
            else:
                startnode = self._tail
                p = startnode
                while(p is not None and p._pre is not None and p._pre._pre is not None):
                    q = p._pre._pre
                    self.delete(p)
                    p = q
                if (self._size == 1):
                    return p._value
                else:
                    self.delete(p)
            i+=1

class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        xs = range(1,n+1)
        l = LinkeList(xs)

        return l.lastRemaining()


s = Solution()
s.lastRemaining(9)

