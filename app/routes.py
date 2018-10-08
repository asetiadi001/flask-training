from app import app


#first view function
@app.route('/')
@app.route('/index')
def index():
    return "Hello, world!"

