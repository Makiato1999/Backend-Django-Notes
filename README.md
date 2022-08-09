# Coursera-Backend-Development
#### Table of Contents
1. [Introduction to Backend Development](#anchor_1)<br/>
2. [Programming in Python](#anchor_2)
   - [Object Oriented Programming](#anchor_21)
3. [Version Control](#anchor_3)
   - [git commands](#anchor_31)
4. [Web Application Technologies and Django](#anchor_4)
   - [If db gets messed up](#anchor_41)
   - [django document 01(intro), 02(model, migration)](#anchor_42)
6. [Building Web Applications in Django](#anchor_5)
   - [django document 03(url.py, views.py, templete(html))](#anchor_51)
   - [django document 04(forms, GET, POST, generic views)](#anchor_52)
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
   - unit(PyTest)<br/>refer to [test_spellcheck.py](https://github.com/Makiato1999/Coursera-Backend-Development/blob/main/2.%20Programming%20in%20Python/Week4-Assignment-unitTesting/test_spellcheck.py)
   - integration
   - system
   - acceptance 
6. test-driven development(TDD)
## Version Control<a name="anchor_3"></a>
1. workflow
   - Continuous Integration
   - Continuous Delivery
   - Continuous Deployment
2. bash
   - cd, Change Directory
   - ls - List command used for showing the content of a directory.
   - rm - Remove command used for removing a file or a directory
   - mv - Used to move files or folders to another location
   - touch - Allows creating of a new empty file or to upate a timestamp on a file
   - cp - Used to make a copy of a file or foldler
   - mkdir - Make a new directory
   - pwd - Print work directory, shows the current location in the shell
   - cat - Allows reading or concatenation of a file
   - less - Displays the contents of a file one page at a time.
   - grep - Global regular expression, allows for searching contents of files or folders
3. pip
   - ```cat file.txt | wc -w```
4. redirection 
5. grep
6. correct workflow
   - from the working directory to the staging area(git add), then to committed files(git commit), remote repository(git push)  
8. How to use simple git commands<a name="anchor_31"></a>
   - login Github, ```gh auth login```
   - if u want to clone repository, ```gh repo clone <YOUR USERNAME>/<REPOSITORY-NAME>```
   - if repository is exist,
   - open terminal and find the location of the clone repository 
   - ```git clone -b branch``` + urlLink
   - check if there is the file you need
   - create a new branch, ```git checkout -b yourNewBranchName```, go back to main branch, ```git checkout main```
   - check current branches, ```git status```
   - change untracked file to tracked, add file in staging status, ```git add helloWorld.java``` / ```git add *```
   - restore file from tracked to untracked, go back to last step, ```git restore --stage helloWorld.java```
   - ```git commit -m "add helloWorld.java to main branch..."```
   - ```git push -u origin yourBranchName```
   - updated local content from remote repository, ```git pull```
## Web Application Technologies and Django<a name="anchor_4"></a>
1. Model-View-Controller
   - Model: The persistent data that we keep in the data store
   - View: Html, Css, etc. which makes up the look and feel of the application
   - Controller: The code that does the thinking and decision making
   - Which of the following files does Django consult first when it receives an incoming HTTP Request?
      - urls.py
2. SQL summary
   - ```INSERT INTO Users (name, email) VALUES ('Kristina', 'kf@uofm.ca')```
   - ```DELETE FROM Users WHERE email='ted@uofm.ca'```
   - ```UPDATE Users SET name="Shawn" WHERE email='csev@uofm.ca'```
   - ```SELECT * FROM Users```
   - ```SELECT * FROM Users WHERE email='csev@uofm.ca'```
   - ```SELECT * FROM Users ORDER BY email'```
3. Object Relational Mapping
4. CRUD in the ORM
   - ```INSERT INTO Users (name, email) VALUES ('Kristina', 'kf@uofm.ca')```
     <br>is same as:
     ```
     u = User(name='Kristina', email='kf@uofm.ca')
     u.save()
     ```
   - ```SELECT * FROM Users```
     <br>is same as:
     ```
     User.objects.values()
     ```
   - ```SELECT * FROM Users WHERE email='csev@uofm.ca'```
     <br>is same as:
     ```
     User.objects.filter(email='csev@uofm.ca').values
     ```
   - ```UPDATE Users SET name="Shawn" WHERE email='csev@uofm.ca'```
     <br>is same as:
     ```
     User.objects.filter(email='csev@uofm.ca').update(name='Shawn')
     ```
   - ```SELECT * FROM Users ORDER BY email'```
     <br>is same as:
     ```
     User.objects.values().order_by('email')
     ```
5. If db gets messed up (if you screw up)<a name="anchor_41"></a>
   - ```cd ~/django_projects/mysite/polls/```
   - ```rm *migrations/00*```
   - ```rm db.sqlite3```
   - ```python manage.py makemigrations```
   - ```python manage.py migrate```
   - ```python manage.py createsuperuser```
7. What does the "python manage.py migrate" command do?
   - Builds/updates the database structure for the project
8. What is the purpose of the models.py file?
   - To define the shape of the data objects to be stored in a database
9. three-step guide to making model changes:
   - Change your models (in models.py).
   - Run ```python manage.py makemigrations``` to create migrations for those changes
   - Run ```python manage.py migrate``` to apply those changes to the database.
1. there are too many contents, read django document is a better way to study it<a name="anchor_42"></a>
   - [django tutorial01](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)
   - models and mogration [django tutorial02](https://docs.djangoproject.com/en/3.2/intro/tutorial02/)
## Building Web Applications in Django<a name="anchor_5"></a>
1. views
   - function based views
      ```
      # url:
      # http://samples.dj4e.com/views/rest/41
      
      # url.py:
      urlpatterns = [
         path('rest/<int:guess>', view.rest),
      ]
      
      # response:
      from django.http import HttpResponse
      from django.utils.html import escape
      
      def rest(request, guess):
         response = """<html><body><p>"""+escape(guess)+"""</p></body></html>"""
         return HttpResponse(response)
      ```
   - class based views
      ```
      # url:
      # http://samples.dj4e.com/views/remain/xxr123-33-nbnb
      
      # url.py:
      urlpatterns = [
         path('remain/<slug:guess>', views.RestMainView.as_view()),
      ]
      
      # response:
      from django.http import HttpResponse
      from django.utils.html import escape
      from django.views import View
      
      Class RestMainView(View):
         def get(self, request, guess):
            response = """<html><body><p>"""+escape(guess)+"""</p></body></html>"""
            return HttpResponse(response)
      ```
2. there are too many contents, read django document is a better way to study it<a name="anchor_51"></a>
   - url.py, views.py, templete(html)[django tutorial03](https://docs.djangoproject.com/en/3.2/intro/tutorial03/)
3. render
   ```
   from django.shortcuts import render
   from .models import Question
   
   def index(request):
      latest_question_list = Question.objects.order_by('-pub_date')[:5]
      context = {'latest_question_list': latest_question_list}
      return render(request, 'polls/index.html', context)
   ```
4. Templates
   - Django template language
      - Removing hardcoded URLs in templates
5. {% csrf_token %} 
6. there are too many contents, read django document is a better way to study it<a name="anchor_52"></a>
   - forms, GET, POST, generic views[django tutorial04](https://docs.djangoproject.com/en/3.2/intro/tutorial04/)

