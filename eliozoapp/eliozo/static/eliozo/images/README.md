# Images for olympiad problems

Every image is a PNG file (name derived from the unique problem ID). 
When deployed, this directory holds images that exist in the markdown 
content (just as local links). Our conversion ensures that image links 
are properly reflected in HTML. 

* **Production environment:** As before we serve the PNG files from a 
  static directory using Nginx (or any non-Flask Web server). 
* **Development environment:** On a local machine we create "url_for" 
  expression for the given url and then it is served by Flask. 

Sample code to be used in our app for serving these images:

``` python
from flask import Flask, url_for

app = Flask(__name__)
app.config.from_pyfile('config.py')

def static_url(filename):
    if app.config.get('USE_REMOTE_STATIC'):
        return f"https://www.dudajevagatve.lv/static/{filename}"
    else:
        return url_for('static', filename=filename)

app.jinja_env.globals['static_url'] = static_url

@app.route('/show/<problemid>')
def show(problemid):
    return render_template('show.html', problemid=problemid) 
```

Here is a Jinja2 template sample that makes use of "static_url": 
```
<img src="{{ static_url('eliozo/images/' ~ problemid ~ '.png') }}">
```


The image files (PNGs) do not reside in this directory permanently; 
on the production server they will end up in the following location: 
```
/var/www/html/static/eliozo/images
```
This ensures the ability by Nginx to serve them as static files.
