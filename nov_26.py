s1 = 'DtDudents of this batch are going to rock the INDIAN software industry?'
# s2 = "What is ß"

# print(s2.lower())
# print(s1)
# print(s1.casefold())

# s3 = s1.center()
# print(s1.center(1000,"a"))
#
# print(s1.rjust(100, "*"))
# print(s1.ljust(100, "-"))
# # print(s3)
# # Alignment related methods
# """
# s3 = s1.center(100)
# print(s1.center(100, "-"))
# print(s1.rjust(100, "*"))
# print(s1.ljust(100, "-"))
#
# print("-" * 102)
# print("|" + "Welcome to our software!".center(100,'\') + "|")
# print("-" * 102)
# """
#
#
#

s1 = 'DtDudents of this batch are DtDgoing to rock the INDIAN software industry?'
# print(s1.count("a"))
# print(s1.count("are"))
# # print(s1.count("europe"))
# #
# # print(s1.count("z", 20))
# # print(s1.count("e", 20, 40))
# print(s1[-1])
# print(s1.count("e"))


# s1 = 'stDudents of this batch are going to rock the INDIAN software industry?'
# # s2=s1.encode()
# s2=s1.encode('utf-16')
# print(s2)
# print(s2.decode('utf-16'))
# s2.lower()
# print(s2)
# print(type(s2))
# print(s1.encode("utf-16"))

s1 = 'try !stDudents of this batch are going to rock the INDIAN software industry?is'
# print(s1.endswith("?"))
# print(s1.startswith("try!"))
# print(s1.endswith("is", -40))
# s1.endswith("s", 40, 60)


#
# # print(s1.startswith("s"))
# # print(s1.startswith("t", 1,3))

s1 = 'try D!students of this batch are going to rock the INIAN software industry?is'
# print(s1.find("D"))
# # print(s1.find("e"))
# print(s1.index("D",10,15))
# print(s1.rfind("D"))
# # print(s1.lfind("D"))
# print(s1.rindex("D"))
# print(s1.lindex("D"))
#
# """
# print(s1.find("D"))
# print(s1.find("e"))
# print(s1.find("rock"))
#
# a = s1.find("e")
# print(s1.find("e", a+1))
#
# print(s1.find("e", 5))
# print(s1.find("e", 5, 30))
#
# print(s1.find("e", 5, -5))
# print(s1.find("Python"))
#
# print()
#
# print(s1.index("D"))
# print(s1.index("e"))
# print(s1.index("rock"))
#
# a = s1.index("e")
# print(s1.index("e", a+1))
#
# print(s1.index("e", 5))
# print(s1.index("e", 5, 30))
#
# print(s1.index("e", 5, -5))
# print(s1.index("Python"))
#
#
# print(s1.rfind("e"))
# print(s1.rfind("are", 20, -3))
# print(s1.rindex("D"))
# print(s1.rindex("r", 20, -20))
# """
#
#
#
s1 = "Abc"
s2 = "5⁴"
s3 = "②⓪②②"
s4 = "½"
s5 = "二千二十二"
# #
# # # methods starting from is: All these methods return True or False
# #
# print(s1.isupper())
# print(s1.islower())
# print(s1.istitle())

s1 = "二千二十"
s2 = "AlakhPandya"
s3 = "9876543210"
s4 = "AlakhPandya9876543210"
s5 = "5⁴"
s6 = "②⓪②②"
s7 = "½"
s8 = "二千二十二"
# print(s2.isnumeric())
# print(s2.isalpha())
# print(s4.isalnum())
# print(s3.isdecimal())
# print(s7.isnumeric())
# print(s3.isdigit())
# print(s6.isdigit())
# print(s8.isascii())
# # #
# # #
# # # s5 = "₹5000"
# s6 = "ab     dh"
# print(s6.isidentifier())
# # # #
# # # # #
# s7 = "abc\\n"
# # print(s7.isspace())
# print(s7.isprintable())
# # # #
# # # """
# # # The difference between isnumeric, isdigit & isdecimal
# # # """
# # # """
# # # print(s4.isdecimal())   # only recognizes digits from 0 to 9 and nothing else.
# # # print(s4.isdigit())     # also recognizes subscript, superscript, circled numbers
# # # print(s4.isnumeric())   # also recognizes roman numerals, vulgar fractions, digits from other languages
# # # 1/2
# # # print(s5.isnumeric())
# # # """
# # #
# # #
# # #
# # #
# # #
# # # # list(strings)
# # # # s1=[] datatype list

s6 = 'students of this batch are going to rock the indian software industry!Because they are very sincere.They also do their homework on time.        '
print(s6)
print(s6.split(" "))
# # print(s6.split("are")) #return list
# # # print(s6.split("z"))
# # print(s6.split(" ", 4))
# # # # # #
# # print(s6.rsplit(" ",3))
# # # # # print(s6.split(" "))
# # # #
# # # # # # print(s6)
# print(s6.split("are"))
# print(s6.splitlines())
# print(s6.partition("are"))


# # #
# # # # s7 = "Harsh is a good boy.
# # # # But, this sentence has an error."
# # #


s6 = 'students of this batch are going to rock the indian software industry!Because they are very sincere.They also do their homework on time.        '
# print(s6)

# s8 = "--"
print(s6.split(" "))
s9 = '*'.join(s6.split(" "))
print(s9)
# s9 = s8.join(s6.split(" "))
# print(s9)

# s1="   a b     c   b\n"
# print(s1.strip())

# s1= "abc"
# print(s1)
# print(s1.replace("a","b"))
# # #
# # # # print(" ".join(s8))
# # #
# # # s6 = '            students         of this batch are going batch are to rock the indian software industry!         '
# # # # print(s6.partition("batch"))
# # # # print(s6.partition("are are")) #return tuple
# # # # print(s6.rpartition("batch"))
# # #
# # # # print(s6.strip("s"))
# # # s8 = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Happy$$Birthday!$$$$$$$$$$$$$$$$$"
# # #
# # # print(s8.replace("$", " "))
# #
# # """
# #
# # s8 = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Happy$$Birthday!$$$$$$$$$$$$$$$$$"
# # print(s8.lstrip("$"))
# # print(s8.rstrip("$"))
# # print(s8.strip("$"))
# # """
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
