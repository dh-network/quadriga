---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 🏆Selbsttest: Wissen und Praxis

## Assessment 1.1: Forschungsfrage und Operationalisierung

### Teil 1: Fragestellung und Operationalisierung

**Anweisungen**
1. Lesen Sie jede Option sorgfältig
2. Wählen Sie alle zutreffenden Aussagen aus
3. Beachten Sie das Feedback zu jeder Option, um Ihr Verständnis zu vertiefen
4. Reflektieren Sie, warum bestimmte Aussagen korrekt oder inkorrekt sind

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

""" 
Lernziel: 
    Sie können an einem konkreten Beispiel (Spanische Grippe) nachvollziehen, wie eine qualitative Forschungsfrage für quantitative Analyse operationalisiert wird.
Bloom-Stufe: Verstehen
Format: Multiple Choice + Selbsteinschätzung
Geschätzte Zeit: 30 Minuten
Schwerpunkte:
    - Verständnis der Operationalisierung
    - Anwendung auf konkrete Forschungsfrage
    - Reflexion methodischer Entscheidungen
"""

question1 = [
    {
        "question": "Welche der folgenden Aussagen über Korpora in den Digital Humanities sind korrekt?",
        "type": "multiple_choice",
        "answers": [
                {
                    "answer": "Korpora sind Sammlungen von maschinenlesbaren Textdokumenten",
                    "correct": True,
                    "feedback": """✓ Korrekt! Diese Definition ist grundlegend richtig, weil:
                    - Maschinenlesbarkeit ist ein zentrales Merkmal für DH-Korpora
                    - Dies ermöglicht die computergestützte Analyse
                    - Es unterscheidet DH-Korpora von traditionellen Textsammlungen"""
                },
                {
                    "answer": "Jedes Korpus muss alle verfügbaren Texte zu einem Thema enthalten",
                    "correct": False,
                    "feedback": """× Nicht korrekt, weil:
                    - Es gibt verschiedene Strategien des Korpusaufbaus
                    - Vollständige Korpora sind nur eine mögliche Option
                    - Vollständigkeit ist nur bei klar begrenzten, kleinen Bereichen sinnvoll
                    - Repräsentative Stichproben können ebenso valide sein"""
                },
                {
                    "answer": "Die Zusammenstellung eines Korpus erfolgt nach bestimmten Kriterien",
                    "correct": True,
                    "feedback": """✓ Korrekt! Dies ist ein wesentliches Merkmal, weil:
                    - Kriterien sichern die wissenschaftliche Qualität
                    - Sie machen die Auswahl nachvollziehbar
                    - Sie orientieren sich an der Forschungsfrage
                    - Sie ermöglichen systematische Analysen"""
                },
                {
                    "answer": "Ein Referenzkorpus muss immer digital vorliegen",
                    "correct": False,
                    "feedback": """× Nicht korrekt, weil:
                    - Referenzkorpora sind durch ihre Repräsentativität definiert
                    - Das Format (digital/analog) ist nicht entscheidend
                    - Die Repräsentativität für eine bestimmte Domäne ist das Hauptmerkmal
                    - Digitalisierung kann später erfolgen"""
                },
                {
                    "answer": "Die Größe eines Korpus bestimmt seine wissenschaftliche Qualität",
                    "correct": False,
                    "feedback": """× Nicht korrekt, weil:
                    - Die Qualität hängt von der Auswahlstrategie ab
                    - Auch kleine Korpora können wissenschaftlich wertvoll sein
                    - Entscheidend ist die Passung zur Forschungsfrage
                    - Die systematische Zusammenstellung ist wichtiger als die Größe"""
                },
                {
                    "answer": "Ein Korpus kann nach verschiedenen Strategien aufgebaut werden",
                    "correct": True,
                    "feedback": """✓ Korrekt! Dies ist wichtig, weil:
                    - Verschiedene Forschungsfragen erfordern verschiedene Ansätze
                    - Es gibt vollständige und repräsentative Korpora
                    - Die Wahl der Strategie hängt von praktischen Faktoren ab
                    - Unterschiedliche Strategien haben spezifische Vor- und Nachteile"""
                }
        ]
    }
]
display_quiz(question1, colors=colors.jupyterquiz, max_width=1000)
```

### Teil 2: Operationalisierung in der Praxis

#### Kontext
Eine Forschungsfrage im Bereich der Digital Humanities lautet: "Wie entwickelte sich die öffentliche Aufmerksamkeit für Umweltthemen in deutschen Tageszeitungen zwischen 1960-1980?"

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

question2 = [
    {
        "question": "Welche der folgenden Operationalisierungen eignen sich, um die öffentliche Aufmerksamkeit für Umweltthemen in deutschen Tageszeitungen zwischen 1960-1980 messbar zu machen? (Mehrere Antworten sind korrekt)",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Zählen der Häufigkeit von umweltbezogenen Begriffen (wie 'Umweltschutz', 'Verschmutzung') in den Zeitungstexten",
                "correct": True,
                "feedback": """✓ Korrekt! Diese Operationalisierung ist geeignet, weil:
                    - Sie ein quantifizierbares Maß für die Intensität der Berichterstattung liefert
                    - Die Häufigkeit von Schlüsselbegriffen messbar ist
                    - Systematische Vergleiche über Zeit möglich sind
                    - Die Analyse auf dem definierten Korpus basiert"""
            },
            {
                "answer": "Messen der Länge von Artikeln, die Umweltthemen behandeln",
                "correct": True,
                "feedback": """✓ Korrekt! Diese Methode ist geeignet, weil:
                    - Sie den Umfang der Berichterstattung quantifiziert
                    - Längere Artikel oft mehr Aufmerksamkeit bedeuten
                    - Die Messung über Zeit vergleichbar ist
                    - Die Analyse innerhalb des Quellenkorpus bleibt"""
            },
            {
                "answer": "Erfassen der tatsächlichen Umweltverschmutzungswerte aus diesem Zeitraum",
                "correct": False,
                "feedback": """× Nicht korrekt, weil:
                    - Dies keine mediale Aufmerksamkeit misst
                    - Es außerhalb des Untersuchungskorpus liegt
                    - Es das tatsächliche Geschehen statt der Berichterstattung erfasst
                    - Es nicht die Forschungsfrage beantwortet"""
            },
            {
                "answer": "Analyse von Regierungsdokumenten zur Umweltpolitik",
                "correct": False,
                "feedback": """× Nicht korrekt, weil:
                    - Dies außerhalb des definierten Quellenkorpus (Tageszeitungen) liegt
                    - Es eine andere Textgattung betrifft
                    - Es nicht die mediale Aufmerksamkeit misst
                    - Es eine andere Forschungsfrage erfordern würde"""
            },
            {
                "answer": "Erfassen des prozentualen Anteils der Zeitungsseiten mit Umweltthemen",
                "correct": True,
                "feedback": """✓ Korrekt! Diese Operationalisierung ist geeignet, weil:
                    - Sie den relativen Stellenwert des Themas misst
                    - Sie verschiedene Zeitpunkte vergleichbar macht
                    - Sie auf dem definierten Korpus basiert
                    - Sie ein quantifizierbares Maß liefert"""
            }
        ]
    }
]
display_quiz(question2, colors=colors.jupyterquiz, max_width=1000)
```

