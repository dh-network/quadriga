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
### Korpora als Forschungsobjekte

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

question1 = [
    {
        "question": "Welche der folgenden Aussagen beschreiben korrekt die wesentlichen Merkmale eines Korpus in den Digital Humanities?Wählen Sie alle zutreffenden Aussagen.",
            "type": "multiple_choice",
            "answers": [
            {
                "answer": "Eine Sammlung von maschinenlesbaren Textdokumenten",
                "correct": True,
                "feedback": "✓ Korrekt! Die Maschinenlesbarkeit ist ein zentrales Merkmal von DH-Korpora, da sie die computergestützte Analyse ermöglicht.\\nDies unterscheidet DH-Korpora von traditionellen Textsammlungen und ist Voraussetzung für quantitative Analysen."
            },    
            {
                "answer": "Eine nach bestimmten Kriterien zusammengestellte Textsammlung",
                "correct": True,
                "feedback": "✓ Korrekt! Die kriteriengeleitete Zusammenstellung ist essentiell für wissenschaftliche Korpora.Die Kriterien müssen dabei:\n- transparent dokumentiert sein\n- zur Forschungsfrage passen\n- systematisch angewendet werden"
            },
            {
                "answer": "Eine Sammlung, die nur digitalisierte Bücher enthält",
                "correct": False,
                "feedback": "× Nicht korrekt. Korpora können verschiedene Arten von Texten enthalten:\n- Zeitungsartikel (wie in unserer Fallstudie)\n- Literarische Texte\n- Dokumente\n- Andere Textformen\nDie Art der Texte wird durch die Forschungsfrage bestimmt, nicht durch das Format."
            },
            {
                "answer": "Eine Textsammlung, die spezifischen Forschungszwecken dient",
                "correct": True,
                "feedback": "✓ Korrekt! Die Zweckgebundenheit ist ein wichtiges Merkmal:\n- Das Korpus wird für bestimmte Forschungsfragen zusammengestellt\n- Die Forschungszwecke bestimmen die Auswahlkriterien\n- Die Zweckbindung beeinflusst auch die Art der Aufbereitung der Texte"
            },
            {
                "answer": "Eine beliebige Sammlung von digitalisierten Texten",
                "correct": False,
                "feedback": "× Nicht korrekt. Eine beliebige Sammlung erfüllt nicht die wissenschaftlichen Anforderungen an ein Korpus:\n- Es fehlen systematische Auswahlkriterien\n- Die Zusammenstellung ist nicht durch Forschungsfragen motiviert\n- Eine methodisch fundierte Analyse wäre nicht möglich"
            },
            {
                "answer": "Eine Sammlung, die immer alle verfügbaren Texte zu einem Thema enthalten muss",
                "correct": False,
                "feedback": "× Nicht korrekt. Vollständigkeit ist nur eine mögliche Strategie des Korpusaufbaus:\n- Wie im Text erläutert, gibt es verschiedene Strategien (z.B. repräsentative Stichproben)\n- Die Vollständigkeit ist nur bei klar begrenzten, kleinen Untersuchungsbereichen sinnvoll\n- Die Strategie der Korpuserstellung richtet sich nach der Forschungsfrage und praktischen Erwägungen"
            }
        ]
    }
]
display_quiz(question1, colors=colors.jupyterquiz)
```
## Frage 2
### Digital Text Formats

Welche Aussage trifft auf das jeweilige Textformat zu? Wählen Sie für jede Aussage das passende Format.

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

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

## Frage 3

Analysieren Sie die folgenden Anwendungsfälle. Wählen Sie das am besten geeignete Format und begründen Sie die Vor- und Nachteile.

Ein Forschungsprojekt möchte einen historischen Zeitungskorpus erstellen, der:
- für automatische Textanalysen nutzbar ist
- die ursprüngliche Seitengestaltung dokumentiert
- langfristig archiviert werden soll

Welche Kombination von Formaten würden Sie empfehlen?

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
**Empfohlene Lösung:** Kombination aus Bilddigitalisaten (PDF) und Plain Text

Diese Kombination ist optimal, weil:

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

## Frage 4
### Metadaten

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

question = [
    {
        "question": "Welche Aussagen beschreiben die verschiedenen Metadatenschemata korrekt?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Dublin Core umfasst 15 grundlegende Elemente wie Titel, Autor und Datum.",
                "correct": True,
                "feedback": """✓ Richtig! Dublin Core:
                - Bietet ein einfaches, universelles Schema
                - Die 15 Kernelemente sind standardisiert
                - Eignet sich für grundlegende Beschreibungen
                - Ist weit verbreitet und leicht anzuwenden"""
            },
            {
                "answer": "TEI wurde speziell für die Auszeichnung von Texten entwickelt und speichert Metadaten im teiHeader.",
                "correct": True,
                "feedback": """✓ Richtig! TEI:
                - Ist ein spezialisiertes Schema für Texte
                - Nutzt den teiHeader für Metadaten
                - Ermöglicht detaillierte Textauszeichnung
                - Bietet umfangreiche Beschreibungsmöglichkeiten"""
            },
            {
                "answer": "MODS und METS sind identische Standards für Bibliotheken.",
                "correct": False,
                "feedback": """× Nicht korrekt. Die Standards unterscheiden sich:
                - MODS ist für bibliographische Beschreibungen
                - METS dient der Kodierung und Übertragung von Digitalisaten
                - Beide haben unterschiedliche Schwerpunkte und Anwendungsbereiche"""
            }
        ]
    }
]
display_quiz(question, colors=colors.jupyterquiz)
```

