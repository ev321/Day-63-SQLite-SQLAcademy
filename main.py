from flask import Flask, render_template, request, redirect, url_for

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

all_books = []  # Global list to store books


@app.route('/')
def home():
    return render_template("index.html", books=all_books)  # Pass books to the template


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        # Retrieve form data
        new_book = {
            'title': request.form.get('title'),
            'author': request.form.get('author'),
            'rating': request.form.get('rating')
        }
        all_books.append(new_book)  # Append new book to the global list
        return redirect(url_for('home'))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

