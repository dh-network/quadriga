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

## Frage 1

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

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
display_quiz(question1, colors=colors.jupyterquiz)
```
## Frage 2

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
                "feedback": "✓ Korrekt! Die Worthäufigkeitsanalyse ist geeignet, weil sie ein quantifizierbares Maß für die Intensität der medialen Berichterstattung liefert."
            },
            {
                "answer": "Messen der Länge von Artikeln, die Umweltthemen behandeln",
                "correct": True,
                "feedback": "✓ Korrekt! Die Artikellänge und der prozentuale Seitenanteil sind ebenfalls geeignet, da sie die dem Thema gewidmete Aufmerksamkeit quantitativ erfassen."
            },
            {
                "answer": "Erfassen der tatsächlichen Umweltverschmutzungswerte aus diesem Zeitraum",
                "correct": False,
                "feedback": "× Nicht korrekt! Umweltverschmutzungswerte sind ungeeignet, da sie nicht die mediale Aufmerksamkeit, sondern das tatsächliche Umweltgeschehen messen."
            },
            {
                "answer": "Analyse von Regierungsdokumenten zur Umweltpolitik",
                "correct": False,
                "feedback": "× Nicht korrekt! Regierungsdokumente fallen außerhalb des definierten Untersuchungskorpus (Tageszeitungen) und sind daher ungeeignet."
            },
            {
                "answer": "Erfassen des prozentualen Anteils der Zeitungsseiten mit Umweltthemen",
                "correct": True,
                "feedback": """✓ Korrekt! Die geeigneten Operationalisierungen zeichnen sich dadurch aus, dass sie:
                    - ein quantifizierbares Maß für mediale Aufmerksamkeit bieten
                    - sich auf das definierte Quellenkorpus (Tageszeitungen) beschränken
                    - eine systematische Analyse über den gesamten Zeitraum ermöglichen"""
            }
        ]
        }
]
display_quiz(question2, colors=colors.jupyterquiz)
```

## Frage 3
### Self-Assessment-Aufgabe

#### Schritt 1: Formulieren Sie zunächst selbst eine mögliche Operationalisierung für folgende Forschungsfrage
Wie veränderte sich die Berichterstattung über wissenschaftliche Themen in der Wochenzeitung 'Die Zeit' zwischen 1950-1970?


```{code-cell} ipython3
:tags: [remove-input]
from IPython.display import HTML

HTML("""
<div padding: 15px; border-radius: 5px; margin: 10px 0;">
    <textarea id="answer" rows="3" style="width: 100%; margin-top: 10px; padding: 10px; border: 1px solid #ced4da; border-radius: 4px;" placeholder="Ihre Antwort"></textarea>
</div>
""")
```
#### Schritt 2:Vergleichen Sie Ihre Antwort mit den folgenden Kriterien für eine geeignete Operationalisierung. Bewerten Sie Ihre eigene Antwort anhand dieser Kriterien

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
                "feedback": "× Nicht korrekt!"
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
                "feedback": "× Nicht korrekt!"
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
                "feedback": "× Nicht korrekt!"
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
                "feedback": "× Nicht korrekt!"
            }
        ]
    }
]
display_quiz(questions, colors=colors.jupyterquiz)
```

````{admonition}  Lösungen
:class: solution, dropdown
**Beispiel einer möglichen Operationalisierung:**

"Die Veränderung der Berichterstattung wird durch die Analyse von Worthäufigkeiten wissenschaftsbezogener Begriffe, die Länge der Artikel und deren Platzierung in der Zeitung gemessen. Diese Indikatoren werden pro Ausgabe erfasst und über den Zeitraum verglichen."

**Reflexionsfragen:**
- Welche Stärken hat Ihre Operationalisierung im Vergleich zum Beispiel?
- Welche zusätzlichen Aspekte haben Sie berücksichtigt?
- Wo sehen Sie potenzielle Herausforderungen bei Ihrer Operationalisierung?

**Hinweis:** Es gibt nicht die eine "richtige" Operationalisierung. Verschiedene Ansätze können geeignet sein, solange sie den grundlegenden Kriterien entsprechen und praktisch umsetzbar sind.
````