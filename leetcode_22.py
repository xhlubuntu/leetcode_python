#22 ac

parenMap = {
    1:'('
    ,-1:')'
}
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def generate(cumsum, parenlist, poscnt, negcnt, k, n):
            if k == 2 * n:
                parenlist.append(')')
                result.append(parenlist)
                return
            else:
                for toadd in [1, -1]:
                    if cumsum + toadd >= 0:  # legal
                        if toadd == 1 and poscnt < n:
                            generate(cumsum + toadd, parenlist + [parenMap[toadd]], poscnt + 1, negcnt, k + 1, n)
                        if toadd == -1 and negcnt < n:
                            generate(cumsum + toadd, parenlist + [parenMap[toadd]], poscnt, negcnt + 1, k + 1, n)

        generate(0,[],0,0,1,n)
        return [''.join(i) for i in result ]


#     sigma(xi,1,2n) = 0
#{    sigma(xi,1,j) >= 0   j = 1,2,...2n
#     xi = {1,-1}          i = 1,2,...2n