from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html')

@app.route('/bug')
def bug():
    return 'Lets check what is wrong here'

@app.route('/name/<username>')
def username(username):
    return f'Hello {username}'


# if __name__ == "__main__":
#     app.run(debug = True)