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

**Geschätzte Zeit**: 45min

Viel Erfolg!
````

## Frage 1

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

"""
Lernziel: Sie können die Grundkonzepte des Natural Language Processing erklären und die Funktionen von Tokenisierung und Lemmatisierung für die Textanalyse beschreiben.
Bloom-Stufe: Verstehen
Format: Multiple Choice
"""


import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice_1 = [{
    "question": """Welche der folgenden Aussagen beschreibt korrekt, was NLP im Kontext der Textanalyse leistet?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "NLP dient ausschließlich der automatischen Übersetzung zwischen Sprachen",
            "correct": False,
            "feedback": """× Nicht korrekt. Obwohl maschinelle Übersetzung ein Anwendungsgebiet von NLP ist, umfasst NLP viel mehr, insbesondere die Anreicherung von Texten mit linguistischen Informationen für verschiedene Analysezwecke. NLP beinhaltet Methoden wie Tokenisierung, Lemmatisierung und viele weitere Techniken zur Textverarbeitung."""
        },
        {
            "answer": "NLP ermöglicht die Anreicherung von Texten mit linguistischen Informationen, die für Computer sonst nicht erkennbar wären",
            "correct": True,
            "feedback": """✓ Richtig! NLP (Natural Language Processing) ermöglicht es, Texte mit linguistischen Informationen anzureichern und damit für Computer "verständlich" zu machen. Computer sehen Text zunächst nur als Zeichenkette, während NLP-Methoden semantische Strukturen hinzufügen und Analysen auf Wortebene ermöglichen."""
        },
        {
            "answer": "NLP ist ein Verfahren zur manuellen Annotation von Texten durch Sprachwissenschaftler",
            "correct": False,
            "feedback": """× Nicht korrekt. NLP bezieht sich auf automatisierte Verfahren zur Textverarbeitung durch Computer, nicht auf manuelle Annotation. Während manuelle Annotation durchaus für Training und Evaluation von NLP-Systemen wichtig sein kann, ist NLP selbst ein computergestützter Prozess."""
        },
        {
            "answer": "NLP kann nur auf modernen Texten angewendet werden, nicht auf historischen Dokumenten",
            "correct": False,
            "feedback": """× Nicht korrekt. NLP kann grundsätzlich auf Texte jeder Epoche angewendet werden, auch wenn historische Texte aufgrund von Sprachveränderungen, anderen Schriften oder OCR-Qualität besondere Herausforderungen darstellen können. Gerade in den Digital Humanities wird NLP häufig für historische Textanalyse eingesetzt."""
        }
    ]
}]

display_quiz(multiple_choice_1, colors=colors.jupyterquiz)
```

## Frage 2

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice_2 = [{
    "question": """Welche Funktion erfüllt die Tokenisierung im NLP-Prozess?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Sie übersetzt den Text in eine andere Sprache",
            "correct": False,
            "feedback": """× Nicht korrekt. Die Übersetzung ist eine komplexe NLP-Aufgabe, die weit über die Tokenisierung hinausgeht. Tokenisierung ist ein grundlegender Vorverarbeitungsschritt, der Texte in kleinere Einheiten zerlegt, aber keine Übersetzung vornimmt."""
        },
        {
            "answer": "Sie identifiziert die Stimmung (positiv/negativ) eines Textes",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage beschreibt nicht die Tokenisierung, sondern die Sentimentanalyse, die eine fortgeschrittene NLP-Aufgabe ist. Tokenisierung ist ein Vorverarbeitungsschritt, der für die Sentimentanalyse notwendig sein kann, aber selbst keine emotionale Bewertung vornimmt."""
        },
        {
            "answer": "Sie zerlegt einen Text in einzelne, sinnvolle Einheiten wie Wörter und Satzzeichen",
            "correct": True,
            "feedback": """✓ Richtig! Die Tokenisierung ist der Prozess der Zerlegung eines Textes in einzelne, bedeutungstragende Einheiten (Token). Diese können Wörter, Zahlen oder Satzzeichen sein. Sie ist der erste grundlegende Schritt in der NLP-Pipeline, auf dem weitere Verarbeitungsschritte aufbauen."""
        },
        {
            "answer": "Sie wandelt alle Wörter in ihre Grundform um",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage beschreibt nicht die Tokenisierung, sondern die Lemmatisierung. Die Tokenisierung zerlegt Text in einzelne Einheiten, während die Lemmatisierung in einem späteren Schritt diese Einheiten auf ihre Grundform zurückführt."""
        }
    ]
}]

