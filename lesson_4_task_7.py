def fact(n):
    n = int(4)
    for el in fact(n):
        math.fact(n)
    yield fact(n)
    print(fact(n))  # не пойму почему не принтит О_О

