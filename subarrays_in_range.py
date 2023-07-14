def sub_arrays(array,i,n):
    return array[i:n+1]
array = list(map(int,input("Enter the array elements: ").split()))
b= int(input("ENTER B: "))
c=int(input("ENTER C :"))
print(sub_arrays(array,b,c))