display_quiz(multiple_choice_2, colors=colors.jupyterquiz)
```

## Frage 3

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice_3 = [{
    "question": """Was ist das Hauptziel der Lemmatisierung in der NLP-Pipeline?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Die Bestimmung der grammatikalischen Funktion eines Wortes im Satz",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage beschreibt nicht die Lemmatisierung, sondern das Part-of-Speech Tagging (POS-Tagging). Die Lemmatisierung befasst sich mit der Reduktion von Wortformen auf ihre Grundform, nicht mit der grammatikalischen Funktionsanalyse."""
        },
        {
            "answer": "Die Zurückführung verschiedener Wortformen auf ihre gemeinsame Grundform",
            "correct": True,
            "feedback": """✓ Richtig! Die Lemmatisierung führt verschiedene Formen eines Wortes auf ihre gemeinsame Grundform (Lemma) zurück. Beispielsweise werden "gehe", "gehst", "geht", "ging" auf "gehen" zurückgeführt. Dies vereinfacht die Textanalyse, da verschiedene Formen desselben Wortes als eine Einheit betrachtet werden können."""
        },
        {
            "answer": "Die Erkennung von Eigennamen und geographischen Bezeichnungen",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage beschreibt nicht die Lemmatisierung, sondern die Named Entity Recognition (NER). Die Lemmatisierung hat nicht das Ziel, bestimmte semantische Kategorien von Wörtern zu identifizieren, sondern Wortformen zu vereinheitlichen."""
        },
        {
            "answer": "Die Zerlegung von Komposita in ihre Bestandteile",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage beschreibt nicht die primäre Funktion der Lemmatisierung. Die Zerlegung von Komposita (zusammengesetzten Wörtern) ist eine separate NLP-Aufgabe, die als Compound Splitting bezeichnet wird. Die Lemmatisierung befasst sich mit der Reduktion von flektierten Formen auf ihre Grundform."""
        }
    ]
}]

display_quiz(multiple_choice_3, colors=colors.jupyterquiz)
```

