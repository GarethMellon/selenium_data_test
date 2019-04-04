from flask import Flask, render_template, request, redirect, url_for, flash
from mongo_connect import mongo_connect
import os

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = ({"fname": request.form['fname'], "sname": request.form['sname'], "email": request.form['email']})
        try:
            coll = mongo_connect()
            coll.insert_one(data)
            flash("Your data has been submitted")
        except Exception as ex:
            flash("There was an error with the data {}".format(ex))

        return redirect(url_for('home'))

    return render_template("index.html")


if __name__ == '__main__':
    app.secret_key = os.environ.get('secret_key')
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)
