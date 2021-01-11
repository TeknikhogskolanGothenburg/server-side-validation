from flask import Flask, render_template, redirect, request, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey!"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login_get():
    return render_template('login.html', error=None)


@app.route('/login', methods=['POST'])
def login_post():
    if request.form['username'] != 'admin' or request.form['password'] != 'supersecret1':
        flash("Pucko! Du skrev fel!")
        return render_template('login.html', error="Invalid credentials")
    flash('You are now logged in!')
    return render_template('index.html')
    #return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
