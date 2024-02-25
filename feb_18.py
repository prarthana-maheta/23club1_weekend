# # # while:
# i=1
# i+=1
# while True:
#     print(i)
#     i +=1
#     if i == 5:
#         # pass
#         # print("------------------")
#         break

# i=1
# while i==1:
#     # print("yes")
#     print(i)
#     i+=1

# if i ==1:
#     for i in range(1,10):
#         print(i)
    
# calculate the sum of five numbers entered by user using while loop
    


# String --immutable--"char"--ordered
# list --mutable--[]--ordered

# # tuple --- immutable --- ordered --- (12,3)

# thistuple = ("apple", "banana", "cherry")
# thistuple = ["apple", "banana", "cherry"]
# print(type(thistuple))


# # # Ordered
# # # When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# # #
# # # Unchangeable
# # # Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# # #
# # # Allow Duplicates


# # # print(type(thistuple))
# # # print(len(thistuple))
# # #print(max(thistuple)) print(min(thistuple)) print(sum(thistuple))
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# tuple(thistuple)

# for i in range(thistuple[len(thistuple)-1:-1:-1]):
#     print(i)

# # # check if present
# thistuple = ("apple", "cherry", "apple")
# if "apple" in thistuple:
#     print("Yes, 'apple' is in the fruits tuple")
# if "cherry" in thistuple:
#     print("yes, 'cherry' in ")

# for i in (1,2,3):
#     print(i)


# # # change tuple value update tuple
# # #
# x = ("apple", "banana", "cherry")
# y =list(x)
# y[0]="kiwi"
# print(tuple(y))
# y = list(x)
# # print(y)
# # y=[x]
# # print(y)
# #
# # # y[0] = "kiwi"
# # #
# # # print(y)
# # # x = tuple(y)
# # #
# # # print(x)


# # # add items to tuple
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple)

# # thistuple = ("apple", "banana", "cherry")
# # y = list(thistuple)
# # y.remove("apple")
# # thistuple = tuple(y)
# # print(thistuple)

# # tuple1 = ('abc','royal','pvt','ltd','Mango')
# # find min and max of this tuple
# # remove all the elements from 'pvt'
# # add ['apple','banana'] to tuple1


# # # # unpack tuple
# # fruits = ["apple", "banana", "cherry"]
# # # #
# # green, yellow, red = fruits
# # # #
# # print(green)
# # print(yellow)
# # print(red)


# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# green, yellow, *red = fruits
# # #
# print(green)
# print(yellow)
# print(red)

# # # tuple method
# # # count,index



# # #loop through tuple
# # # thistuple = ("apple", "banana", "cherry")
# # # for x in thistuple:
# # #     for i in x:
# # #         print(i)
# # #   print(x)

# # # thistuple = ("apple", "banana", "cherry")
# # # for i in range(1,len(thistuple),2):
# # #   print(thistuple[i])


# # # while loop in tuple

# # # thistuple = ("apple", "banana", "cherry","abc")
# # # i = 0
# # # while i < len(thistuple):
# # #     print(thistuple[i])
# # #     i = i + 1


# # # join two tuple 
# tuple1 = [1,2,3]
# tuple2 = [1, 2, 3]

# tuple3 = tuple1*2
# print(tuple3)

# # l1=["hello"]
# # print(l1+l1)

# # # Multiply two tuple
# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2
# print(mytuple)





# # # thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# # #
# # # x = thistuple.count(5)
# # #
# # # print(x)
# # #
# # # thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# # #
# # # x = thistuple.index(8)
# # #
# # # print(x)

# Write a Python program to remove an item from a tuple.


# Write a Python program to replace the last value of tuples in a list.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]


# Write a Python program to remove an empty tuple(s) from a list of tuples.
# s1=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# # Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
# s2=[]
# for i in s1:
#     if len(i) >0:
#         print(i)
#         s2.append(i)
# print(s2)


# Write a Python program to convert a tuple of
# string values to a tuple of integer values.
# Original tuple values:
t1=(('333', '33'), ('1416', '55'))
# New tuple values:
# ((333, 33), (1416, 55))
# t2=list(t1)
# for i in t2:
# t2=[]
# for i in t1:
#     list1=[]
#     for j in i:
#         list1.append(int(j))
#     t2.append(tuple(list1))
# print(tuple(t2))

# print(isinstance(123,str))
# Write a Python program to convert a given tuple
# of positive integers into an integer.
# Original tuple:
# (1, 2, 3)
# Convert the said tuple of positive integers into an integer:
# 123
# Original tuple:
# (10, 20, 40, 5, 70)
# Convert the said tuple of positive integers into an integer:
# 102040570