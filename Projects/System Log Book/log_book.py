print(" =======System Log Book======= ")

log_level= input("Enter the log level(INFO/WARNING/ERROR):").strip().upper()
log_message= input("Enter your log message: ").strip()


if not log_level or not log_message:
    print("Log level and message can't be empty")
else:
    with open("system_log","a+") as file:
        file.write(f"[{log_level}] - {log_message}\n")
    print("Log entry added successfully")

with open("system_log","r") as file:
    print("\n---Current Log---")
    print(file.read())