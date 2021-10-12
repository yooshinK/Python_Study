import random

num_article = 69
index = num_article

l = list(range(index))
print(l)

storyphotography_new = random.sample(l, len(l))
print(storyphotography_new)

print('---------------------------')
for x in range(index):
  print(str(x+1)+' <==> '+str(storyphotography_new[x]+1))
