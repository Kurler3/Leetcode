

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            elif not stack or char != stack.pop():
                return False
        return len(stack) == 0
if __name__ == '__main__':
    sol = Solution()
    
    s = "()"
    is_valid = sol.isValid(s)
    
    if is_valid:
        print("Correct answer!")
    