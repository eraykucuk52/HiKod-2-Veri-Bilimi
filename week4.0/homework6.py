value = "0123456789" 

even_number = [] 
odd_number = []

for i in value:
    if (int(i) % 2) == 0:
        even_number.append(i)
    
    else:
        odd_number.append(i)

a = ""
for i in even_number:
    a += i

b = ""
for i in odd_number:
    b += i

print(repr(a),",",repr(b))
