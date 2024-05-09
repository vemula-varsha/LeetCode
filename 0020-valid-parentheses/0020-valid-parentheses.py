class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False
        
       
        bracket_map = {')': '(', ']': '[', '}': '{'}
        
       
        stack = []
        
        
        for char in s:
            
            if char in bracket_map.values():
                stack.append(char)
           
            elif char in bracket_map.keys():
               
                if not stack or bracket_map[char] != stack.pop():
                    return False
        
       
        return not stack
