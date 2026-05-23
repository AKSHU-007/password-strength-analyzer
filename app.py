from flask import Flask, render_template, request, jsonify
import re

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check',methods=['POST'])

def check():

    password=request.json['password']

    score=0
    suggestions=[]

    if len(password)>=8:
        score+=2
    else:
        suggestions.append(
        "Increase password length")

    if re.search("[A-Z]",password):
        score+=2
    else:
        suggestions.append(
        "Add uppercase letter")

    if re.search("[0-9]",password):
        score+=2
    else:
        suggestions.append(
        "Add numbers")

    if re.search("[!@#$%^&*]",password):
        score+=2
    else:
        suggestions.append(
        "Add special characters")

    strength="Weak"

    if score>=6:
        strength="Medium"

    if score>=8:
        strength="Strong"

    return jsonify({
        "score":score,
        "strength":strength,
        "suggestions":suggestions
    })

import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )