def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        dic  = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        s = str(s)
        l = list(s)
        ans = 0
        for i in range(len(l)):
            if i == 0:
               ans = ans + dic[l[i]]
            elif dic[l[i]] <= dic[l[i-1]]:
                ans = ans + dic[l[i]]
            else:
                ans = ans + abs(dic[l[i]]-dic[l[i-1]]) - dic[l[i-1]]
                
        return ans
    
    
S = input()
ans  = romanToInt(S)
print(ans)
