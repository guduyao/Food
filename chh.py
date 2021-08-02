from flask import Flask, redirect, url_for, request
from predict import result
from flask import render_template
from PIL import Image
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
   img = result(name)
   return render_template("pridet.html",user_image = img)


@app.route('/jm',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['myfile']
      return redirect(url_for('success',name = user))
      # return request.form["image"]


   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))


if __name__ == '__main__':
   app.run(host='0.0.0.0')