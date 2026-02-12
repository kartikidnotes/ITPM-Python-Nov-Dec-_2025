# Design a console-based Dmart Billing System in Python.
# The program should:
# 1. Ask customer name
# 2. Ask product category:
# Grocery
# Electronics
# Clothing
# 3. Take purchase amount
# 4. Apply discount based on category:
# Grocery → 5%
# Clothing → 10%
# Electronics → 15% (only if amount > 5000)
# 5. If final bill > ₹10,000 → add 8% GST
# 6. Display:
# Customer Name
# Category
# Original Amount
# Discount
# GST (if any)
# Final Payable Amount




print("================ Dmart Billing System ==========================")

name=input("Enter Name of Customer : ")
category=input("Enter Category (grocery/electronics/clothing ) : ")
amount=float(input("Enter Purchase Amount : ₹"))

discount=0
gst=0

if category=="grocery":
    discount=amount*0.05
elif category=="clothing":
    discount=amount*0.10
elif category=="electronics":
    if amount>5000:
        discount=amount*0.15
    else:
        discount=0
else:
    print("Please give a category !! ")
    exit()

#applying GST
final_amount=amount-discount

if final_amount>10000:
    gst=final_amount*0.08
    final_amount=final_amount+gst


#bill details 
print("\n \n ================= Bill Details =======================\n\n")
print("Customer Name : ",name)
print("Category : ",category)
print("Original Amount : ₹",amount)
print("Discounted Amount : ₹",discount)
print("GST : ₹",gst)
print("Final Amount to be Paid : ₹",final_amount)
print("=================================================")
