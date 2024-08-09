from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/meditation')
def meditation():
    return 'Meditation Page!'

@app.route('/workouts')
def workouts():
    return 'Workouts Page!'

@app.route('/nutrition')
def nutrition():
    return 'Nutrition Page!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
