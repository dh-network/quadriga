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

````{admonition} Hinweis
:class: hinweis
Diese Übungsaufgaben dienen Ihrer Selbsteinschätzung und helfen Ihnen, das im Kapitel Gelernte zu reflektieren.

Sie können die Fragen in beliebiger Reihenfolge beantworten und auch mehrfach versuchen. 

**So funktioniert es:**
- Wählen Sie bei jeder Frage die Antwort(en), die Sie für richtig halten
- Lesen Sie das Feedback zu den einzelnen Antwortoptionen sorgfältig durch
- Die Erklärungen helfen Ihnen, Ihr Verständnis zu vertiefen – auch bei korrekten Antworten 

Es erfolgt keine Bewertung oder Speicherung Ihrer Ergebnisse. Nutzen Sie dieses Assessment, um Wissenslücken zu identifizieren und gegebenenfalls die entsprechenden Abschnitte des Kapitels noch einmal zu bearbeiten. 

**Geschätzte Zeit**: 1h 10min

Viel Erfolg!
````

## Frage 1
(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

""" 
Lernziel: 
     Sie können den Prozess der Optical Character Recognition (OCR) für die Korpuserstellung beschreiben und dessen Qualität systematisch analysieren.
Bloom-Stufe: Verstehen
Format: Multiple Choice
Geschätzte Zeit: 15 Minuten
Schwerpunkte:
    - Grundprinzipien der OCR
    - Anwendungsbereiche
    - Funktionsweise

"""

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

ocr_sequence_question = [
    {
        "question": "Welche Reihenfolge der Prozessschritte ist für eine OCR-Pipeline korrekt?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "1. Texterkennung → 2. Bildvorverarbeitung → 3. Qualitätskontrolle",
                "correct": False,
                "feedback": """× Falsch. Die Bildvorverarbeitung muss vor der Texterkennung erfolgen, um optimale Ergebnisse zu erzielen."""
            },
            {
                "answer": "1. Qualitätskontrolle → 2. Bildvorverarbeitung → 3. Texterkennung",
                "correct": False,
                "feedback": """× Falsch. Die Qualitätskontrolle kann erst nach der Texterkennung durchgeführt werden, da sie den OCR-Output überprüft."""
            },
            {
                "answer": "1. Bildvorverarbeitung → 2. Texterkennung → 3. Qualitätskontrolle",
                "correct": True,
                "feedback": """✓ Richtig! Dies ist die korrekte Reihenfolge einer OCR-Pipeline:
                * Schritt 1: Die Bildvorverarbeitung verbessert die Bildqualität (durch Entfernung von Rauschen, Kontrastanpassung, etc.), erhöht dadurch die OCR-Genauigkeit und reduziert potenzielle Fehler.
                * Schritt 2: Bei der Texterkennung werden einzelne Zeichen erkannt, das Layout analysiert und die visuellen Elemente in digitalen Text umgewandelt.
                * Schritt 3: Die abschließende Qualitätskontrolle überprüft die Genauigkeit des erzeugten Textes, identifiziert Probleme und hilft bei der Entscheidung über notwendige Nachbearbeitungen."""
            },
            {
                "answer": "1. Bildvorverarbeitung → 2. Qualitätskontrolle → 3. Texterkennung",
                "correct": False,
                "feedback": """× Falsch. Die Qualitätskontrolle kann erst durchgeführt werden, nachdem die Texterkennung Text erzeugt hat, den man überprüfen kann."""
            }
        ]
    }
]

