def solution():
    multiples = set()
    for i in range(3, 1000):
        if i % 3 == 0:
            multiples.add(i)
        elif i % 5 == 0:
            multiples.add(i)
    return sum(multiples)

print(solution())




