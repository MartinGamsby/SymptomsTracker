import os
import subprocess
from datetime import datetime

from report import generate_pdf
from data import Symptom, Event, String, Date, MonthDate

def run_cmd(arg):
    args = arg.split()
    args = [os.path.expandvars(i) for i in args]
    subprocess.run(args)

    
def main():
    print("Initializing")
    
    summary_text = String("""- Symptômes multi-systémiques sévères depuis décembre 2022.
<br />
- Sensibilité sévère au gluten et son retrait complet a résolu la majorité des symptômes pendant plusieurs mois.
<br />
- Cependant, reviennent lentement malgré un régime strict, et s'intensifient à chaque retour au domicile après une absence.""",

    """- Severe multisystem symptoms since December 2022.
<br />
- Severe gluten sensitivity, and its complete withdrawal resolved most of the symptoms for several months.
<br />
- However, they slowly return despite a strict diet, and intensify each time returning home after an absence.""")



    key_events = [
        Event(String("<div style='text-align:center'>2022</div>",""), String("","")),
        Event(MonthDate(datetime(
            2022, 12, 20)), String(
            "Orteil cassé. Important parce que je ne suis pas maladroit d'habitude. Mais j'ai commencé à le devenir et avec du recul, c'était déjà commencé, avec une baisse de sensibilité aussi. Tout devient pire à chaque semaine à partir d'ici.", 
            "Broken toe. Important because I'm not usually clumsy. But I started to become clumsy, and looking back, it had already started, with a decrease in sensitivity as well. Everything is getting worse every week starting here.")),
        Event(String("<div style='text-align:center'>2023</div>",""), String("","")),
        Event(MonthDate(datetime(
            2023, 2, 12)), String(
            "Premier espoir: ça va un peu mieux après une 'retraite' de 2 jours avec spa. Première amélioration depuis le début, 2 mois auparavant.", 
            "First hope: I'm feeling a little better after a two-day spa 'retreat'. This is the first improvement since it started, two months ago.")),
        Event(MonthDate(datetime(
            2023, 2, 15)), String(
            "Tout devient pire à chaque semaine. Je prends rendez-vous avec un médecin.", 
            "Everything is getting worse every week. I make an appointment with a doctor.")),
        Event(MonthDate(datetime(
            2023, 2, 28)), String(
            "Rendez-vous avec le médecin: Tests sanguins, EMG.", 
            "Appointment with the doctor: Blood tests, EMG.")),
        Event(MonthDate(datetime(
            2023, 3, 1)), String(
            "Le symptôme de 'pression' semble apparaître après la prise de sang. Et d'autres symptômes ont une 2e vague.",
            "The 'pressure' symptom seems to appear after the blood test. And other symptoms have a 2nd wave.")),
        ]
        
        

    symptoms = [
                
        Symptom(name=String(
                "Engourdissement",
                "Numbness"),
            start_date=Date(datetime(
                2022, 12, 21)),
            current_status=String(
                "Résolu à 80% après avoir remédié un nerf coincé.",
                "80% resolved after fixing a pinched nerve."),
            notes=String(
                "Parfois locallisé. Quelques périodes le corps au complet.",
                "Sometimes localized. Sometimes the whole body.")
            ),
                
        Symptom(name=String(
                "Palpitations",
                "Heart Palpitations"),
            start_date=Date(datetime(
                2022, 12, 25)),
            current_status=String(
                "Était résolu sans gluten, mais revient tranquillement.",
                "Was resolved gluten-free, but is slowly coming back."),
            notes=String(
                "Plus souvent le soir, quelques fois réveillé avec palpitations, sueurs, engourdissements.",
                "More often in the evening, sometimes waking up with palpitations, sweating, numbness.")
            ),
               
        Symptom(name=String(
                "Maladroit",
                "Clumsy"),
            start_date=Date(datetime(
                2022, 12, 26)),
            current_status=String(
                "Résolu à 80% après nerf décoincé",
                "80% resolved after nerve unpinched"),
            notes=String(
                "Problèmes de dextérité, échappe les choses. Tourner les pages, clavier et piano difficiles. S'accroche partout. Mots mal articulés.",
                "Dexterity issues, dropping things. Turning pages, keyboard and piano difficulties. Gets caught on everything. Slurred words.")
            ),
                
        Symptom(name=String(
                "Faiblesse musculaire",
                "Muscle weakness"),
            start_date=Date(datetime(
                2023, 1, 13)),
            #triggers=String(
            #    "Finalement trouvé que c'était dû à un nerf coincé",
            #    "Found to be caused by a pinched nerve"),
            current_status=String(
                "Résolu à 100% après nerf décoincé",
                "100% resolved after nerve unpinched"),
            notes=String(
                "Finalement trouvé que c'était dû à un nerf coincé. Avant: difficulté à fermer les doigts, à prendre une assiette à bout de doigts.",
                "Found to be caused by a pinched nerve. Before: difficulty closing fingers, picking up a plate with fingertips."),
            ),
                
        Symptom(name=String(
                "Faiblesse générale",
                "General weakness"),
            start_date=Date(datetime(
                2023, 2, 4)),
            current_status=String(
                "Résolu à 50% après nerf décoincé",
                "50% resolved after nerve unpinched"),
            notes=String(
                "Avant le nerf décoincé, parfois impossible de marcher sans devoir s'appuyer sur quelque chose. Lance pas assez fort, etc.",
                "Before nerve unpinched, sometimes impossible to walk without having to lean on something. Doesn't throw strong enough, etc.")
            ),
                
        Symptom(name=String(
                "Étourdissements / Manque d'équilibre",
                "Dizziness / Loss of balance"),
            start_date=Date(datetime(
                2023, 2, 13)),
            current_status=String(
                "Était résolu sans gluten, mais revient tranquillement.",
                "Was resolved gluten-free, but is slowly coming back."),
            notes=String(
                "",
                "")
            ),
                
        Symptom(name=String(
                "Tremblements",
                "Tremors"),
            start_date=Date(datetime(
                2023, 1, 14)),
            #triggers=String(
            #    "Finalement trouvé que c'était dû à un nerf coincé",
            #    "Found to be caused by a pinched nerve"),
            current_status=String(
                "Résolu à 100% après nerf décoincé",
                "100% resolved after nerve unpinched"),
            notes=String(
                "",
                "")
            ),
                
        Symptom(name=String(
                "Respiration difficile / Essouflement rapide",
                "Difficulty breathing / Rapid shortness of breath"),
            start_date=Date(datetime(
                2023, 2, 15)),
            current_status=String(
                "Était résolu sans gluten, mais revient tranquillement.",
                "Was resolved gluten-free, but is slowly coming back."),
            notes=String(
                "",
                "")
            ),
        ]
    
    print("PDF generation start")
    generate_pdf(patient_name="Martin Gamsby",
        summary_text=summary_text,
        symptoms=symptoms,
        key_events=key_events,
        output_pdf='output/rapport.pdf',
        language="fr")
    print("PDF generation end")
    run_cmd("cmd.exe /c start output\\rapport.pdf")
    #run_cmd("explorer.exe output")


if __name__ == "__main__":
    main()
