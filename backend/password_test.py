import bcrypt

password = "123456"

hashed_password = bcrypt.hashpw(
    password.encode('utf-8'),
    bcrypt.gensalt()
)

print("Stored Password:")
print(hashed_password)

result = bcrypt.checkpw(
    password.encode('utf-8'),
    hashed_password
)

print(result)