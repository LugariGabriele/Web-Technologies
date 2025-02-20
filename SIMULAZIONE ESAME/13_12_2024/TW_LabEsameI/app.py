import csv
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    prodotti = []
    intestazioni = []

    # esercizio 1
    with open('data/magazzino.csv', 'r', encoding='utf-8') as file:
        lettore_csv = csv.DictReader(file)
        intestazioni = lettore_csv.fieldnames
        for riga in lettore_csv:
            prodotti.append(riga)

    return render_template('index.html', prodotti=prodotti, intestazioni=intestazioni)


# esercizio 3
@app.route('/prodotto/<codice>')
def prodotto(codice):
    prodotto = None
    with open('data/magazzino.csv', 'r', encoding='utf-8') as file:
        lettore_csv = csv.DictReader(file)
        for riga in lettore_csv:
            if riga['codice'] == codice:
                prodotto = riga
                break

    return render_template('prodotto.html', prodotto=prodotto)


# esercizio 4
@app.route('/api/elimina/<codice>', methods=['DELETE'])
def api_elimina_prodotto(codice):
    prodotti = []

    with open('data/magazzino.csv', 'r', encoding='utf-8') as file:
        lettore_csv = csv.DictReader(file)
        for riga in lettore_csv:
            if riga['codice'] != codice:
                prodotti.append(riga)

    with open('data/magazzino.csv', 'w', encoding='utf-8') as file:
        intestazioni = ['codice', 'nome', 'quantita', 'prezzo']
        scrittore_csv = csv.DictWriter(file, fieldnames=intestazioni)
        scrittore_csv.writeheader()
        for prodotto in prodotti:
            scrittore_csv.writerow(prodotto)

    return {'eliminato': True}


# esercizio 5
@app.route('/api/prodotti')
def api_prodotti():
    prodotti = []

    with open('data/magazzino.csv', 'r', encoding='utf-8') as file:
        lettore_csv = csv.DictReader(file)
        for riga in lettore_csv:
            prodotti.append(riga)

    return {'prodotti': prodotti}


# api to get the product with the specified code
@app.route('/api/prodotto/<codice>')
def api_prodotto(codice):
    prodotto = None

    with open('data/magazzino.csv', 'r', encoding='utf-8') as file:
        lettore_csv = csv.DictReader(file)
        for riga in lettore_csv:
            if riga['codice'] == codice:
                prodotto = riga
                break

    return {'prodotto': prodotto}


# esercizio 6
@app.route('/react')
def react():
    return render_template('index_react.html')


if __name__ == '__main__':
    app.run(debug=True)
