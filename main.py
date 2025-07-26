import os
import subprocess
from datetime import datetime

from report import generate_pdf, Symptom, Event, String, Date, MonthDate

def run_cmd(arg):
    args = arg.split()
    args = [os.path.expandvars(i) for i in args]
    subprocess.run(args)

    
def main():
    print("Initializing")
    
    summary_text = String("""- Symptômes multi-systémiques sévères qui ont débuté en décembre 2022.
<br />
- Sensibilité sévère au gluten et son retrait complet a résolu la majorité des symptômes pendant plusieurs mois.
<br />
- Cependant, reviennent lentement malgré un régime strict, et s'intensifient à chaque retour au domicile après une absence.""",
    "test en")


    symptoms = [
        Symptom(String("Fatigue", "Fatigue"), 
            String("Catégorie", "Category"), 
            Date(datetime(2022, 12, 20)),
            String("Déclencheurs", "Triggers"),
            String("Statut Actuel", "Current Status"), 
            String("Remarques", "Notes")),
               ]
    key_events = [
        Event(MonthDate(datetime(2022, 12, 20)), String("Orteil cassé", "Broke my toe"))]
    
    print("pdf start")
    generate_pdf(patient_name="Martin Gamsby",
        summary_text=summary_text,
        symptoms=symptoms,
        key_events=key_events,
        output_pdf='output/rapport.pdf',
        language="fr")
    print("pdf end")
    run_cmd("cmd.exe /c start output\\rapport.pdf")
    #run_cmd("explorer.exe output")


if __name__ == "__main__":
    main()