display_quiz(ocr_sequence_question, colors=colors.jupyterquiz,max_width=1000)
```
## Frage 4
(Wählen Sie alle zutreffenden Antworten aus)

### Frage 4(a)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

""" 
Lernziel: 
     Sie können die notwendigen Schritte zur Verarbeitung eines einseitigen und eines mehrseitigen PDFs zu einem Text aufzählen und das Ursprungs- sowie das Zielformat nennen und Unterschiede erklären.
Bloom-Stufe: Verstehen
Format: Tool-Vergleich und Zuordnungsaufgabe
Geschätzte Zeit: 20 Minuten
Schwerpunkte:
    - Verarbeitungsschritte für PDFs
	- Format-Transformationen und Formate
	- Unterschiede einseitig/mehrseitig
"""

import sys
sys.path.append("..")
from quadriga_config import colors

question1 = [
    {
        "question": "Welche Aussagen über Einzelbilder (JPEG) im OCR-Prozess sind korrekt? (Mehrere Antworten können richtig sein)",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Eine direkte OCR-Verarbeitung ist ohne zusätzliche Konvertierung möglich",
                "correct": True,
                "feedback": """✓ Richtig. Einzelbilder im JPEG-Format können direkt an OCR-Engines wie Tesseract übergeben werden, z.B. mit der Funktion `image_to_string`."""
            },
            {
                "answer": "Es muss eine Seitenextraktion durchgeführt werden",
                "correct": False,
                "feedback": """× Falsch. Bei Einzelbildern ist keine Seitenextraktion notwendig, da sie bereits genau eine "Seite" darstellen."""
            },
            {
                "answer": "Die OCR-Komplexität ist in der Regel niedrig",
                "correct": True,
                "feedback": """✓ Richtig. Einzelbilder stellen den einfachsten Verarbeitungsfall dar, da keine zusätzlichen Verarbeitungsschritte wie Seitenextraktion erforderlich sind."""
            },
            {
                "answer": "Sie erfordern eine Konvertierung in ein anderes Format vor der OCR-Verarbeitung",
                "correct": False,
                "feedback": """× Falsch. JPEG-Dateien können direkt von OCR-Engines verarbeitet werden."""
            },
            {
                "answer": "Sie eignen sich gut für einzelne Zeitungsartikel",
                "correct": True,
                "feedback": """✓ Richtig. Für einzelne Zeitungsartikel oder isolierte Textabschnitte sind Einzelbilder ein geeignetes Format."""
            }
        ]
    }
]

display_quiz(question1, colors=colors.jupyterquiz)
```

### Frage 4(b)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

question2 = [
    {
        "question": "Welche Aussagen über mehrseitige PDF-Dokumente im OCR-Prozess sind korrekt? (Mehrere Antworten können richtig sein)",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Sie können direkt an die OCR-Engine übergeben werden",
                "correct": False,
                "feedback": """× Falsch. Mehrseitige PDFs müssen zunächst in Bilder konvertiert werden, bevor sie von den meisten OCR-Engines verarbeitet werden können."""
            },
            {
                "answer": "Sie erfordern eine PDF-zu-Bild-Konvertierung vor der OCR",
                "correct": True,
                "feedback": """✓ Richtig. PDFs müssen in Bildformate konvertiert werden, bevor sie durch OCR-Engines wie Tesseract verarbeitet werden können."""
            },
            {
                "answer": "Eine seitenweise Verarbeitung ist notwendig",
                "correct": True,
                "feedback": """✓ Richtig. Mehrseitige PDFs müssen Seite für Seite verarbeitet werden, was zusätzliche Programmierlogik erfordert."""
            },
            {
                "answer": "Die Speicherung von Zwischenergebnissen ist wichtig",
                "correct": True,
                "feedback": """✓ Richtig. Bei der Verarbeitung umfangreicher PDFs ist es wichtig, Zwischenergebnisse zu speichern, um bei möglichen Fehlern nicht den gesamten Prozess neu starten zu müssen."""
            },
            {
                "answer": "Die Verarbeitungskomplexität ist niedriger als bei Einzelbildern",
                "correct": False,
                "feedback": """× Falsch. Die Komplexität ist bei mehrseitigen PDFs mittel bis hoch, da zusätzliche Verarbeitungsschritte notwendig sind."""
            }
        ]
    }
]

