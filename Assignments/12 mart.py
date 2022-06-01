f=[0,1]

for i in range(9):
    f.append(f[i]+f[i+1])

print(f)