### Teil 3: Selbsteinschätzungsaufgabe

#### Aufgabe
Entwickeln Sie eine Operationalisierung für folgende Forschungsfrage: "Wie veränderte sich die Berichterstattung über wissenschaftliche Themen in der Wochenzeitung 'Die Zeit' zwischen 1950-1970?"

#### Schritt 1
Formulieren Sie zunächst selbst eine mögliche Operationalisierung

```{code-cell} ipython3
:tags: [remove-input]
from IPython.display import HTML

HTML("""
<div padding: 15px; border-radius: 5px; margin: 10px 0;">
    <textarea id="answer" rows="3" style="width: 100%; margin-top: 10px; padding: 10px; border: 1px solid #ced4da; border-radius: 4px;" placeholder="Ihre Antwort"></textarea>
</div>
""")
```

#### Schritt 2 

Vergleichen Sie Ihre Antwort mit den folgenden Kriterien für eine geeignete Operationalisierung. Bewerten Sie Ihre eigene Antwort anhand dieser Kriterien


```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

questions = [
    {
        "question": "Verwendet Ihre Operationalisierung quantifizierbare Indikatoren?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Ja",
                "correct": True,
                "feedback": "✓ Korrekt!"
            },
            {
                "answer": "Nein",
                "correct": False,
                    "feedback": """× Nicht korrekt! Die Indikatoren müssen in Zahlen ausdrückbar sein
                    - Beispiele für quantifizierbare Indikatoren:
                    - Worthäufigkeiten (z.B. Anzahl wissenschaftsbezogener Begriffe), Textlängen (z.B. Wörter pro Artikel), Prozentuale Anteile (z.B. Anteil am Gesamtumfang)
                    - Gegenbeispiele (nicht quantifizierbar):
                    "Wichtigkeit" ohne weitere Spezifikation, "Qualität der Berichterstattung" ohne Messkriterien, Vage Beschreibungen wie "häufig" oder "selten"."""
            }
        ]
    },
    {
        "question": "Basieren die Messungen auf dem definierten Quellenkorpus (Die Zeit)?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Ja",
                "correct": True,
                "feedback": "✓ Korrekt!"
            },
            {
                "answer": "Nein",
                "correct": False,
                "feedback": """× Nicht korrekt! Alle Messungen müssen im Korpus der "Zeit" durchführbar sein. 
                - Zu beachten:
                Verfügbarkeit aller Ausgaben im Untersuchungszeitraum, 
                Konsistenz des Zeitungsformats, 
                Zugänglichkeit der relevanten Artikel. 
                - Nicht geeignet sind Messungen, die:
                Andere Zeitungen einbeziehen, 
                Externe Datenquellen erfordern, 
                Nicht im Zeitungskorpus enthaltene Informationen benötigen"""
            }
        ]
    },
    {
        "question": "Lassen sich die Messungen über den gesamten Zeitraum durchführen?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Ja",
                "correct": True,
                "feedback": "✓ Korrekt!"
            },
            {
                "answer": "Nein",
                "correct": False,
                "feedback": """× Nicht korrekt! Die Messungen müssen von 1950-1970 konsistent möglich sein
                - Wichtige Aspekte:
                Gleichbleibende Verfügbarkeit der Daten, 
                Vergleichbarkeit der Messungen über Zeit, 
                Berücksichtigung möglicher Formatänderungen. 
                - Problematisch wären:
                Indikatoren, die nur für Teilzeiträume verfügbar sind, 
                Messungen, die durch Änderungen der Zeitung beeinflusst werden, 
                Nicht durchgängig dokumentierte Aspekte"""
            }
        ]
    },
    {
        "question": "Sind die vorgeschlagenen Messverfahren praktisch umsetzbar?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Ja",
                "correct": True,
                "feedback": "✓ Korrekt!"
            },
            {
                "answer": "Nein",
                "correct": False,
                "feedback": """× Nicht korrekt! - Die Methoden müssen mit verfügbaren Ressourcen durchführbar sein
                - Praktische Aspekte:
                Verfügbare Zeit und Personal, 
                Technische Möglichkeiten (z.B. OCR, Textanalysetools), 
                Aufwand-Nutzen-Verhältnis. 
                - Problematisch wären:
                Zu zeitaufwendige manuelle Analysen, 
                Technisch nicht realisierbare Messungen, 
                Unverhältnismäßig komplexe Verfahren"""
            }
        ]
    }
]
display_quiz(questions, colors=colors.jupyterquiz)
```

#### Anwendung der Kriterien

Bei der Bewertung Ihrer Operationalisierung:

1. Prüfen Sie jeden Indikator einzeln gegen alle Kriterien
2. Identifizieren Sie mögliche Schwachstellen
3. Erwägen Sie Alternativen für problematische Aspekte
4. Dokumentieren Sie Ihre Überlegungen zu jedem Kriterium


````{admonition} Lösungen
:class: solution, dropdown
**Beispielhafte Anwendung**
Ein Indikator wie "Anzahl wissenschaftlicher Artikel pro Ausgabe":
- ✓ Quantifizierbar (zählbare Einheit)
- ✓ Basiert auf Quellenkorpus (nur Zeit-Artikel) 
- ✓ Durchgängig messbar (über gesamten Zeitraum)
- ✓ Praktisch umsetzbar (mit klarer Definition und OCR)

**Hinweis** 
Es gibt nicht die eine "richtige" Operationalisierung. Verschiedene Ansätze können geeignet sein, solange sie den grundlegenden Kriterien entsprechen und praktisch umsetzbar sind.
````