## Frage 5
```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

question = [
    {"question": "Welche Metadatenelemente sind charakteristisch für die Beschreibung einzelner Korpus-Dokumente?",
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
            - Gehört nicht zur Dokumentbeschreibung
            Für Einzeldokumente sind stattdessen relevant:
            - Individuelle Eigenschaften
            - Spezifische Publikationsdaten
            - Dokumentspezifische Merkmale"""
        }
    ]}
]
display_quiz(question, colors=colors.jupyterquiz)
```
## Frage 6
### Aufbau des Forschungskorpus

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

question = [
    {
        "question": "Welche Aussagen beschreiben den Prozess des Korpusaufbaus korrekt?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Die Entwicklung des Korpuskonzepts muss pragmatische Einschränkungen wie verfügbare Ressourcen berücksichtigen.",
                "correct": True,
                "feedback": """✓ Richtig! Dies zeigt sich im Beispiel deutlich:
                - Die ursprüngliche Schätzung von 2 Terabyte war nicht praktikabel
                - Es wurde auf ein balanciertes Korpus mit zwei Zeitungen reduziert
                - Der Zeitraum wurde auf 1918-1919 eingegrenzt
                Die Berücksichtigung praktischer Grenzen ist ein wichtiger Teil der Konzeptentwicklung."""
            },{
                "answer": "Die Metadaten für die Korpuselemente müssen vor der Datensammlung vollständig definiert sein.",
                "correct": True,
                "feedback": """✓ Richtig! Im Beispiel wird dies deutlich durch:
                - Festlegung der Metadatenfelder (ID, Name, Datum, URL)
                - Systematische Dokumentation in tabellarischer Form
                - Nutzung standardisierter Dublin Core Elemente
                Diese Strukturierung ermöglicht erst die systematische Sammlung."""
            },
            {
                "answer": "Ein vollständiges Korpus ist immer die beste Wahl für ein Forschungsprojekt.",
                "correct": False,
                "feedback": """× Nicht korrekt! Das Beispiel zeigt:
                - Vollständige Korpora können zu groß für praktische Handhabung sein
                - Balancierte oder repräsentative Korpora können ausreichen
                - Die Wahl der Korpusstrategie hängt von verschiedenen Faktoren ab:
                  * Verfügbare Ressourcen
                  * Forschungsziele
                  * Praktische Umsetzbarkeit"""
            }
        ]
    }
]
display_quiz(question, colors=colors.jupyterquiz)
```

## Frage 7
### Korpusaufbau: Einflussfaktoren

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

question = [
    {
        "question": "Welche Faktoren beeinflussen die Entscheidungen beim Korpusaufbau am Beispiel des Zeitungskorpus?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Die technische Zugänglichkeit der Quellen über eine API oder ähnliche Schnittstellen",
                "correct": True,
                "feedback": """✓ Richtig! Im Beispiel wird dies deutlich durch:
                - Nutzung des ZEFYS-Portals
                - Systematische URL-Strukturen
                - Automatisierbare Download-Möglichkeiten"""
            },
            {
                "answer": "Die Größe der einzelnen Dateien und des Gesamtkorpus",
                "correct": True,
                "feedback": """✓ Richtig! Dies zeigt sich durch:
                - Berechnung der durchschnittlichen PDF-Größe (74 MB)
                - Abschätzung des Gesamtvolumens
                - Anpassung des Konzepts an praktische Limitationen"""
            }, {
                "answer": "Das persönliche Interesse der Forschenden an bestimmten Zeitungen",
                "correct": False,
                "feedback": """× Nicht korrekt! Die Auswahl basiert auf:
                - Systematischen Kriterien (renommierte Zeitungen)
                - Praktischer Verfügbarkeit
                - Forschungsfrage und Zeitraum
                Persönliche Präferenzen sind kein valides Auswahlkriterium."""
            }
        ]
    }
]
display_quiz(question, colors=colors.jupyterquiz)
```

## Frage 8
### Dokumentationselemente im Korpusaufbau

Identifizieren Sie die wesentlichen Dokumentationselemente für den Korpusaufbau-Prozess.


```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

question = [
    {
        "question": "Welche Dokumentationselemente sind für den Korpusaufbau-Prozess wesentlich?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Korpus-Metadaten (z.B. DC.title, DC.description)",
                "correct": True,
                "feedback": """✓ Richtig! Wichtig weil:
                - Identifiziert das Korpus eindeutig
                - Beschreibt Umfang und Inhalt
                - Ermöglicht Nachnutzung"""
            },
            {
                "answer": "Element-Metadaten (ID, Name, Datum, URL)",
                "correct": True,
                "feedback": """✓ Richtig! Wichtig weil:
                - Ermöglicht systematische Erfassung
                - Unterstützt Datenmanagement
                - Erleichtert spätere Analyse"""
            },
            {
                "answer": "Sammlungsprozess (Download-Methode, Skripte)",
                "correct": True,
                "feedback": """✓ Richtig! Wichtig weil:
                - Macht Prozess nachvollziehbar
                - Ermöglicht Reproduzierbarkeit
                - Dokumentiert technische Entscheidungen"""
            }
        ]
    }
]
display_quiz(question, colors=colors.jupyterquiz)
```