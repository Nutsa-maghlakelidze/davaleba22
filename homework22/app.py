from flask import Flask, render_template, request, session, redirect, url_for
from datetime import timedelta
app = Flask(__name__)
app.secret_key = 'dzaandzneliparoli123'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        session['user'] = user
        return redirect(url_for('home'))
    else:
        if 'user' in session:
            return redirect(url_for('home'))
        return render_template('login.html')

@app.route('/home')
def home():
    if 'user' in session:
        user = session['user']
        return render_template('home.html', username=user)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True)
