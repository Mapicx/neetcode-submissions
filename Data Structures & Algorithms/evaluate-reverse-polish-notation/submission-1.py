from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                if token == "+":
                    result = operand1 + operand2
                elif token == "-":
                    result = operand1 - operand2
                elif token == "*":
                    result = operand1 * operand2
                elif token == "/":
                    # Truncate toward zero (important for LeetCode-style problems)
                    result = int(operand1 / operand2)
                
                stack.append(result)
        
        return stack[0]