## Frage 4

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice_4 = [{
    "question": """Warum ist die Kombination von Tokenisierung und Lemmatisierung für die quantitative Textanalyse besonders wertvoll?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Sie ermöglicht die automatische Übersetzung des Textes",
            "correct": False,
            "feedback": """× Nicht korrekt. Obwohl Tokenisierung und Lemmatisierung grundlegende Schritte in der Übersetzungspipeline sein können, reichen sie allein nicht aus, um eine automatische Übersetzung zu ermöglichen. Dafür sind komplexere Modelle notwendig."""
        },
        {
            "answer": "Sie verbessert die Lesbarkeit des Textes für Menschen",
            "correct": False,
            "feedback": """× Nicht korrekt. Tokenisierung und Lemmatisierung sind in erster Linie für die maschinelle Verarbeitung gedacht, nicht für die menschliche Lesbarkeit. Im Gegenteil, ein lemmatisierter Text kann für Menschen sogar schwerer zu lesen sein, da er nicht mehr den gewohnten grammatikalischen Formen entspricht."""
        },
        {
            "answer": "Sie ermöglicht präzisere Häufigkeitsanalysen durch Normalisierung verschiedener Wortformen",
            "correct": True,
            "feedback": """✓ Richtig! Die Kombination von Tokenisierung und Lemmatisierung ist für quantitative Textanalysen besonders wertvoll, weil sie die Varianz der Wortformen reduziert. Dadurch können Häufigkeitsanalysen präziser durchgeführt werden, da verschiedene Formen desselben Wortes nicht mehr als verschiedene Wörter gezählt werden."""
        },
        {
            "answer": "Sie korrigiert Rechtschreibfehler im Originaltext",
            "correct": False,
            "feedback": """× Nicht korrekt. Weder Tokenisierung noch Lemmatisierung sind primär darauf ausgerichtet, Rechtschreibfehler zu korrigieren. Rechtschreibkorrektur ist eine separate NLP-Aufgabe, die vor der Tokenisierung und Lemmatisierung durchgeführt werden sollte."""
        }
    ]
}]

display_quiz(multiple_choice_4, colors=colors.jupyterquiz)
```

## Frage 5

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice_5 = [{
    "question": """Welcher Unterschied besteht zwischen dem ursprünglichen Text und dem mit NLP-Methoden verarbeiteten Text?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Der verarbeitete Text enthält keine Satzzeichen mehr",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage ist nicht allgemein zutreffend. Ob Satzzeichen im verarbeiteten Text erhalten bleiben, hängt von den spezifischen NLP-Methoden und deren Konfiguration ab. In vielen NLP-Pipelines werden Satzzeichen als eigene Token behandelt und bleiben somit erhalten."""
        },
        {
            "answer": "Der verarbeitete Text ist in eine andere Sprache übersetzt",
            "correct": False,
            "feedback": """× Nicht korrekt. NLP-Methoden umfassen viele verschiedene Verarbeitungsschritte, von denen Übersetzung nur einer ist. Die meisten grundlegenden NLP-Verarbeitungsschritte wie Tokenisierung und Lemmatisierung verändern die Sprache des Textes nicht."""
        },
        {
            "answer": "Der verarbeitete Text ist mit zusätzlichen linguistischen Informationen angereichert",
            "correct": True,
            "feedback": """✓ Richtig! Der wesentliche Unterschied besteht darin, dass der mit NLP-Methoden verarbeitete Text mit zusätzlichen linguistischen Informationen angereichert ist. Dies können Informationen über Wortarten, Grundformen, syntaktische Beziehungen oder semantische Bedeutungen sein. Der Computer kann dadurch auf verschiedenen linguistischen Ebenen mit dem Text arbeiten."""
        },
        {
            "answer": "Der verarbeitete Text ist kürzer als der Originaltext",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage ist nicht allgemein zutreffend. Die Länge des verarbeiteten Textes hängt von den angewendeten NLP-Methoden ab. Bei manchen Methoden (wie z.B. Zusammenfassung) kann der Text kürzer werden, bei anderen (wie z.B. Annotation) kann er durch zusätzliche Informationen sogar länger werden."""
        }
    ]
}]

display_quiz(multiple_choice_5, colors=colors.jupyterquiz)
```

## Frage 6

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice_6 = [{
    "question": """Was unterscheidet die Lemmatisierung von der einfacheren Methode des Stemmings?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Stemming wird nur für englische Texte verwendet, Lemmatisierung für alle Sprachen",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage ist nicht korrekt. Sowohl Stemming als auch Lemmatisierung können grundsätzlich auf verschiedene Sprachen angewendet werden, wobei es für beide Methoden sprachspezifische Implementierungen gibt. Der Unterschied liegt nicht in der Sprachunterstützung."""
        },
        {
            "answer": "Lemmatisierung berücksichtigt den linguistischen Kontext und erzeugt echte Wörter, Stemming kürzt Wörter oft nur mechanisch",
            "correct": True,
            "feedback": """✓ Richtig! Die Lemmatisierung unterscheidet sich vom Stemming dadurch, dass sie den linguistischen Kontext berücksichtigt und Wörter auf ihre tatsächliche Grundform (Lemma) zurückführt. Stemming wendet dagegen oft nur mechanische Regeln an, um Wortendungen zu entfernen, was zu nicht-existierenden "Wortstämmen" führen kann. Lemmatisierung ist linguistisch präziser, aber auch rechenintensiver."""
        },
        {
            "answer": "Lemmatisierung kann nur auf moderne Texte angewendet werden, Stemming auch auf historische",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage ist nicht korrekt. Sowohl Lemmatisierung als auch Stemming können grundsätzlich auf Texte jeder Epoche angewendet werden. Die Herausforderungen bei historischen Texten (wie Sprachveränderungen) betreffen beide Methoden, wobei kontextsensitive Lemmatisierung bei historischen Texten sogar Vorteile haben kann."""
        },
        {
            "answer": "Stemming ist genauer, aber rechenintensiver als Lemmatisierung",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage ist nicht korrekt. Tatsächlich verhält es sich umgekehrt: Lemmatisierung ist in der Regel genauer, aber rechenintensiver als Stemming. Stemming ist eine einfachere, regelbasierte Methode, die schneller arbeitet, aber oft weniger präzise Ergebnisse liefert."""
        }
    ]
}]

