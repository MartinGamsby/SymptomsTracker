import os
import subprocess
from datetime import datetime

from report import generate_pdf
from data import Symptom, Event, String, Date, MonthDate, TestResults

def run_cmd(arg):
    args = arg.split()
    args = [os.path.expandvars(i) for i in args]
    subprocess.run(args)

    
def main():
    print("Initializing")
    
    summary_text = String("""Symptômes multi-systémiques sévères depuis décembre 2022. Nerf décoincé et régime 100% sans gluten ont résolu les symptômes quelques mois.
Mais les symptômes reviennent graduellement.
<br /><br />
Nouvelle découverte: les symptômes s'intensifient à chaque retour au domicile après une absence (Moisissure soupçonnée).""",

    """Severe multisystem symptoms since December 2022. A pinched nerve and a 100% gluten-free diet resolved the symptoms for a few months.
But the symptoms gradually returned.
<br /><br />
New discovery: symptoms intensify each time returning home after an absence (suspected mold).""")



    notable_events = [
        Event(String("<div style='text-align:center'>2022</div>",""), String("",""), String("","")),
        Event(MonthDate(datetime(
            2022, 12, 20)), String(
            "Orteil cassé.", 
            "Broken toe."), String(
            "Important parce que je ne suis pas maladroit d'habitude. Mais j'ai commencé à le devenir et avec du recul, c'était déjà commencé, avec une baisse de sensibilité aussi. Tout devient pire à chaque semaine à partir d'ici.",
            "Important because I'm not usually clumsy. But I started to become clumsy, and looking back, it had already started, with a decrease in sensitivity as well. Everything is getting worse every week starting here.")),

        Event(String("<div style='text-align:center'>2023</div>",""), String("",""), String("","")),
        
        Event(MonthDate(datetime(
            2023, 2, 12)), String(
            "Premier espoir: ça va un peu mieux après une 'retraite' de 2 jours avec spa.", 
            "First hope: I'm feeling a little better after a two-day spa 'retreat'."), String(
            "Première amélioration depuis le début, 2 mois auparavant.",
            "This is the first improvement since it started, two months ago.")),
        Event(MonthDate(datetime(
            2023, 2, 15)), String(
            "Tout devient pire à chaque semaine. Je prends rendez-vous avec un médecin.", 
            "Everything is getting worse every week. I make an appointment with a doctor."), String(
            "",
            "")),
        Event(MonthDate(datetime(
            2023, 2, 28)), String(
            "Rendez-vous avec le médecin: Tests sanguins, EMG.", 
            "Appointment with the doctor: Blood tests, EMG."), String(
            "",
            "")),
        #Event(MonthDate(datetime(
        #    2023, 3, 1)), String(
        #    "Le symptôme de 'pression' semble apparaître après la prise de sang. Et d'autres symptômes ont une 2e vague.",
        #    "The 'pressure' symptom seems to appear after the blood test. And other symptoms have a 2nd wave.")),
        Event(MonthDate(datetime(
            2023, 3, 7)), String(
            "Réveil avec la 'pression', palpitations, sueurs, membres lourds.",
            "Waking up with 'pressure', palpitations, sweat, heavy limbs."), String(
            "",
            "")),
        Event(MonthDate(datetime(
            2023, 3, 13)), String(
            "Rendez-vous avec un 2e médecin: C'était quoi, le diabète? (De l'hypoglycémie? Anémie?)", 
            "Appointment with a 2nd doctor: What was that? diabetes? (Hypoglycemia? Anemia?)"), String(
            "Il a dit 'C'est de l'anxiété'",
            "He said 'It's anxiety'")),
        Event(MonthDate(datetime(
            2023, 3, 27)), String(
            "EMG + visite neurologue: EMG ok, neurologue dit que ça peut être un nerf coincé.", 
            "EMG + neurologist visit: EMG ok, neurologist says it could be a pinched nerve."), String(
            "",
            "")),
        Event(MonthDate(datetime(
            2023, 4, 3)), String(
            "Je saigne du nez.",
            "My nose is bleeding."), String(
            "Rien d'inquiétant, mais je réalise plus tard que c'est parce que je ne sentait pas mon nez et j'ai trop gratté (sans rien sentir). Ça fait combien de temps?",
            "Nothing concerning, but I later realize it's because I couldn't feel my nose and I scratched too much (without feeling anything). How long has it been?")),
        Event(MonthDate(datetime(
            2023, 4, 18)), String(
            "2e rendez-vous avec le 1er médecin (suivi)", 
            "2nd appointment with the 1st doctor (follow-up)"), String(
            "Je parles de la perte de sensation. Elle me prescrit des vitamines B12 (sang: dans les normes, mais bas), et demande un IRM (pour éliminer la sclérose en plaques)",
            "I talk about the loss of sensation. She prescribes me vitamin B12 (blood: within the norm, but low), and orders an MRI (to rule out multiple sclerosis)")),
        Event(MonthDate(datetime(
            2023, 4, 20)), String(
            "Rendez-vous avec un ostéopathe pour le nerf coincé (Aucune différence notable après)", 
            "Appointment with an osteopath for the pinched nerve (No noticeable difference after)"), String(
            "",
            "")),
        Event(MonthDate(datetime(
            2023, 4, 25)), String(
            "IRM 1", ""), String(
            "",
            "")),
        Event(MonthDate(datetime(
            2023, 5, 12)), String(
            "IRM 2 (+Gadolinium)", ""), String(
            "",
            "")),
        Event(MonthDate(datetime(
            2023, 6, 1)), String(
            "Résultat d'IRM: Rien",
            "MRI result: Nothing"), String(
            "seulement télangiectasie? 6mm?",
            "just a telangiectasia? 6mm?")),
        Event(MonthDate(datetime(
            2023, 6, 9)), String(
            "Nutritionniste",
            "Nutritionist"), String(
            "Diète d'élimination avec diminution notable des symptômes (~50%)",
            "Elimination diet with significant reduction in symptoms (~50%).")),
            
            
            
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
            "Traitement ostéopathique pour un nerf coincé (recommandation d'un neurologue)",
            "Osteopathic treatment for a pinched nerve (recommended by a neurologist)"), String(
            "Résout quelques symptômes et réduit d'environ 50% le reste.",
            "Resolves some symptoms and reduces the rest by about 50%.")),
        Event(MonthDate(datetime(
            2023, 9, 12)), String(
            "Rendez-vous avec l'ostéopathe.",
            "Appointment with the osteopath."), String(
            "Peut-être qu'il peut régler ce qui reste...",
            "Maybe he can fix what's left...")),
        Event(MonthDate(datetime(
            2023, 11, 8)), String(
            "Rendez-vous avec l'ostéopathe...",
            "Appointment with the osteopath..."), String(
            "",
            "")),
        Event(MonthDate(datetime(
            2023, 11, 23)), String(
            "Rendez-vous avec l'ostéopathe...",
            "Appointment with the osteopath..."), String(
            "",
            "")),
            
        Event(String("<div style='text-align:center'>2024</div>",""), String("",""), String("","")),
        
        Event(MonthDate(datetime(
            2024, 12, 18)), String(
            "Rendez-vous avec un 2e acupuncteur.",
            "Appointment with a second acupuncturist."), String(
            "Ça règle un autre 80% de ma perte de sensibilité.",
            "That fixes another 80% of my loss of sensitivity.")),
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
            "Finalement trouvé grâce au régime d'élimination : le gluten",
            "Finally found from elimination diet: gluten."), String(
            "C'était difficile à trouver, parce qu'il y avait des traces dans la mayonnaise, l'avoine, etc.",
            "It was hard because I had traces in the mayonnaise, the oats, etc.")),
        #Event(MonthDate(datetime(
        #    2024, 2, 26)), String(
        #    "Suivi acupuncteur",
        #    "Acupuncturist follow-up")),
        Event(MonthDate(datetime(
            2024, 4, 4)), String(
            "Rendez-vous avec un 3e médecin: Coeliaque?", 
            "Appointment with a 3rd doctor: Celiac?"), String(
            "Ils veulent que je fasse un gluten challenge pour tester (ça fait des mois que j'ai arrêté le gluten)",
            "They want me to do a gluten challenge to test (it's been months since I stopped eating gluten)")),
        Event(MonthDate(datetime(
            2024, 6, 4)), String(
            "DÉFI GLUTEN: Tous les symptômes reviennent.",
            "GLUTEN CHALLENGE: All symptoms come back."), String(
            "Je me sens très mal, et le médecin ne me recontacte pas, la secrétaire m'appelle pour dire que c'est négatif ... après 2 semaines, et plusieurs mois sans en prendre avant, pas demandé mes symptômes ni rien... Sensibilité au gluten confirmée, je continue d'éviter le gluten.",
            "I feel very bad, and the doctor doesn't contact me again, the secretary calls me to say that it's negative... after 2 weeks, and several months without taking it before, not asking about my symptoms or anything... Gluten sensitivity confirmed, I continue avoiding gluten.")),
        Event(MonthDate(datetime(
            2024, 9, 2)), String(
            "Première grosse réaction depuis longtemps",
            "First major reaction in a long time"), String(
            "J'ai reçu une goutte de bouillon (gluten) dans le visage/yeux. Pas besoin d'en manger...",
            "I got a drop of broth (gluten) in my face/eyes. No need to eat it...")),
        #Event(MonthDate(datetime(
        #    2024, 9, 24)), String(
        #    "Rendez-vous avec l'ostéopathe pour prévention.",
        #    "Appointment with the osteopath for prevention.")),

        Event(String("<div style='text-align:center'>2025</div>",""), String("",""), String("","")),
        
        Event(MonthDate(datetime(
            2025, 5, 31)), String(
            "J'étais pratiquement sans symptômes pendant plus qu'un an, mais ça revient...",
            "I was virtually symptom-free for over a year, but it's back..."), String(
            "'Pression' et respiration difficile après avoir mangé une pizza sans gluten. (Et ça continue pour d'autres aliments, de plus en plus)",
            "'Pressure' and difficulty breathing after eating gluten-free pizza. (And it continues for other foods, more and more)")),
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
            "Ça revient les symptômes ...",
            "The symptoms are back..."), String(
            "(Je reviens de 3 nuits en camping)",
            "(I'm back from 3 nights camping)")),
        Event(MonthDate(datetime(
            2025, 7, 19)), String(
            "Après 3 nuits à la maison, je retourne 4 autres nuits à l'extérieur.",
            "After 3 nights at home, I'm 4 more nights away."), String(
            "Ok ce n'est pas une coïncidence, je réagis à ma maison aussi (en arrivant), pas juste la bouffe. Et c'est pire que le dernier retour.",
            "Okay, it's not a coincidence, I'm reacting to my home too (when I arrived), not just the food. And it's worse than the last time I came back.")),
            
        ]
       
    may_2025 = datetime(2025, 5, 15)
    months_since_may_2025 = (datetime.now().year - may_2025.year) * 12 + (datetime.now().month - may_2025.month)
    key_events = [
        Event(String(
            "(6 mois) Décembre 2022 - Juin 2023",
            "(6 months)December 2022 - June 2023"), String(
            "Début de symptômes neurologiques sévères, coïncidant avec un dégât d'eau", 
            "Onset of severe neurological symptoms, coinciding with water damage"), String(
            "Escalade des symptômes jusqu'à leur pic de sévérité. Multiples consultations médicales et tests (Sang, EMG, IRM) sans résultats concluants.",
            "Escalation of symptoms until their peak severity. Multiple medical consultations and tests (Blood tests, EMG, MRI) without conclusive results.")),
        Event(String(
            "(8 mois) Juin 2023 - Février 2024",
            "(8 months) June 2023 - February 2024"), String(
            "Suivi Nutritionniste. Diète d'élimination avec diminution notable des symptômes (~50%)",
            "Nutritionist. Elimination diet with significant reduction in symptoms (~50%)"), String(
            "L'alimentation joue un grand rôle. Probablement inflammatoire.",
            "Diet plays a big role. Probably inflammatory.")),
        Event(String(
            "&emsp;[Juillet 2023]",
            "&emsp;[July 2023]"), String(
            "Traitement ostéopathique pour un nerf coincé (recommandation d'un neurologue)",
            "Osteopathic treatment for a pinched nerve (recommended by a neurologist)"), String(
            "Résout quelques symptômes et réduit d'environ 50% le reste.",
            "Resolves some symptoms and reduces the rest by about 50%.")),
        Event(String(
            "(15 mois) Février 2024 - Mai 2025",
            "(15 months) February 2024 -  May 2025"), String(
            "J'ai une révélation : le gluten.",
            "I had an epiphany : gluten. "), String(
            "C'était difficile à trouver, parce qu'il y avait des traces dans la mayonnaise, l'avoine, etc. Ça règle pratiquement tout (avec le nerf coincé), jusqu'à ~mai 2025",
            "It was hard to find, because there were traces in mayonnaise, oats, etc. It fixes almost everything (with the pinched nerve), until ~May 2025")),
        Event(String(
            "&emsp;[Juin 2024]",
            "&emsp;[June 2024]"), String(
            "Sous le conseil d'un médecin: DÉFI GLUTEN: Tous les symptômes reviennent.",
            "Under the advice of a doctor: GLUTEN CHALLENGE: All symptoms come back."), String(
            "Je me sens très mal, la secrétaire m'appelle pour dire que c'est négatif, sans suivi.",
            "I feel very bad, the secretary calls me to say that it's negative, without any follow-up.")),
        Event(String(
            "&emsp;[Septembre 2024]",
            "&emsp;[September 2024]"), String(
            "Première grosse réaction depuis longtemps",
            "First major reaction in a long time"), String(
            "J'ai reçu une goutte de bouillon (gluten) dans le visage/yeux. Pas besoin d'en manger... Ce n'est définitivement pas la maladie coeliaque.",
            "I got a drop of broth (gluten) in my face/eyes. No need to eat it... It's definitely not celiac disease.")),
        Event(String(
            f"({months_since_may_2025} mois) Mai 2025 - Aujourd'hui",
            f"({months_since_may_2025} months) May 2025 - Now"), String(
            "J'étais pratiquement sans symptômes pendant plus qu'un an, mais ça revient, graduellement... Malgré un régime 100% sans gluten",
            "I was virtually symptom-free for over a year, but it's back, gradually... Despite a 100% gluten-free diet"), String(
            "Après 2 séjours en dehors de la maison, le retour augmente les symptômes, ce n'est pas une coincidence. C'est la maison? De la moisissure?",
            "After two trips away from home, returning home increases symptoms; this is no coincidence. Is it the house? Mold?")),
        Event(String(
            "&emsp;[Août 2024]",
            "&emsp;[August 2024]"), String(
            "Amélioration notable des symptômes matinaux depuis l'installation du purificateur d'air HEPA iAdaptAir 2.0",
            "Notable improvement in morning symptoms since installing iAdaptAir 2.0 HEPA air purifier"), String(
            "Moins de raideur/faiblesse/fatigue matinale.",
            "Less morning stiffness/weakness/fatigue.")),
            
        ]
        
    ermi_test_1 = "Aspergillus sydowii, Aspergillus versicolor, Cladosporium sphaerospermum, Penicillium brevicompactum, Penicillium crustosum, Cladosporium cladosporioides2, Mucor amphibiorum, Penicillium chrysogenum, Rhizopus stolonifer"
    ermi_test_1_other_q3s = "Wallemia sebi, Alternaria alternata, Epicoccum nigrum"
    ermi_test_1_q2s = "Aspergillus niger, Aspergillus ochraceus, Aspergillus penicillioides, Aspergillus restrictus, Chaetomium globosum, Paecilomyces variotii, Penicillium corylophilum, Stachybotrys chartarum, Cladosporium herbarum"
    ermi_test_1_q1s = "Aspergillus flavus/oryzae, Aspergillus fumigatus, Aureobasidium pullulans, Eurotium (Asp.) amstelodami, Penicillium purpurogenum, Penicillium variabile, Scopulariopsis chartarum, Trichoderma viride, Acremonium strictum, Cladosporium cladosporioides1"
    ermi_test_1_none = "Aspergillus sclerotiorum, Aspergillus unguis, Penicillium Spinulosum, Scopulariopsis brevicaulis/fusca, Aspergillus ustus"
    
    tests =  [
        TestResults(MonthDate(datetime(
            2022, 7, 28)), String(
            "Covid-19", 
            "Covid-19"), String(
            "positif (j'ai eu des symptômes intenses, mais seulement quelques jours)",
            "positive (had intense symptoms, but only a few days)")),
            
        TestResults(MonthDate(datetime(
            2023, 2, 28)), String(
            "Tests sanguins", 
            "Blood tests"), String(
            "(crea) Créatinine, (k) Potassium, (na) Sodium, (alb) Albumine, (ca) Calcium, (ferri) Ferritine, (thyr) Bilan thyroïdien, (hba1c) hémoglobine glyquée, (fsc) Formule sanguine, CRP, Vitamine B12, Magnésium:<br /><strong>ok, Vitamines B12 dans la normale, mais bas.</strong>",
            "Creatinine, Potassium, Sodium, Albumin, Calcium, Ferritin, Thyroid panel, Glycated hemoglobin, Complete blood count, CRP, Vitamin B12, Magnesium:<br /><strong>ok, Vitamin B12 is within normal, but low.</strong>")),

        TestResults(MonthDate(datetime(
            2023, 3, 27)), String(
            "EMG", 
            "EMG"), String(
            "ok, neurologue dit que ça peut être un nerf coincé.",
            "ok, neurologist says it could be a pinched nerve.")),
 
        TestResults(MonthDate(datetime(
            2023, 6, 1)), String(
            "IRM (avec contraste)",
            "MRI (with gadolinium contrast)"), String(
            "ok, seulement télangiectasie? 6mm?",
            "ok, just a telangiectasia? 6mm?")),

        TestResults(MonthDate(datetime(
            2024, 6, 4)), String(
            "Tests sanguins",
            "Blood tests"), String(
            "Glucose aléatoire non à jeun, TSH, Ferritine, B12, Créatinine, Électronytes (Na, K, Cl), CRP / Protéine C réactive, F.S.C., Ac anti-transglutaminases, IgA totaux, malabsorption, HbA1C: ok",
            "Random (non-fasting) glucose, TSH, Ferritin, B12, Creatinine, Electrolytes (Na, K, Cl), CRP / C-reactive protein, CBC (Complete Blood Count), Anti-transglutaminase antibodies, Total IgA, Malabsorption, HbA1C: ok")),
            
        TestResults(MonthDate(datetime(
            2024, 6, 18)), String(
            "Test d'urine: Ratio albumine/créatinine urinaire.",
            "Urine test: albumin/creatinine ratio."), String(
            "ok",
            "ok")),
            
        TestResults(MonthDate(datetime(
            2024, 7, 25)), String(
            "Test VCS (Visual Contrast Sensitivity Test): vcstest.com",
            "VCS test (Visual Contrast Sensitivity Test): vcstest.com"), String(
            "positif (échec)",
            "positive (failed)")),
            
        TestResults(MonthDate(datetime(
            2024, 7, 28)), String(
            "Test VCS: survivingmold.com",
            "VCS test: survivingmold.com"), String(
            "positif (échec)",
            "positive (failed)")),
            
        TestResults(MonthDate(datetime(
            2025, 7, 23)), String(
            "ERMI: 10.4",
            "ERMI test: 10.4"), String(
            f"G1: 29.1, G2: 18.7. Étoilé : {ermi_test_1} (Plus de dix fois la moyenne de la moisissure)",
            f"G1: 29.1, G2: 18.7. Starred: {ermi_test_1} (Higher than ten fold of the mean)")),
        TestResults(MonthDate(datetime(
            2025, 7, 23)), String(
            "HERTSMI-2: 18",
            "HERTSMI-2 test: 18"), String(
            "\"Il est déconseillé de réoccuper les lieux tant que des travaux de remédiation et une réévaluation ne seront pas concluants.\"",
            "\"Re-occupancy is ill-advised until further remediation and re-assessment are conclusive.\"")),
        TestResults(MonthDate(datetime(
            2025, 7, 31)), String(
            "GENIE (pour SRIC/CIRS)",
            "GENIE (for CIRS)"), String(
            "Clinique en Alberta le recommande. En attente de confirmation.",
            "Clinic in Alberta recommends it. Pending confirmation.")),
            
            
        ]

        

    symptoms = [
        Symptom(name=String("Respiration difficile / Essouflement rapide",
                "Difficulty breathing / Rapid shortness of breath"),
            start_date=Date(datetime(
                2023, 2, 15)),
            nerve=False,wave1=True,wave2=True,wave3=False,
            current_status=String(
                "Était résolu sans gluten, mais revient tranquillement.",
                "Was resolved gluten-free, but is slowly coming back."),
            notes=String(
                "",
                "")
            ),
        Symptom(name=String("Enflement/'Pression' gorge, tempes, oreilles",
                "'Pressure' in throat, temples, ears"),
            start_date=Date(datetime(
                2023, 3, 1)),
            nerve=False,wave1=True,wave2=False,wave3=False,
            current_status=String(
                "Idem", ""),
            notes=String(
                "Le plus souvent après avoir mangé, au pire les tempes sont visiblement enflées.",
                "Most often after eating, at the worst the temples are visibly swollen.")
            ),
        Symptom(name=String("Palpitations",
                "Heart Palpitations"),
            start_date=Date(datetime(
                2022, 12, 25)),
            nerve=False,wave1=True,wave2=True,wave3=False,
            current_status=String(
                "Était résolu sans gluten, mais revient tranquillement.",
                "Was resolved gluten-free, but is slowly coming back."),
            notes=String(
                "Plus souvent le soir, quelques fois réveillé avec palpitations, sueurs, engourdissements.",
                "More often in the evening, sometimes waking up with palpitations, sweating, numbness.")
            ),                
        
        Symptom(name=String("Engourdissement (corps entier)",
                "Numbness (whole body)"),
            start_date=Date(datetime(
                2022, 12, 21)),
            nerve=False,wave1=False,wave2=True,wave3=False,
            current_status=String(
                "Résolu à 80% après avoir remédié un nerf coincé.",
                "80% resolved after fixing a pinched nerve."),
            notes=String(
                "Parfois locallisé. Quelques périodes le corps au complet (à partir d'avril 2023). Je ne sens pas un poil épilé, un nez qui saigne, mon pied par terre. Cogner sur une porte... Je sens rien. J'ai essayé sur de la brique. Rien. etc.",
                "Sometimes localized. Sometimes the whole body (starting April 2023). I don't feel a plucked hair, a bleeding nose, my foot on the ground. Knocking on a door... I don't feel anything. I tried it on brick. Nothing. etc.")
            ),
        Symptom(name=String("Perte de sensation de soif/faim",
                "Loss of thirst/hunger sensation"),
            start_date=Date(datetime(
                2023, 4, 25)),
            nerve=False,wave1=False,wave2=True,wave3=True,
            current_status=String(
                "Idem", ""),
            notes=String(
                "J'ai réalisé la première fois après plusieurs jours où je ne sentais rien. Quand c'est revenu, j'avais très soif... J'ai oublié de boire.",
                "I first realized it after several days of not feeling anything. When it came back, I was very thirsty... I forgot to drink.")
            ),
        Symptom(name=String("Étourdissements / Manque d'équilibre",
                "Dizziness / Loss of balance"),
            start_date=Date(datetime(
                2023, 2, 13)),
            nerve=False,wave1=True,wave2=True,wave3=False,
            current_status=String(
                "Était résolu sans gluten, mais revient tranquillement.",
                "Was resolved gluten-free, but is slowly coming back."),
            notes=String(
                "",
                "")
            ),
        Symptom(name=String("Faiblesse générale / jusqu'à difficulté à marcher",
                "General weakness / up to difficulty walking"),
            start_date=Date(datetime(
                2023, 2, 4)),
            nerve=False,wave1=True,wave2=True,wave3=False,
            current_status=String(
                "Résolu à 50% après nerf décoincé",
                "50% resolved after nerve unpinched"),
            notes=String(
                "Avant le nerf décoincé, parfois impossible de marcher sans devoir s'appuyer sur quelque chose. Lance pas assez fort, etc.",
                "Before nerve unpinched, sometimes impossible to walk without having to lean on something. Doesn't throw strong enough, etc.")
            ),
        Symptom(name=String("Maladroit",
                "Clumsy"),
            start_date=Date(datetime(
                2022, 12, 26)),
            nerve=True,wave1=False,wave2=True,wave3=False,
            current_status=String(
                "Résolu à 80% après nerf décoincé",
                "80% resolved after nerve unpinched"),
            notes=String(
                "Problèmes de dextérité, échappe les choses. Tourner les pages, clavier et piano difficiles. S'accroche partout. Mots mal articulés.",
                "Dexterity issues, dropping things. Turning pages, keyboard and piano difficulties. Gets caught on everything. Slurred words.")
            ),

        Symptom(name=String("Nausée",
                "Nausea"),
            start_date=Date(datetime(
                2023, 7, 2)),
            nerve=False,wave1=False,wave2=True,wave3=True,
            current_status=String(
                "Idem", ""),
            notes=String(
                "",
                "")
            ),
        Symptom(name=String("Fatigue", ""),
            start_date=Date(datetime(
                2023, 2, 9)),
            nerve=True,wave1=False,wave2=True,wave3=False,
            current_status=String(
                "Résolu à 80% après nerf décoincé. Un autre 80% après l'acupunture.",
                "80% resolved after nerve unpinched. Another 80% after acupuncture."),
            notes=String(
                "",
                "")
            ),

        Symptom(name=String("Mal de tête",
                "Headache"),
            start_date=Date(datetime(
                2023, 3, 6)),
            nerve=False,wave1=False,wave2=False,wave3=True,
            current_status=String(
                "Idem", ""),
            notes=String(
                "",
                "")
            ),
        Symptom(name=String("Courbatures",
                "Body aches"),
            start_date=Date(datetime(
                2023, 3, 28)),
            nerve=False,wave1=False,wave2=True,wave3=True,
            current_status=String(
                "Idem", ""),
            notes=String(
                "",
                "")
            ),

        Symptom(name=String("Irritabilité",
                "Irritability"),
            start_date=Date(datetime(
                2023, 4, 19)),
            nerve=False,wave1=False,wave2=True,wave3=True,
            current_status=String(
                "Idem", ""),
            notes=String(
                "Je semble être plus irritable qu'avant ... Difficile à mesurer.",
                "I seem to be more irritable than before... Hard to measure.")
            ),

        Symptom(name=String("Douleur inhabituelle",
                "Unusual pain"),
            start_date=Date(datetime(
                2023, 4, 26)),
            nerve=False,wave1=False,wave2=True,wave3=True,
            current_status=String(
                "Idem", ""),
            notes=String(
                "Parfois j'ai des douleurs difficile à décrire... ça brule? non.. ça 'pince'? non... Parfois ça pique et je ne peux pas m'empêcher de gratter. Ça ne m'était jamais arrivé avant.",
                "Sometimes I have pain that's hard to describe... does it burn? No... does it 'pinch'? No... Sometimes it stings and I can't stop scratching. This has never happened to me before.")
            ),
        Symptom(name=String("Difficulté à se concentrer / apprendre",
                "Difficulty concentrating / learning"),
            start_date=Date(datetime(
                2023, 5, 8)),
            nerve=False,wave1=False,wave2=True,wave3=True,
            current_status=String(
                "Idem", ""),
            notes=String(
                "Je l'ai remarqué tard, mais avec du recul, c'est arrivé souvent. Ça n'arrivait pas avant.",
                "I noticed it late, but looking back, it happened often. It didn't happen before.")
            ),
        Symptom(name=String("Insomnie",
                "Insomnia"),
            start_date=Date(datetime(
                2023, 5, 30)),
            nerve=False,wave1=False,wave2=True,wave3=True,
            current_status=String(
                "Idem", ""),
            notes=String(
                "Je semble avoir plus de difficulté à m'endormir quand j'ai le plus d'autres symptômes dans la journée.",
                "I seem to have more difficulty falling asleep when I have the most other symptoms during the day.")
            ),
        Symptom(name=String("Mal au ventre",
                "Stomach ache"),
            start_date=Date(datetime(
                2023, 6, 3)),
            nerve=False,wave1=True,wave2=True,wave3=False,
            current_status=String(
                "Idem", ""),
            notes=String(
                "",
                "")
            ),

        Symptom(name=String("Nez bloqué",
                "Blocked nose"),
            start_date=Date(datetime(
                2024, 6, 4)),
            nerve=False,wave1=False,wave2=True,wave3=False,
            current_status=String(
                "Idem", ""),
            notes=String(
                "Je l'ai remarqué tard, mais avec du recul, c'est arrivé souvent, surtout la nuit et le matin, sans avoir de rhume. Ça n'arrivait pas avant.",
                "I noticed it late, but looking back, it happened often, especially at night and in the morning, without having a cold. It didn't happen before.")
            ),
        Symptom(name=String("Oreilles bouchées",
                "Ears feel plugged"),
            start_date=Date(datetime(
                2024, 6, 4)),
            nerve=False,wave1=False,wave2=True,wave3=False,
            current_status=String(
                "Idem", ""),
            notes=String(
                "Idem", "")
            ),
        Symptom(name=String("Acouphène",
                "Tinnitus"),
            start_date=Date(datetime(
                2024, 6, 4)),
            nerve=False,wave1=False,wave2=True,wave3=False,
            current_status=String(
                "Idem", ""),
            notes=String(
                "Idem", "")
            ),
        Symptom(name=String("Raideur/douleur matinale",
                "Morning stiffness/body pain"),
            start_date=Date(datetime(
                2024, 6, 4)),
            nerve=False,wave1=False,wave2=True,wave3=False,
            current_status=String(
                "Idem", ""),
            notes=String(
                "Idem", "")
            ),
        Symptom(name=String("Faiblesse musculaire",
                "Muscle weakness"),
            start_date=Date(datetime(
                2023, 1, 13)),
            nerve=True,wave1=False,wave2=False,wave3=False,
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
        
        Symptom(name=String("Perte de sensation de chaud/froid",
                "Loss of sensation of hot/cold"),
            start_date=Date(datetime(
                2023, 4, 17)),
            nerve=False,wave1=False,wave2=True,wave3=False,
            current_status=String(
                "Idem", ""),
            notes=String(
                "Outre la sensation sur les mains: J'ai faillit me brûler (j'ai réalisé que c'était chaud, ce n'était pas un réflexe), une autre fois j'ai réalisé que je grelottait. Mais je n'avais pas froid.",
                "Besides the sensation on my hands: I almost burned myself (I realized it was hot, it wasn't a reflex), another time I realized I was shivering. But I wasn't cold.")
            ),
        Symptom(name=String("Tremblements",
                "Tremors"),
            start_date=Date(datetime(
                2023, 2, 14)),
            nerve=True,wave1=False,wave2=False,wave3=False,
            #triggers=String(
            #    "Finalement trouvé que c'était dû à un nerf coincé",
            #    "Found to be caused by a pinched nerve"),
            current_status=String(
                "Résolu à 100% après nerf décoincé",
                "100% resolved after nerve unpinched"),
            notes=String(
                "Résolu à 100% après nerf décoincé",
                "100% resolved after nerve unpinched")
            ),
        Symptom(name=String("'Toujours Soif' (parfois)",
                "'Always Thirsty' (sometimes)"),
            start_date=Date(datetime(
                2023, 3, 6)),
            nerve=False,wave1=False,wave2=True,wave3=True,
            current_status=String(
                "Idem", ""),
            notes=String(
                "C'est arrivé seulement une ou 2 fois.",
                "It only happened once or twice.")
            ),
                Symptom(name=String("Perte de l'envie d'aller aux toilettes",
                "Loss of urge to go to the toilet"),
            start_date=Date(datetime(
                2023, 4, 17)),
            nerve=False,wave1=False,wave2=True,wave3=False,
            current_status=String(
                "Idem", ""),
            notes=String(
                "",
                "")
            ),
        Symptom(name=String("Envie d'aller aux toilettes fréquente",
                "Frequent urge to go to the toilet"),
            start_date=Date(datetime(
                2023, 3, 6)),
            nerve=False,wave1=False,wave2=True,wave3=True,
            current_status=String(
                "Idem", ""),
            notes=String(
                "Idem.",
                "Idem.")
            ),
        ]
    symptoms_chrono = sorted(symptoms, key=lambda symptom: symptom.start_date.date)
        
    symptoms_summary_text = String(
            """Les symptômes ne se déclenchent pas tous au même moment. J'ai noté trois vagues après exposition: <ol><li>
<strong>Minutes:</strong> pression, difficultés respiratoires, etc.
</li><li>
<strong>Jours:</strong> engourdissements, vertiges, fatigue, etc.
</li><li>
<strong>Post-inflammatoire:</strong> maux de tête, nausées, etc.
</li></ol>""",
            """The symptoms are not all triggered at the same time, I noticed 3 waves after exposure:<ol><li>
<strong>Minutes:</strong> pressure, breathing issues, etc.
</li><li>
<strong>Days:</strong> numbness, vertigo, fatigue, etc.
</li><li>
<strong>Post-inflammatory:</strong> headache, nausea, etc.
</li></ol>"""
        )
    
    print("FR PDF generation start")
    generate_pdf(patient_name="Martin Gamsby",
        summary_text=summary_text,
        symptoms_summary_text=symptoms_summary_text,
        symptoms=symptoms,
        symptoms_chrono=symptoms_chrono,
        key_events=key_events,
        notable_events=notable_events,
        tests=tests,
        output_pdf='output/rapport.pdf',
        language="fr", 
        orientation='Portrait')#'Landscape')
        
    print("EN PDF generation start")
    generate_pdf(patient_name="Martin Gamsby",
        summary_text=summary_text,
        symptoms_summary_text=symptoms_summary_text,
        symptoms=symptoms,
        symptoms_chrono=symptoms_chrono,
        key_events=key_events,
        notable_events=notable_events,
        tests=tests,
        output_pdf='output/report.pdf',
        language="en", 
        orientation='Portrait')#'Landscape')
        
    print("PDF generation end")
    run_cmd("cmd.exe /c start output\\rapport.pdf")
    run_cmd("cmd.exe /c start output\\report.pdf")
    #run_cmd("explorer.exe output")


if __name__ == "__main__":
    main()
