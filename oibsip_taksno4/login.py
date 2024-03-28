from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret_key_for_session'  # Change this to a more secure key in production

# Sample database to store user credentials
users = {'user1': 'password1', 'user2': 'password2'}

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return 'Username already exists! Please choose another username.'
        users[username] = password
        return 'Registration successful! You can now <a href="/login">login</a>.'
    return render_template('register.html')

# Route for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users or users[username] != password:
            return 'Invalid username or password. <a href="/login">Try again</a>.'
        session['logged_in'] = True
        session['username'] = username
        return redirect(url_for('secured'))
    return render_template('login.html')

# Route for secured page
@app.route('/secured')
def secured():
    if 'logged_in' in session:
        return render_template('secpage.html')
    return redirect(url_for('login'))

# Route for logout
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
