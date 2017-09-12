Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #pp 43-49
In Exercises 1 through 4, determine the output displayed by the lines of code
#ques-1
SyntaxError: invalid syntax
>>> print("python")
python
>>> #2
>>> var="Ernie"
>>> print (var)
Ernie
>>> #In Exercises 5 through 46, determine the value of the expression.
>>> #5
>>> "python"[4]
'o'
>>> "python"[4]
'o'
>>> "python"[-3]
'h'
>>> "python"[0:3]
'pyt'
>>> "python"[:2]
'py'
>>> "python"[-3:-2]
'h'
>>> "python"[2:-2]
'th'
>>> "python"[:]
'python'
>>> "python".find("tho")
2
>>> "python".find("oh")
-1
>>> "whippersnapper".rfind("pp")
10
>>> "Mississippi".find("ss")
2
>>> "colonel".find("k")
-1
>>> 
>>> "Knickknack".count('k')
3
>>> "8 Ball".lower()
'8 ball'
>>> "8 Ball".upper()
'8 BALL'
>>> "Python"[3:len("Python")]
'hon'
>>> "the artist".title()
'The Artist'
>>> len("Grand Hotel"[:6].rstrip())
5
>>> "let it go".title().find('G')
7
>>> "Amazon".lower().count('a')
2
>>> "King kONG".title()
'King Kong'
>>> 
>>> #In Exercises 47 through 70, determine the output displayed by the lines of code.
>>> a=4
>>> b=6
>>> c="Municipality"
>>> d="pal"
>>> print(len(c))
12
>>> print(c.upper())
MUNICIPALITY
>>> print(c[a:b]+c[b+4:])
city
>>> print(c.find(d))
6
>>> #ques: 49
>>> print("f" + "lute")
flute
>>> #ques: 51
>>> print("Your age is " + str(21) + ".")
Your age is 21.
>>> #ques: 53
>>> r = "A ROSE"
>>> b = " IS "
>>> print(r + b + r + b + r)
A ROSE IS A ROSE IS A ROSE
>>> 
>>> #ques: 55
>>> var = "WALLA"
>>> var += var
>>> print(var)
WALLAWALLA
>>> 
>>> #ques: 57
>>> str1 = "good"
>>> str1 += "bye"
>>> print(str1)
goodbye
>>> 
>>> #ques: 59
>>> print('M' + ('m' * 6) + '.')
Mmmmmmm.
>>> 
>>> #ques: 61
>>> print('a' + (" " * 5) + 'b')
a     b
>>> #ques: 63
>>> s = "trombones"
>>> n = 76
>>> print(n, s)
(76, 'trombones')
>>> 
>>> #ques: 65
>>> num = input("Enter an integer: ")
Enter an integer: 7
>>> print('1' + str(num))
17
>>> 
>>> #ques: 67
>>> num = float(input("Enter a number: "))
Enter a number: 7
>>> print(1 + num)
8.0
>>> #ques: 69
>>> film = "the great gatsby".title()[:10].rstrip()
>>> print(film, len(film))
('The Great', 9)
>>> 
>>> #ques: 71
>>> #Give a simple expression that lops off the last character of a string.
>>> fruit= “apple”
SyntaxError: invalid syntax
>>> fruit= ("apple")
>>> print(fruit[0:4])
appl
>>> 
>>> #ques: 73
>>> #What is the negative index of the first character in a string of eight characters?
>>> #answer:  -8
>>> 
>>> #ques:75. (True or false) If n is the length of str1, then str1[n – 1:] is the string consisting of the last character of str1.
Ans: True

