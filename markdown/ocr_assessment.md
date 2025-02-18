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

```{admonition} Feinlernziel
:class: lernziele
Sie können die Funktionsweise und Einsatzzwecke von OCR erläutern.
```

## Frage 1 

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice_1 = [{
    "question": """Welche Aussagen beschreiben die Funktionsweise und Einsatzzwecke von OCR korrekt?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "OCR ermöglicht die automatische Umwandlung von gescannten Dokumenten in maschinenlesbaren Text.",
            "correct": True,
            "feedback": """✓ Richtig! Dies ist die Kernfunktion von OCR:
            - Erkennt Textzeichen in Bildern
            - Wandelt diese in digitalen Text um
            - Macht Dokumente maschinenlesbar
            Diese Funktion ist grundlegend für die Digitalisierung historischer Dokumente."""
        },
        {
            "answer": "OCR wird ausschließlich für die Digitalisierung von handgeschriebenen Texten verwendet.",
            "correct": False,
            "feedback": """× Nicht korrekt. OCR hat verschiedene Anwendungsbereiche:
            - Gedruckte Texte (Hauptanwendung)
            - Handgeschriebene Texte (schwieriger)
            - Formulare und Dokumente
            - Historische Zeitungen (wie in unserem Beispiel)"""
        },
        {
            "answer": "Die Erstellung durchsuchbarer Dokumentensammlungen ist ein wichtiger Einsatzzweck von OCR.",
            "correct": True,
            "feedback": """✓ Richtig! OCR ermöglicht:
            - Volltextsuche in digitalisierten Dokumenten
            - Effiziente Informationsfindung
            - Automatisierte Textanalyse
            - Verbesserte Zugänglichkeit von Archiven"""
        }
    ]
}]

display_quiz(multiple_choice_1, colors=colors.jupyterquiz)
```
## Frage 2

Analysieren Sie die folgenden Aussagen zur OCR-Qualitätskontrolle.

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

question2 = [
    {
        "question": "Eine stichprobenartige Qualitätskontrolle ist für große Korpora ausreichend.",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Ja",
                "correct": True,
                "feedback": """✓ Richtig, weil:
                - Vollständige Überprüfung oft nicht praktikabel
                - Repräsentative Stichproben geben guten Überblick
                - Systematische Fehler können erkannt werden"""
            },
            {
                "answer": "Nein",
                "correct": False,
                "feedback": "× Nicht korrekt!"
            }
        ]
    },
    {
        "question": "Die OCR-Qualität ist unabhängig von der Qualität der Eingabebilder.",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Ja",
                "correct": False,
                "feedback": """× Nicht korrekt. Die Bildqualität ist entscheidend:
                - Schlechte Scans führen zu schlechteren Ergebnissen
                - Vorverarbeitung kann Qualität verbessern
                - Originalqualität beeinflusst Erkennungsrate"""
            },
            {
                "answer": "Nein",
                "correct": True,
                "feedback": "✓ Richtig!"
            }
        ]
    },
]
display_quiz(question2, colors=colors.jupyterquiz)
```

## Frage 3

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

question3 = [
    {
        "question": "Welche Aussagen über die OCR-Verarbeitung verschiedener Dokumenttypen sind korrekt?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Mehrseitige PDFs müssen vor der OCR-Verarbeitung in Einzelbilder konvertiert werden.",
                "correct": True,
                "feedback": """✓ Richtig! Dies ist notwendig weil:
                - PyTesseract arbeitet nur mit Bilddaten
                - PDFs müssen seitenweise verarbeitet werden
                - convert_from_path wird für die Konvertierung verwendet
                - Jede Seite wird einzeln durch OCR verarbeitet"""
            },
            {
                "answer": "Die Verarbeitung eines Einzelbildes und einer PDF-Seite erfolgt mit unterschiedlichen OCR-Funktionen.",
                "correct": False,
                "feedback": """× Nicht korrekt. Tatsächlich:
                - Beide verwenden image_to_string
                - Der Unterschied liegt in der Vorverarbeitung
                - Die OCR-Funktion selbst ist identisch
                - Nur das Handling der Eingabedaten unterscheidet sich"""
            },
            {
                "answer": "Bei der Korpusverarbeitung müssen zusätzliche Aspekte wie Dateiverwaltung berücksichtigt werden.",
                "correct": True,
                "feedback": """✓ Richtig! Bei der Korpusverarbeitung:
                - Systematische Dateiorganisation nötig
                - Verwaltung von Ein- und Ausgabepfaden
                - Handhabung großer Datenmengen
                - Strukturierte Speicherung der Ergebnisse"""
            }
        ]
    }
]
display_quiz(question3, colors=colors.jupyterquiz)
```

## Frage 4

dentifizieren Sie mögliche Probleme in den folgenden Aussagen zur OCR-Verarbeitung.

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

question4 = [
    {
        "question": "Es ist effizienter, ein mehrseitiges PDF direkt durch OCR zu verarbeiten, ohne es vorher in Bilder zu konvertieren.",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Ja",
                "correct": False,
                "feedback": """× Nicht korrekt! Diese Aussage ist falsch, weil:
                - PyTesseract benötigt Bilddaten
                - Direkte PDF-Verarbeitung nicht möglich
                - Konvertierung ist zwingend erforderlich
                - Effizient bedeutet hier nicht schneller"""
            },
            {
                "answer": "Nein",
                "correct": True,
                "feedback": "✓ Richtig!"
            }
        ]
    },
    {
        "question": "Bei der Korpusverarbeitung sollte jede Datei einzeln manuell verarbeitet werden.",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Ja",
                "correct": False,
                "feedback": """× Nicht korrekt! Diese Aussage ist falsch, weil:
                - Automatisierung für große Korpora notwendig
                - Manuelle Verarbeitung zeitaufwändig
                - Fehleranfälligkeit bei manueller Arbeit
                - Systematische Verarbeitung vorteilhaft"""
            },
            {
                "answer": "Nein",
                "correct": True,
                "feedback": "✓ Richtig!"
            }
        ]
    }
]
display_quiz(question4, colors=colors.jupyterquiz)
```

## Frage 5

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

question5 = [{
    "question": """Welche Aussagen zu OCR-Qualitätsmetriken sind korrekt?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Eine hohe Präzision bedeutet, dass die erkannten Zeichen überwiegend korrekt identifiziert wurden.",
            "correct": True,
            "feedback": """✓ Richtig! Präzision misst die Genauigkeit der Erkennung:
            - Fokus auf korrekt erkannte Zeichen
            - Verhältnis: korrekt erkannt zu insgesamt erkannt
            - Wichtig für Zuverlässigkeit der Ergebnisse
            - Reduziert falsch-positive Erkennungen"""
        },
        {
            "answer": "Ein hoher Recall bedeutet, dass alle vorhandenen Zeichen erkannt wurden, unabhängig von der Korrektheit.",
            "correct": True,
            "feedback": """✓ Richtig! Recall misst die Vollständigkeit:
            - Erfasst alle vorhandenen Zeichen
            - Verhältnis: gefunden zu tatsächlich vorhanden
            - Wichtig für Vollständigkeit der Erkennung
            - Minimiert falsch-negative Erkennungen"""
        },
        {
            "answer": "Der F1-Score ist immer der Durchschnitt von Präzision und Recall.",
            "correct": False,
            "feedback": """× Nicht korrekt. Der F1-Score:
            - Ist das harmonische Mittel
            - Gewichtet beide Metriken gleich
            - Berücksichtigt den Trade-off
            - Berechnung: 2 × (Präzision × Recall)/(Präzision + Recall)"""
        }
    ]
}]
display_quiz(question5, colors=colors.jupyterquiz)
```

## Frage 6

Analysieren Sie die Bedeutung der verschiedenen Metriken in folgenden Szenarien.

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

question6 = [
    {
        "question": "Welche Metrik ist bei der Digitalisierung historischer Zeitungen für wissenschaftliche Forschung besonders wichtig?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Präzision",
                "correct": False,
                "feedback": """× Nicht korrekt."""
            },
            {
                "answer": "Recall",
                "correct": False,
                "feedback": """× Nicht korrekt."""
            },
            {
                "answer": "Ausgewogener F1-Score",
                "correct": True,
                "feedback": """✓ Richtig! Ein ausgewogener F1-Score ist ideal, weil:
                - Balanciert Präzision und Recall
                - Wissenschaftliche Forschung benötigt beide Aspekte
                - Minimiert Fehler und Auslassungen
                - Optimale Balance für Forschungszwecke"""
            }
        ]
    },
    {
        "question": "Welche Metrik sollte bei der automatischen Erfassung von Formulardaten priorisiert werden?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Präzision",
                "correct": True,
                "feedback": """✓ Richtig! Präzision ist hier entscheidend, weil:
                - Falsche Dateneingaben müssen vermieden werden
                - Korrektheit der erfassten Daten ist kritisch
                - Manuelle Nachkontrolle ist aufwendig
                - Fehlerhafte Daten können Prozesse stören"""
            },
            {
                "answer": "Recall",
                "correct": False,
                "feedback": """× Nicht korrekt."""
            },
            {
                "answer": "F1-Score",
                "correct": False,
                "feedback": """× Nicht korrekt."""
            }
        ]
    }
]
display_quiz(question6, colors=colors.jupyterquiz)
```
## Frage 7
Erklären Sie die Beziehungen zwischen den OCR-Qualitätsmetriken.

