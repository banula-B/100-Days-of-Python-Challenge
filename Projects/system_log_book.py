print("==========System Log Book==========\n")

log_level = input("Enter Log Level[INFO|WARNING|ERROR]: ").upper()
log_message = input("Enter Log Message: ").capitalize()

if not log_level:
    print("Log Level is Empty. Please Enter Log Level! ")

if not log_message:
    print("Log Message is Empty. Please Enter Log Message! ")

log_entry = f"[{log_level}]:{log_message}"

with open(r"Resources/text files/system_log.txt", "a") as file:
    file.write(f"{log_entry}\n")
    print("Success!. Log entry saved.")


print("")
print("==========System Log Book==========")

with open(r"Resources/text files/system_log.txt", "r") as file:
    log = file.readlines()
    for line in log:
        print(line)

