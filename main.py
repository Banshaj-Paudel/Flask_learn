from flask import Flask, request, render_template

# Create instance
app = Flask(__name__)

# index route
@app.route("/")
def index():
    return "<h1>Index Page!!</h1>"

# static route
@app.route("/smoke")
def smoke():
    return "<h1>Smoke Page!!</h1>"

# dynamic route
@app.route("/device/<int:name>")
def user(name):
    return f"<h1>Hello, {name + name}!!</h1>"

# Defining allowed methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            return f"<h1>Login successful!!</h1>"
    else:
        return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)