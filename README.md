# Coursera-Backend-Development
## Introduction to Back-End Development
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
## Programming in Python
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
      - slice function
      ```
      # str[start:stop:step]
      temop_string = string[::-1]
      ```
      - recursion
      ```
      def reverse_str(str):
         if len(str) == 0:
            return str
         else:
            return reverse_str(str[1::]) + str[0]
      ```
 9. Map