display_quiz(question2, colors=colors.jupyterquiz)
```

### Frage 4(c)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

question3 = [
    {
        "question": "Welcher Dokumenttyp erfordert keine zusätzliche Vorverarbeitung für OCR?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Einzelbild (JPEG)",
                "correct": True,
                "feedback": """✓ Richtig. Einzelbilder können direkt an OCR-Engines übergeben werden, ohne dass zusätzliche Vorverarbeitung notwendig ist."""
            },
            {
                "answer": "Mehrseitiges PDF",
                "correct": False,
                "feedback": """× Falsch. PDFs erfordern eine Konvertierung in Bilder vor der OCR-Verarbeitung."""
            },
            {
                "answer": "Beide Formate",
                "correct": False,
                "feedback": """× Falsch. Nur Einzelbilder können ohne zusätzliche Vorverarbeitung verarbeitet werden."""
            },
            {
                "answer": "Keines der Formate",
                "correct": False,
                "feedback": """× Falsch. Einzelbilder benötigen keine zusätzliche Vorverarbeitung."""
            }
        ]
    }
]

display_quiz(question3, colors=colors.jupyterquiz)
```

### Frage 4(d)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

question4 = [
    {
        "question": "Welcher Dokumenttyp eignet sich gut für vollständige Zeitungsausgaben?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Einzelbild (JPEG)",
                "correct": False,
                "feedback": """× Falsch. Einzelbilder eignen sich besser für einzelne Artikel, nicht für vollständige Ausgaben."""
            },
            {
                "answer": "Mehrseitiges PDF",
                "correct": True,
                "feedback": """✓ Richtig. Mehrseitige PDFs sind ideal für vollständige Zeitungsausgaben, da sie mehrere Seiten in einer Datei zusammenfassen."""
            },
            {
                "answer": "Beide Formate",
                "correct": False,
                "feedback": """× Falsch. Einzelbilder sind für vollständige Ausgaben unpraktisch, da sie für jede Seite eine separate Datei erfordern würden."""
            },
            {
                "answer": "Keines der Formate",
                "correct": False,
                "feedback": """× Falsch. Mehrseitige PDFs eignen sich durchaus für vollständige Zeitungsausgaben."""
            }
        ]
    }
]

display_quiz(question4, colors=colors.jupyterquiz)
```


## Frage 5
(Wählen Sie alle zutreffenden Antworten aus)

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
## Frage 6

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

question5 = [
    {
        "question": "In welcher Reihenfolge werden die folgenden Schritte bei der OCR-Verarbeitung eines mehrseitigen PDFs durchgeführt?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "1. OCR auf jeder Seite durchführen → 2. PDF in Einzelseiten konvertieren → 3. Erkannten Text speichern",
                "correct": False,
                "feedback": """× Falsch. Die OCR-Engine benötigt Bilddaten als Eingabe, daher muss das PDF zuerst in Einzelbilder konvertiert werden, bevor die OCR durchgeführt werden kann."""
            },
            {
                "answer": "1. PDF in Einzelseiten konvertieren → 2. OCR auf jeder Seite durchführen → 3. Erkannten Text speichern",
                "correct": True,
                "feedback": """✓ Richtig! Dies ist die korrekte Reihenfolge:
                * Zuerst wird das PDF in Einzelseiten konvertiert, da OCR Bilddaten benötigt und PDFs seitenweise verarbeitet werden müssen
                * Dann wird auf jeder konvertierten Bildseite die OCR durchgeführt (typischerweise mit Funktionen wie `image_to_string`), wodurch Text für jede Seite erzeugt wird
                * Schließlich wird der erkannte Text gespeichert, um die OCR-Ergebnisse zu sichern, weitere Verarbeitung zu ermöglichen und für die Dokumentation"""
            },
            {
                "answer": "1. PDF in Einzelseiten konvertieren → 2. Erkannten Text speichern → 3. OCR auf jeder Seite durchführen",
                "correct": False,
                "feedback": """× Falsch. Man kann keinen Text speichern, bevor die OCR durchgeführt wurde, da die OCR erst den Text aus den Bildern erzeugt."""
            },
            {
                "answer": "1. Erkannten Text speichern → 2. PDF in Einzelseiten konvertieren → 3. OCR auf jeder Seite durchführen",
                "correct": False,
                "feedback": """× Falsch. Diese Reihenfolge ist logisch unmöglich, da der Text erst nach der PDF-Konvertierung und OCR-Durchführung vorhanden ist und gespeichert werden kann."""
            }
        ]
    }
]

display_quiz(question5, colors=colors.jupyterquiz, max_width=1000)
```

