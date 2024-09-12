def test():
    yield 1
    yield 2
    yield 3
    yield 4
    yield {a: 1, b: 2}

# print(test())
for i in test():
    print(i)
