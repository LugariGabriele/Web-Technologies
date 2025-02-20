from itertools import product

from flask import Flask, render_template, jsonify, request
import csv
import os

app = Flask(__name__)

data_file = os.path.join(os.path.dirname(__file__), 'data', 'products.csv')


# ESERCIZIO 1 scrivere una funzione che legga e restituisca tutti i prodotti di products.csv
def get_all_products():
    products = []
    with open(data_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            products.append(row)
    return products


# ESERCIZIO 2  modificare la route /index per renderizzare un template index.html
# che estenda il base. index.html deve mostrare una tabella con l'elenco dei prodotti
# disponibili, se non ci sono prodotti disponibili deve mostrare un messaggio "Nessun prodotto disponibile"
# nella tabella deve essere riportato solo il nome del prodotto,il prezzo e la dicitura esaurito
# in una colonna a parte in caso del prodotto non sia disponibile
@app.route('/index')
def index():
    products = get_all_products()
    return render_template('index.html', products=products)


# ESERCIZIO 3 rendere cliccabile il nome del prodotto nella tabella. quando ci clicca viene reinderizzato
# alla route /product/<product_code> che mostra il dettaglio del prodotto. nella pagina di dettaglio devono essere
# presenti tutte le informazioni del prodotto e anche un pulsante indietro per tornare a index.html

@app.route('/product/<product_code>')
def product_detail(product_code):
    products = get_all_products()
    product = next((p for p in products if p['codice_prodotto'] == product_code), None)
    if product:
        return render_template('product_detail.html', product=product)
    else:
        return "Prodotto non trovato", 404


# ESERCIZIO 4 nella pagina del prodotto deve essere presente un pulsante "Acquista" che deve chiamare un API /api/buy/<product_code> tramite
# il metodo POST. ridurre di uno la disponibiltà del prodotto e salvare il file products.csv. gestire eventuali errori come se il prodotto non è disponibile mostrando messaggi
# opportuni all utente

@app.route('/api/buy/<product_code>', methods=['POST'])
def buy_product(product_code):
    products = get_all_products()
    product = next((p for p in products if p['codice_prodotto'] == product_code), None)

    if product:
        if int(product['disponibilita']) > 0:
            product['disponibilita'] = str(int(product['disponibilita']) - 1)
            with open(data_file, 'w', encoding='utf-8', newline='') as file:
                fieldnames = products[0].keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(products)
            return jsonify({'message': 'Acquisto completato'}), 200
        else:
            return jsonify({'message': 'Prodotto esaurito'}), 400
    else:
        return jsonify({'message': 'Prodotto non trovato'}), 404


# ESERCIZIO 5 creare una API che restituisce tutti i prodotti in formato JSON
# ed un aòtra per restituire i dettagli del singolo prodotto basandosi sul codice del prodotto
# non è rischisto che ritorni la lista con le colonne del file, solo il dizionario deI dati del prodotto

@app.route('/api/products', methods=['GET'])
def get_products():
    products = get_all_products()
    return jsonify(products)


@app.route('/api/products/<codice_prodotto>', methods=['GET'])
def get_event(codice_prodotto):
    products = get_all_products()
    for p in products:
        if p['codice_prodotto'] == codice_prodotto:
            return jsonify(p)
    return jsonify({'message': 'Evento non trovato!'}), 404


# ESERCIZIO 6 creare una route /react lato flask per renderizzare il template index_react.html
# dove costruire una SPA con React. tutte le route impostate con React devono seguire
# il prefisso /react, ad esempio /react/product_detail, /react/buy,ecc..

@app.route('/react')
def react():
    return render_template('index_react.html')


# ESERCIZIO #8
@app.route('/api/products/filter', methods=['POST'])
def filter_products():
    name_filter = request.json.get('name', '').lower()  # Recupera il filtro dal payload della richiesta
    products = get_all_products()
    if name_filter:
        products = [p for p in products if name_filter in p['nome_prodotto'].lower()]
    return jsonify(products)


if __name__ == '__main__':
    app.run(debug=True)
