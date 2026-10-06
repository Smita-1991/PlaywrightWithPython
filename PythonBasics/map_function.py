from PlaywrightWithPython.PythonBasics.list import words


def square_fun(x):
    square=x*x
    return square

square=square_fun(5)
print(square)

# If we want to use map function to get the square of the list of numbers we can do it as follows

square1=lambda x:x*2

numbers = [1, 2, 3, 4, 5]
squares = list(map(square1, numbers))
print(squares)


number1=[1, 2, 3, 4, 5]
number2=[4, 5, 6, 7, 8]

sums=list(map(lambda x,y:x+y, number1, number2))
print(sums)


string_num=["1", "2", "3", "4", "5"]
int_num=list(map(int,string_num))
print(int_num)

words=["hello","Indira","there"]
cap_word=list(map(lambda word:word.upper(), words))
print(cap_word)

len_word=list(map(lambda word:len(word),words))
print(len_word)


def getName(person):
    return person['name']

people=[
    {'name':'Indira','age':30},
    {'name':'Ravi','age':25},
    {'name':'Sita','age':28}
]
names=list(map(getName, people))
print(names)
