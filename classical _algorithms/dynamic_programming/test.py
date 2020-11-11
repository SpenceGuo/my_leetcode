# 递归方法求斐波那契数列
def fib_recursion(n: int):
    if n < 2:
        return n
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)


# print(fib_recursion(100))


# 动态规划方法求斐波那契数列
def fib_dynamic(n: int):
    # 该数列用于缓存以往结果，以便于复用
    result = list(range(n+1))

    for i in range(n+1):
        if i < 2:
            result[i] = i
        else:
            result[i] = result[i-1] + result[i-2]
    return result[n]


print(fib_dynamic(100))
