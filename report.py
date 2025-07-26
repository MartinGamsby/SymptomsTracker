import jinja2
import pdfkit
from datetime import datetime
from dataclasses import dataclass


@dataclass
class Event:
    date: str
    description: str


@dataclass
class Symptom:
    name: str
    category: str
    start_date: str
    triggers: str
    current_status: str
    notes: str
    
    @property
    def subtotal_dollar(self):
        return f'${self.subtotal:.2f}'


def run_cmd(self, arg):
    args = arg.split()
    args = [os.path.expandvars(i) for i in args]
    subprocess.run(args)


def generate_pdf(patient_name, summary_text):
    item1 = "Item 1"
    item2 = "Item 2"
    item3 = "Item 3"

    subtotal1 = 123
    subtotal2 = 456
    subtotal3 = 789
    total = subtotal1 + subtotal2 + subtotal3

    report_date = datetime.today().strftime("%d %b, %Y")
    month = datetime.today().strftime("%B")

    name: str
    category: str
    subtotal: float
    start_date: str
    triggers: str
    current_status: str
    notes: str
    
    symptoms = [Symptom("Fatigue", "Catégorie", "Start date", "Triggers", "Current Status", "Notes"),
               ]
    key_events = [Event("December 2022", "Broke my toe")]
    context = { 'patient_name': patient_name,
                'report_date': report_date,
                'summary_text': summary_text,
                'key_events': key_events,
                'symptoms': symptoms
              }

    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)

    html_template = 'templates/report.html'
    template = template_env.get_template(html_template)
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    output_pdf = 'output/report.pdf'
    pdfkit.from_string(output_text, output_pdf, configuration=config, css='templates/report.css')

