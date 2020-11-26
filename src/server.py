from flask import Flask
server = Flask(__name__)

@server.route("/")
def root():
    return "Bootstraped Flask Application"

if __name__ == "__main__":
   server.run(host='0.0.0.0') 