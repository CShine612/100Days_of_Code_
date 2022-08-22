import requests
from flask import Flask, render_template


app = Flask(__name__)

response = requests.get("https://api.npoint.io/4af156202f984d3464c3")
data = response.json()
print(data)

@app.route('/')
def home():
    return render_template("index.html", data=data)

@app.route("/<int:id>")
def post(id):
    return render_template("post.html", data=data, id=id)

if __name__ == "__main__":
    app.run(debug=True)
