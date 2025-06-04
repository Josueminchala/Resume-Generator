import yaml
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

def load_file():
    with open("resume.yaml", encoding="utf-8") as stream:
        try:
            data_dict = (yaml.safe_load(stream))
            return data_dict
        except yaml.YAMLError as exc:
            print(exc)
        
def load_template():
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('template.html')
    return template

def main():
    resume_data = load_file()
    template = load_template()
    rendered_html = template.render(resume_data)
    with open('output/resume.html', 'w', encoding='utf-8') as f:
        f.write(rendered_html)
    HTML('output/resume.html').write_pdf('output/resume.pdf')    

if __name__ == "__main__":
    main()
