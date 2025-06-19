from flask import Flask, request, render_template, send_from_directory
import yaml
from weasyprint import HTML

app = Flask(__name__)
@app.route('/output/<filename>')
def serve_file(filename):
    return send_from_directory('output', filename)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    access = request.data.decode('utf-8')

    try:
        data = yaml.safe_load(access)
    except yaml.YAMLError:
        return "Invalid YAML format.", 400

    html_string = render_resume_html(data)
    HTML(string=html_string).write_pdf('resume-webapp/output/resume.pdf')

    with open('resume-webapp/output/resume.html', 'w', encoding='utf-8') as f:
        f.write(html_string)

    return "Resume successfully generated!", 200

def render_resume_html(data):
    return render_template("template.html", **data)

if __name__ == "__main__":
    app.run(debug=True)
