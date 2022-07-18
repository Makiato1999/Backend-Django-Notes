# Coursera-Backend-Development
#### Table of Contents
1. [Introduction to Backend Development](#anchor_1)<br/>
2. [Programming in Python](#anchor_2)
   - [Object Oriented Programming](#anchor_21)
## Introduction to Backend Development<a name="anchor_1"></a>
1. HTML, CSS
2. UI framworks and libraries, Bootstrap
   - breakpoint
      - infix(indicate the breakpoint in Bootstrap CSS rules)
      - bootstrap modifiers(add a CSS class to change the visual style of components)
   - [grid system](https://getbootstrap.com/docs/4.0/layout/grid/)
   - containers, row, col col-12/col-lg-6(different screen size)
   - [cards](https://getbootstrap.com/docs/4.0/components/card/)
   - [badge](https://getbootstrap.com/docs/4.0/components/badge/)(can insert between span tag)
   - [alert](https://getbootstrap.com/docs/4.0/components/alerts/)
   - [bootstrap web](https://getbootstrap.com/docs/5.2/getting-started/introduction/)<br>bootstrap.min.css, bootstrap.min.js
3. Into React
   - SAP(single application page)
   - Virtual DOM(Document Object Model)
   - component hierarchy
## Programming in Python<a name="anchor_2"></a>
1. install Python/change python version
   - [Installing Python path for MacOS](https://github.com/Makiato1999/Coursera-Backend-Development/blob/main/2.%20Programming%20in%20Python/PythonPath.md)
2. type casting
3. String
   - "I am a {major} student in {university}".format(major="Shawn", university="UofM")
   - "I am a {0} student in {1}".format("Shawn", "UofM")
   - "I am a {} student in {}".format("Shawn", "UofM")
4. loop
   - for index, item in enumerate(func):
5. data structure
   - list [], tuple ()
      - list can be modified(append, insert, pop), but tuple is immutable
   - set
      - is a collection with no duplicated
      - set is not a sequence, it doesn't contain order index, set can not search with index
   - dictionary 
      - key:value
      ```
      for key, value in my_dict.items(): 
         print(str(key) + ":" + value)
      ```
   - args
      ```
      def sum(*args): 
         for x in args:
            sum += x
      sum(1, 3, 4, 6, 7)
      ```
   - kwargs
      ```
      def sum(**kwargs):
         for k, v in kwargs.items():
            sum += v
      sum(coffee:2.9, tea:1.6, sanwich:4.3)
      ```
6. read/write file
   - ```with open(filename, "r") as file:```
   - use 'with' operate file, otherwise need to use close
7. :smiling_face_with_tear: I got COVID this week and i have to suspend the studying. The fever made me feel headache, and sore throat felt like swallowing a blade down my throat, please protect yourself. TAKE CARE.
8. recursion
   - reverse String
      - slice function(Using Indexing Syntax)
      ```
      # str[start:stop:step]
      temop_string = string[::-1]
      ```
      [more string slice() details](https://www.tutorialsteacher.com/python/slice-method#:~:text=Python%20slice()%20function,and%20__len__()%20methods.)
      - recursion
      ```
      def reverse_str(str):
         if len(str) == 0:
            return str
         else:
            return reverse_str(str[1::]) + str[0]
      ```
9. Map & filter 
   - map() returns every item in an iterable, including 'None', 'False', etc.
   - same as map, but filter() only returns values if True
1. comprehension
   - list comprehension
      - ```[ <expression> for x in <sequence> if <condition>]```
   - dictionary comprehension
      - ```dict = { key:value for key, value in <sequence> if <condition> }```
   - Generator comprehension
      - similiar to list, but use ()
   - zip()
      - [Week3-Assignment can use zip(), good idea even it makes code complex](https://github.com/Makiato1999/Coursera-Backend-Development/blob/main/2.%20Programming%20in%20Python/Week3-Assignment/zip.png)
   - refer to [comprehensions.py](https://github.com/Makiato1999/Coursera-Backend-Development/blob/main/2.%20Programming%20in%20Python/Week3-Assignment/comprehensions.py)
2. Object Oriented Programming<a name="anchor_21"></a>
   - almost same as Java
   - encapsulation, polymorphism, inheritance and abstraction
   - constructor
     ```
     def __init__(self, newData):
         self.data = newData
     ```
   - Inheritance and Multiple Inheritance
   - abstract
     ```
     from abc import ABC
     class abstractClass(ABC):
         pass
     ```
     if there is abstract method, then
     ```
     from abc import ABC, abstractmethod
     class abstractClass(ABC):
         @abstractmethod
         def someAbstractMethod(self):
            pass
     ```
   - override
   - refer to [bank.py](https://github.com/Makiato1999/Coursera-Backend-Development/blob/main/2.%20Programming%20in%20Python/Week3-Assignment-abstract/bank.py)
3. module
   - build-in
     ```
     import sys
     ```
   - not build-in
     ```
     import sys
     sys.path.insert(1, r"C:\Users\Madecraft Author\Programs\Workplace")
     import trial
     ```
   - others, such as```from json import *```
   - refer to [jsongenerator.py](https://github.com/Makiato1999/Coursera-Backend-Development/blob/main/2.%20Programming%20in%20Python/Week4-Assignment-import/jsongenerator.py)
4. web dev
   - full stack(Django)
   - microframework(Flask)
   - asynchronous
5. testing
   - unit
   - integration
   - system
   - acceptance 