**Trade-off zwischen Präzision und Recall**
```{code-cell} ipython3
:tags: [remove-input]
from IPython.display import HTML

HTML("""
<div padding: 15px; border-radius: 5px; margin: 10px 0;">
    <textarea id="answer" rows="2" style="width: 100%; margin-top: 10px; padding: 10px; border: 1px solid #ced4da; border-radius: 4px;" placeholder="Ihre Antwort"></textarea>
</div>
""")
```
````{admonition}  Lösungen
:class: solution, dropdown
Wichtig zu verstehen:
- Verbesserung einer Metrik kann andere verschlechtern
- Optimierung für Präzision kann Recall reduzieren
- Fokus auf Recall kann Präzision verringern
- F1-Score hilft bei Ausgleich

**Beispiel:** 
"Strengere Erkennungsregeln erhöhen Präzision, können aber Recall senken."
````

**Rolle des F1-Scores**
```{code-cell} ipython3
:tags: [remove-input]
from IPython.display import HTML

HTML("""
<div padding: 15px; border-radius: 5px; margin: 10px 0;">     
    <textarea id="answer" rows="2" style="width: 100%; margin-top: 10px; padding: 10px; border: 1px solid #ced4da; border-radius: 4px;" placeholder="Ihre Antwort"></textarea>
</div>
""")
```
````{admonition}  Lösungen
:class: solution, dropdown
Der F1-Score:
- Kombiniert beide Metriken ausgewogen
- Ermöglicht einzelne Bewertungszahl
- Hilft bei Systemvergleichen
- Berücksichtigt beide Aspekte der Qualität
````

