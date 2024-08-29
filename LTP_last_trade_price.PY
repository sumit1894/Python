ltp=float(input("Enter a last trade  price:-  "))
lot=int(input("enter a lot value:- "))
lotvalue=ltp*lot
print("your trade price value ",lotvalue)


points=float(input("enter a points value:- "))
delta=float(input("Enter a delta  normal value:- ")) 
PDvalue=points*delta
# print(PDvalue)

var=PDvalue+ltp
ans=var*lot
print("your increased value ",ans)

result=ans-lotvalue
print("The profit are ",result)
