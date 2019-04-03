i = 0
base = 10
number = 4672

while True:
    if base ** i > number:
        i -= 1
        break
    i += 1
print(i)

i = 0 

while True:
    if base ** i > number:
        break
    else:
        i += 1

print(i)