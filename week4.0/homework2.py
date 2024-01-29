eray = 23
ertugrul = 5
metehan = 2

# True and True
to_compare1 = (eray > ertugrul) and (eray > metehan)
print("True and True"," - ",to_compare1)
print()

# True and False 
to_compare2 = (eray > ertugrul) and (eray < metehan)
print("True and False"," - ",to_compare2)
print()

# False and False
to_compare3 = (eray < ertugrul) and (eray < metehan)
print("False and False"," - ",to_compare3)
print()
print()



# True or True
to_compare4 = (eray > ertugrul) or (eray > metehan)
print("True or True"," - ",to_compare4)
print()

# True or False
to_compare5 = (eray > ertugrul) or (eray < metehan)
print("True or False"," - ",to_compare5)
print()

# False or False
to_compare6 = (eray < ertugrul) or (eray < metehan)
print("False or False"," - ",to_compare6)
print()