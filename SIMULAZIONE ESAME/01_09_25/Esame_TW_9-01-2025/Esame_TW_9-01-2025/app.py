from flask import Flask, render_template, jsonify, request
import csv
import os

app = Flask(__name__)

# Percorso al file events.csv
data_file = os.path.join(os.path.dirname(__file__), 'data', 'events.csv')


# ESERCIZIO #2: Visualizzare eventi nella route /index
@app.route('/index')
def index():
    events = get_all_events()
    return render_template('index.html', events=events)


# ESERCIZIO 1
def get_all_events():
    events = []
    with open(data_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            events.append(row)
    return events


# ESERCIZIO #3: Dettaglio di un evento
@app.route('/event/<event_code>')
def event_details(event_code):
    events = get_all_events()
    for event in events:
        if event['code'] == event_code:
            return render_template('event_detail.html', event=event)
    return "Evento non trovato", 404


# Funzione per scrivere nel file CSV
def write_events(events):
    with open(data_file, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['code', 'name', 'sport', 'date', 'place', 'available_places']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(events)


# ESERCIZIO #4: Prenotare un posto
@app.route('/api/book/<event_code>', methods=['POST'])
def book_event(event_code):
    events = get_all_events()
    for event in events:
        if event['code'] == event_code:
            available_places = int(event['available_places'])
            if available_places > 0:
                event['available_places'] = available_places - 1
                write_events(events)
                return jsonify({'success': True, 'message': 'Posto prenotato con successo!'})
            return jsonify({'success': False, 'message': 'Posti esauriti!'}), 400
    return jsonify({'success': False, 'message': 'Evento non trovato!'}), 404


# ESERCIZIO #5: API per gli eventi
# ritorna eventi json
@app.route('/api/events', methods=['GET'])
def get_events():
    event_details = get_all_events()
    return jsonify(event_details)


# ritorna dati evento specifico in json
@app.route('/api/event/<event_code>', methods=['GET'])
def get_event(event_code):
    events = get_all_events()
    for event in events:
        if event['code'] == event_code:
            return jsonify(event)
    return jsonify({'message': 'Evento non trovato!'}), 404


#ESERCIZIO #6: SPA con React
@app.route('/react')
def react():
    return render_template('index_react.html')


if __name__ == '__main__':
    app.run(debug=True)
