total=0

while True:
    price=float(input("Enter Product Price :: Enter 0 to Exit "))
    if price==0:
        break
    total=total+price
    print("Total Bill :: ",total)


if total>5000:
    discount=total*0.10
    total=total-discount
    print("Discount amount is :: ",discount)

    print("Final Bill :: ",total)