## Frage 7

Identifizieren Sie mögliche Probleme in den folgenden Aussagen:

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
                "feedback": """× Diese Aussage ist falsch, weil:
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
                "feedback": """× Diese Aussage ist falsch, weil:
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

## Frage 8
(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

""" 
Lernziel: 
     Sie können die grundlegenden Metriken zur OCR-Qualitätsevaluation (Präzision, Recall, F1-Score) erläutern und ihre Bedeutung für die Bewertung von OCR-Systemen beschreiben.
Bloom-Stufe: Verstehen, Analysieren
Format: Vergleichsmatrix + Multiple Choice
Geschätzte Zeit: 25 Minuten
Schwerpunkte:
    - Definition und Berechnung der Qualitätsmetriken
    - Zusammenhänge zwischen den Metriken
    - Interpretation der Messwerte
    - Anwendung in der OCR-Evaluation
"""

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

## Frage 9

Analysieren Sie die Bedeutung der verschiedenen Metriken in folgenden Szenarien.

### Frage 9(a)
**Szenario 1: Digitalisierung historischer Zeitungen für wissenschaftliche Forschung**

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
                - Wissenschaftliche Forschung benötigt sowohl Genauigkeit als auch Vollständigkeit
                - Falsche Erkennungen können Forschungsergebnisse verfälschen
                - Fehlende Erkennungen können wichtige Informationen übersehen
                - Balance zwischen Präzision und Recall notwendig
                """
            }
        ]
    } 
]
display_quiz(question6, colors=colors.jupyterquiz)
```
### Frage 9(b)
**Szenario 2: Automatische Erfassung von Formulardaten**

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

question7 = [
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
display_quiz(question7, colors=colors.jupyterquiz)
```
## Frage 10
Erklären Sie die Beziehungen zwischen den OCR-Qualitätsmetriken.

### Frage 10(a)
**Trade-off zwischen Präzision und Recall**
```{code-cell} ipython3
:tags: [remove-input]
from IPython.display import HTML

HTML("""
<div padding: 15px; border-radius: 5px; margin: 10px 0;">
    <textarea id="answer" rows="4" style="width: 100%; margin-top: 10px; padding: 10px; border: 1px solid #ced4da; border-radius: 4px;" placeholder="Ihre Antwort"></textarea>
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
### Frage 10(b)
**Rolle des F1-Scores**
```{code-cell} ipython3
:tags: [remove-input]
from IPython.display import HTML

HTML("""
<div padding: 15px; border-radius: 5px; margin: 10px 0;">     
    <textarea id="answer" rows="4" style="width: 100%; margin-top: 10px; padding: 10px; border: 1px solid #ced4da; border-radius: 4px;" placeholder="Ihre Antwort"></textarea>
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

## Frage 11
(Wählen Sie alle zutreffenden Antworten aus)

### Frage 11(a)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

precision_question = [
    {
        "question": "Welche Aussagen treffen auf OCR-Ergebnisse mit HOHER PRÄZISION zu? (Mehrere Antworten können richtig sein)",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Weniger Korrekturaufwand ist notwendig",
                "correct": True,
                "feedback": """✓ Richtig. Hohe Präzision bedeutet, dass die meisten erkannten Zeichen korrekt sind, was den Korrekturaufwand reduziert."""
            },
            {
                "answer": "Es entstehen viele falsch positive Erkennungen",
                "correct": False,
                "feedback": """× Falsch. Hohe Präzision bedeutet genau das Gegenteil - es gibt wenige falsch positive Erkennungen."""
            },
            {
                "answer": "Der erkannte Text ist sehr zuverlässig",
                "correct": True,
                "feedback": """✓ Richtig. Präzision misst die Zuverlässigkeit der gefundenen Elemente; bei hoher Präzision kann man den erkannten Wörtern vertrauen."""
            },
            {
                "answer": "Die Ergebnisse können unvollständig sein",
                "correct": True,
                "feedback": """✓ Richtig. Ein System, das auf hohe Präzision optimiert ist, könnte unsichere Erkennungen weglassen, was zu unvollständiger Texterfassung führen kann."""
            },
            {
                "answer": "Hoher manueller Nachbearbeitungsaufwand ist zu erwarten",
                "correct": False,
                "feedback": """× Falsch. Hohe Präzision reduziert den Nachbearbeitungsaufwand, da weniger falsche Erkennungen korrigiert werden müssen."""
            }
        ]
    }
]

display_quiz(precision_question, colors=colors.jupyterquiz)
```

### Frage 11(b)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

precision_applications = [
    {
        "question": "Für welche Anwendungsfälle sind OCR-Ergebnisse mit HOHER PRÄZISION besonders wichtig? (Mehrere Antworten können richtig sein)",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Erfassung historischer Dokumente, bei denen Vollständigkeit wichtiger ist als absolute Genauigkeit",
                "correct": False,
                "feedback": """× Falsch. Bei historischen Dokumenten ist oft Vollständigkeit (hoher Recall) wichtiger als Präzision."""
            },
            {
                "answer": "Kritische Anwendungen, bei denen falsche Informationen schwerwiegende Folgen haben können",
                "correct": True,
                "feedback": """✓ Richtig. In kritischen Anwendungen sind zuverlässige, fehlerfreie Daten wichtiger als vollständige Erfassung."""
            },
            {
                "answer": "Datenmining-Projekte, bei denen einzelne Fehler tolerierbar sind",
                "correct": False,
                "feedback": """× Falsch. Beim Datenmining ist oft eine umfassende Erfassung (hoher Recall) wichtiger als absolute Präzision."""
            },
            {
                "answer": "Automatische Verarbeitung von Dokumenten ohne manuelle Nachkontrolle",
                "correct": True,
                "feedback": """✓ Richtig. Wenn keine manuelle Überprüfung erfolgt, ist hohe Präzision besonders wichtig, um Fehler zu minimieren."""
            },
            {
                "answer": "Explorative Analyse großer Textkorpora",
                "correct": False,
                "feedback": """× Falsch. Bei explorativen Analysen ist Vollständigkeit oft wichtiger als absolute Fehlerfreiheit."""
            }
        ]
    }
]

