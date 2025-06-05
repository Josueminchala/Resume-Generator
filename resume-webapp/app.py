from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    # Add your logic here to handle the form submission
    return "Resume generated!"

if __name__ == "__main__":
    app.run(debug=True)
