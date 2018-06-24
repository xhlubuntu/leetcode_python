
#ac
import Queue

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = Queue.deque()
        i=0
        while i<len(s):
            if s[i] == '[':
                stack.append(s[i])
                i+=1
            elif '0'<= s[i]<='9':
                j = i+1
                while j<len(s) and '0'<= s[j] <='9':
                    j+=1
                stack.append(s[i:j])
                i=j
            elif 'a'<= s[i] <='z' or 'A' <= s[i] <= 'Z':
                j=i+1
                while j< len(s) and ('a' <= s[j] <='z' or 'A' <= s[j] <= 'Z'):
                    j += 1
                stack.append(s[i:j])
                i=j
            elif s[i]==']':
                tmpword = []
                while True:
                    word = stack.pop()
                    if word == '[':
                        break
                    else:
                        tmpword.append(word)
                w = ''.join(tmpword[::-1])
                cnt = stack.pop()
                stack.append(int(cnt)*w)
                i+=1
            else:
                break
        return ''.join(list(stack))

s = "3[a2[c]]"
sol = Solution()
sol.decodeString(s)