
from flask import Flask, render_template, request

from getdata import getHitRepo


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/user', methods=['POST'])
def handle_data():
    username = request.form['username']
    print(username)
    x = getHitRepo(username)
    if x=="err":
        return render_template('err.html')
    elif x=="frr":
        return render_template('notenough.html')

    else:
        return render_template('result.html', res=x, username = username)
    # return render_template('err.html')
if __name__ == "__main__":
    app.run(debug=True)