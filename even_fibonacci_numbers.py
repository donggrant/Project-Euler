def solution():
    table = [0 for _ in range(40)]
    table[0] = 1
    table[1] = 1
    for i in range(2, len(table)):
        tmp = table[i-1] + table[i-2]
        if tmp > 4*10**6:
            break
        table[i] = tmp
    ans = 0
    print(table)
    for n in table:
        if n % 2 == 0:
            ans += n
    return ans

print(solution())