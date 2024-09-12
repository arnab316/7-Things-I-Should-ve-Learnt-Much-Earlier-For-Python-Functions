def add_exclamation(func):
  def wrapper(name):
    return func(name) + '!'
  return wrapper
@add_exclamation
def hello(name):
    return 'Hello ' + name


# hello = add_exclamation(hello)
print(hello('tom'))


