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
- Nerf décoincé a résolu quelques symptômes et réduit la majorité des symptômes pendant plusieurs mois.
<br />
- Les symptômes reviennent ensuite lentement. Sensibilité sévère au gluten trouvée par élimination, et son retrait complet a résolu la majorité des symptômes pendant plusieurs mois.
<br />
- Les symptômes reviennent ensuite lentement malgré un régime strict, et s'intensifient à chaque retour au domicile après une absence (Moisissure soupçonnée).""",

    """- Severe multisystem symptoms since December 2022.
<br />
- Unpinched nerve resolved some symptoms and reduced the majority of symptoms for several months.
<br />
- Symptoms then slowly return. Severe gluten sensitivity was found through an elimination diet, and complete removal resolved most symptoms for several months.
<br />
- Symptoms then return slowly despite a strict diet, and intensify each time you return home after an absence (suspected mold).""")



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
        #Event(MonthDate(datetime(
        #    2023, 3, 1)), String(
        #    "Le symptôme de 'pression' semble apparaître après la prise de sang. Et d'autres symptômes ont une 2e vague.",
        #    "The 'pressure' symptom seems to appear after the blood test. And other symptoms have a 2nd wave.")),
        Event(MonthDate(datetime(
            2023, 3, 7)), String(
            "Réveil avec la 'pression', palpitations, membres lourds.",
            "Waking up with 'pressure', palpitations, heavy limbs.")),
        Event(MonthDate(datetime(
            2023, 3, 13)), String(
            "Rendez-vous avec un 2e médecin: C'était quoi, le diabète? (De l'hypoglycémie? Anémie?) -- Il a dit 'C'est de l'anxiété'", 
            "Appointment with a 2nd doctor: What was that? diabetes? (Hypoglycemia? Anemia?) -- He said 'It's anxiety'")),
        Event(MonthDate(datetime(
            2023, 3, 27)), String(
            "EMG + visite neurologue: EMG ok, neurologue dit que ça peut être un nerf coincé.", 
            "EMG + neurologist visit: EMG ok, neurologist says it could be a pinched nerve.")),
        Event(MonthDate(datetime(
            2023, 4, 3)), String(
            "Je saigne du nez. Rien d'inquiétant, mais je réalise plus tard que c'est parce que je ne sentait pas mon nez et j'ai trop gratté (sans rien sentir). Ça fait combien de temps?",
            "My nose is bleeding. Nothing concerning, but I later realize it's because I couldn't feel my nose and I scratched too much (without feeling anything). How long has it been?")),
        Event(MonthDate(datetime(
            2023, 4, 18)), String(
            "2e rendez-vous avec le 1er médecin (suivi):  Je parles de la perte de sensation. Elle me prescrit des vitamines B12 (sang: dans les normes, mais bas), et demande un IRM (pour éliminer la sclérose en plaques)", 
            "2nd appointment with the 1st doctor (follow-up): I talk about the loss of sensation. She prescribes me vitamin B12 (blood: within the norm, but low), and orders an MRI (to rule out multiple sclerosis)")),
        Event(MonthDate(datetime(
            2023, 4, 20)), String(
            "Rendez-vous avec un ostéopathe pour le nerf coincé (Aucune différence notable après)", 
            "Appointment with an osteopath for the pinched nerve (No noticeable difference after)")),
        Event(MonthDate(datetime(
            2023, 4, 25)), String(
            "IRM 1", "")),
        Event(MonthDate(datetime(
            2023, 5, 12)), String(
            "IRM 2 (+Gadolinium)", "")),
        Event(MonthDate(datetime(
            2023, 6, 1)), String(
            "Résultat d'IRM: Rien, seulement télangiectasie? 6mm?",
            "MRI result: Nothing, just a telangiectasia? 6mm?")),
        #Event(MonthDate(datetime(
        #    2023, 6, 13)), String(
        #    "Rendez-vous avec un massothérapeute pour 'préparer' pour l'acupuncture (on essaye tout)", 
        #    "Appointment with a massage therapist to 'prepare' for acupuncture (we try everything)")),
        #Event(MonthDate(datetime(
        #    2023, 6, 29)), String(
        #    "Rendez-vous avec un acupuncteur (on essaye tout) : demande si c'est une intolérance ou allergie (Je sais pas)",
        #    "Appointment with an acupuncturist (we try everything): ask if it's an intolerance or allergy (I don't know)")),
        Event(MonthDate(datetime(
            2023, 7, 5)), String(
            "Rendez-vous avec un 2e ostéopathe pour le nerf coincé (On réessaye): Ça va mieux! J'ai encore le manque de sensibilité, mais ça va 80% mieux, je suis content.",
            "Appointment with a 2nd osteopath for the trapped nerve (We'll try again): I'm getting better! I still have the lack of sensitivity, but it's 80% better, I'm happy.")),
        Event(MonthDate(datetime(
            2023, 9, 12)), String(
            "Rendez-vous avec l'ostéopathe. Peut-être qu'il peut régler ce qui reste...",
            "Appointment with the osteopath. Maybe he can fix what's left...")),
        Event(MonthDate(datetime(
            2023, 11, 8)), String(
            "Rendez-vous avec l'ostéopathe...",
            "Appointment with the osteopath...")),
        Event(MonthDate(datetime(
            2023, 11, 23)), String(
            "Rendez-vous avec l'ostéopathe...",
            "Appointment with the osteopath...")),
        Event(String("<div style='text-align:center'>2024</div>",""), String("","")),
        Event(MonthDate(datetime(
            2024, 12, 18)), String(
            "Rendez-vous avec un 2e acupuncteur. Ça règle un autre 80% de ma perte de sensibilité.",
            "Appointment with a second acupuncturist. That fixes another 80% of my loss of sensitivity.")),
        #Event(MonthDate(datetime(
        #    2024, 1, 8)), String(
        #    "Suivi acupuncteur",
        #    "Acupuncturist follow-up")),
        #Event(MonthDate(datetime(
        #    2024, 1, 29)), String(
        #    "Suivi acupuncteur",
        #    "Acupuncturist follow-up")),
        Event(MonthDate(datetime(
            2024, 2, 2)), String(
            "J'ai eu une révélation : le gluten. C'était difficile à trouver, parce qu'il y avait des traces dans la mayonnaise, l'avoine, etc.",
            "I had an epiphany : gluten. It was hard because I had traces in the mayonnaise, the oats, etc.")),
        #Event(MonthDate(datetime(
        #    2024, 2, 26)), String(
        #    "Suivi acupuncteur",
        #    "Acupuncturist follow-up")),
        Event(MonthDate(datetime(
            2024, 4, 4)), String(
            "Rendez-vous avec un 3e médecin: Coeliaque? Ils veulent que je fasse un gluten challenge pour tester (ça fait des mois que j'ai arrêté le gluten)", 
            "Appointment with a 3rd doctor: Celiac? They want me to do a gluten challenge to test (it's been months since I stopped eating gluten)")),
        Event(MonthDate(datetime(
            2024, 6, 4)), String(
            "DÉFI GLUTEN: Tout revient, je me sens très mal, et le médecin ne me recontacte pas, la secrétaire m'appelle pour dire que c'est négatif ... après 2 semaines, et plusieurs mois sans en prendre avant, pas demandé mes symptômes ni rien...",
            "GLUTEN CHALLENGE: Everything comes back, I feel very bad, and the doctor doesn't contact me again, the secretary calls me to say that it's negative... after 2 weeks, and several months without taking it before, not asking about my symptoms or anything...")),
        Event(MonthDate(datetime(
            2024, 9, 2)), String(
            "Première grosse réaction depuis longtemps: J'ai reçu une goutte de bouillon (gluten) dans le visage/yeux. Pas besoin d'en manger...",
            "First major reaction in a long time: I got a drop of broth (gluten) in my face/eyes. No need to eat it...")),
        #Event(MonthDate(datetime(
        #    2024, 9, 24)), String(
        #    "Rendez-vous avec l'ostéopathe pour prévention.",
        #    "Appointment with the osteopath for prevention.")),
        Event(String("<div style='text-align:center'>2025</div>",""), String("","")),
        Event(MonthDate(datetime(
            2025, 5, 31)), String(
            "J'étais pratiquement sans symptômes pendant plus qu'un an, mais ça revient... 'Pression' et respiration difficile après avoir mangé une pizza sans gluten. (Et ça continue pour d'autres aliments, de plus en plus)",
            "I was virtually symptom-free for over a year, but it's back... 'Pressure' and difficulty breathing after eating gluten-free pizza. (And it continues for other foods, more and more)")),
        #Event(MonthDate(datetime(
        #    2025, 7, 7)), String(
        #    "Rendez-vous avec un 3e ostéopathe (le 2e est en vacances) pour un mal de dos",
        #    "Appointment with a 3rd osteopath (the 2nd is on vacation) for back pain")),
        #Event(MonthDate(datetime(
        #    2025, 7, 14)), String(
        #    "Suivi avec l'ostéopathe",
        #    "Follow-up with the osteopath")), 
        Event(MonthDate(datetime(
            2025, 7, 12)), String(
            "Je retourne de 3 nuits en camping: ça revient les symptômes ...",
            "I'm back from 3 nights camping: the symptoms are back...")),
        Event(MonthDate(datetime(
            2025, 7, 19)), String(
            "Après 3 nuits à la maison, je retourne 4 autres nuits à l'extérieur. Ok ce n'est pas une coïncidence, je réagis à ma maison aussi (en arrivant), pas juste la bouffe. Et c'est pire que le dernier retour.",
            "After 3 nights at home, I'm 4 more nights away. Okay, it's not a coincidence, I'm reacting to my home too (when I arrived), not just the food. And it's worse than the last time I came back.")),
            
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
                "Parfois locallisé. Quelques périodes le corps au complet (à partir d'avril 2023). Je ne sens pas un poil épilé, un nez qui saigne, mon pied par terre, Cogner sur une porte... Je sens rien. J'ai essayé sur de la brique. Rien. etc.",
                "Sometimes localized. Sometimes the whole body (starting April 2023). I don't feel a plucked hair, a bleeding nose, my foot on the ground, Knocking on a door... I don't feel anything. I tried it on brick. Nothing. etc.")
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
                "Fatigue", ""),
            start_date=Date(datetime(
                2023, 2, 9)),
            current_status=String(
                "Résolu à 80% après nerf décoincé. Un autre 80% après l'acupunture.",
                "80% resolved after nerve unpinched. Another 80% after acupuncture."),
            notes=String(
                "",
                "")
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
                2023, 2, 14)),
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
                
        Symptom(name=String(
                "'Pression' gorge, tempes, oreilles",
                "'Pressure' in throat, temples, ears"),
            start_date=Date(datetime(
                2023, 3, 1)),
            current_status=String(
                "Idem", ""),
            notes=String(
                "Le plus souvent après avoir mangé, au pire les tempes sont visiblement enflées.",
                "Most often after eating, at the worst the temples are visibly swollen.")
            ),
                
        Symptom(name=String(
                "'Toujours Soif' (parfois)",
                "'Always Thirsty' (sometimes)"),
            start_date=Date(datetime(
                2023, 3, 6)),
            current_status=String(
                "Idem", ""),
            notes=String(
                "",
                "")
            ),
                
        Symptom(name=String(
                "Envie d'aller aux toilettes fréquente",
                "Frequent urge to go to the toilet"),
            start_date=Date(datetime(
                2023, 3, 6)),
            current_status=String(
                "Idem", ""),
            notes=String(
                "",
                "")
            ),
                
        Symptom(name=String(
                "Mal de tête",
                "Headache"),
            start_date=Date(datetime(
                2023, 3, 6)),
            current_status=String(
                "Idem", ""),
            notes=String(
                "",
                "")
            ),

        Symptom(name=String(
                "Courbatures",
                "Body aches"),
            start_date=Date(datetime(
                2023, 3, 28)),
            current_status=String(
                "Idem", ""),
            notes=String(
                "",
                "")
            ),

        Symptom(name=String(
                "Perte de l'envie d'aller aux toilettes",
                "Loss of urge to go to the toilet"),
            start_date=Date(datetime(
                2023, 4, 17)),
            current_status=String(
                "Idem", ""),
            notes=String(
                "",
                "")
            ),

        Symptom(name=String(
                "Perte de sensation de chaud/froid",
                "Loss of sensation of hot/cold"),
            start_date=Date(datetime(
                2023, 4, 17)),
            current_status=String(
                "Idem", ""),
            notes=String(
                "Outre la sensation sur les mains: J'ai faillit me brûler (j'ai réalisé que c'était chaud, ce n'était pas un réflexe), une autre fois j'ai réalisé que je grelottait. Mais je n'avais pas froid.",
                "Besides the sensation on my hands: I almost burned myself (I realized it was hot, it wasn't a reflex), another time I realized I was shivering. But I wasn't cold.")
            ),

        Symptom(name=String(
                "Irritabilité",
                "Irritability"),
            start_date=Date(datetime(
                2023, 4, 19)),
            current_status=String(
                "Idem", ""),
            notes=String(
                "Je semble être plus irritable qu'avant ... Difficile à mesurer.",
                "I seem to be more irritable than before... Hard to measure.")
            ),

        Symptom(name=String(
                "Perte de sensation de soif/faim",
                "Loss of thirst/hunger sensation"),
            start_date=Date(datetime(
                2023, 4, 25)),
            current_status=String(
                "Idem", ""),
            notes=String(
                "J'ai réalisé la première fois après plusieurs jours où je ne sentais rien. Quand c'est revenu, j'avais très soif... J'ai oublié de boire.",
                "I first realized it after several days of not feeling anything. When it came back, I was very thirsty... I forgot to drink.")
            ),

        Symptom(name=String(
                "Douleur inhabituelle",
                "Unusual pain"),
            start_date=Date(datetime(
                2023, 4, 26)),
            current_status=String(
                "Idem", ""),
            notes=String(
                "Parfois j'ai des douleurs difficile à décrire... ça brule? non.. ça 'pince'? non... Parfois ça pique et je ne peux pas m'empêcher de gratter. Ça ne m'était jamais arrivé avant.",
                "Sometimes I have pain that's hard to describe... does it burn? No... does it 'pinch'? No... Sometimes it stings and I can't stop scratching. This has never happened to me before.")
            ),

        Symptom(name=String(
                "Insomnie",
                "Insomnia"),
            start_date=Date(datetime(
                2023, 5, 30)),
            current_status=String(
                "Idem", ""),
            notes=String(
                "Je semble avoir plus de difficulté à m'endormir quand j'ai le plus d'autres symptômes dans la journée.",
                "I seem to have more difficulty falling asleep when I have the most other symptoms during the day.")
            ),

        Symptom(name=String(
                "Mal au ventre",
                "Stomach ache"),
            start_date=Date(datetime(
                2023, 6, 3)),
            current_status=String(
                "Idem", ""),
            notes=String(
                "",
                "")
            ),

        Symptom(name=String(
                "Nausée",
                "Nausea"),
            start_date=Date(datetime(
                2023, 7, 2)),
            current_status=String(
                "Idem", ""),
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
        language="fr", 
        orientation='Portrait')#'Landscape')
    print("PDF generation end")
    run_cmd("cmd.exe /c start output\\rapport.pdf")
    #run_cmd("explorer.exe output")


if __name__ == "__main__":
    main()
