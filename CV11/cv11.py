import csv

users = []

with open(file="cv11/users.csv", mode="r", newline="")as file:
    reader = csv.reader(file)
    for row in reader: 
        print(row)
    
    if row[0] != "Jane Smith":
        users.append(row)

    new_user = ["John Kokot", 30, "JohnDoe@kokot.cz"]
    users.append(new_user)
    with open(file="cv11/users2.csv", mode="w", newline="")as file2:
        writer = csv.writer(file2)
        file2.write("name,age,email\n")
        writer.writerows(users)