display_quiz(precision_applications, colors=colors.jupyterquiz)
```

### Frage 11(c)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

recall_question = [
    {
        "question": "Welche Aussagen treffen auf OCR-Ergebnisse mit HOHEM RECALL zu? (Mehrere Antworten können richtig sein)",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Vollständige Erfassung des Originaltextes",
                "correct": True,
                "feedback": """✓ Richtig. Hoher Recall bedeutet, dass ein großer Teil der tatsächlich vorhandenen Zeichen erkannt wird."""
            },
            {
                "answer": "Erhöhte Wahrscheinlichkeit von Fehlerkennungen",
                "correct": True,
                "feedback": """✓ Richtig. Systeme mit hohem Recall neigen dazu, auch zweifelhafte Fälle zu erkennen, was zu mehr Fehlern führen kann."""
            },
            {
                "answer": "Reduzierter Korrekturaufwand",
                "correct": False,
                "feedback": """× Falsch. Wegen der höheren Fehlerrate steigt der Korrekturaufwand in der Regel an."""
            },
            {
                "answer": "Mehr manuelle Überprüfung notwendig",
                "correct": True,
                "feedback": """✓ Richtig. Da mehr Fehler zu erwarten sind, ist eine gründlichere manuelle Überprüfung erforderlich."""
            },
            {
                "answer": "Optimale Eignung für sicherheitskritische Anwendungen",
                "correct": False,
                "feedback": """× Falsch. Für sicherheitskritische Anwendungen ist in der Regel hohe Präzision wichtiger als hoher Recall."""
            }
        ]
    }
]

display_quiz(recall_question, colors=colors.jupyterquiz)
```

