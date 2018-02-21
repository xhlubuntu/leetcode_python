
#17 ac

def dfs(s,i,tmparr,output):
    if(i==len(s) - 1):
        for j in s[i]:
            output.append(''.join(tmparr + [j]))
    else:
        for j in s[i]:
            dfs(s , i+1 , tmparr + [j],output )

phoneNumberMap = {
     '1':'1'
     ,'2':'abc'
     ,'3':'def'
    ,'4':'ghi'
    ,'5':'jkl'
    ,'6':'mno'
    ,'7':'pqrs'
    ,'8':'tuv'
    ,'9':'wxyz'
}

class Solution(object):

    def letterCombinations(self,digits):
        if digits == '':
            return []
        output = []
        letters = [phoneNumberMap[i] for i in digits ]
        #debug
        print letters
        dfs(letters,0,[],output)
        return output

sol = Solution()
print sol.letterCombinations('23')