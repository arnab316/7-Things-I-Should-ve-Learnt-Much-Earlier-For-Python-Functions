def add(a:int, b:int):
    return a+b;


# print(add(5, 6))    
# def test2(a:str, b:bool, c:dict[str,str]) -> dict[str,int]:

def magic(*args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)

# magic(1, 2, 3, a=4, b=5, c=['apple', 'kiwi'])
# all positional arguments are caught as a tuple args
# all keyword arguments are caught as a dict kwargs


# add = lambda a, b: a+b shorter like es6 arrow function