### Frage 11(d)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

recall_applications = [
    {
        "question": "Für welche Anwendungsfälle sind OCR-Ergebnisse mit HOHEM RECALL besonders wichtig? (Mehrere Antworten können richtig sein)",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Automatische Dokumentenverarbeitung ohne manuelle Nachkontrolle",
                "correct": False,
                "feedback": """× Falsch. Ohne manuelle Nachkontrolle ist hohe Präzision wichtiger, um Fehler zu vermeiden."""
            },
            {
                "answer": "Explorative textuelle Datenanalyse",
                "correct": True,
                "feedback": """✓ Richtig. Bei explorativen Analysen ist es wichtiger, möglichst alle relevanten Daten zu erfassen, auch wenn einige Fehler enthalten sind."""
            },
            {
                "answer": "Vollständige Digitalisierung historischer Archive",
                "correct": True,
                "feedback": """✓ Richtig. Bei der Archivdigitalisierung ist es oft wichtig, keinen Teil des Textes zu verlieren, auch wenn nachträgliche Korrekturen erforderlich sind."""
            },
            {
                "answer": "Sicherheitskritische Finanztransaktionen",
                "correct": False,
                "feedback": """× Falsch. Bei Finanztransaktionen ist Präzision wichtiger als Vollständigkeit."""
            },
            {
                "answer": "Erstellung durchsuchbarer Textdatenbanken",
                "correct": True,
                "feedback": """✓ Richtig. Für durchsuchbare Datenbanken ist es wichtig, dass alle relevanten Informationen erfasst werden, damit sie bei Suchanfragen gefunden werden können."""
            }
        ]
    }
]

