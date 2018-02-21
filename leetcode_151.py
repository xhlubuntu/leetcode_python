#151 ac

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        strlist = s.strip().replace('  ', ' ').split(' ')
        strlist.reverse()
        tojoin = []
        for i in strlist:
            if i.strip() <> '':
                tojoin.append(i.strip())
        return ' '.join(tojoin)