4
from flask import Flask, render_template

app = Flask(__name__)

# Define the home route and its corresponding view
@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

# Define the route for the location page and its corresponding view
@app.route('/location')
def location():
    return render_template('location.html')

# Define the route for the classes page and its corresponding view
@app.route('/classes')
def classes():
    return render_template('classes.html')

# Define the route for the notes page and its corresponding view
@app.route('/notes')
def notes():
    return render_template('notes.html')

# Define the route for the teachers page and its corresponding view
@app.route('/teachers')
def teachers():
    return render_template('teachers.html')

# Define the route for the lessons page and its corresponding view
@app.route('/lessons')
def lessons():
    return render_template('lessons.html')

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port=8081)
