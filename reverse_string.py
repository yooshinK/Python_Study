names = ['yooshinK','Keroro']

name1 = 'yooshinK'
name2 = str('Noah')

names.reverse()
print(names)
# print(names.reverse) -> Result: None

s_reverse = ''
for char in name2:
    s_reverse = char + s_reverse
print(s_reverse) # Result: haoN

s_list = list(name1)
s_list.reverse()
print(s_list) # Result: ['K', 'n', 'i', 'h', 's', 'o', 'o', 'y']
print(''.join(s_list)) # Result: Knihsooy
print(''.join(reversed(name2))) # Result: haoN
