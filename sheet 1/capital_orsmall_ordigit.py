char=input()
if char.isupper() and char.isalpha():
    print("ALPHA")
    print("IS CAPITAL")
elif char.isdigit():
    print("IS DIGIT")

elif char.islower() and char.isalpha():
    print("ALPHA")
    print("IS SMALL")