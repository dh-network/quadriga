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

## Theoretische Grundlagen

### Assessment 2.1: Korpora als Forschungsobjekte

#### Frage 1: Merkmale von Korpora

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

"""
Lernziel: 
    Sie können Korpora als geisteswissenschaftliche Forschungsobjekte definieren und ihre wesentlichen Merkmale beschreiben.
Bloom-Stufe: Verstehen
Format: Multiple Choice + Zuordnungsaufgabe
Geschätzte Zeit: 5 Minuten
Schwerpunkte:
    - Verständnis der Korpus-Grundprinzipien
    - Unterscheidung von Korpustypen
    - Bewertung von Korpusqualität
"""


question1 = [
    {
        "question": "Welche der folgenden Aussagen beschreiben korrekt die wesentlichen Merkmale eines Korpus in den Digital Humanities? Wählen Sie alle zutreffenden Aussagen.",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Eine Sammlung von maschinenlesbaren Textdokumenten",
                "correct": True,
                "feedback": """✓ Korrekt! Die Maschinenlesbarkeit ist ein zentrales Merkmal von DH-Korpora, da sie die computergestützte Analyse ermöglicht. Dies unterscheidet DH-Korpora von traditionellen Textsammlungen und ist Voraussetzung für quantitative Analysen."""
            },
            {
                "answer": "Eine nach bestimmten Kriterien zusammengestellte Textsammlung",
                "correct": True,
                "feedback": """✓ Korrekt! Die kriteriengeleitete Zusammenstellung ist essentiell für wissenschaftliche Korpora. Die Kriterien müssen dabei:
                - transparent dokumentiert sein
                - zur Forschungsfrage passen
                - systematisch angewendet werden"""
            },
            {
                "answer": "Eine Sammlung, die nur digitalisierte Bücher enthält",
                "correct": False,
                "feedback": """× Nicht korrekt. Korpora können verschiedene Arten von Texten enthalten:
                - Zeitungsartikel (wie in unserer Fallstudie)
                - Literarische Texte
                - Dokumente
                - Andere Textformen
                Die Art der Texte wird durch die Forschungsfrage bestimmt, nicht durch das Format."""
            },
            {
                "answer": "Eine Textsammlung, die spezifischen Forschungszwecken dient",
                "correct": True,
                "feedback": """✓ Korrekt! Die Zweckgebundenheit ist ein wichtiges Merkmal:
                - Das Korpus wird für bestimmte Forschungsfragen zusammengestellt
                - Die Forschungszwecke bestimmen die Auswahlkriterien
                - Die Zweckbindung beeinflusst auch die Art der Aufbereitung der Texte"""
            },
            {
                "answer": "Eine beliebige Sammlung von digitalisierten Texten",
                "correct": False,
                "feedback": """× Nicht korrekt. Eine beliebige Sammlung erfüllt nicht die wissenschaftlichen Anforderungen an ein Korpus:
                - Es fehlen systematische Auswahlkriterien
                - Die Zusammenstellung ist nicht durch Forschungsfragen motiviert
                - Eine methodisch fundierte Analyse wäre nicht möglich"""
            },
            {
                "answer": "Eine Sammlung, die immer alle verfügbaren Texte zu einem Thema enthalten muss",
                "correct": False,
                "feedback": """× Nicht korrekt. Vollständigkeit ist nur eine mögliche Strategie des Korpusaufbaus:
                - Wie im Text erläutert, gibt es verschiedene Strategien (z.B. repräsentative Stichproben)
                - Die Vollständigkeit ist nur bei klar begrenzten, kleinen Untersuchungsbereichen sinnvoll
                - Die Strategie der Korpuserstellung richtet sich nach der Forschungsfrage und praktischen Erwägungen"""
            }
        ]
    }
]
display_quiz(question1, colors=colors.jupyterquiz, max_width=1000)
```

### Assessment 2.2: Digitale Textformate

#### Frage 2: Digitale Textformate

Welche Aussage trifft auf das jeweilige Textformat zu? Wählen Sie für jede Aussage das passende Format.

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

"""
Lernziel:
    Sie können die vier Hauptformate digitaler Texte (Bilddigitalisate, Plain Text, XML/TEI, CSV) anhand ihrer charakteristischen Eigenschaften unterscheiden und deren Vor- und Nachteile für spezifische Anwendungsfälle analysieren.
Bloom-Stufe: Analysieren
Format: Vergleichsmatrix + Multiple Choice
Geschätzte Zeit: 15 Minuten
Schwerpunkte:
    - Eigenschaften digitaler Textformate
    - Vor- und Nachteile verschiedener Formate
    - Formatauswahl für spezifische Zwecke
"""


statements = [
    {
        "question": "Dieses Format eignet sich besonders für linguistische Annotationen wie Wortarten und Lemmata in tabellarischer Form.",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "CSV",
                "correct": True,
                "feedback": "✓ Korrekt! Weil:\n    - Tabellarische Struktur ermöglicht klare Zuordnung von Token und Annotationen\n    - Einfache Verarbeitung mit Analysewerkzeugen\n    - Gut geeignet für große Datenmengen\n    - Standardformat für viele linguistische Tools"
            },
            {
                "answer": "XML/TEI",
                "correct": False,
                "feedback": """× Nicht optimal. Obwohl XML/TEI auch Annotationen unterstützt:
                    - Komplexerer Aufbau als nötig für einfache tabellarische Daten
                    - Weniger effizient für große Mengen einfach strukturierter Annotatione"""
            },
            {
                "answer": "Plain Text",
                "correct": False,
                "feedback": """× Nicht korrekt, weil:
                    - Keine Strukturierung für Annotationen möglich
                    - Keine Möglichkeit, zusätzliche Informationen systematisch zu speichern"""
            },
            {
                "answer": "Bilddigitalisate",
                "correct": False,
                "feedback": """× Nicht optimal, weil:
                    - Keine maschinenlesbare Textstruktur
                    - Keine Möglichkeit für systematische Annotationen"""
            }
        ]
    },
    {
        "question": "Dieses Format bewahrt die ursprüngliche visuelle Erscheinung des Dokuments, ist aber nicht direkt maschinenlesbar.",
        "type": "multiple_choice",
        "answers":  [
            {
                "answer": "CSV",
                "correct": False,
                "feedback": """× Nicht korrekt, weil:
                    - CSV nur tabellarische Daten speichert
                    - Keine visuellen Informationen enthält
                    - Primär für strukturierte Daten gedacht ist"""
            },
            {
                "answer": "XML/TEI",
                "correct": False,
                "feedback": """× Nicht ganz korrekt. XML/TEI:
                    - Kann zwar Layoutinformationen beschreiben
                    - Bewahrt aber nicht das visuelle Erscheinungsbild selbst
                    - Ist bereits maschinenlesbar"""
            },
            {
                "answer": "Plain Text",
                "correct": False,
                "feedback": """× Nicht korrekt, weil:
                    - Alle Formatierungen verloren gehen
                    - Nur der reine Text erhalten bleibt
                    - Keine visuellen Informationen gespeichert werden"""
            },
            {
                "answer": "Bilddigitalisate",
                "correct": True,
                "feedback": """✓ Korrekt! Bilddigitalisate (PDF, PNG, JPG) sind ideal dafür, weil sie:
                    - Layout und Typographie originalgetreu bewahren
                    - Illustrationen und grafische Elemente erhalten
                    - Als historische Referenz dienen können
                    Allerdings benötigen sie OCR für Textanalysen."""
            }
        ]
    }
]
display_quiz(statements, colors=colors.jupyterquiz)
```

