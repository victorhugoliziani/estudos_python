from flask import Flask

app = Flask(__name__)


@app.route("/<numero>", methods=['GET'])
def ola(numero):
    return 'Hello Wolrd. {}'.format(numero)


if __name__ == "__main__":
    app.run(debug=True)
