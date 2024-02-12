tribes = ["Luo", "Chonyi", "Karamojong", "Sukuma", "Kamba"]
print(tribes)

tribes.append("Swahili")
print(tribes)

tribes.pop(2)
print(tribes)

for x in tribes:
    print(x + " are from East Africa.")
