
def string(text):
    return len(text)

def string2(*args):
    result = " ".join(args)
    return result

print(string("hello my name alex"))

print(string2("dota 2 best game","cs-2 too"))

print("-" * 150 )
def int1(*args):
    return [x ** 2 for x in args][0]

print(int1(2))

def int2(*args):
    return sum(args)

print(int2(2,2))

def int3(a,b):
    return divmod(a,b)

print(int3(1, 2))

print("-" * 150 )


def lis1(a):
    if len(a) >= 1:
        return sum(a) / len(a)
    else:
        return 0

print(lis1([2, 4, 6]))


def lis2(a,b):
    result = []
    for x in a :
        if x in b :
            result.append(x)
    return result

print(lis2([1, 2, 3, 4],[3, 4, 5, 6]))

print("-" * 150)

def dict1 (a):
    return a.keys()

print(dict1({"age":10,"name":"alex"}))

def dict2 (a,b):
    return  a | b

print(dict2({"ages":29,"name":"bob"},{"names":"alex","age":30}))

print("-" * 150)

def sets(a,b):
    return a | b

print(sets({1,2,3,4,5},{4,5,6,7,8}))


def sets2(a,b):
    return  a.issubset(b)

print(sets2({1, 2},{1, 2, 3, 4}))

print("-" * 150)

def func1(*args):
    return ["Парне" if i % 2 == 0 else "Не парне" for i in args]

print(func1(1, 2, 3))

def func2(*args):
  result = []
  for i in args:
      if i % 2 == 0:
          result.append(i)
  return result

print(func2(1, 2, 3,4,5,6,7,8))

print("-" * 150)

a = lambda x: "парне" if x % 2 == 0 else "не парне"
print(a(1))
print(a(2))
print(a(3))
print(a(4))
print("-" * 150)