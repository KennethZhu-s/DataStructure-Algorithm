import time
from Cal_Time import cal_time

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]


def cut_rod_recursion_1(p, n):  # super slow! O(2^n)
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res = max(res, cut_rod_recursion_1(p, i) + cut_rod_recursion_1(p, n - i))
        return res


@cal_time
def c1(p, n):
    return cut_rod_recursion_1(p, n)


def cut_rod_recursion_2(p, n):  # slow! O(2^n)
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1, n + 1):
            res = max(res, p[i] + cut_rod_recursion_2(p, n - i))
        return res


@cal_time
def c2(p, n):
    return cut_rod_recursion_2(p, n)


@cal_time
def cut_rod_dp(p, n):  # faster! O(n^2)
    r = [0]
    for i in range(1, n + 1):
        res = 0
        for j in range(1, i + 1):
            res = max(res, p[j] + r[i - j])
        r.append(res)
    return r[n]


def cut_rod_extend(p, n):
    r = [0]
    s = [0]
    for i in range(1, n + 1):
        res_r = 0  # record optimized price
        res_s = 0  # record left part associated with best price
        for j in range(1, i + 1):
            if p[j] + r[i - j] > res_r:
                res_r = p[j] + r[i - j]
                res_s = j
        r.append(res_r)
        s.append(res_s)
    return r[n], s


def cut_rod_solution(p, n):
    r, s = cut_rod_extend(p, n)
    ans = []
    while n > 0:
        ans.append(s[n])
        n -= s[n]
    return ans


# print(c1(p, 15))
# print(c2(p, 15))
# print(cut_rod_dp(p, 15))

r, s = cut_rod_extend(p, 20)
print(s)
print(cut_rod_dp(p, 20))
print(cut_rod_solution(p, 20))
