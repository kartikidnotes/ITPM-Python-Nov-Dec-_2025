# check the price of data plan 

plan=input("Enter plan (Basic,Standard,Premium : ) : ")

if plan=="Basic":
    print("==="*10)
    print("Price is ₹ 200")
elif plan=="Standard":
    print("==="*10)
    print("Price is ₹ 399")
elif plan=="Premium":
    print("==="*10)
    print("Price is ₹ 499")
else:
    print("==="*10)
    print("Invalid Plan ")
