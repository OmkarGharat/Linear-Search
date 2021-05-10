# Linear Search

a = [5,28,15,31,27,54,14,6,87]

x = int(input('Enter the number that you want to search in list : '))

for i in range(0,len(a)):
    if x == a[i] :
        print(x,"is found in ",a)
        print("location of ",x,"according to python is",i)
        print("location of ",x,"according to user is",i+1)
        break
    if x not in a :
        print(x,"is not present in",a)
