#for val in sequence:
    #loop body 

n="hello"
for i in n:
    print(i)
#for loop stynax
for i in range (10):
    print(i)

n=int(input('enter a number whose sum you want to find'))
sum=0
for i in range(1,n+1):
    sum=sum+i
    print("\n sum=",sum)
#reverse the string
str=input("please enter your str")
str2=""
for i in str:
    str2=i+str2
    print("\n str",str)
    print("reverse string  is",str2)
