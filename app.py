from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'AshutoshGoswami'


if __name__ == "__main__":
    app.run()

# Don't Remove Credit @AshutoshGoswami24