SyntaxError: invalid syntax
>>> 
>>> #ques: 77
>>> #(True or false) str1[:n] consists of the first n characters of str1.
>>> #Answer: True
>>> 
>>> # In Exercises 79 through 92, identify all errors.
>>> #ques: 79
>>> phoneNumber = 234-5678
>>> print("My phone number" + phoneNumber)

Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    print("My phone number" + phoneNumber)
TypeError: cannot concatenate 'str' and 'int' objects
>>>  #error: variable ‘phoneNumber’ must be of type str, and not int for the concatenation to take place.
>>> 
>>> 
>>> #ques: 81
>>> 
>>> for = "happily ever after."
SyntaxError: invalid syntax
>>> 
>>> #ERROR: The error is in line 1 ‘for = "happily ever after."’ because it contains an invalid syntax using ‘for’ as ‘for’ is used only for looping purposes and is a pre-defined term.
>>> 
>>> 
>>> #Ques : 83
>>> print('Say it ain't so.')
      
SyntaxError: invalid syntax
>>> #ERROR : The error lies in the word “ain’t” since it contains a single apostrophe which makes the syntax for printing a string totally incorrect.
>>> 
>>> #Ques: 85
>>> print("Python".Upper())

Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    print("Python".Upper())
AttributeError: 'str' object has no attribute 'Upper'
>>> #ERROR : The attribute must be ‘upper()’ instead of ‘Upper()’.
>>> 
>>> 
>>> #Ques: 87
>>> age= 19
>>> print("Age:" + age)

Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    print("Age:" + age)
TypeError: cannot concatenate 'str' and 'int' objects
>>> #ERROR: The error lies in line 2 ‘print("Age: " + age)’ because the variable age must be of type str, and not int.
>>> 
>>> #Ques: 89
>>> num=1234
>>> print(num.find('2'))

Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    print(num.find('2'))
AttributeError: 'int' object has no attribute 'find'
>>> #ERROR: The error is in line 2 print(num.find('2')) because the 'int' object has no attribute 'find'.
>>> 
>>> 
>>> #Ques: 91
>>> language= "Python"
>>> print(language[8])

Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    print(language[8])
IndexError: string index out of range
>>> #ERROR: The error is in line 2 because the string index is out of range.
>>> 
>>> #Ques: 97
>>> # Distance from a Storm If n is the number of seconds between lightning and thunder, the storm is n/5 miles away. Write a program that requests the number of seconds between lightning and thunder and reports the distance from the storm rounded to two decimal places.?
>>> 
>>> #Answer:
>>> second=float(input("Enter number of seconds between lightning and thunder: "))
Enter number of seconds between lightning and thunder: 5
>>> print("Distance from storm: " + str(distance))

Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    print("Distance from storm: " + str(distance))
NameError: name 'distance' is not defined
>>>  #answer: 97
>>> second=float(input("Enter number of seconds between lightning and thunder: "))
Enter number of seconds between lightning and thunder: 1
>>> distance= seconds/5

Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    distance= seconds/5
NameError: name 'seconds' is not defined
>>> 
>>> 
>>> #answer:97
>>> second=float(input("Enter number of seconds between lightning and thunder: "))
Enter number of seconds between lightning and thunder: 1
>>> second = int(60)
>>> distance = second/5
>>> print("Distance from storm: " + str(distance))
Distance from storm: 12
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #ques: 100
>>> #Cost of Electricity The cost of the electricity used by a device is given by the formula cost of electricity (in dollars) = wattage of device # hours used 1,000 # cost per kWh (in cents) where kWh is an abbreviation for “kilowatt hour.” The cost per kWh of electricity varies with locality. Suppose the current average cost of electricity for a residential customer in the United States is 11.76¢ per kWh. Write a program that allows the user to calculate the cost of operating an electrical device. Figure 2.10 calculates the cost of keeping a light bulb turned on for an entire month.
>>> 
>>> #Answer:
>>> wattage=float(input("Enter wattage: "))
Enter wattage: 1
>>> hours= int(input("Enter number of hours used: "))
Enter number of hours used: 1
>>> price=float(input("Enter price per kWh in cents: "))
Enter price per kWh in cents: 1176 #$11.76= 1176cents
>>> cost = round(((wattage*hours))/((1000*price)),2)
>>> print("Cost of electricity: $"+str(cost))
Cost of electricity: $0.0
>>> #here, I put wattage= 1, That is why it shows 0.0 cost.
>>> #Also, number of hours = 1 per month
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #ques: 102
>>> #Price-to-Earnings Ratio Write a program that requests a company’s earnings-pershare for the year and the price of one share of stock as input, and then displays the company’s price-to-earnings ratio (that is, price ÷ earnings).
>>> earnings= float(input("Enter earnings per share: "))
Enter earnings per share: 5.25
>>> price= float(input("Enter price per share: "))
Enter price per share: 68.25
>>> pte=round(price/earnings,2)
>>> print("Price-to-Earnings ratio: "+str(pte))
Price-to-Earnings ratio: 13.0
>>> 
>>> 
>>> 
>>> 
>>> #QUES: 110
>>> #Write a program that requests a sentence, a word in the sentence, and another word and then displays the sentence with the first word replaced by the second.
>>> 
>>> sentence=input("Enter a sentence: ")
Enter a sentence: WHAT YOU DO NOT KNOW WILL NOT HURT YOU

Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    sentence=input("Enter a sentence: ")
  File "<string>", line 1
    WHAT YOU DO NOT KNOW WILL NOT HURT YOU
           ^
SyntaxError: invalid syntax
>>> sentence=input("Enter a sentence: ")
Enter a sentence: "WHAT YOU DO NOT KNOW WILL NOT HURT YOU"
>>> toreplace=input("Enter word to replace: ")
Enter word to replace: "KNOW"
>>> replacement=input("Enter replacement word: ")
Enter replacement word: "OWE"
>>> sp=sentence.split()
>>> if toreplace in sp:
	replacement=toreplace
    print(sentence)
    
  File "<pyshell#197>", line 4
    print(sentence)
                  ^
IndentationError: unindent does not match any outer indentation level
>>> 
>>> 
>>> 
>>> sentence=input("Enter a sentence: ")
Enter a sentence: "WHAT YOU DO NOT KNOW WILL NOT HURT YOU"
>>> sentence = sentence.replace('KNOW', 'OWE')
>>> print (sentence)
WHAT YOU DO NOT OWE WILL NOT HURT YOU
>>> 
>>> 
>>> 
>>> 
>>> #ques:113
>>> #Write a program that asks the user to enter a whole number of months as input and then converts that amount of time to years and months. See Fig. 2.21. The program should use both integer division and the modulus operator.
>>> 
>>> months=int(input("Enter number of months: "))
Enter number of months: 234
>>> div=int(months/12)
>>> mod=int(months%12)
>>> print(str(months)+" months is "+str(div)+" years and "+str(mod)+ " months.")
234 months is 19 years and 6 months.
>>> 