display_quiz(multiple_choice_6, colors=colors.jupyterquiz)
```

## Frage 7
Analysieren Sie den folgenden Satz mit NLP-Methoden und beschreiben Sie die Ergebnisse:

Originaltext: "Die Forscher untersuchten verschiedene Zeitungsartikel zur Spanischen Grippe."

1.	Führen Sie eine Tokenisierung durch.
2.	Bestimmen Sie die Lemmata der einzelnen Token.
3.	Reflektieren Sie, wie diese Verarbeitung eine quantitative Analyse unterstützen würde.


```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga_config")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('process-1')
```

````{admonition} Lösung
:class: solution, dropdown

**Beispiellösung zur Selbstbewertung:**
1.	Tokenisierung: ["Die", "Forscher", "untersuchten", "verschiedene", "Zeitungsartikel", "zur", "Spanischen", "Grippe", "."]
2.	Lemmatisierung: ["die", "Forscher", "untersuchen", "verschieden", "Zeitungsartikel", "zu", "spanisch", "Grippe", "."]

**Reflexion:**
- Die Tokenisierung ermöglicht die Analyse auf Wortebene und bereitet den Text für weitere Verarbeitung vor
- Die Lemmatisierung würde alle Formen von "untersuchen" zusammenfassen, was bei einer Frequenzanalyse hilfreich ist
- Durch die Lemmatisierung werden verschiedene Flexionsformen (wie "Spanischen" zu "spanisch") vereinheitlicht
- Bei einer größeren Textsammlung würden verschiedene grammatikalische Formen desselben Wortes nicht als unterschiedliche Begriffe gezählt
- Diese Normalisierung verbessert die Qualität von Häufigkeitsanalysen, Keyword-Extraktion und thematischen Analysen
- Die Informationen über die ursprüngliche Form bleiben erhalten und können für detailliertere linguistische Analysen genutzt werden

**Bewertungskriterien für die Selbsteinschätzung:**
- Korrekte Tokenisierung mit Berücksichtigung von Satzzeichen als eigene Token
- Korrekte Bestimmung der Grundformen bei der Lemmatisierung
- Verständnis des Nutzens für quantitative Textanalyse, insbesondere für Häufigkeitsanalysen
- Reflexion über die Vor- und Nachteile der Methoden für die spezifische Forschungsfrage

````



## Frage 8
(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

"""
Lernziel: Sie können die notwendigen Schritte zur automatischen Annotation eines Texts aufzählen und Vorteile der Tokenisierung gegenüber einfacheren Methoden der Worttrennung nennen.
Bloom-Stufe: Verstehen
Format: Multiple Choice
"""

import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice_1 = [{
    "question": """Welche Schritte gehören zur automatischen Annotation eines Textes mit spaCy?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Einlesen des Textes",
            "correct": True,
            "feedback": """✓ Richtig! Der erste Schritt im Notebook ist das Einlesen des Textes mit text_path.read_text(), nachdem der Pfad zur Datei definiert wurde (text_path = Path("../data/txt/SNP2719372X-19181015-0-0-0-0.txt"))."""
        },
        {
            "answer": "Laden des sprachspezifischen Modells",
            "correct": True,
            "feedback": """✓ Richtig! Im Notebook wird das deutsche Sprachmodell mit nlp = spacy.load('de_core_news_sm') geladen, welches für die Verarbeitung deutscher Texte optimiert ist."""
        },
        {
            "answer": "Auswahl der relevanten Analysekomponenten",
            "correct": True,
            "feedback": """✓ Richtig! Im Notebook werden nicht benötigte Komponenten deaktiviert: disable_components = ['ner', 'morphologizer', 'attribute_ruler', 'sentencizer'], um die Verarbeitungsgeschwindigkeit zu erhöhen."""
        },
        {
            "answer": "Manuelle Korrektur der Tokenisierungsfehler",
            "correct": False,
            "feedback": """× Nicht korrekt. Die Annotation mit spaCy erfolgt vollautomatisch. Im Notebook gibt es keinen Schritt zur manuellen Korrektur von Tokenisierungsfehlern."""
        },
        {
            "answer": "Speichern der Ergebnisse in einem strukturierten Format",
            "correct": True,
            "feedback": """✓ Richtig! Im letzten Schritt werden die Ergebnisse als CSV-Datei gespeichert: text_annotated_df.to_csv(output_path, index=False). Das Notebook erwähnt, dass CSV das Standardformat ist, um tabellarische Daten im Klartext zu speichern."""
        }
    ]
}]

display_quiz(multiple_choice_1, colors=colors.jupyterquiz)
```