#### Frage 3: Anwendungsfall-Analyse


**Szenario:** Ein Forschungsprojekt möchte einen historischen Zeitungskorpus erstellen, der:
- für automatische Textanalysen nutzbar ist
- die ursprüngliche Seitengestaltung dokumentiert
- langfristig archiviert werden soll

**Frage:** Welche Kombination von Formaten würden Sie empfehlen?

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
**Musterlösung:** Kombination aus Bilddigitalisaten (PDF) und Plain Text

**Begründung:**

Bilddigitalisate (PDF):
- Bewahren das originale Layout
- Dienen als Referenz
- Eignen sich für die Langzeitarchivierung

Plain Text (nach OCR):
- Ermöglicht automatische Textanalysen  
- Einfach zu verarbeiten
- Geringer Speicherbedarf

Alternative Ansätze:
- XML/TEI wäre zu aufwendig für große Korpora
- CSV ist nicht geeignet für Volltext
- Nur Bilddigitalisate würden Analysen erschweren
````
### Assessment 2.3: Metadaten und Dokumentation

#### Frage 5: Metadatenschemata

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

"""
Lernziel:
    Sie können die grundlegenden Metadatenschemata (Dublin Core, TEI, MODS, METS) und deren charakteristische Elemente für Korpora und Einzeldokumente beschreiben.
Bloom-Stufe: Verstehen
Format: Multiple Choice + Selbsteinschätzung
Zeitaufwand: 25 Minuten
Schwerpunkte:
    - Verständnis verschiedener Metadatenschemata (Dublin Core, TEI, MODS, METS)
    - Kenntnis charakteristischer Elemente 
    - Unterscheidung Korpus- und Dokumentebene
"""

