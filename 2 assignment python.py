Python 3.13.11 (tags/v3.13.11:6278944, Dec  5 2025, 16:26:58) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
Enter "help" below or click "Help" above for more information.
# list creation

1
1
#1
age_list =[24,25,26,27,28]
print(age_list)
[24, 25, 26, 27, 28]
name_list =["aa","bb","cc","dd","ee"]
print(name_list)
['aa', 'bb', 'cc', 'dd', 'ee']

# list operation/modification

name_list.append("yazhini")
print(name_list)
['aa', 'bb', 'cc', 'dd', 'ee', 'yazhini']
age_list.insert(2,30)
print(age_list)
[24, 25, 30, 26, 27, 28]
name_list.remove("yazhini")
print(name_list)
['aa', 'bb', 'cc', 'dd', 'ee']
age_list.pop()
28
age_list.extend(29,30,26)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    age_list.extend(29,30,26)
TypeError: list.extend() takes exactly one argument (3 given)
print(age_list)
[24, 25, 30, 26, 27]
age_list =[24,25,26,27,28]
age_list.extend(29,30,26)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    age_list.extend(29,30,26)
TypeError: list.extend() takes exactly one argument (3 given)
age_list.sort(reverese=true)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    age_list.sort(reverese=true)
NameError: name 'true' is not defined. Did you mean: 'True'?
NameError: name 'true' is not defined. Did you mean: 'True'?
SyntaxError: invalid syntax
>>> age_list.extend([29,30,26])
>>> print(age_list)
[24, 25, 26, 27, 28, 29, 30, 26]
>>> age_list.sort(reverse=True)
>>> print(age_list)
[30, 29, 28, 27, 26, 26, 25, 24]
>>> max_age = max(age_list)
>>> print(max(age_list))
30
>>> min_age = min(age_list)
>>> print(min(age_list))
24
>>> sum_age = sum(age_list)
>>> print(sum(age_list))
215
>>> 
>>> # accessing list elements
>>> 
>>> print(name_list[0])
aa
>>> print(name_list[-1])
ee
>>> name_list=[-1]
>>> print(name_list)
[-1]
>>> print(name_list[2:4])
[]
>>> name_list=["aa","bb","cc","dd","ee"]
>>> print(name_list)
['aa', 'bb', 'cc', 'dd', 'ee']
>>> print(name_list[2:4])
['cc', 'dd']
>>> print(name_list[::-1])
['ee', 'dd', 'cc', 'bb', 'aa']
>>> 
>>> 
>>> 
>>> # dictionary
>>>
student_name = {"aa":50,"bb":89,"cc":67,"dd":90,"ee":82}
print(student_name)
SyntaxError: invalid syntax
student_name = {"aa":50,"bb":89,"cc":67,"dd":90,"ee":82}
print(student_name)
{'aa': 50, 'bb': 89, 'cc': 67, 'dd': 90, 'ee': 82}
student_name["cc"]
67
student_name["janani"]=80
print(student_name)
{'aa': 50, 'bb': 89, 'cc': 67, 'dd': 90, 'ee': 82, 'janani': 80}
student_name["ee"]=99
print(student_name)
{'aa': 50, 'bb': 89, 'cc': 67, 'dd': 90, 'ee': 99, 'janani': 80}
student_name.keys()
dict_keys(['aa', 'bb', 'cc', 'dd', 'ee', 'janani'])
student_name.values()
dict_values([50, 89, 67, 90, 99, 80])
student_name.items()
dict_items([('aa', 50), ('bb', 89), ('cc', 67), ('dd', 90), ('ee', 99), ('janani', 80)])



# sets

my_set ={"a","e","i","o","u","a","a","i"}
print(my_set)
{'u', 'i', 'o', 'e', 'a'}
# set do not allowed duplicate,set is unorderd
my_set[4]="s"
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    my_set[4]="s"
TypeError: 'set' object does not support item assignment
# set is unordered so 4th value doesn't work
set1={1,3,5,7,9}
print(set1)
{1, 3, 5, 7, 9}
set2={2,3,5,8,10}
print(set2)
{2, 3, 5, 8, 10}
set1.union(set2)
{1, 2, 3, 5, 7, 8, 9, 10}
set1.intersection(set2)
{3, 5}



# operations and conditional statements


score =int(input("score(0 to 10): "))
score(0 to 10): 
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    score =int(input("score(0 to 10): "))
ValueError: invalid literal for int() with base 10: ''
score =int(input("score(0 to 10): "))
score(0 to 10): 8
score =int(input("score(0 to 10): "))
score(0 to 10): 
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    score =int(input("score(0 to 10): "))
ValueError: invalid literal for int() with base 10: ''
if score > 7:
    print("above average")
 elif score >= 4:
     
SyntaxError: unindent does not match any outer indentation level
>>> if score > 7:
...     print("above average")
... elif score >= 4:
...     print("average")
... else
SyntaxError: expected ':'
>>> else:
...     
SyntaxError: invalid syntax
>>> if score > 7:
...     print("above average")
... elif score >= 4:
...     print)'average")
...     
SyntaxError: unmatched ')'
>>> if score > 7:
...     print("above average")
... elif score >= 4:
...     print("average")
... else:
...     print("below average")
... 
...     
above average
>>> score =int(input("score(0 to 10): "))
score(0 to 10): 8
>>> if score > 7:
...     print("performance: above average")
... elif score >=4 :
...     print("performance: average")
... else:
...     print("performance: below average")
... 
...     
performance: above average
>>> score =int(input("score(0 to 10): "))
score(0 to 10): 6
>>> if score > 7:
...     print("above average: excellent work ! keep going")
... elif score >=4 :
...     print("average: good effort! keep practicing, there's room for improvement")
... else:
...     print("below average: need to improve your performance, consistent practise will lead to better result")
... 
...     
average: good effort! keep practicing, there's room for improvement
