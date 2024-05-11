from flask import Flask, render_template
import pandas as pd


app = Flask(__name__) #create the app

# Read the CSV file
df = pd.read_csv('data/India_Covid_Status.csv')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/active')
def active():
    return render_template('active.html')

@app.route('/adjusted')
def adjusted():
    return render_template('adjusted.html')

@app.route('/death')
def death():
    return render_template('death.html')

@app.route('/discharge')
def discharge():
    return render_template('discharge.html')


@app.route('/discharged')
def discharged():
    return render_template('discharged.html')

@app.route('/regional')
def regional():
    return render_template('regional.html')

@app.route('/total')
def total():
    return render_template('total.html')

@app.route('/all')
def all():
    return render_template('all.html')

@app.route('/discharge1')
def discharge1():
    return render_template('discharge1.html')





@app.route('/India_Covid_Status')
def get_data():
    # Convert DataFrame to JSON
    data_json = df.to_json(orient='records')
    return data_json

if __name__ == '__main__':
    app.run(debug=True)
