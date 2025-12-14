choice = input("Select option (1 = Encrypt or 2 = Decrypt): ").strip()
message = input("Enter message: ")
key = int(input("Enter key (number of positions to shift): "))

# ASCII ranges
UpperStart = 65
LowerStart = 97

result = ""

# Reverse shift for decryption
if choice == "2":
    key = -key

for char in message:
    if char.isupper():
        newChar = (ord(char) - UpperStart + key) % 26 + UpperStart
        result += chr(newChar)
    elif char.islower():
        newChar = (ord(char) - LowerStart + key) % 26 + LowerStart
        result += chr(newChar)
    else:
        result += char  # non-letter characters stay the same

print(f"Result: {result}")
