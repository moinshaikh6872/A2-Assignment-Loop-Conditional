num = int(input("Enter a number to count its digits: "))
count = 0
temp = abs(num) # Handle negative numbers

if temp == 0:
    count = 1
else:
    while temp > 0:
        count += 1
        temp //= 10

print(f"Number of digits: {count}")
