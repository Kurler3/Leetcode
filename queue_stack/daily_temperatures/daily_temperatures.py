def get_answer(temperatures) -> [int]:
    n = len(temperatures)
    result = [0] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and temperatures[i] >= temperatures[stack[-1]]:
            stack.pop()
        if stack:
            result[i] = stack[-1] - i
        stack.append(i)
    return result

if __name__ == '__main__':
    temperatures = [73,74,75,71,69,72,76,73] 
    
    print(get_answer(temperatures)) # [1,1,4,2,1,1,0,0]

    