## Frage 8
Analysieren Sie die folgenden OCR-Qualitätswerte aus dem Beispiel:
- Precision: 0.778
- Recall: 0.7932
- F1-score: 0.7855

**Was bedeutet die Precision von 0.778 in diesem Kontext?**
```{code-cell} ipython3
:tags: [remove-input]
from IPython.display import HTML

HTML("""
<div padding: 15px; border-radius: 5px; margin: 10px 0;">
     <textarea id="answer" rows="1" style="width: 100%; margin-top: 10px; padding: 10px; border: 1px solid #ced4da; border-radius: 4px;" placeholder="Ihre Antwort"></textarea>
</div>
""")
```
````{admonition}  Lösungen
:class: solution, dropdown
**77.8% der vom OCR-System erkannten Zeichen sind korrekt.**

Erklärung:
- Precision misst den Anteil korrekter Erkennungen
- Wert von 0.778 entspricht 77.8%
- Zeigt moderate bis gute Erkennungsgenauigkeit
- Typisch für historische Frakturschrift
````

**Warum ist der Recall (0.7932) höher als die Precision?**
```{code-cell} ipython3
:tags: [remove-input]
from IPython.display import HTML

HTML("""
<div padding: 15px; border-radius: 5px; margin: 10px 0;">
     <textarea id="answer" rows="1" style="width: 100%; margin-top: 10px; padding: 10px; border: 1px solid #ced4da; border-radius: 4px;" placeholder="Ihre Antwort"></textarea>
</div>
""")
```
````{admonition}  Lösungen
:class: solution, dropdown
**Das System erkennt mehr vorhandene Zeichen, macht dabei aber auch mehr Fehler.**

