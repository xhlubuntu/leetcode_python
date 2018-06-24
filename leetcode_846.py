

class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if(len(hand)%W!=0):
            return False
        sortedhand = sorted(hand)
        i = 0
        handcnt = []
        while i < len(sortedhand):
            j = i+1
            while j < len(sortedhand) and sortedhand[j] == sortedhand[i]:
                j+=1
            handcnt.append(j-i)
            if(j<len(sortedhand) and sortedhand[j] - sortedhand[i] > 1):
                handcnt.append(0)
            i = j
        #print handcnt
        i = 0
        while i < len(handcnt):
            if(handcnt[i]>0):
                t = handcnt[i]
                for j in range(i,i+W):
                    if(j<len(handcnt)):
                        handcnt[j] = handcnt[j] -  t
                    else:
                        return False
                j = i + 1
                while(j<len(handcnt) and handcnt[j] <=0):
                    if (handcnt[j] < 0):
                        return False
                    j+=1
                i = j
                #print handcnt
            elif handcnt[i] ==0:
                i+=1
            else:
                return False
        return True

hand = [1,2,3,6,2,3,4,7,8]
W = 3
sol = Solution()

sol.isNStraightHand(hand,W)


