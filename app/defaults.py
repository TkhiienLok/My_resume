"""
Summary
-------
The summary is a brief intro. You can put raw HTML into this field.
"""
summary = "<p>Experienced Teacher with a demonstrated history of working in the primary/secondary education industry. \
Strong education professional with a Bachelors degree focused in Computer Science from Kharkiv National \
Pedagogical Univercity of G.S. Scovoroda. </p><p>Aiming to perform difficult tasks that require hard skills in programming \
and deep understanding of programming principles. But so far have an experience just in Python, Git, HTML5/CSS/JS/JQuery/WordPress, \
basics of MySQL, Pandas&Numpy (Worked with Jupyter Notebook), Flask, C# </p>"


languages = [
    ['English', ' (Upper Intermidiate)'],
    ['Russian', ' (Native)'],
    ['Ukrainian', ' (Native)'],
    ['Spanish', ' (Elementary)']],

education = [
    ['BSc in Computer Science', 'KhNPU of G.S. Scovoroda', '2013 - 2017'],
    ['Refresher courses for Python tutors', 'Tutor club \"IT-Univer\"', '2015 - 2016']
]

interests = ['Programming', 'Digital Art']

skills = [
    ['Python & Django', '77%'],
    ['Javascript & jQuery', '75%'],
    ['HTML5 & CSS', '80%'],
    ['MyPaint, Photoshop & Gimp, ScatchUp', '78%'],
    ['ReactJS', '55%']
]

"""
Experience
----------
This should be a list of lists. Each sublist corresponds to a particular job
and is of the form:
    ['Title', 'Date range', 'Company name and location', 'Description of role']

The 'Description of role' field does not get escaped by the templating engine,
so you can put raw HTML in it if you like.
"""
experience = [
    ['Python programming Tutor',
        'Sep 2015 - Sep 2019',
        'IT-Univer, Kharkiv',
        '<p>Teaching middle/high school students programming in Python. Also a private tutor for older students</p> '],
    ['Junior JavaScript Developer',
     'Jul 2019 - Apr 2020',
     'Webspark, Kharkiv',
     'Worked with ReactJS, ExpressJS, Django (happened to work with this framework as the only developer in the \
     company with Python background. Used Postgresql, had experience with BeautifulSoup and Celery).']
    ]

"""
Projects
--------
The project_intro field is for a short introduction to your work.
Project are a list of lists, where each sublist refers to a specific project,
and is of the form:
    ['Title', 'Description', 'Link to project webpage']
"""
project_intro = '<p>You can list your side projects or open source libraries in this section. </p>'
projects = [
    ['Web Application for my CV',
     'Application was built with Flask and deployed on heroku.com.\
     Check it out on github https://github.com/TkhiienLok/My_resume.',
     'https://appformycv.herokuapp.com/'
     ],

    ['Django Personal Blog',
     'CRUD app where you can create, edit,  delete posts, add comments or vote as logged in user, and just \
     read posts and comments as not authenticated user. Application uses Postgresql database. There is a bit \
     of JQuery used. Project on github \
     https://github.com/TkhiienLok/blog-app',
     'https://lok-blog-app.herokuapp.com/'],

    ['Django Quiz App',
     'platform for  creating and passing quizzes -crud application. Application uses Postgresql database. \
     Some JQuery is used. Project on github \
     https://github.com/TkhiienLok/my-quiz-site',
     'https://lok-quiz-platform.herokuapp.com/'],

    ['KMeans algorithm',
     'Demonstration of KMeans clustering algorithm in Jupyter Notebook.',
     'https://github.com/TkhiienLok/Clustering-in-Numpy-Pandas'],

    ['Snake Pygame',
     'Game "Snake" with a basic logic. The project demonstrates work with \
     pygame, tkinter and files. Check it out on github.',
     'https://github.com/TkhiienLok/Snake-Pygame'],

]



"""
default_data
------------
This dictionary puts everything together. It will be read by the Flask app when
it is instantiated.
"""
default_data = {
    'site_title': 'Responsive Resume/Lok Chan CV',
    'name': 'Tkhiien Lok Chan',
    'tagline': 'Python Developer',
    'email': 'tkhiien@gmail.com',
    'phone': '+38(096)-936-48-91',
    'linkedin': 'linkedin.com/in/tkhiien-lok-chan-629a6a125/',
    'github': 'github.com/TkhiienLok',
    'languages': languages,
    'education': education,
    'interests': interests,
    'skills': skills,
    'summary': summary,
    'experience': experience,
    'projects': projects
    }
