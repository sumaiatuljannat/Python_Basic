import os
f=open("sumaia.txt","w")
f.write("Sumaia is a good girl\n")
f.write("It would be the great day of my life\n")
f.write("you should walk away")
f.close()
print("File written Successfully")

f=open("sumaia.txt","r")
content=f.read()
f.close()

print(content)

f=open("sumaia.txt","r")
first_line=f.readline()
f.close()
print(first_line)

with open("sumaia.txt", "r") as f:
    for line in f:
        print(line.strip())