Erklärung:
- Höherer Recall bedeutet bessere Vollständigkeit
- Kompromiss zwischen Genauigkeit und Vollständigkeit
- Typisches Muster bei historischen Dokumenten
- Balance durch F1-Score (0.7855) ersichtlich
````

## Frage 9

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

question9 = [
    {
        "question": "Basierend auf den gemessenen Qualitätswerten, welche Verbesserungsmaßnahmen wären sinnvoll?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Verwendung eines spezialisierten Fraktur-OCR-Modells",
                "correct": True,
                "feedback": """✓ Sinnvoll, weil:
                - Bereits lang='frk' verwendet
                - Spezialisierte Modelle oft bessere Ergebnisse
                - Besonders wichtig bei historischen Schriften
                - Kann beide Metriken verbessern"""
            },
            {
                "answer": "Ausschließliche Fokussierung auf Precision-Verbesserung",
                "correct": False,
                "feedback": """× Nicht optimal, weil:
                - Balance zwischen Precision und Recall wichtig
                - Aktuelle Werte relativ ausgewogen
                - F1-Score zeigt akzeptable Gesamtleistung
                - Beidseitige Verbesserung anzustreben"""
            }
        ]
    }
]
display_quiz(question9, colors=colors.jupyterquiz)
```
## Frage 10
Bewerten Sie die Eignung der gemessenen OCR-Qualität für verschiedene Anwendungsfälle.

**Volltextsuche in digitalisierten Zeitungen**
```{code-cell} ipython3
:tags: [remove-input]
from IPython.display import HTML

HTML("""
<div padding: 15px; border-radius: 5px; margin: 10px 0;">
    <textarea id="answer" rows="1" style="width: 100%; margin-top: 10px; padding: 10px; border: 1px solid #ced4da; border-radius: 4px;" placeholder="Ihre Antwort"></textarea>
</div>
""")
```
````{admonition}  Lösungen
:class: solution, dropdown
Bedingt geeignet, weil:
- Recall von 0.79 ermöglicht Auffinden der meisten Begriffe
- Precision von 0.78 bedeutet moderate Fehlerrate
- F1-Score zeigt akzeptable Gesamtqualität
- Suchfunktionen tolerieren gewisse Fehler

**Empfehlung:**
- Einsatz von Fuzzy-Suche
- Berücksichtigung häufiger OCR-Fehler
- Mögliche manuelle Nachkorrektur wichtiger Passagen
````

**Exakte Texttranskription für Edition**
```{code-cell} ipython3
:tags: [remove-input]
from IPython.display import HTML

HTML("""
<div padding: 15px; border-radius: 5px; margin: 10px 0;">
    <textarea id="answer" rows="1" style="width: 100%; margin-top: 10px; padding: 10px; border: 1px solid #ced4da; border-radius: 4px;" placeholder="Ihre Antwort"></textarea>
</div>
""")
```
````{admonition}  Lösungen
:class: solution, dropdown
Nicht ausreichend, weil:
- Precision unter 80% zu viele Fehler bedeutet
- Recall nicht vollständig genug
- Editorische Arbeit erfordert höhere Genauigkeit
- Manuelle Korrektur notwendig

**Empfehlung:**
 - Verwendung als Vorverarbeitung
- Systematische manuelle Korrektur
- Dokumentation der OCR-Qualität
- Mehrfache Qualitätskontrolle
````