## Frage 9
(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice_2 = [{
    "question": """Welche Vorteile bietet die Tokenisierung mit spaCy gegenüber einer einfachen Worttrennung mittels split()?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Satzzeichen werden als eigene Token erkannt",
            "correct": True,
            "feedback": """✓ Richtig! Das Notebook zeigt im Beispiel words[100:120], dass bei der einfachen Teilung mit split() Satzzeichen an Wörtern hängen bleiben (z.B. "Entfernung,", "anzugreisen."), während spaCy sie als separate Token erkennt."""
        },
        {
            "answer": "Die Gesamtanzahl der Token ist akkurater",
            "correct": True,
            "feedback": """✓ Richtig! Im Notebook wird explizit darauf hingewiesen: "Wie zu sehen ist, hat diese Art der 'falschen' Tokenisierung den Nachteil, dass Satzzeichen nicht von Wörtern abgetrennt werden. Die Wortanzahl ist dementsprechend auch nicht akkurat." Der Vergleich zeigt 11.612 Wörter mit split() gegenüber 15.062 Token mit spaCy."""
        },
        {
            "answer": "Die Tokenisierung mit spaCy ist immer schneller",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage wird nicht durch das Notebook unterstützt. Im Gegenteil, das Notebook zeigt, dass die spaCy-Annotation 1,47 Sekunden dauert, und für größere Textmengen werden sogar Optimierungen vorgeschlagen, indem nicht benötigte Komponenten deaktiviert werden."""
        },
        {
            "answer": "Sie ermöglicht die Lemmatisierung der Tokens",
            "correct": True,
            "feedback": """✓ Richtig! Das Notebook demonstriert, wie spaCy nicht nur tokenisiert, sondern auch lemmatisiert: "Um flektierte Wörter aufeinander abbildbar zu machen (Lemmatisierung), wird der Text im folgenden durch die Bibliothek spaCy annotiert." """
        },
        {
            "answer": "Sie korrigiert automatisch OCR-Fehler im Text",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage wird nicht durch das Notebook unterstützt. spaCy führt keine automatische Korrektur von OCR-Fehlern durch. Die Qualität der Annotation hängt von der Qualität des Eingabetextes ab."""
        }
    ]
}]

display_quiz(multiple_choice_2, colors=colors.jupyterquiz)
```

## Frage 10

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice_3 = [{
    "question": """Warum werden im Beispiel bestimmte Analysekomponenten von spaCy deaktiviert?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Um die Genauigkeit der Tokenisierung zu erhöhen",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage wird nicht durch das Notebook unterstützt. Das Deaktivieren von Komponenten dient nicht der Verbesserung der Genauigkeit."""
        },
        {
            "answer": "Um die Verarbeitungsgeschwindigkeit zu erhöhen",
            "correct": True,
            "feedback": """✓ Richtig! Im Notebook steht explizit: "Es werden einige Analysekomponent wie z. B. das Aufteilen des Texts in Sätze (sentencizer) oder die Named Entity Recognition (ner) ausgeschlossen, da diese für die Tokenisierung und die Lemmatisierung nicht benötigt werden. Der Auschluss der Komponentnen erhöht die Annotationsgeschwindikgeit." """
        },
        {
            "answer": "Um mehr Speicherplatz für die Ergebnisse zu haben",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage wird nicht durch das Notebook unterstützt. Der Speicherplatz für die Ergebnisse wird nicht als Grund für die Deaktivierung von Komponenten genannt."""
        },
        {
            "answer": "Um Kompatibilitätsprobleme mit dem CSV-Format zu vermeiden",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage wird nicht durch das Notebook unterstützt. Es gibt keinen Hinweis darauf, dass die Deaktivierung von Komponenten mit dem CSV-Format zusammenhängt."""
        }
    ]
}]

