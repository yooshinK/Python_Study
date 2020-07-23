members1 = ['keroro','dororo','tamama']
members2 = ['keroro1','dororo1','tamama1']

i = 0
j = 0

# while
while i < len(members1):
    print(members1[i]+" ")
    i+=1
    pass
print("-----------------------------")

# for with range
for k in range(3): # k is automatically set as 0
    print(members2[k]+" "+ str(j))
    j += 1
    pass
    
print("-----------------------------")
# for with container
for member in members2: # member is automatically set as 0
    print(member+" "+ str(j))
    j += 1
    pass
