import csv
import os
from asyncore import write
from crypt import methods
from logging import exception
from string import whitespace

from Tools.scripts.make_ctype import method
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)  # creazione dell'app


@app.route('/')  # questa e una roote
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/books')
def books():
    books = load_book_data()
    return render_template('books.html', books=books)


@app.route('/api/books/<title>', methods=['GET'])
def api_books(title):
    books = load_book_data()
    for book in books:
        if book['Title'] == title:
            return jsonify(book)
    return jsonify({'error': 'book not found'}), 404


@app.route('/api/books', methods=['POST'])
def api_add_books():
    try:
        new_book = request.get_json()
        books = load_book_data()
        if not all(key in new_book for key in ('Title', 'Author')):
            return jsonify({'Error': 'Missing fiels'})

        books.append(new_book)
        print(new_book)
        # append to csv file
        csv_path = os.path.join(os.path.dirname(__file__), 'static/files/books.csv')
        with open(csv_path, mode='a', encoding='utf-8', newline='') as cvs_file:
            write = csv.DictWriter(cvs_file, fieldnames=['Title', 'Author', 'Genre', 'Height', 'Publisher'])
            write.writerow(new_book)

        return jsonify({'message': 'screenwriter'}), 201
    except Exception as e:
        return jsonify({'Error': str(e)}), 500


# funzione gestione caricamento dati da file
def load_team_data():
    team_members = []  # creo lista team vuota
    csv_path = os.path.join(os.path.dirname(__file__), 'static/files/team.csv')  # creo puntatore a file

    try:
        with open(csv_path, mode='r', encoding='utf-8') as csvfile:  # apro in modalità lettura file csv
            reader = csv.DictReader(csvfile)  # creo ogg reader per file
            for row in reader:  # per ogni riga file letta con il reader  la leggo e la metto in lista
                team_members.append(row)
            return team_members  # una volta finita lettura ritorno lista
    except FileNotFoundError:
        print('File not found')


@app.route('/team')
def team():
    # prima di fare passagio a pagina html prepariamo i dati (team)
    team_members = load_team_data()
    # passiamo a pagina html  e rendiamo disponibile lista team a file html
    return render_template('team.html', team_members=team_members)

@app.route('/api/team',methods=['GET'])
def get_data_team():
    team_members = load_team_data()
    return jsonify(team_members)

def load_book_data():
    books = []
    csv_path = os.path.join(os.path.dirname(__file__), 'static/files/books.csv')

    try:
        with open(csv_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                books.append(row)
            return books
    except FileNotFoundError:
        print(f"Warning: {csv_path} not found")
        return []
    except Exception as e:
        print(f"Error loading: {e}")
        return []


if __name__ == '__main__':
    app.run(debug=True)
