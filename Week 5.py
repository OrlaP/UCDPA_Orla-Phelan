import re
print(re.findall("#excited", "I am so #excited to present this certificate!"))
#Spliting text
print(re.split("!","Nice place! We should come back!"))
#sub -
print(re.sub("ice\Scream","ice cream","I like ice-cream"))
#replacing red with blue
print(re.sub(r"red","blue", "I have a red car"))
#finding users with digits
print(re.findall(r"User\d","The winners are:User9,UserN,User8"))
#finding non-digits
print(re.findall(r"User\D","The winners are:User9,UserN,User8"))
#finding non-words
print(re.findall("\W\d","The price is:$1,$2,$3"))
#whitespace
print(re.findall("Data\sScience","What is Data Science"))
#Non-White Space
print(re.sub("ice\Scream","ice cream","I like ice-cream"))
