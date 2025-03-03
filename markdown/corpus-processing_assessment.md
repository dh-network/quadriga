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

**Geschätzte Zeit**: 30min

Viel Erfolg!
````

## Frage 1


```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice_1 = [{
    "question": """Welche Aussagen über Natural Language Processing (NLP) sind korrekt?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "NLP dient dazu, Texte mit linguistischen Informationen anzureichern.",
            "correct": True,
            "feedback": """✓ Richtig! Der Text erklärt:
            - Computer sieht Text zunächst nur als Zeichenliste
            - NLP fügt semantische Struktur hinzu
            - Ermöglicht Analyse auf Wortebene
            - Grundlage für weitere Textanalysen"""
        },
        {
            "answer": "Tokenisierung und Lemmatisierung sind die einzigen NLP-Methoden.",
            "correct": False,
            "feedback": """× Nicht korrekt. Laut Text:
            - NLP umfasst verschiedene Methoden
            - Auch Sentiment Analysis möglich
            - Chatbot-Entwicklung gehört dazu
            - Tokenisierung/Lemmatisierung sind Grundlagen"""
        }
    ]
}]

display_quiz(multiple_choice_1, colors=colors.jupyterquiz)
```

## Frage 2

Analysieren Sie die Verarbeitung des folgenden Satzes:

Original: "Die Krankenhäuser waren überfüllt."

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice_2a = [{
    "question": """Welche Reihenfolge ist für die linguistische Verarbeitung des Beispielsatzes korrekt?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "1. Tokenisierung → 2. Lemmatisierung",
            "correct": True,
            "feedback": """✓ Richtig! Die korrekte Reihenfolge:
            - Erst Zerlegung in Token
            - Dann Analyse der Grundformen
            - Entspricht NLP-Pipeline
            - Logische Verarbeitungsfolge"""
        },
        {
            "answer": "1. Lemmatisierung → 2. Tokenisierung",
            "correct": False,
            "feedback": """× Nicht korrekt. Lemmatisierung benötigt bereits tokenisierten Text als Grundlage."""
        }
    ]
}]

display_quiz(multiple_choice_2a, colors=colors.jupyterquiz)
```

### Frage 2(b)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

method_example_q1 = [{
    "question": "Was geschieht bei der Tokenisierung des Satzes?",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Der Satz wird in einzelne Wörter und Satzzeichen zerlegt",
            "correct": True,
            "feedback": """✓ Richtig! Die Tokenisierung:
            - Teilt Text in einzelne Wörter
            - Behandelt Satzzeichen als eigene Token
            - Grundlage für weitere Verarbeitung"""
        },
        {
            "answer": "Der Satz wird auf Grundformen zurückgeführt",
            "correct": False,
            "feedback": """× Nicht korrekt. Dies wäre die Aufgabe der Lemmatisierung, nicht der Tokenisierung."""
        },
        {
            "answer": "Der Satz wird direkt analysiert, ohne ihn zu zerlegen",
            "correct": False,
            "feedback": """× Nicht korrekt. Tokenisierung ist ein grundlegender erster Schritt der Textverarbeitung."""
        }
    ]
}]

display_quiz(method_example_q1, colors=colors.jupyterquiz)
```

### Frage 2(c)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

method_example_q2 = [{
    "question": "Was geschieht bei der Lemmatisierung des Satzes?",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Wörter werden auf ihre Grundform zurückgeführt",
            "correct": True,
            "feedback": """✓ Richtig! Die Lemmatisierung:
            - Führt Wörter auf Grundform zurück
            - Vereinheitlicht verschiedene Formen
            - Ermöglicht bessere Häufigkeitsanalyse"""
        },
        {
            "answer": "Der Satz wird in einzelne Token zerlegt",
            "correct": False,
            "feedback": """× Nicht korrekt. Tokenisierung ist ein anderer Schritt der Textverarbeitung."""
        },
        {
            "answer": "Alle Wörter werden groß geschrieben",
            "correct": False,
            "feedback": """× Nicht korrekt. Lemmatisierung bezieht sich auf die grammatikalische Grundform."""
        }
    ]
}]

display_quiz(method_example_q2, colors=colors.jupyterquiz)
```

## Frage 3

(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

tool_understanding_q1 = [{
    "question": "Welche Aussagen treffen auf spaCy zu?",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Schnelle Verarbeitung großer Korpora",
            "correct": True,
            "feedback": """✓ Richtig! Vorteile von spaCy:
            - Effizient für große Korpora
            - Integrierte Visualisierung
            - Geeignet für Standardfälle"""
        },
        {
            "answer": "Komplexe manuelle Konfiguration erforderlich",
            "correct": False,
            "feedback": """× Nicht korrekt. spaCy ist bekannt für seine Benutzerfreundlichkeit und einfache Konfiguration."""
        },
        {
            "answer": "Vollständige integrierte Verarbeitungspipeline",
            "correct": True,
            "feedback": """✓ Richtig! spaCy bietet eine komplette Verarbeitungspipeline mit verschiedenen linguistischen Komponenten."""
        },
        {
            "answer": "Sehr hohe Einstiegshürde",
            "correct": False,
            "feedback": """× Nicht korrekt. spaCy ist für Anfänger relativ leicht zu erlernen."""
        }
    ]
}]

display_quiz(tool_understanding_q1, colors=colors.jupyterquiz)
```
## Frage 4
(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

tool_understanding_q2 = [{
    "question": "Welche Aussagen treffen auf NLTK zu?",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Sehr flexible Anpassungsmöglichkeiten",
            "correct": True,
            "feedback": """✓ Richtig! Eigenschaften von NLTK:
            - Gut für spezielle Anforderungen
            - Detaillierte Kontrolle möglich
            - Längere Verarbeitungszeit"""
        },
        {
            "answer": "Standardmäßig sehr schnelle Verarbeitung",
            "correct": False,
            "feedback": """× Nicht korrekt. NLTK ist im Vergleich zu spaCy eher langsam."""
        },
        {
            "answer": "Transparente Verarbeitungsschritte",
            "correct": True,
            "feedback": """✓ Richtig! NLTK ermöglicht eine sehr detaillierte Einsicht in die Textverarbeitungsschritte."""
        },
        {
            "answer": "Sehr einfache Bedienung für Anfänger",
            "correct": False,
            "feedback": """× Nicht korrekt. NLTK hat eine relativ hohe Einstiegshürde."""
        }
    ]
}]

display_quiz(tool_understanding_q2, colors=colors.jupyterquiz)
```

## Frage 5

Bringen Sie die Schritte der Textannotation in die richtige Reihenfolge:

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

process_steps_q1 = [{
    "question": "In welcher Reihenfolge werden die Schritte der Textannotation mit spaCy durchgeführt?",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "1. Laden des Sprachmodells → 2. Einlesen des Textes → 3. Durchführung der Annotation",
            "correct": False,
            "feedback": """× Falsch"""
        },
        {
            "answer": "1. Laden des Sprachmodells → 2. Durchführung der Annotation → 3. Einlesen des Textes ",
            "correct": False,
            "feedback": """× Falsch"""
        },
        {
            "answer": "1. Einlesen des Textes → 2. Laden des Sprachmodells → 3. Durchführung der Annotation",
            "correct": True,
            "feedback": """✓ Richtig! Dies ist die korrekte Reihenfolge:
            1. Einlesen des Textes:
               - Text muss verfügbar sein
               - Basis für weitere Verarbeitung
               - Dateiformat wird geprüft
            2. Laden des Sprachmodells:
               - Sprachspezifisches Modell notwendig
               - Auswahl der Modelleigenschaften
               - Festlegung der Analysekomponenten
            3. Durchführung der Annotation:
               - Verarbeitung mit geladenem Modell
               - Extraktion von Token und Lemmata
               - Speicherung der Ergebnisse"""
        },
        {
            "answer": "1. Durchführung der Annotation → 2. Einlesen des Textes → 3. Laden des Sprachmodells",
            "correct": False,
            "feedback": """× Falsch"""
        }
    ]
}]

display_quiz(process_steps_q1, colors=colors.jupyterquiz, max_width = 1000)
```

## Frage 6

(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

tokenization_q1 = [{
    "question": "Welche Unterschiede bestehen zwischen einfacher Worttrennung (split()) und spaCy-Tokenisierung?",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "spaCy behandelt Satzzeichen separat",
            "correct": True,
            "feedback": """✓ Richtig! Dieser Unterschied ist wichtig weil:
            - Bessere Wortidentifikation
            - Genauere Häufigkeitszählung
            - Korrekte linguistische Analyse
            - Vorbereitung für weitere NLP-Schritte"""
        },
        {
            "answer": "Die einfache Worttrennung produziert genau die gleiche Anzahl von Token",
            "correct": False,
            "feedback": """× Nicht korrekt. Es gibt signifikante Unterschiede in der Tokenanzahl."""
        },
        {
            "answer": "spaCy-Tokenisierung führt zu mehr Token als einfache Worttrennung",
            "correct": True,
            "feedback": """✓ Richtig! Der Unterschied zeigt:
            - Genauere Textaufbereitung durch spaCy
            - Erfassung aller Textbestandteile
            - Bedeutung professioneller NLP-Tools
            - Auswirkung auf Analyseergebnisse"""
        },
        {
            "answer": "Die Worttrennung ist immer präziser als spaCy-Tokenisierung",
            "correct": False,
            "feedback": """× Nicht korrekt. spaCy bietet eine deutlich sophistiziertere Tokenisierung."""
        }
    ]
}]

display_quiz(tokenization_q1, colors=colors.jupyterquiz)
```

## Frage 7

Analysieren Sie die folgenden Aussagen zur praktischen Implementierung der Annotation.

### Frage 7(a)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

implementation_q1 = [{
    "question": "Die Deaktivierung nicht benötigter Analysekomponenten erhöht die Verarbeitungsgeschwindigkeit.",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Ja",
            "correct": True,
            "feedback": """✓ Richtig"""
        },
        {
            "answer": "Nein",
            "correct": False,
            "feedback": """✓ Richtig! Wichtig weil:
            - Fokus auf relevante Komponenten
            - Effizientere Verarbeitung
            - Sinnvoll für große Korpora
            - Ressourcenoptimierung"""
        }   
    ]
}]

display_quiz(implementation_q1, colors=colors.jupyterquiz)
```

### Frage 7(b)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

implementation_q2 = [{
    "question": "Das Ergebnis der Annotation sollte immer als TXT-Datei gespeichert werden",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Nein",
            "correct": True,
            "feedback": """✓ Richtig"""
        },
        {
            "answer": "Ja",
            "correct": False,
            "feedback": """× Nicht korrekt. Der Text erklärt:
            - CSV ist das Standardformat
            - Tabellarische Struktur wichtig
            - Token und Lemmata als Spalten
            - Bessere Weiterverarbeitung möglich"""
        }
    ]
}]

display_quiz(implementation_q2, colors=colors.jupyterquiz)
```