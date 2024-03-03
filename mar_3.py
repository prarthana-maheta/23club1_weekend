# string  ---immutable ---"",''
# list --- mutable--[]
# tuple--- immutable--()

# dictionary 
# key --- value
# key--immutable--unique
# value--mutable,duplicate,iterable
# [1,2,3,4]
# fast seraching
# data reduncing
# [#0,#1,]
# dict1= {
#     "apple":"red",
#     "green":"peach",
#     1:"one",
#     None:"none",
#     "":"empty",
#     "list":[1,2,3,4,56],
#     '[1,4.78]':"list1",
# }
# list1=[1,2,3,4]
# list1[1]
# print(type(dict1))
# print(len(dict1))
# print(list(dict1))
# print(dict(list1))


# print(dict1['[1,4.78'])
# print(dict1.get('[1,4.78',dict1[  1]))


dict1= {
    "apple":"red",
    "green":"peach",
    1:"one",
    None:"none",
    "":"empty",
    "list":[1,2,3,4,56],
    '[1,4.78]':"list1",
}

# print(dict1.keys())
# print(dict1.values())

# a,b=("red","banana","gj")


# for k,v in dict1.items():

#     print(k,v)
# counter=0
# {
#     'one':1,
#     'two':2,
#     'three':3
# }


# adding

# list1=[]
# list1[0]='iiii'
# dict1={}

# dict1['key1']='value1'
# dict1['key2']='value2'

# dict1.update({'key2':[12345],'key4':'value4'},key5='value5')
# print(dict1)

#  Write a Python program to filter the height and weight of students,
#        which are stored in a dictionary.
# Original Dictionary:
# student={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65),
# 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# Height > 6ft and Weight>= 70kg:
# {'Cierra Vega': (6.2, 70)}

# out={}
# for k,v in student:
#     if v[0] >6 and v[1]>=70:
#         out.update({k:v})
# Write a Python script to concatenate the following
# dictionaries to create a new one.

# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# [dict1,dict2,dict3]

# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output:
# {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}



#  Write a Python program to match key values in two dictionaries.
# Sample dictionary: 
#       x={'key1': 1, 'key2': 3, 'key3': 2}, 
#       y={'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y