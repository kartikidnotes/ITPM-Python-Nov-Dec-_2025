#check the product is in stock or not

prodqty=int(input("Enter Product Quantity : "))
print("In stock " if prodqty>0 else "Out of Stock ")