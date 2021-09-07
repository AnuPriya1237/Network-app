from flask import Flask, request, render_template
from flask_cors import CORS

import model
app = Flask(__name__)
CORS(app)
@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        model.create_post(name, post)



    posts = model.get_posts()

    return render_template('index.html',posts = posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001,debug = True)




