import re
name = input("Enter name: ")
surname = input("Enter surname: ")

fullname = f"{name} {surname}"

print(fullname)
phone_number_pattern = r"^[0-9]{3} [0-9]{3} [0-9]{3}$"
while True:
    phone_num = input("Enter phone number: ")
    match = re.match(phone_number_pattern, phone_num)
    if match is not None:
        print(f"Your phone number is correct: {phone_num}")
        break
    else:
        print(f"Your phone number is incorrect: {phone_num}")
     