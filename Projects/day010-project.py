# this is simple countdown program.
import time

count = int(input("Enter the starting number: "))

while count >= 0:
    print(count)
    count -= 1
    
    # this will wait for 1 second before printing the next number
    time.sleep(1)

# this will print the final message
print("Blast off!")

