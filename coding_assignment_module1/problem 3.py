list=list(eval(input("Enter a list of numbers")))
print(list)
n=len(list)
ele=int(input ("enter search"))
first=0
last=n-1
flag=0
while(first<=last):
     mid=((first+last)//2)
     if(list[mid]<ele):
         first=mid+1
     elif(list[mid]>ele):
         last=mid-1
     elif(list[mid]==ele):
         print("Element",ele,"is found in position",mid)
         flag=1
         break
if(flag==0):
     print("Element absent")