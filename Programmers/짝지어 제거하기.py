def solution(s):
    s = list(s)
    while True:
        stack = []
        for letter in s:
            if stack and stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)
        
        if not stack:
            return 1
        elif stack == s:
            return 0
        
        s = stack
