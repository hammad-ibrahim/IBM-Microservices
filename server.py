from flask import Flask
app = Flask("Hello Form the World of COde Base")
@app.route("/")
def hello ():
    return " Hello From COde base with Hammad "

if __name__ == "__name__":
    app.run(debug=True)
