db1 = [101, 102, 105, 108, 110]
db2 = [105, 199, 101, 115, 105]

common_users = []

for user in db1:
    if user in db2 and user not in common_users:
        common_users.append(user)
print(f"Совпадающие ID: {common_users}")