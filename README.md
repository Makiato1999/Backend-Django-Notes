# Django for Everybody Specialization
_provided by University of Michigen & Coursera_
#### Table of Contents
1. [Web Application Technologies and Django](#anchor_4)
   - [If db gets messed up](#anchor_41)
   - [django document 01(intro), 02(model, migration)](#anchor_42)
2. [Building Web Applications in Django](#anchor_5)
   - [django document 03(url.py, views.py, templete(html))](#anchor_51)
   - [django document 04(forms, GET, POST, generic views)](#anchor_52)
3. [Django Features and Libraries](#anchor_6)
   - [Building a Main Page](#anchor_61)
   - [CRUD](#anchor_62)
   - [one-to-many](#anchor_63)
   - [many-to-many](#anchor_64)
4. [Using JavaScript, JQuery, and JSON in Django](#anchor_7)
   - [first class function](#anchor_71)
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
   - ```workon django3                  # as needed```
   - ```python manage.py check```
   - ```python manage.py makemigrations```
   - ```python manage.py migrate```
   - ```python manage.py check```
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
   - url.py, views.py, templete(html) [django tutorial03](https://docs.djangoproject.com/en/3.2/intro/tutorial03/)
3. render
   ```
   from django.shortcuts import render
   from .models import Question
   
   def index(request):
      latest_question_list = Question.objects.order_by('-pub_date')[:5]
      context = {'latest_question_list': latest_question_list}
      return render(request, 'polls/index.html', context)
   ```
4. Templates, most of them are HTML
   - Django template language
      - Removing hardcoded URLs in templates, this is the example:
        - ```<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>```
      - other using ways, such as normal statement in python
        - ```
          {% if latest_question_list %}
          <ul>
               {% for question in latest_question_list %}
                  <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
               {% endfor %}
          </ul>
          {% else %}
               <p>No polls are available.</p>
          {% endif %}
          ```
       - in the form and using POST, we should take care about {% csrf_token %} 
         - ```
           <form action="{% url 'polls:vote' question.id %}" method="post">
           {% csrf_token %}
               <fieldset>
                  <legend><h1>{{ question.question_text }}</h1></legend>
                  {% if error_message %}
                   <p><strong>{{ error_message }}</strong></p>
                  {% endif %}
                  {% for choice in question.choice_set.all %}
                     <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
                     <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label>
                     <br>
                  {% endfor %}
               </fieldset>
                     <input type="submit" value="Vote">
           </form>
           ```
6. there are too many contents, read django document is a better way to study it<a name="anchor_52"></a>
   - forms, GET, POST, generic views [django tutorial04](https://docs.djangoproject.com/en/3.2/intro/tutorial04/)
7. a sqlite3 db has existed in https://makiato1999.pythonanywhere.com/polls, if you want to use admin, you should use 
   - Account: dj4e, Password: bc53a9938
## Django Features and Libraries<a name="anchor_6"></a>
1. Building a Main Page/ add a new application<a name="anchor_61"></a>
   ```
   workon django3                  # as needed
   cd ~/django_projects/mysite
   python3 manage.py startapp home
   ```
   Create an HTML file in ~/django_projects/mysite/home/templates/home/main.html
   <br>
   dont forgot to update ~/django_projects/mysite/mysite/urls.py
   ```
   path('', TemplateView.as_view(template_name='home/main.html')),
   ```
   Then edit the file ~/django_projects/mysite/mysite/settings.py and add a line to load the home application.
   ```
   python3 manage.py check
   ```
2. cookies and session
   - google to view difference 
   - how to create session and cookie in django, in views.py
     ```
     from django.http import HttpResponse

     def myview(request):
         num_visits = request.session.get('num_visits', 0) + 1
         request.session['num_visits'] = num_visits
         resp = HttpResponse('view count='+str(num_visits))
         resp.set_cookie('dj4e_cookie', '37e3398f', max_age=1000)
         return resp
     ```
3. login and logout
   - form
      - form/forms.py
      ```
      from django import forms
      from django.core.exceptions import ValidationError
      from django.core import validators
   
      class BasicForm(forms.Form):
         title = forms.CharField(validators=[validators.MinLengthValidator(2, "...")])
         mileage = forms.IntegerField()
         purchase_date = forms.DataField()
   
      ``` 
      - form/views.py
      ```
      from form.forms import BasicForm
      
      def example(request):
         form = BasicForm()
         return HttpResponse(form.as_table)
      ```
      form.as_table() will create form html, so there is another way to write, we can put it in templete
      - form/templete/form/form.html
      ```
      <p>
         <form action="" method="post">
            {% csrf_token %}
            <table>
               {{form.as_table}}
            </table>
            <input type="submit" value="Submit">
            <input type="submit" onclick="window.location='{% url 'form:main'%}'; return false;" value="Cancel">
         </form>
      </p>
      ```
4. login and CRUD(create, read, update, delete)<a name="anchor_62"></a>
   - this assignment is hard -> [week3 assignment](https://www.dj4e.com/assn/dj4e_autos.md?PHPSESSID=15b0d8e4bd0299496cc47e7134333eff)
5. model and database, one-to-many<a name="anchor_63"></a>
   - keep the row but set foreign key to null
   ```
   lan = models.ForeignKey('Language', on_delete = models.SET_NULL, null = True)
   ```
   - delete the row
   ```
   lan = models.ForeignKey('Book', on_delete = models.CASCADE)
   ```
6. Cats CRUD assignment is almost same as autos CRUD
   - assignment [week4 assignment document](https://www.dj4e.com/tools/crud/02spec.php?assn=02cats.php&PHPSESSID=c2840d8b5b59a34e71bd1dac410e4081)
   - [week4 assignment code](https://github.com/Makiato1999/Coursera-Backend-Development/tree/main/3.%20Django%20Features%20and%20Libraries/catList)
   - user login
      ```
      Account: dj4e_user 
      Password: Meow_7e3398_42
      ```
   - dont forget to update admin.py in cats! Otherwise you cannot see its database in admin mode
   - user login
      ```
      Account: casual_user 
      Password: test_uofm_22
      ```
7. MySQL
   - login
      ```
      Account:  
      Password: test_uofm_1999
      ```
   - admin
      ```
      Account: admin_user
      Password: admin_uofm_1999
      ```
8. Debug, Searching through all your files in the bash shell
   - If you have errors, you might find the grep tool very helpful in figuring out where you might find your errors.
      ```
      cd ~/django_projects/mysite
      grep -ri myarts *
      ```
9. navigation bar and CRUD, profile
   - [week5 assignment document](https://www.dj4e.com/tools/crud/?PHPSESSID=0f8cbabfd47cfc4b5228c5a8845d724f&PHPSESSID=0f8cbabfd47cfc4b5228c5a8845d724f&url=http%3A%2F%2Fmakiato1999.pythonanywhere.com%2F)
   - user account and password is also in the assignment document
1. model and database, many-to-many<a name="anchor_64"></a>
   - it is hard to understand, there is an example, the relationship between books and authors is many-to-many
   - a book is writen by many authors, and an author can write many books, this is the basic logic
   - under this condition, for book, author is foreign key. As same logic, for author, book is foreign key 
   - hence, we need a 'through table' set between books and authors, which name is authored
      - models.py, Book, Author, Authored
      ```
      from django.db import models
      
      class Book(models.Model):
         title = models.CharField(max_length = 200)
         authors = models.MangToManyField('Author', through = 'Authored')
      
      class Author(models.Model):
         name = models.CharField(max_length = 200)
         books = models.MangToManyField('Book', through = 'Authored')
         
      class Authored(models.Model):
         book = models.ForeignKey(Book, on_delete = models.CASCADE)
         author = models.ForeignKey(Author, on_delete = models.CASCADE)
      ```
    - there is another way to implement many to many relationship, and it looks like dynamic
      - models.py, Person, Course, Membership
      ```
      from django.db import models
      
      class Person(models.Model):
         email = models.CharField(max_length = 128, unique = True)
         name = models.CharField(max_length = 128, null = True)
         def __str__(self):
            return self.email
      
      class Course(models.Model):
         title = models.CharField(max_length = 128, unique = True)
         members = models.MangToManyField(Person, through = 'Book', through = 'Membership', related_name = 'courses')
         def __str__(self):
            return self.title
            
      class Membership(models.Model):
         person = models.ForeignKey(Person, on_delete = models.CASCADE)
         course = models.ForeignKey(Ccourse, on_delete = models.CASCADE)
         created_at = models.DateTimeField(auto_now_add = True)
         updated_at = models.DateTimeField(auto_now = True)
         
         LEARNER = 1
         IA = 1000
         GSI = 2000
         INSTRUCTOR = 5000
         ADMIN = 10000
         
         MEMBER_CHOICES = (
            (LEARNER, 'Learner'),
            (IA, 'Instructional Assistant'),
            (GSI, 'Grad Student Instructor'),
            (INSTRUCTOR, 'Instrucctor'),
            (ADMIN, 'Administrator '),
         )
         
         role = models.IntegerField(
            choices = MEMBER_CHOICES,
            default = LEARNER,
         )
         def __str__(self):
            return "Person" + str(self.person.id) + "<...>Course" + str(self.course.id)
      ```
   - Indeed there are three ways for creating many-to-many table, django can create table automatically, but use through table would be clear for programming
      - [实战Django之Model操作之多对多(ManyToMany)正反调用](https://blog.csdn.net/Burgess_zheng/article/details/86594225)
2. extract information from csv into database by using Django
   - [week6 assignment document](https://www.dj4e.com/assn/dj4e_load.md?PHPSESSID=e77607e111f0d6cbbba985a07d3a2a38)
   - [week6 assignment code](https://github.com/Makiato1999/Coursera-Backend-Development/tree/main/3.%20Django%20Features%20and%20Libraries/readCSV)
## Using JavaScript, JQuery, and JSON in Django<a name="anchor_7"></a>
1. JavaScript
   - difference between python dictionary and javascript array
      - they look similar[from google](https://nibes.cn/blog/24300)
   - first class function<a name="anchor_71"></a>
      - A programming language is said to have First-class functions when functions in that language are treated like any other variable. For example, in such a language, a function can be passed as an argument to other functions, can be returned by another function and can be assigned as a value to a variable.
      - example
      ```
      function sayHello() {
         return "Hello, ";
      }
      
      function greeting(helloMessage, name) {
         console.log(helloMessage() + name);
      }
      // Pass `sayHello` as an argument to `greeting` function
      greeting(sayHello, "JavaScript!");
      // Hello, JavaScript!
      ```
2. Ads website with nav bar, uploaded pic, comments features
   - [week2 assignment document](https://www.dj4e.com/assn/dj4e_ads2.md?PHPSESSID=12d4b9da3f5eed4fb4520246b1e81689)
   - [week2 assignment code](https://github.com/Makiato1999/Coursera-Backend-Development/tree/main/4.%20Using%20JavaScript%2C%20JQuery%2C%20and%20JSON%20in%20Django/Week2-Ads)
   - admin account is 
      - admin
      ```
      Account: admin_user
      Password: admin_uofm_1999
      ```
   - user login
      ```
      Account: casual_user 
      Password: test_uofm_22
      ```
3. backend flow
   - ![backend flow with javascript](https://github.com/Makiato1999/Coursera-Backend-Development/blob/main/images/1.png)
4. jQuery
   - ID Selector (“#id”), example is below
     ```
     <p>
         <a href="#" id="the-href">More</a>
     </p>
     <ul id=the-list"">
         <li>First Item</li>
     </ul>
     <script type="text/javascript" src="jquery.min.js"></script>
     <script>
     counter = 1;
     $(document).ready(function(){
         $("#the-href").on('click', funtion(){
               console.log('Clicked');
               $('#the-list').append('<li>The counter is  '+counter+'</li>');
               counter++;
         });
     });
     </script>
     ```
  - difference between ```$(window)``` and ```$(document)```
      - The window object represents the container that the document object is displayed in. In fact, when you reference document in your code, you are really referencing window.document (all properties and methods of window are global and, as such, can be referenced without actually specifying window at the beginning...)
      - it's hard to describe, but we can say,
         - ```document``` can be written as ```window.document```
         - ```alert()``` can be written as ```window.alert()```
      - image for easily understanding [image](https://stackoverflow.com/questions/9895202/what-is-the-difference-between-window-screen-and-document-in-javascript#:~:text=window%20is%20the%20root%20of,document%20is%20top%20DOM%20object.)
5. unique_together
6. Ads website with nav bar, uploaded pic, comments features, favourite list(only add and delete, can't filter)
   - [week4 assignment document](https://www.dj4e.com/tools/crud/?PHPSESSID=f014970ff589279c4957d77c9fc451a5)
   - [week4 assignment code](https://www.dj4e.com/assn/dj4e_ads3.md?PHPSESSID=27e271482bb7d0b118a789c3a52901fe)
   - admin account is 
      - admin
      ```
      Account: admin_user
      Password: admin_uofm_1999
      ```
   - user login
      ```
      Account: casual_user 
      Password: test_uofm_22
      ```
8. review 
   - object-orientation
      - [django view object-orientation](https://www.coursera.org/learn/django-javascript-jquery-json/lecture/OoGDt/walkthrough-dj4e-my-articles-myarts-sample-code)
   - save(commit=False)
      - [in the form_valid](https://blog.csdn.net/weixin_42134789/article/details/80520500)
   - request.user.is_authenticated
   - LoginRequiredMixin
      - [login/authenticated](https://zhuanlan.zhihu.com/p/40405889)
   - list[:10]
9. django-taggit
1. Ads website with nav bar, uploaded pic, comments features, favourite list(only add and delete, can't filter), search bar, tags
   - [week5 assignment document](https://www.dj4e.com/assn/dj4e_ads4.md?PHPSESSID=5c6a91001ef8f382471447a8784c8262)
   - [week5 assignment code]()
   - admin account is 
      - admin
      ```
      Account: admin_user
      Password: admin_uofm_1999
      ```
   - user login
      ```
      Account: casual_user 
      Password: test_uofm_22
      ```
 
