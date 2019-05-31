"""
Summary
-------
The summary is a brief intro. You can put raw HTML into this field.
"""
summary = "<p>Experienced Teacher with a demonstrated history of working in the primary/secondary education industry. \
Strong education professional with a Bachelors degree focused in Computer Science from Kharkiv National \
Pedagogical Univercity of G.S. Scovoroda. </p><p>Aiming to perform difficult tasks that require hard skills in programming \
and deep understanding of programming principles. But so far have an experience just in Python/Git/HTML5/CSS/JS/JQuery/Wordpress/basics of \
MySQL, Pandas&Numpy (Worked with Jupyter Notebook)\
/ Flask /C# </p>"


languages = [
        ['English', ' (Upper Intermidiate)'],
        ['Russian', ' (Native)'],
        ['Spanish', ' (Elementary)'],
        ['Ukrainian', ' (Native)']]

education = [
        ['BSc in Computer Science', 'KhNPU of G.S. Scovoroda', '2013 - 2017']
        ]

interests = ['Programming', 'Digital Art']

skills = [
        ['Python & Django', '75%'],
        ['Javascript & jQuery', '65%'],
        ['HTML5 & CSS', '90%'],
        ['MyPaint & Photoshop & Gimp & ScatchUp', '85%'],
        ['AngularJS & AJAX', '45%']
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
        ['Programming Tutor',
            '2015 - Present',
            'IT-Univer, Kharkiv',
            '<p>Teaching middle/high school students programming in Python. Also a private tutor for older students</p> '
        ]

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
projects = [['Web Application for my CV',
            'Application was built with Flask and deployed on heroku.com.\
             Check it out on github https://github.com/TkhiienLok/My_resume',
             'https://appformycv.herokuapp.com/'
             ],
            ['Snake Pygame',
             'Game "Snake" with a basic logic. The project demonstrates work with \
             pygame, tkinter and files. Check it out on github',
             'https://github.com/TkhiienLok/Snake-Pygame'],

            ['Django Blog',
            'Simple blog app made on DjangoGirls  – workshop. Students make a small working web application, their\
             own blog, using Django framework and deploy it via git on pythonanywhere.com',
             'http://tkhiienlok.pythonanywhere.com/']

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
    'languages' : languages,
    'education' : education,
    'interests' : interests,
    'skills' : skills,
    'summary' : summary,
    'experience' : experience,
    'projects' : projects
    }
