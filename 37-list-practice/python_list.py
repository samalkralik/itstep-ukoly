Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
furniture=['table', 'chair', 'rack','shelf']
furniture[0:3]
['table', 'chair', 'rack']
furniture[1:4]
['chair', 'rack', 'shelf']
furniture[0:-1]
['table', 'chair', 'rack']
furniture[:1]
['table']
furniture[1:]
['chair', 'rack', 'shelf']
furniture[:-1]
['table', 'chair', 'rack']
furniture[:]
['table', 'chair', 'rack', 'shelf']

spam = ['cat','bat', 'rat', 'spider']
spam
['cat', 'bat', 'rat', 'spider']
spam2=spam[:]
spam2
['cat', 'bat', 'rat', 'spider']
spam2[:]
['cat', 'bat', 'rat', 'spider']
spam.append('dog')
spam2
['cat', 'bat', 'rat', 'spider']
spam
['cat', 'bat', 'rat', 'spider', 'dog']
len(spam)
5
spam[-1]='fox'
spam
['cat', 'bat', 'rat', 'spider', 'fox']
spam[2]=spam[0]
spam
['cat', 'bat', 'cat', 'spider', 'fox']

for item in spam:
    print(item)

    
cat
bat
cat
spider
fox

my_list = [1,2,3,4,5]
my_list = my_list + [s,g,h,j]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    my_list = my_list + [s,g,h,j]
NameError: name 's' is not defined
my_list= my_list = [A, B, C, D, E]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    my_list= my_list = [A, B, C, D, E]
NameError: name 'A' is not defined
my_list= my_list + [A, B, C, D, E]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    my_list= my_list + [A, B, C, D, E]
NameError: name 'A' is not defined
my_list= my_list + ['A', 'B', 'C']
my_list
[1, 2, 3, 4, 5, 'A', 'B', 'C']
['a', 'b','c']*3
['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']






















spam
['cat', 'bat', 'cat', 'spider', 'fox']
for index, item in enumerate(spam):
    print(f'index: {index} - item: {item}')

    
index: 0 - item: cat
index: 1 - item: bat
index: 2 - item: cat
index: 3 - item: spider
index: 4 - item: fox
for index, item in enumerate(furniture):
    print(f'index: {index} - item: {item}')

    
index: 0 - item: table
index: 1 - item: chair
index: 2 - item: rack
index: 3 - item: shelf
index: 3 - item: shelf
SyntaxError: invalid syntax

for item in spam:
    print(f'index: {index} - item: {item}')
    index += 1

    
index: 3 - item: cat
index: 4 - item: bat
index: 5 - item: cat
index: 6 - item: spider
index: 7 - item: fox



furniture
['table', 'chair', 'rack', 'shelf']
price=[100,50,45,70]
for item,amount in zip(furniture,price):
    print(f'the {item} costs ${amount}')

    
the table costs $100
the chair costs $50
the rack costs $45
the shelf costs $70
# zip -  brings two lists together side by side
colors = ["red", "brown", "blue","pink"]
for item, amount, color in zip(furniture, price, colors):
    print(f'the {color} {item} costs ${amount}')

SyntaxError: multiple statements found while compiling a single statement
colors = ["red", "brown", "blue", "pink"]
for item, amount, color in zip(furniture, price, colors):
    print(f'the {color} {item} costs ${amount}')

    
the red table costs $100
the brown chair costs $50
the blue rack costs $45
the pink shelf costs $70

#in and not in
furniture
['table', 'chair', 'rack', 'shelf']
'bed'in furniture
False
'bed' not in furniture
True

furniture
['table', 'chair', 'rack', 'shelf']
table, chair, rack, shelf = furniture
table
'table'
chair
'chair'
rack
'rack'
shelf
'shelf'

a,b = 'table', 'rack'
a,b=b,a
print(a)
rack
print(b)
table
a
'rack'

furniture
['table', 'chair', 'rack', 'shelf']
furniture.index('rack')
2
furniture.insert(1, 'bed')
furniture
['table', 'bed', 'chair', 'rack', 'shelf']
furniture.append('sofa')
furniture
['table', 'bed', 'chair', 'rack', 'shelf', 'sofa']
del furniture[2]
furniture
['table', 'bed', 'rack', 'shelf', 'sofa']
furniture.remove('sofa')
furniture
['table', 'bed', 'rack', 'shelf']
furniture.pop()
'shelf'
furniture
['table', 'bed', 'rack']
furniture.pop(0)
'table'
furniture
['bed', 'rack']
furniture=['table', 'bed', 'chair', 'rack', 'shelf']
furniture
['table', 'bed', 'chair', 'rack', 'shelf']
furniture.sort()
furniture
['bed', 'chair', 'rack', 'shelf', 'table']
furniture.sort(reverse=True)
furniture
['table', 'shelf', 'rack', 'chair', 'bed']
numbers = [ 5,5.5,-6,89,12]
numbers.sort()
numbers
[-6, 5, 5.5, 12, 89]
numbers.sort(reverse=True)
numbers
[89, 12, 5.5, 5, -6]
sorted(furniture)
['bed', 'chair', 'rack', 'shelf', 'table']


#tuple, list
tuple(['cat', 'dog', 55])
('cat', 'dog', 55)
tuple
<class 'tuple'>
list((
KeyboardInterrupt
list((55,5,555))
[55, 5, 555]
list('hello')
['h', 'e', 'l', 'l', 'o']
>>> list(44,55,5)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    list(44,55,5)
TypeError: list expected at most 1 argument, got 3
>>> 
>>> 
>>> 
>>> furniture
['table', 'shelf', 'rack', 'chair', 'bed']
>>> furniture.count()
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    furniture.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> furniture.count('bed')
1
>>> furniture.append('rack')
>>> furniture.count('rack')
2
>>> furniture.reverse()
>>> 
>>> furniture
['rack', 'bed', 'chair', 'rack', 'shelf', 'table']
>>> furniture.sort(reverse=True)
>>> furniture
['table', 'shelf', 'rack', 'rack', 'chair', 'bed']
