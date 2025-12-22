total = 0
i = 1

while i <= 5:
    price = float(input(f"Enter price of product {i}: "))
    if price >= 0:
        total = total + price
        i = i + 1
    else:
        print("Invalid price! Please enter a positive number.")


gst = total * 0.18
final_bill = total + gst

print("\n--- Bill Summary ---")
print("Subtotal:", total)
print("GST (18%):", gst)
print("Total Bill:", final_bill)