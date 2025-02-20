from flask import Flask, render_template
import csv
import os
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/team')
def team():
    team_members = [{
        'name': 'John Doe',
        'position': 'Founder and CEO',
        'email': 'john@company.com',
        'image': '1.jpg'
    }, {
        'name': 'Jane Smith',
        'position': 'Marketing Manager',
        'email': 'jane@company.com',
        'image': '2.jpg'
    }, {
        'name': 'Bob Lauren',
        'position': 'Accountant',
        'email': 'bob@company.com',
        'image': '3.jpg'

    }]

    return render_template('team.html', team_members=team_members)

def load_team_data():
    team_members = []
    csv_path = os.path.join(os.path.dirname(__file__), 'static','team_data.csv')

    try:
        with open(csv_path, mode= 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                team_members.append(row)
        return team_members
    except FileNotFoundError:
        print(f'File:{csv_path} not found')
        return []
    except Exception as e:
        print(f'Error loading data: {e}')
        return []

@app.route('/team_conCSV')
def team2():
    team_members = load_team_data()
    return render_template('team_conCSV.html', team_members=team_members)

if __name__ == '__main__':
    app.run(debug=True)
