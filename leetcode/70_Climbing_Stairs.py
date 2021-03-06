# 70. Climbing Stairs easy
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.
#
# Example 1:
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
def climbStairs(self, n: int) -> int:
    self.dict = {}
    return self.mem_recursion(n)
    # return self.iterative(n)


def mem_recursion(self, n: int, i: int = 0) -> int:
    # If 1 step left, only take 1 step
    if n == 1: return 1
    # If 2 steps left, there are 2 possible step paths.
    # 1 step + 1 step OR 2 steps
    if n == 2: return 2

    if n in self.dict:
        return self.dict[n]

    self.dict[n] = self.mem_recursion(n - 1) + self.mem_recursion(n - 2)
    return self.dict[n]


def iterative(self, n: int, i: int = 0) -> int:
    arr = [0] * (n + 1)
    arr[0] = 1
    arr[1] = 1

    for i in range(2, n + 1):
        arr[i] = (arr[i - 1] + arr[i - 2])

    return arr[n]


