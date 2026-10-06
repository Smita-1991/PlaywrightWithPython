fruits=["Banana","Mango","Orange","Apple","Grapes"]
print(fruits)
print(fruits[0:])
print(fruits[::2])
fruits[1]="Papaya"
print(fruits)

#List Methods

fruits.append("Pineapple") # Add an item to the end of the list
print(fruits)
fruits.insert(1,"Watermelon") # Add an item at the specified index
print(fruits)
fruits.remove("Banana") # Remove the specific item with the specified value
print(fruits)
fruits.pop() # Remove the last item in the list
print(fruits)
fruits.sort() # Sort the list in ascending order
print(fruits)
index=fruits.index("Orange") # Get the index of the specified item
print(index)
fruits.reverse() # Reverse the order of the list
print(fruits)
fruits.clear() # Remove all items from the list
print(fruits)

## slicing list
numbers=[1,2,3,4,5]
print(numbers[0:3]) # last number is not included
print(numbers[::2])
print(numbers[::-1]) # reverse the list

## List Iteration
for num in numbers:
    print(num)

## Iteration using index
for index,num in enumerate(numbers):
    print(index,num)

## List comprehension
squared_numbers=[num**2 for num in numbers]
print(squared_numbers)

##Even numbers using list comprehension
even_number=[num for num in numbers if num%2==0]
print(even_number)

##Prime numbers using list comprehension

prime_numbers=[num for num in range(1,10) if num%2==0]
print(prime_numbers)


isprime=False
prime_numbers=[]
for num in range(1,10):
    if num==1:
        prime_numbers.append(num)
    else:
        for i in range(2,num):
            if num%i==0:
                isprime=False
                break
            else:
                isprime=True
        if isprime:
            prime_numbers.append(num)
print(prime_numbers)


##Nested list comprehension
list1=[1,2,3,4]
list2=['a','b','c','d']
nested_list=[(num,letter) for num in list1 for letter in list2]
print(nested_list)

## List comprehension with function calls
words=["hello","Indira","there"]
word_len=[len(word) for word in words]
print(word_len)