display_quiz(multiple_choice_3, colors=colors.jupyterquiz)
```

## Frage 11

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice_4 = [{
    "question": """Welches Dateiformat wird im Beispiel für die Speicherung der annotierten Texte verwendet und warum?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "TXT, weil es am wenigsten Speicherplatz benötigt",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage ist nicht korrekt. Laut Notebook werden die annotierten Texte nicht als TXT-Dateien gespeichert."""
        },
        {
            "answer": "CSV, weil es gut für die Speicherung tabellarischer Daten geeignet ist",
            "correct": True,
            "feedback": """✓ Richtig! Im Notebook steht explizit: "CSV (comma-separated value) ist das Standardformat um tabellarische Daten im Klartext zu speichern." Außerdem wird erwähnt: "Das Tabellenformat wurde gewählt, da sich darin gut relationale Daten speichern lassen." """
        },
        {
            "answer": "JSON, weil es die hierarchische Struktur der Annotation am besten abbildet",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage ist nicht korrekt. Im Notebook wird JSON nicht als Speicherformat erwähnt."""
        },
        {
            "answer": "XML, weil es von den meisten Textanalysewerkzeugen unterstützt wird",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage ist nicht korrekt. Im Notebook wird XML nicht als Speicherformat erwähnt."""
        }
    ]
}]

display_quiz(multiple_choice_4, colors=colors.jupyterquiz)
```

## Frage 12

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice_5 = [{
    "question": """Was zeigt der Vergleich der Textlänge vor und nach der Tokenisierung mit spaCy im Beispiel?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Der tokenisierte Text ist kürzer, weil Stoppwörter entfernt wurden",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage ist nicht korrekt. Im Notebook gibt es keinen Hinweis darauf, dass Stoppwörter entfernt wurden. Im Gegenteil, die Tokenzahl erhöht sich."""
        },
        {
            "answer": "Der tokenisierte Text enthält mehr Elemente, weil Satzzeichen als eigene Token erkannt werden",
            "correct": True,
            "feedback": """✓ Richtig! Das Notebook zeigt: "Durch die Tokenisierung wurden z. B. Satzzeichen von Wörtern abgetrennt. An der Textlänge lässt sich dies schon erkennen." Die Anzahl steigt von 11.612 auf 15.062 Token."""
        },
        {
            "answer": "Der tokenisierte Text ist unverändert in seiner Länge, nur die Qualität der Tokens ist verbessert",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage widerspricht dem im Notebook gezeigten Unterschied in der Tokenanzahl (11.612 vs. 15.062)."""
        },
        {
            "answer": "Der tokenisierte Text ist kürzer, weil zusammengehörige Mehrwortausdrücke als ein Token erkannt werden",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage widerspricht dem im Notebook gezeigten Anstieg der Tokenanzahl."""
        }
    ]
}]

display_quiz(multiple_choice_5, colors=colors.jupyterquiz)
```

## Frage 13
Ordnen Sie die Schritte in die richtige Reihenfolge, um einen Text mit spaCy zu annotieren:

1. Speichern der Annotation als CSV-Datei
2. Auswahl der Analysekomponenten
3. Laden des Sprachmodells
4. Einlesen des Textes
5. Durchführung der Annotation mit nlp(text)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice_6 = [{
    "question": """Welche Reihenfolge der Verarbeitungsschritte ist korrekt für die Textannotation mit spaCy?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "3 → 2 → 4 → 5 → 1",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Reihenfolge ist nicht korrekt. Laut Notebook wird zuerst der Text eingelesen (Schritt 1), bevor weitere Verarbeitungsschritte folgen."""
        },
        {
            "answer": "3 → 4 → 2 → 5 → 1",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Reihenfolge stimmt nicht mit dem Ablauf im Notebook überein, wo zuerst der Text eingelesen wird."""
        },
        {
            "answer": "4 → 3 → 2 → 5 → 1",
            "correct": True,
            "feedback": """✓ Richtig! Die Reihenfolge im Notebook ist: 1. Einlesen des Texts, 2. Laden des Sprachmodells, 3. Auswahl der Analysekomponenten, 4. Durchführung der Annotation, 5. Speichern der Ergebnisse."""
        },
        {
            "answer": "4 → 5 → 3 → 2 → 1",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Reihenfolge ist nicht korrekt. Das Sprachmodell muss vor der Annotation geladen werden, wie im Notebook gezeigt."""
        }
    ]
}]

display_quiz(multiple_choice_6, colors=colors.jupyterquiz)
```
