import os
import csv
from datetime import datetime
import json
from flask import Flask, render_template, request, jsonify, redirect, url_for

from soluzione.app import load_comments

app = Flask(__name__)

DATA_PATH = 'static\\data'

blog_path = os.path.join(DATA_PATH, 'blog.csv')
comments_path = os.path.join(DATA_PATH, 'comments.csv')

post_categories = [
    {"name": "Tecnologia", "description": "Articoli all'avanguardia sulle ultime innovazioni tecnologiche"},
    {"name": "Viaggi", "description": "Racconti di viaggio, consigli e avventure da tutto il mondo"},
    {"name": "Lifestyle", "description": "Riflessioni e consigli per migliorare la qualità della vita"}
]


def create_csv_if_not_exists(filename, header=[]):
    # Controlla se il file non esiste
    if not os.path.exists(filename):
        # Crea il file CSV con gli header passati
        with open(filename, mode='w+', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
        print(f"File '{filename}' creato con successo con header: {header}")
    else:
        print(f"File '{filename}' esiste già. Nessuna azione necessaria.")


# Funzione per leggere tutti i post.
def load_posts():
    # Controlla se il file CSV esiste. Se no, crealo passandogli degli header
    create_csv_if_not_exists(blog_path, header=['id', 'title', 'author', 'date', 'content', 'category'])

    with open(blog_path, 'r+', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        posts = list(csv_reader)

        return posts


@app.route('/')
def index():
    return render_template('index.html', post_categories=post_categories)


@app.route('/blog')
@app.route('/blog')
def blog_list():
    try:
        # Leggi i post dal file CSV
        posts = load_posts()
        return render_template('blog_list.html', posts=posts)
    except FileNotFoundError:
        return render_template('blog_list.html', posts=[])
    except Exception as e:
        return f"Error reading posts: {str(e)}", 500


@app.route('/new_post', methods=['POST', 'GET'])
def new_post():
    if request.method == 'POST':
        # METODO POST
        try:
            posts = load_posts()

            ids = [int(post["id"][1:]) for post in
                   posts]  # Estrai gli ID numerici dei post che di solito sono p001, p002, ecc. e prende solo num
            if len(ids) > 0:
                new_id = "P" + str(max(ids) + 1).zfill(3)
            else:
                new_id = "P001"

                # Dati del nuovo post
            new_post = {
                'id': new_id,
                'title': request.form['title'],
                'author': request.form['author'],
                'date': datetime.now().strftime('%Y-%m-%d'),
                'content': request.form['content'],
                'category': request.form['category']
            }

            with open(blog_path, 'a', encoding='utf-8') as file:
                fieldnames = ['id', 'title', 'author', 'date', 'content', 'category']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow(new_post)

            print('Post creato con successo!', 'success')
            return redirect(url_for('blog_list'))

        except Exception as e:

            print(f'Errore nella creazione del post: {str(e)}', 'danger')
            return redirect(url_for('new_post'))

    else:
        return render_template('new_post.html', post_categories=post_categories)


@app.route('/react')
def index_react():
    return render_template('index_react.html')


# API REST
@app.route('/api/posts', methods=['GET'])
def get_posts():
    try:
        posts = load_posts()
        return jsonify(posts)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/comments/<post_id>', methods=['POST'])
def add_comment(post_id):
    try:
        # Read all the posts
        posts = load_posts()

        # Find the specific post
        post_found = None
        post_index = -1
        for i, post in enumerate(posts):
            if post['id'] == post_id:
                post_found = post
                post_index = i
                break

        if not post_found:
            return jsonify({'success': False, 'message': 'Post not found'}), 404

        # Load comments
        new_comment = request.get_json()  # Get data from the request

        comments = load_comments()

        ids = [int(comment["id"][1:]) for comment in comments]

        if len(ids) > 0:
            new_id = "C" + str(max(ids) + 1).zfill(3)
        else:
            new_id = "C001"

        # New comment
        new_comment = {
            'id': new_id,
            'post_id': new_comment['post_id'],
            'author': new_comment['author'],
            'email': new_comment['email'],
            'text': new_comment['text'],
            'date': datetime.now().strftime('%Y-%m-%d')
        }

        # Rewrite all the file
        with open(comments_path, mode='a', encoding='utf-8', newline='') as file:
            fieldnames = ['id', 'post_id', 'author', 'email', 'text', 'date']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(new_comment)

        return jsonify({'success': True, 'message': 'Comment added'}), 201

    except Exception as e:
        print(e)
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/post/<post_id>', methods=['GET'])
def get_post(post_id):
    try:
        posts = load_posts()

        post = next((post for post in posts if post['id'] == post_id), None)

        if post:
            comments = load_comments()
            comments_to_return = [comment for comment in comments if comment["post_id"]== post_id]
            post["comments"] = comments_to_return

            return jsonify(post)
        else:
            return jsonify({'error': 'Post not found'}), 404


    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
