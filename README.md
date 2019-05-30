# resume-site  
**resume-site** is a Flask-driven, single-page resume site.
The design implements the [Orbit](https://themes.3rdwavemedia.com/website-templates/orbit-free-resume-cv-template-for-developers/) bootstrap template for a simple, yet colorful, look and feel.
Data and design are decoupled by using an [HTML template](https://github.com/johnmarcampbell/resume-site/blob/master/app/templates/index.html) to parse a [python dictionary](https://github.com/johnmarcampbell/resume-site/blob/master/app/defaults.py) which stores all the information contained in the resume.

## Running resume-site
You can run the app in a python interpreter or standalone script like so:  

```python  
import app
app.create_app().run()  
```  
or simply run the `run_resume_site.py` file

This will start Flask's own web server and make **resume-site** available on your local machine at `127.0.0.1:5000`.

