num=int(input("Enter the number upto which you want the sum"))

i=0
num_sum=0
while i<=num:
    num_sum=num_sum+i
    i+=1

print(num_sum)


num_sum=0
for i in range (1,num+1):
  num_sum=num_sum+i
print(num_sum)