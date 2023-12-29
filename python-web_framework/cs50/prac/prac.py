#!/usr/bin/python3

#! import the python Flask class
from flask import Flask

# Create an instance of the class.The first arg is the name of the application's
# module or package
app = Flask(__name__)


# we use route() to tell flask what URL should trigger the function
@app.route("/")
def home():
    return "Welcome Home"


# You can run it as a normal py file(python3 prac.py)
# or using flask command (flask --app prac run)
# If you want it to be publicly available, add (--host=0.0.0.0)
# it tells the OS to listen to public IPs

#! Debug Mode
"""
    With this, the server will automatically update with any changes made,
    and will show an interactive debugger on the browser if any error occurs
    during a request
    You can run this mode with *--debug* option
"""

#! HTML Escaping
"""
    The default response is HTML in Flask, any user-provided values rendered 
    in the output must be escaped to avoid injection attacks. 
    HTML templates rendered with JINJA(template engine) will do this automatically.
    
    escape() ==> can be used manually. First (from markupsafe import escape)
    
        @app.route("/<name>")
        def hello(name):
            return f"Hello, {escape(name)}!"
            
    <name> in the route captures a value from the URL and passes it to the view
    function. These variable rules are explained below.
"""

#! Routing
"""
    Modern web apps use meningful URLs to help users.
    Use (route) decorator to bind a function to a URL
    
        @app.route('/')
        def index():
            return 'Index Page'

        @app.route('/hello')
        def hello():
            return 'Hello, World'
"""

#! Var Rules
"""
    You can add var sections to a URL by marking the sections with <variable_name>.
    Function then receives the <.....> as a keyword argument
    You can use a converter to specify the argument type <converter:variable_name>   
    
from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    #shows the user profile of that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id , the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show subpath after /path/
    return f'Subpath {escape(subpath)}'
    
"""

#! Unique URLs / Redirection Behaviours
"""
    The following two rules differ in their use of a trailing slash.
    
    @app.route('/projects/')
    def projects():
        return 'The project page'
        
#if you access the URL without a trailing slash(/projects), it redirects 
you to the canonical URL (/projects/)
        
    @app.route('/about')
    def about():
        return 'The about page'
        
#The canonical url for the about page doesn't have a trailing slash.
If you access it with a trailing slash (/about/), you will get 
404 Page Not Found

"""

#! URL building
"""
    To build a URL for a specific function, we use the *url_for()* function
    
"""

from flask import url_for


@app.route("/")
def index():
    return "index"


@app.route("/login")
def login():
    return "login"


@app.route("/user/<username>")
def profile(username):
    return f"{username}'s profile"


with app.test_request_context():
    print(url_for("index"))
    print(url_for("login"))
    print(url_for("login", next="/"))
    print(url_for("profile", username="Jon Doe"))

#! HTTP Methods
"""
    Web apps use different HTTP methods when accessing URLs.
    By default, a route only answers to GET requests.
    You can use the methods of the argument of the *route()* 
    decorator to handle different HTTP methods:
"""
from flask import request


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return do_the_login()
    else:
        return show_the_login_form()


"""
    You can also seperate views for different methods 
    into different functions.
    *Flask provides a shortcut for such functions: 
    *get(), post() etc. for each common HTTP method.*
"""


@app.get("/login")
def login_get():
    return show_the_login_form()


@app.post("login")
def login_post():
    return do_the_login()


#!Static Files
"""
    Dynamic web apps also need static files. That's usually where 
    CSS files and javascript files come from
    * Just create a folder called *static* in your package or next 
    to your module and it will be available at */static* in the app.
    
    To generate URLs for static files, use special 'static' endpoint name:
"""
url_for("static", filename="style.css")
# *The file has to be stored on the filesystem as /static/style.class

#!Rendering Templates
# * To render templates, use *render_template()* method
# Then provide the template name and variables you want to pass to the
# template engine as keyword args.

from flask import render_template


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)

#*Here's an example of a template

<!doctype html>
<title>Hello from Flask</title>
{%if name%}
    <h1>Hello {{name}}!</h1>
{%else%}
    <h1>Hello, World!</h1>
{%endif%}

#* Templates are especially useful if inheritance is used.
#Automatic escaping is enabled

#! Using test_request_context()
from flask import request

with app.test_request_context('/hello', method='POST'):
    #you can now do something with the request until the end
    #of the with block, such as basic assertions
    assert request.path == '/hello'
    assert request.method == 'POST'
    
#* The other possibility is passing the whole WSGI environment
#* to the request_context() method:
with app.request_context(environ):
    assert request.method = 'POST'
    

#! The Request Object
# Of course you have to import it from the flask module

"""
    To access form data(data transmitted through POST & PUT request)
    you can use *form* attribute. Here is a full example of the two 
    attributes mention above
"""
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                        request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method was GET 
    # or the credentials were wrong
    return render_template('/login.html', error=error)

#* To access the parameters submitted in the URL (?key=value),
#* you can use the *args* attribute

searchword = request.args.get('key', '')


#! File Uploads
#Don't forget to set the attribute:
enctype="multipart/form-data" # on your HTML form. Otherwise,
#the browser will not transmit your files at all

#You can access stored files by looking at the *files* attribute
#on the request object. Each uploaded file is stored in that dictionary
#It behaves like a standard Python Object but has a *save()* method
#that allows you to store that file on the filesystem of the server:

from flask import request

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
        ...

#If you want to save a file on the server with the filename from the
#client, pass it through the *secure_filename()* function provided by Werkzeug:

from werkzeug.utils import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/{secure_filename(file.filename)}')
        ...


#! COOKIES
"""
    To access cookies, use the *cookies*  attribute.
    To set cookies, we use the *set_cookies()* method of the response object.
    Do not use cookies directly if you want to use sessions, instead use the 
    *Sessions* in flask that add some security on top of cookies for you
    Reading Cookies: 
"""

from flask import request

@app.route('/')
def index():
    username = request.cookies.get('username')
    #use cookies.get(key) instead of cookies[key] to not get
    #an error if cookies are missing

#*Storing Cookies

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
    ...


#! REDIRECTS AND ERRORS
"""
    To redirect a user to another endpoint use the 
    *redirect() function,
    To abort a request early with an error code, use
    *abort() function
"""

flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))
    ...

@app.route('/login')
def login():
    abort(401) #401 means access denied
    this_is_never_executed()

"""
    Black and white pages are used for error codes by default,
    but you can customize using 
    *errorhandler() decorator
"""

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

#* The 404 after render_template(), tells flask that the status cod of
#*that pag should be 404, instead of 200 which is the default(all went well)

#! APIs With JSON
#A common response when writing an API is JSON
#If you return a *dict* or a *list* from a view, it will be converted to JSON response.

@app.route('/me')
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image)
    }

@app.route('/users')
def users_api():
    users = get_all_users()
    return [user.to_json() for user in users]

#! SESSIONS
"""
    In addition to request object, there is also a second
    one called *session*.
    It allows you to store information specific to a user
    from one request to the next.
    This is implemented on top of cookies for you and signs
    the cookies cryptographically.
    Hence the user can view the cookies but not modify it unless
    they use the secret key used in signing
"""
#In order to use sessions, you have to set a secret key
#Here is how session works:

from flask import session

#set the secret key to some random bytes
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post>
            <p><input type=text name=username>
            <p><input type=submit value=login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the sessions if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


#! LOGGING
#If you want to log that something is fishy, whether a malformed
#code or data tampering, we use loggers.abort
#*Some examples of log calls:

app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')

