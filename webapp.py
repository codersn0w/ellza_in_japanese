# coding: utf-8
import json, html
from flask import Flask, render_template, request, jsonify
from reply_generator import generate_reply
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		query = html.escape(request.form['chat_text'])
		if query == '':
			reply = '再度入力してください。'
		else:
		    reply = generate_reply(query)
		return jsonify(results = reply)
	else:
		return render_template('index.html')

app.run(port=9999, debug=True)
