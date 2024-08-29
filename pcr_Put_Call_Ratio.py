# print("\n")
# print("PCR:- put call ratio")
# print("\n")
# print("if pcr is greater then 1 then it is 'BULISH' market ")
# print("\n")
# print("If pcr is smaller then 1 then it is 'BEARISH' market ")
# print("\n")
# print("if pcr is between (0.9 to 1.1) then it is 'sideways' market ")
# print("\n")
print("\n")
print("\n")
print("\n")
a=float(input("enter a 'put OI' value :- "))
b=float(input("enter a 'call OI' value :- "))
pcr=(a)/(b)
print(pcr)
    
if(pcr==(0.9>=1.1)):
    print(" pcr is between (0.9 to 1.1) , it is 'sideways' market ")
elif(pcr>1):
    print(" pcr is greater then 1 , it is 'BULISH' market ")
elif(pcr<1):
    print(" pcr is smaller then 1 , it is 'BEARISH' market ")
else:
    print("invalid error!! try again, Thank you")
    

    
    


        