display_quiz(recall_applications, colors=colors.jupyterquiz)
```

## Frage 12

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

"""
Lernziel: 
    Sie können die Schritte zur Qualitätsmessung eines OCR-Outputs aufzählen und die Qualitätsmaße interpretieren.
Bloom-Stufe: Verstehen, Anwenden
Format: 
Geschätzte Zeit: 10 Minuten
    - Reihenfolge der Prozessschritte 
    - Bedeutung der Messergebnisse 
    - Praktische Interpretation
"""

import sys
sys.path.append("..")
from quadriga_config import colors

quality_sequence = [
    {
        "question": "In welcher Reihenfolge werden die folgenden Schritte zur Messung der OCR-Qualität durchgeführt?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "1. Berechnung der Qualitätsmetriken → 2. Erstellung der Ground Truth → 3. Durchführung der OCR",
                "correct": False,
                "feedback": """× Falsch. Die Qualitätsmetriken können erst berechnet werden, wenn sowohl der OCR-Output als auch die Ground Truth vorliegen, da sie auf dem Vergleich dieser beiden Texte basieren."""
            },
            {
                "answer": "1. Erstellung der Ground Truth → 2. Durchführung der OCR → 3. Berechnung der Qualitätsmetriken",
                "correct": False,
                "feedback": """× Falsch. Obwohl es möglich wäre, zuerst die Ground Truth zu erstellen und dann die OCR durchzuführen, ist dies in der Praxis ineffizient, da die manuelle Erstellung der Ground Truth oft auf dem OCR-Text aufbaut, der dann korrigiert wird."""
            },
            {
                "answer": "1. Durchführung der OCR → 2. Erstellung der Ground Truth → 3. Berechnung der Qualitätsmetriken",
                "correct": True,
                "feedback": """✓ Richtig! Dies ist die effizienteste und übliche Reihenfolge:
                * Zuerst wird die OCR auf dem Quelldokument durchgeführt, wobei die entsprechende OCR-Engine (hier: Tesseract) mit spezifischen Parametern (z.B. lang='frk' für Fraktur) verwendet wird. Dies erzeugt den OCR-Output, der für den Vergleich benötigt wird.
                * Dann wird die Ground Truth durch manuelle Korrektur erstellt. Dabei wird der OCR-Output als Grundlage genommen und manuell korrigiert, um einen fehlerfreien Referenztext zu erhalten.
                * Zuletzt werden die Qualitätsmetriken berechnet, indem der OCR-Output mit der Ground Truth verglichen wird. Dabei werden Maße wie Precision, Recall und F1-Score ermittelt, die eine quantitative Bewertung der OCR-Qualität ermöglichen."""
            },
            {
                "answer": "1. Durchführung der OCR → 2. Berechnung der Qualitätsmetriken → 3. Erstellung der Ground Truth",
                "correct": False,
                "feedback": """× Falsch. Die Qualitätsmetriken können erst nach Erstellung der Ground Truth berechnet werden, da für die Berechnung beide Texte (OCR-Output und Ground Truth) benötigt werden."""
            }
        ]
    }
]

display_quiz(quality_sequence, colors=colors.jupyterquiz, max_width=1000)
```


## Frage 13

Analysieren Sie die folgenden OCR-Qualitätswerte aus dem Beispiel:
- Precision: 0.778
- Recall: 0.7932
- F1-score: 0.7855

### Frage 13(a)
**Was bedeutet die Precision von 0.778 in diesem Kontext?**
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
**77.8% der vom OCR-System erkannten Zeichen sind korrekt.**

Begründung:
- Precision misst den Anteil korrekter Erkennungen
- Wert von 0.778 entspricht 77.8%
- Zeigt moderate bis gute Erkennungsgenauigkeit
- Typisch für historische Frakturschrift
````
### Frage 13(b)
**Warum ist der Recall (0.7932) höher als die Precision?**
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
**Das System erkennt mehr vorhandene Zeichen, macht dabei aber auch mehr Fehler.**

Begründung:
- Höherer Recall bedeutet bessere Vollständigkeit
- Kompromiss zwischen Genauigkeit und Vollständigkeit
- Typisches Muster bei historischen Dokumenten
- Balance durch F1-Score (0.7855) ersichtlich
````

## Frage 14
Bewerten Sie die Eignung der gemessenen OCR-Qualität für verschiedene Anwendungsfälle.

### Frage 14(a)
**Fall 1: Volltextsuche in digitalisierten Zeitungen**
```{code-cell} ipython3
:tags: [remove-input]
from IPython.display import HTML

HTML("""
<div padding: 15px; border-radius: 5px; margin: 10px 0;">
    <textarea id="answer" rows="4" style="width: 100%; margin-top: 10px; padding: 10px; border: 1px solid #ced4da; border-radius: 4px;" placeholder="Ihre Antwort"></textarea>
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
### Frage 14(b)
**Fall 2: Exakte Texttranskription für Edition**
```{code-cell} ipython3
:tags: [remove-input]
from IPython.display import HTML

HTML("""
<div padding: 15px; border-radius: 5px; margin: 10px 0;">
    <textarea id="answer" rows="4" style="width: 100%; margin-top: 10px; padding: 10px; border: 1px solid #ced4da; border-radius: 4px;" placeholder="Ihre Antwort"></textarea>
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