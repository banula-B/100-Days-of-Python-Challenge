# this is simple countdown program.
import time

# asking user for the starting number
count = int(input("Enter the starting number: "))

# this will run the loop until the count becomes 0
while count > 0:
    # this will print the current count
    print(count)
    # this will decrease the count by 1
    count -= 1
    # this will wait for 1 second before printing the next number
    time.sleep(1)

# this will print the final message
print("Blast off!")

