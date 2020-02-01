from flask import Flask, render_template
from form import SendForm
from config import Config

app=Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


@app.route('/send')
def send():
    form = SendForm()
    return render_template('forms.html',title='Send', form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
