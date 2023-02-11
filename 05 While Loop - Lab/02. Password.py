user = input()
passw = input()
text = input()

while text != passw:
    text = input()
else:
    print(f"Welcome {user}!")