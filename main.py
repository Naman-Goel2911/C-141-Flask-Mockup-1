from flask import Flask, jsonify, request
import csv

all_articles = []

with open('articles.csv', 'r', encoding='utf-8') as f:
    csvreader = csv.reader(f)
    data = list(csvreader)
    all_articles = data[1:]

liked_articles = []
disliked_articles = []

app = Flask(__name__)

@app.route("/get-articles")

def get_articles():
    return jsonify({
        "data": all_articles[0],
        "status": "Success!"
    })

@app.route('/liked-article', methods = ['POST'])

def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "Success!"
    }), 201

@app.route('/disliked-article', methods = ['POST'])

def disliked_article():
    article = all_articles[0]
    disliked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "Success!"
    }), 201