
#20 ac
import Queue
class Solution(object):
  def isValid(self,s):
    tmpStack = Queue.deque()
    for i in s:
      if(len(tmpStack) == 0 or i in ['(','[','{']):
        tmpStack.append(i)
      else:
        l = tmpStack.pop()
        if l+i not in ['()','[]','{}']:
          return False
    if len(tmpStack) >0:
        return False
    return True

sol = Solution()
print sol.isValid("(){}[{]]")