question5 = [
    {
        "question": "Welche Aussagen beschreiben die verschiedenen Metadatenschemata korrekt?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Dublin Core umfasst 15 grundlegende Elemente wie Titel, Autor und Datum",
                "correct": True,
                "feedback": """✓ Richtig! Dublin Core:
                - Bietet ein einfaches, universelles Schema
                - Die 15 Kernelemente sind standardisiert
                - Eignet sich für grundlegende Beschreibungen
                - Ist weit verbreitet und leicht anzuwenden"""
            },
            {
                "answer": "TEI wurde speziell für die Auszeichnung von Texten entwickelt und speichert Metadaten im teiHeader",
                "correct": True,
                "feedback": """✓ Richtig! TEI:
                - Ist ein spezialisiertes Schema für Texte
                - Nutzt den teiHeader für Metadaten
                - Ermöglicht detaillierte Textauszeichnung
                - Bietet umfangreiche Beschreibungsmöglichkeiten"""
            },
            {
                "answer": "MODS und METS sind identische Standards für Bibliotheken",
                "correct": False,
                "feedback": """× Nicht korrekt. Die Standards unterscheiden sich:
                - MODS ist für bibliographische Beschreibungen
                - METS dient der Kodierung und Übertragung von Digitalisaten
                - Beide haben unterschiedliche Schwerpunkte und Anwendungsbereiche"""
            }
        ]
    }
]
display_quiz(question5, colors=colors.jupyterquiz)
```

#### Frage 7: Metadatenebenen

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

question7 = [
    {
        "question": "Welche Metadatenelemente sind charakteristisch für die Beschreibung einzelner Korpus-Dokumente?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Eindeutiger Identifikator (z.B. DOI oder spezifische Kennung)",
                "correct": True,
                "feedback": """✓ Richtig! Ein eindeutiger Identifikator:
                - Ist essentiell für die Dokumentidentifikation
                - Ermöglicht präzise Referenzierung
                - Unterstützt die Langzeitarchivierung
                - Erleichtert die Verknüpfung von Dokumenten"""
            },
            {
                "answer": "Gesamtumfang des Korpus",
                "correct": False,
                "feedback": """× Nicht korrekt! Der Gesamtumfang:
                - Ist ein Korpus-Level Metadatum
                - Beschreibt die gesamte Sammlung
                - Gehört nicht zur Dokumentbeschreibung"""
            }
        ]
    }
]
display_quiz(question7, colors=colors.jupyterquiz)
```
````{admonition} Lösungen
:class: solution, dropdown
Für Einzeldokumente sind stattdessen relevant:
- Individuelle Eigenschaften
- Spezifische Publikationsdaten
- Dokumentspezifische Merkmale
````

## Praktische Anwendung
### Assessment 2.4: Korpusaufbau in der Praxis

<!--

Lernziel:
    Sie können den schrittweisen Prozess des praktischen Korpusaufbaus (Konzeptentwicklung, Metadatenerstellung und Datensammlung) am Beispiel eines Zeitungskorpus beschreiben.
Bloom-Stufe: Verstehen
Format: Multiple Choice + Projektplanung
Geschätzte Zeit: 30 Minuten
Schwerpunkte:
    - Planung des Korpusaufbaus
    - Berücksichtigung praktischer Einschränkungen
    - Qualitätssicherung im Aufbauprozess
-->

#### Frage 10: Analyse eines Korpusaufbau-Konzepts

Analysieren Sie den folgenden Ausschnitt aus einem Korpusaufbau-Konzept:

"Für das Zeitungskorpus zur Spanischen Grippe werden Ausgaben der Berliner Morgenpost und der Vossischen Zeitung aus den Jahren 1918-1919 gesammelt. Die Zeitungen sind über ZEFYS als PDF verfügbar. Aufgrund der Datenmenge (ca. 2 TB) wird ein balanciertes Korpus mit repräsentativen Stichproben erstellt."

Bewerten Sie die folgenden Aspekte:

1.	Quellenauswahl
2.	Technische Umsetzbarkeit
3.	Praktische Einschränkungen
4.	Lösungsansatz



````{admonition} Lösungen
:class: solution, dropdown

**Musterlösung**:

1. Quellenauswahl:
    - Zwei relevante Berliner Zeitungen
    - Zeitraum entspricht Pandemieverlauf
    - Digitale Verfügbarkeit gegeben

2. Technische Umsetzbarkeit:
    - Zugang über ZEFYS-Portal möglich
    - PDF-Format erfordert OCR
    - Systematischer Download möglich

3. Praktische Einschränkungen:
    - Sehr große Datenmenge (2 TB)
    - Hoher Speicherbedarf
    - Aufwendige Verarbeitung

4. Lösungsansatz:
    - Balanciertes Korpus als Alternative
    - Repräsentative Stichproben
    - Praktikable Größe bei wissenschaftlicher Qualität
````
