def isValid(s):
        dic = {")":"(",
              "}":"{",
              "]":"[" 
              }
        s = list(s)
        n = len(s)
        stack = []
        i = 0
        opening = ["(", "[","{"]
        closing = [")","]","}"]
        while i < n:
            if s[i] in opening:
                stack.append(s[i])
            else:
                if len(stack) != 0:
                    c=stack.pop()
                    if c != dic[s[i]]:
                        return False
                else:
                    return False
            i+=1
            
        if len(stack) == 0:
            return True
        
        else:
            return False
        

k = input()
ans = isValid(k)
print(ans)
