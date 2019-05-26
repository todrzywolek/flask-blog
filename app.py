from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Tomasz Odrzywolek',
        'title': 'Blog Post 1',
        'content': 'Hello World Post',
        'date_posted': 'May 25, 2019'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'My favourite languages',
        'date_posted': 'May 26, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(debug=True)
