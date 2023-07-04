class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return len(chars)
        
        comp = []
        count = 1
        previouschar = chars[0]
        
        for i in range(1, len(chars)):
            if chars[i] == previouschar:
                count += 1
                       
            else:
                comp.append(previouschar)
                if count > 1:
                    comp += list(str(count))
                previouschar = chars[i]
                count = 1
                
              
        comp.append(previouschar)
        if count > 1:
            comp += list(str(count))
            
        chars[:] = comp
        return len(comp)
