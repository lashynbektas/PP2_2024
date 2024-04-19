#1
def rectangle_area(length, width):

    return length * width

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = rectangle_area(length, width)
print("The area of the rectagle is:", area)



#2
import json


with open('data.json', 'r') as file:
    data = json.load(file)


for person in data:
    print("Name:", person['name'])
    print("Email:", person['email'])




#3
    
import re

def match_word_beginning(pattern, string):
   
    if re.match(pattern, string):
        return "Found a match!"
    else:
        return "Not matched!"



