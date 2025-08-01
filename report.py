import jinja2
import pdfkit
import locale
from datetime import datetime

from data import CompleteDate


def run_cmd(self, arg):
    args = arg.split()
    args = [os.path.expandvars(i) for i in args]
    subprocess.run(args)


def generate_pdf(patient_name, summary_text, symptoms_summary_text, symptoms, key_events, notable_events, output_pdf, language="fr", orientation='Landscape'):

    if language == "fr":        
        locale.setlocale(locale.LC_ALL, 'fr_CA.UTF-8')
        html_template = 'templates/report.html'
    else: #en
        locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')
        html_template = 'templates/report_en.html'
    
    report_date = CompleteDate(datetime.today())

    context = { 'patient_name': patient_name,
                'report_date': report_date,
                'summary_text': summary_text,
                'symptoms_summary_text': symptoms_summary_text,
                'key_events': key_events,
                'notable_events': notable_events,
                'symptoms': symptoms
              }

    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template(html_template)
    output_text = template.render(context)
    
    with open(output_pdf.replace(".pdf",".html"), "w", encoding="utf-8") as f:
        f.write(output_text)    
    
    
    options = {
          'encoding': 'UTF-8',
          'page-size': 'A4',
          'orientation': orientation
      }

    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    pdfkit.from_string(output_text, output_pdf, configuration=config, options=options)

