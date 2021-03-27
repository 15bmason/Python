z=[]
f = open("EloCount.txt")
contents = f.read()
lists = contents.splitlines()
for i in lists:
    print(i)
    for j in i:
        if j.isdigit():
            z.append(j)
print(z)
f.close()
