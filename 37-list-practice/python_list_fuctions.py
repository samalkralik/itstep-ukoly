Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
squares =[]
squares
[]
for x in range(10):
    squares.append(x**2)

    
squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

addition = []
for x in range(100)
SyntaxError: expected ':'
for x in range(100):
    addition.append(x+20)

    
addition
[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]
addition.clear()
addition
[]
for x in range(5):
    addition.append(x++10)

    
addition
[10, 11, 12, 13, 14]
for x in range(5):
    addition.append(x+10)

    
addition
[10, 11, 12, 13, 14, 10, 11, 12, 13, 14]
addition
[10, 11, 12, 13, 14, 10, 11, 12, 13, 14]
addition.pop()
14

combs = []
for x in [1,2,3]:
    for y in [4,5,6]:
        if x != y:
            combs.append((x,y))

            
combs
[(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
[(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
[(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]

vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]
[-8, -4, 0, 4, 8]
[x/4 for x in vec]
[-1.0, -0.5, 0.0, 0.5, 1.0]
del vec[:]
vec
[]


tel = {'jack':4088, 'luke':5874}
tel['ben']=1452
tel
{'jack': 4088, 'luke': 5874, 'ben': 1452}
tel[luke']
    
SyntaxError: unterminated string literal (detected at line 1)
tel['luke']
    
5874
del tel['jack']
    
tel
    
{'luke': 5874, 'ben': 1452}
'ben'in tel
...     
True
>>> tel['anna'] = 89564
...     
>>> list(tel)
...     
['luke', 'ben', 'anna']
>>> tel
...     
{'luke': 5874, 'ben': 1452, 'anna': 89564}
>>> 
>>> dict(lara=78945, karla = 897, matt=7854)
...     
{'lara': 78945, 'karla': 897, 'matt': 7854}
>>> dict
...     
<class 'dict'>
>>> 
>>> 
>>> 
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
...     
>>> knights
...     
{'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k,v in knights.items():
...     print(k,v)
... 
...     
gallahad the pure
robin the brave
