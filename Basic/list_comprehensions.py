nums = [1,2,3,4,5,6,7,8,9,10]
# an alternate list
my_list = []
for n in nums:
	my_list.append(n)

# List comprehension
my_list = [n for n in nums]
print(my_list)

# n*n for each n in nums
# for loop
sq_list = []
for n in nums:
	sq_list.append(n*n)

sq_list = [n*n for n in nums]
print(sq_list)

# n for each 'n' in nums if 'n' is even
even_list = []
for n in nums:
	if n%2 == 0:
		even_list.append(n)

print(even_list)

even_list = [n for n in nums if n%2 == 0]

# (letter, num) pair for each letter in 'abcd' and each number in '0123'
mix_list = []
for letter in 'abcd':
	for number in range(4):
		mix_list.append((letter, number))
#print(mix_list)

mix_list = [(letter, number) for letter in 'abcd' for number in range(4)]
print(mix_list)

# Dic Comp
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
result = set(zip(names, heros))
#print(result)

my_dict = {}
for name, hero in zip(names, heros):
	my_dict[name] = hero
#print(my_dict)

my_dict = {name: hero for name, hero in zip(names, heros)}
print(my_dict)

# Dont add peter
new_dict = {}
for name, hero in zip(names, heros):
	if name != 'Peter':
		new_dict[name] = hero
#print(my_dict)
new_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(my_dict)

# Set comprehensions
my_set = set()
for n in nums:
	my_set.add(n)
print(my_set)
my_set = {n for n in nums}