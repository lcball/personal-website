import flask
app = flask.Flask(__name__)


@app.route('/<user>')
def show_user(user):
    context = { "user": user }
    return flask.render_template("../pages/index.html", context)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
