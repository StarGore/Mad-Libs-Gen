# A very quickly made Mad Libs Generator to get an introduction to Python

from asyncio import loop

loop = 1
while (loop < 5): 
    s1 = input("Choose a name: ")
    s2 = input("Choose a place: ")
    s3 = input("Name a noun: ")
    s4 = input("Choose an adjective: ")

print ("Hello I'm" ,s1, "and I live in" ,s2, "I have a friend named" ,s3, " and I think he is really", s4)

loop = loop + 1