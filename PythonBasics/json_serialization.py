import json,csv,time,re

dictionary_data={"name": "Indira", "age": 30}

json_data=json.dumps(dictionary_data)
print(json_data)
print(type(json_data))

'''convert back to dictionary'''
dictionary_data=json.loads(json_data)
print(dictionary_data)
print(type(dictionary_data))

#CSV

with open("new_file.csv","w",newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Indira", 30])

with open("new_file.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)


#time

now=time.time()
print(now)
time.sleep(4)
print(time.time())


# Regular Expressions

pattern=r"\d+"

text="There are 123 apples and 456 oranges. "

match=re.findall(pattern,text)
print("Numbers found:", match)
