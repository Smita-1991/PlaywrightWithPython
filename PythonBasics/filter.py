
# The filter() function takes two arguments: a function and an iterable. It applies the function to each element of the iterable
# and returns a new iterable containing only the elements for which the function returned True.


def even(num):
    if num%2==0:
        return True
    else:
        return False

numbers=[1,2,3,4,5,6,7,8,9]
even_numbers=list(filter(even,numbers))
print(even_numbers)

evenNum=list(filter(lambda x:x%2==0,numbers))
print(evenNum)


numbers=[1,2,3,4,5,6,7,8,9]
greater_than_five=list(filter(lambda x:x>5,numbers))
print(greater_than_five)

### filter with lambda function and multiple conditions
numbers=[1,2,3,4,5,6,7,8,9]
even_greater_than_five=list(filter(lambda x:x>5 and x%2==0,numbers))
print(even_greater_than_five)


people=[
    {'name':'Indira','age':30},
    {'name':'Ravi','age':35},
    {'name':'Sita','age':28}]

def age_greater_than_30(person):
    if person['age']>30:
        return True
    else:
        return False

age_greater_than_30=list(filter(age_greater_than_30,people))
print(age_greater_than_30)