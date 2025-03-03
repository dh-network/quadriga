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

import sys
sys.path.append("..")
from quadriga_config import colors

semantic_field_q1 = [{
    "question": "Welche Aussagen zum Konzept des semantischen Feldes sind korrekt?",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Für die Analyse der Spanischen Grippe sollten nur eindeutige, themenbezogene Begriffe ins semantische Feld aufgenommen werden",
            "correct": True,
            "feedback": """✓ Richtig! Wichtig weil:
            - Vermeidung von Mehrdeutigkeiten
            - Spezifischer Themenbezug
            - Kontextunabhängige Aussagekraft
            - Präzise Häufigkeitsanalyse möglich"""
        },
        {
            "answer": "Alle Krankheitsbegriffe sind automatisch Teil des semantischen Feldes 'Grippe'",
            "correct": False,
            "feedback": """× Nicht korrekt, weil:
            - Begriffe müssen spezifisch für Grippe sein
            - Historischer Sprachgebrauch relevant
            - Eindeutigkeit erforderlich
            - Kontextbezug wichtig"""
        }
    ]
}]

display_quiz(semantic_field_q1, colors=colors.jupyterquiz)
```

## Frage 2

Gegeben ist ein Text mit 500 Wörtern, davon 15 aus dem semantischen Feld 'Grippe'.

Berechnen Sie die relative Häufigkeit und interpretieren Sie das Ergebnis.

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga_config")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('frage-2')
```


````{admonition} Lösungen
:class: solution, dropdown

**Berechnung**: 15/500 = 0.03 = 3%

**Interpretation**:
- 3% aller Wörter beziehen sich auf Grippe
- Vergleichbar mit anderen Textlängen
- Basis für zeitliche Analyse
- Normalisierte Darstellung

**Wichtig zu verstehen**:
- Relative Häufigkeiten ermöglichen Vergleiche
- Normalisierung durch Textlänge
- Prozentuale Darstellung sinnvoll
- Basis für weitere Analysen
````

## Frage 3

(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

visualization_q1 = [{
    "question": "Welche Aussagen zum Liniendiagramm treffen zu?",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Ermöglicht die Visualisierung des zeitlichen Verlaufs",
            "correct": True,
            "feedback": """✓ Richtig! Das Liniendiagramm eignet sich besonders für:
            - Visualisierung zeitlicher Entwicklung
            - Erkennung von Mustern
            - Vergleichende Analyse"""
        },
        {
            "answer": "Bietet detaillierte Einblicke in Wortverwendungskontexte",
            "correct": False,
            "feedback": """× Nicht korrekt. Liniendiagramme zeigen:
            - Nur quantitative Perspektive
            - Keine Kontextdetails
            - Rein numerische Darstellung"""
        },
        {
            "answer": "Wellenmuster in der Begriffsverwendung werden sichtbar",
            "correct": True,
            "feedback": """✓ Richtig! Vorteile des Liniendiagramms:
            - Zeigt Schwankungen über Zeit
            - Ermöglicht Vergleich verschiedener Zeiträume
            - Verdeutlicht Trends und Muster"""
        },
        {
            "answer": "Zeigt qualitative Aspekte der Textdaten",
            "correct": False,
            "feedback": """× Nicht korrekt. Liniendiagramme zeigt nur quantitative Trends, keine qualitativen Aspekte."""
        }
    ]
}]

display_quiz(visualization_q1, colors=colors.jupyterquiz)
```

## Frage 4

(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

visualization_q2 = [{
    "question": "Welche Aussagen zur KWIC-Darstellung (Key Word in Context) sind korrekt?",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Ermöglicht eine qualitative Analyse der Wortverwendung",
            "correct": True,
            "feedback": """✓ Richtig! KWIC ist wichtig für:
            - Validierung des semantischen Feldes
            - Detailanalyse der Verwendung
            - Qualitative Ergänzung"""
        },
        {
            "answer": "Bietet eine schnelle Gesamtübersicht der Begriffsverwendung",
            "correct": False,
            "feedback": """× Nicht korrekt. KWIC hat Limitationen:
            - Keine Gesamtübersicht
            - Zeitaufwändige Analyse
            - Fokus auf einzelne Kontexte"""
        },
        {
            "answer": "Zeigt die Verwendung von Schlüsselwörtern in ihrem unmittelbaren Textkontext",
            "correct": True,
            "feedback": """✓ Richtig! Stärken der KWIC-Methode:
            - Kontextuelle Einbettung
            - Überprüfung der Wortverwendung
            - Detaillierte Analyse möglich"""
        },
        {
            "answer": "Ist eine zeiteffiziente Methode für große Textmengen",
            "correct": False,
            "feedback": """× Nicht korrekt. KWIC:
            - Erfordert zeitaufwändige manuelle Analyse
            - Ist detailliert aber langsam
            - Eignet sich für gezielte Detailuntersuchungen"""
        }
    ]
}]

display_quiz(visualization_q2, colors=colors.jupyterquiz)
```

## Frage 5
(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

method_integration_q1 = [{
    "question": "Welche Aussagen beschreiben korrekt das Zusammenspiel verschiedener Methoden in der textanalytischen Workflow?",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Das semantische Feld bildet die Grundlage für die Häufigkeitsanalyse, da es die zu untersuchenden Begriffe definiert",
            "correct": True,
            "feedback": """✓ Richtig! Die Erstellung semantischer Felder:
            - Definiert systematisch die relevanten Suchbegriffe
            - Schafft einen konzeptionellen Rahmen für die quantitative Analyse
            - Ermöglicht eine strukturierte Herangehensweise an den Text"""
        },
        {
            "answer": "Die KWIC-Analyse sollte vor der Erstellung des semantischen Feldes durchgeführt werden",
            "correct": False,
            "feedback": """× Nicht korrekt. Der effiziente Workflow ist anders strukturiert:
            - KWIC-Analysen bauen auf vordefinierten Suchbegriffen auf
            - Die semantische Feldanalyse definiert erst, welche Begriffe kontextuell untersucht werden sollen
            - Die KWIC-Analyse dient der Validierung und qualitativen Vertiefung bereits quantifizierter Ergebnisse"""
        },
        {
            "answer": "Visualisierungen wie Liniendiagramme verwenden die Ergebnisse der Häufigkeitsanalyse als Datengrundlage",
            "correct": True,
            "feedback": """✓ Richtig! Visualisierungen:
            - Basieren auf den quantitativen Daten der Häufigkeitsanalyse
            - Machen zeitliche Entwicklungen und Muster sichtbar
            - Transformieren numerische Daten in visuell erfassbare Informationen"""
        },
        {
            "answer": "Die KWIC-Analyse ersetzt die Notwendigkeit einer quantitativen Häufigkeitsanalyse",
            "correct": False,
            "feedback": """× Nicht korrekt. Beide Methoden ergänzen sich:
            - Die KWIC-Analyse bietet qualitative Einblicke, aber keine systematische Quantifizierung
            - Häufigkeitsanalysen liefern quantitative Daten, aber keinen kontextuellen Einblick
            - Für eine umfassende Analyse werden beide Perspektiven benötigt"""
        },
        {
            "answer": "Die Kombination aus quantitativen und qualitativen Methoden ermöglicht eine Validierung und Vertiefung der Ergebnisse",
            "correct": True,
            "feedback": """✓ Richtig! Die Methodenkombination ist entscheidend:
            - Quantitative Analysen zeigen Trends und Muster
            - Qualitative Methoden wie KWIC validieren und kontextualisieren diese Ergebnisse
            - Erst die Kombination ermöglicht robuste und tiefgehende Interpretationen"""
        },
        {
            "answer": "Häufigkeitsanalysen können unabhängig von einem semantischen Feld durchgeführt werden und liefern dieselbe Qualität an Ergebnissen",
            "correct": False,
            "feedback": """× Nicht korrekt. Ein systematisches semantisches Feld ist essenziell:
            - Ohne konzeptionellen Rahmen fehlt die theoretische Fundierung der Analyse
            - Die Qualität der Häufigkeitsanalyse hängt direkt von der Qualität des semantischen Feldes ab
            - Willkürlich gewählte Suchbegriffe führen zu weniger aussagekräftigen und weniger vergleichbaren Ergebnissen"""
        }
    ]
}]

display_quiz(method_integration_q1, colors=colors.jupyterquiz, max_width=1000)
```


## Frage 6

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

process_steps_q1 = [{
    "question": "In welcher Reihenfolge werden die Schritte der Frequenzanalyse durchgeführt?",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "1. Berechnung der Häufigkeiten → 2. Einlesen des Korpus → 3. Visualisierung",
            "correct": False,
            "feedback": """× Falsch. Der Korpus muss zuerst eingelesen werden, bevor Häufigkeiten berechnet werden können."""
        },
        {
            "answer": "1. Einlesen des Korpus und der Metadaten → 2. Berechnung der Häufigkeiten des semantischen Felds → 3. Visualisierung der Ergebnisse im Liniendiagramm",
            "correct": True,
            "feedback": """✓ Richtig! Dies ist die korrekte Reihenfolge:
            1. Einlesen des Korpus und der Metadaten:
               - Datengrundlage muss verfügbar sein
               - Metadaten für zeitliche Zuordnung wichtig
               - Basis für weitere Verarbeitung
               - Strukturierte Datenorganisation nötig

            2. Berechnung der Häufigkeiten des semantischen Felds:
               - Basiert auf eingelesenen Daten
               - Verschiedene Berechnungsmethoden möglich
               - Absolute und relative Häufigkeiten
               - Zeitliche Gruppierung wichtig

            3. Visualisierung der Ergebnisse im Liniendiagramm:
               - Zeigt zeitlichen Verlauf
               - Macht Muster sichtbar
               - Ermöglicht Vergleiche
               - Basis für Interpretation"""
        },
        {
            "answer": "1. Visualisierung → 2. Einlesen des Korpus → 3. Berechnung der Häufigkeiten",
            "correct": False,
            "feedback": """× Falsch. Die Visualisierung kann erst nach Berechnung der Häufigkeiten erfolgen."""
        },
        {
            "answer": "1. Einlesen des Korpus → 2. Visualisierung der Datengrundlage → 3. Berechnung der Häufigkeiten des semantischen Feldes",
            "correct": False,
            "feedback": """× Falsch. Die Visualisierung sollte nach der Häufigkeitsberechnung erfolgen."""
        }
    ]
}]

display_quiz(process_steps_q1, colors=colors.jupyterquiz, max_width=1000)
```

## Frage 7

(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

frequency_calc_q1 = [{
    "question": "Welche Aussagen zu absoluten Häufigkeiten treffen zu?",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Einfach zu berechnen und zeigen die Gesamtzahl der Vorkommen",
            "correct": True,
            "feedback": """✓ Richtig! Absolute Häufigkeiten:
            - Zeigen rohe Vorkommenshäufigkeit
            - Einfach zu ermitteln
            - Direkte Zahlen ohne Normalisierung"""
        },
        {
            "answer": "Schwierig zu berechnen und verstecken die tatsächliche Anzahl der Vorkommen",
            "correct": False,
            "feedback": """× Nicht korrekt!"""
        },
        {
            "answer": "Ermöglichen direkte Vergleiche zwischen Textkorpora unterschiedlicher Länge",
            "correct": False,
            "feedback": """× Nicht korrekt. Absolute Häufigkeiten:
            - Sind abhängig von Korpusgröße
            - Nicht vergleichbar bei unterschiedlichen Textlängen
            - Benötigen Normalisierung für faire Vergleiche"""
        },
        {
            "answer": "Abhängig von der Gesamtlänge des untersuchten Textkorpus",
            "correct": True,
            "feedback": """✓ Richtig! Wichtig zu verstehen:
            - Größe des Korpus beeinflusst absolute Zahlen
            - Keine Berücksichtigung der Textlänge
            - Begrenzte Aussagekraft ohne Normalisierung"""
        }
    ]
}]

display_quiz(frequency_calc_q1, colors=colors.jupyterquiz)
```
## Frage 8

(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

frequency_calc_q2 = [{
    "question": "Welche Vorteile haben relative Häufigkeiten?",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Ermöglichen faire Vergleiche zwischen unterschiedlich langen Texten",
            "correct": True,
            "feedback": """✓ Richtig! Relative Häufigkeiten sind vorteilhaft weil:
            - Ermöglichen faire Vergleiche
            - Berücksichtigen Textlängen
            - Standardisierte Darstellung
            - Wissenschaftlich fundiert"""
        },
        {
            "answer": "Sind immer leicht zu interpretieren",
            "correct": False,
            "feedback": """× Nicht ganz korrekt. Relative Häufigkeiten:
            - Können abstrakt wirken
            - Erfordern Kontextverständnis
            - Benötigen sorgfältige Interpretation"""
        },
        {
            "answer": "Normalisieren die Häufigkeiten im Verhältnis zur Textlänge",
            "correct": True,
            "feedback": """✓ Richtig! Relative Häufigkeiten:
            - Setzen Vorkommen in Relation zur Textlänge
            - Schaffen Vergleichbarkeit
            - Eliminieren Verzerrungen durch Korpusgröße
            - Wissenschaftlich präzise"""
        },
        {
            "answer": "Benötigen weniger Rechenaufwand als absolute Häufigkeiten",
            "correct": False,
            "feedback": """× Nicht korrekt. Relative Häufigkeiten:
            - Erfordern einen zusätzlichen Berechnungsschritt (Division durch Textlänge)
            - Bauen auf absoluten Häufigkeiten auf, die zuerst berechnet werden müssen
            - Benötigen also mehr, nicht weniger Rechenaufwand
            - Der Mehraufwand ist jedoch gerechtfertigt durch die bessere Vergleichbarkeit"""
        }
    ]
}]

display_quiz(frequency_calc_q2, colors=colors.jupyterquiz)
```

## Frage 9

Gegeben ist folgendes Analyseergebnis: 'Zwei deutliche Häufigkeitsspitzen im Herbst 1918 und Winter 1918/19'

(Wählen Sie alle zutreffenden Antworten aus)

### Frage 9(a)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

results_analysis_q1 = [{
    "question": "Welche Aspekte sind bei der historischen Einordnung dieser Ergebnisse zu berücksichtigen?",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Korrelation mit bekannten Grippewellen",
            "correct": True,
            "feedback": """✓ Richtig! Die Spitzen korrelieren mit:
            - Bekannten Grippewellen
            - Höhepunkten der Pandemie
            - Verstärkter Berichterstattung
            - Gesellschaftlicher Wahrnehmung

            Wichtig für:
            - Validierung der Methode
            - Historische Kontextualisierung
            - Bestätigung der Operationalisierung"""
        },
        {
            "answer": "Absolute Unabhängigkeit von historischen Ereignissen",
            "correct": False,
            "feedback": """× Nicht korrekt. Frequenzanalysen:
            - Müssen historischen Kontext berücksichtigen
            - Sind eng mit gesellschaftlichen Ereignissen verknüpft
            - Erfordern interdisziplinäre Interpretation"""
        },
        {
            "answer": "Reflexion der methodischen Grenzen und Möglichkeiten",
            "correct": True,
            "feedback": """✓ Richtig! Die Analyse zeigt:
            - Funktionalität des semantischen Felds
            - Aussagekraft der Frequenzanalyse
            - Grenzen der Methode
            - Notwendigkeit weiterer Untersuchungen

            Relevant für:
            - Methodische Evaluation
            - Weiterentwicklung der Analyse
            - Wissenschaftliche Einordnung"""
        }
    ]
}]

display_quiz(results_analysis_q1, colors=colors.jupyterquiz)
```
### Frage 9(b)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

results_analysis_q2 = [{
    "question": "Welche methodischen Aspekte sind bei der Interpretation der Frequenzanalyse zu beachten?",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Absolute Zuverlässigkeit der Ergebnisse ohne weitere Überprüfung",
            "correct": False,
            "feedback": """× Nicht korrekt. Wissenschaftliche Analyse erfordert:
            - Kritische Reflexion
            - Methodische Überprüfung
            - Berücksichtigung von Grenzen
            - Kontextuelle Einordnung"""
        },
        {
            "answer": "Notwendigkeit zusätzlicher qualitativer Analysen",
            "correct": True,
            "feedback": """✓ Richtig! Methodische Reflexion bedeutet:
            - Quantitative Ergebnisse ergänzen
            - Tiefere Kontextanalyse erforderlich
            - KWIC-Analyse zur Validierung
            - Umfassenderes Verständnis gewinnen"""
        },
        {
            "answer": "Berücksichtigung von Zufälligkeiten und Verzerrungen",
            "correct": True,
            "feedback": """✓ Richtig! Wichtige methodische Überlegungen:
            - Mögliche Verzerrungen identifizieren
            - Statistische Signifikanz prüfen
            - Zufällige Schwankungen berücksichtigen
            - Wissenschaftliche Präzision gewährleisten"""
        }
    ]
}]

display_quiz(results_analysis_q2, colors=colors.jupyterquiz)
```

## Frage 10
(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

method_understanding_q1 = [{
    "question": "Welche Aussagen zur KWIC-Darstellung (Key Word in Context) sind korrekt?",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Die Kontextinformationen in KWIC helfen bei der Validierung des semantischen Feldes",
            "correct": True,
            "feedback": """✓ Richtig! KWIC ermöglicht:
            - Überprüfung der Wortverwendung
            - Identifikation von Mehrdeutigkeiten
            - Verfeinerung des semantischen Feldes
            - Qualitative Ergänzung zur Frequenzanalyse"""
        },
        {
            "answer": "KWIC bietet nur eine quantitative Analyse der Wortverwendung",
            "correct": False,
            "feedback": """× Nicht korrekt. KWIC ist eine qualitativ-kontextuelle Methode:
            - Zeigt Wortverwendung im Kontext
            - Ermöglicht qualitative Interpretation
            - Geht über reine Häufigkeitszählung hinaus
            - Liefert Einblicke in Sprachgebrauch"""
        },
        {
            "answer": "KWIC erlaubt eine detaillierte Untersuchung der Wortverwendung in verschiedenen Kontexten",
            "correct": True,
            "feedback": """✓ Richtig! KWIC ist ein leistungsfähiges Analyseinstrument:
            - Zeigt Variationen der Wortverwendung
            - Ermöglicht kontextuelle Analyse
            - Unterstützt semantische Feldforschung
            - Liefert nuancierte Einblicke"""
        },
        {
            "answer": "KWIC kann vollständig komplexe historische Diskurse rekonstruieren",
            "correct": False,
            "feedback": """× Nicht korrekt. KWIC:
            - Bietet Einblicke in Sprachverwendung
            - Ist eine ergänzende Analysemethode
            - Kann nicht den gesamten Diskurs vollständig abbilden
            - Erfordert Kombination mit anderen Methoden"""
        }
    ]
}]

display_quiz(method_understanding_q1, colors=colors.jupyterquiz)
```

## Frage 11

Analysieren Sie folgenden KWIC-Ausschnitt:

'... bleiben werden, tritt [Influenza] wieder recht heftig auf ...' (1918-19)

(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

context_interpretation_q1 = [{
    "question": "Welche Aspekte der kontextuellen Bedeutung lassen sich aus diesem Ausschnitt ableiten?",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Beschreibung des Krankheitsverlaufs durch Adjektive wie 'heftig'",
            "correct": True,
            "feedback": """✓ Richtig! Der Kontext zeigt:
            - Krankheitsverlauf ('heftig')
            - Intensität der Erkrankung
            - Qualitative Beschreibung der Epidemie
            - Sprachliche Nuancen des Zeitgeists"""
        },
        {
            "answer": "Zeitliche Dimension durch Wörter wie 'wieder'",
            "correct": True,
            "feedback": """✓ Richtig! Der Kontext verdeutlicht:
            - Zeitliche Entwicklung ('wieder')
            - Wiederholende Natur der Krankheit
            - Dynamik der Pandemie
            - Historische Prozesshaftigkeit"""
        },
        {
            "answer": "Bedeutung des Datums für die historische Einordnung",
            "correct": True,
            "feedback": """✓ Richtig! Das Datum (1918-10) ermöglicht:
            - Zeitliche Einordnung
            - Vergleich mit Pandemiewellen
            - Korrelation mit Häufigkeitsanalyse
            - Historische Kontextualisierung"""
        },
        {
            "answer": "Präzise Beschreibung der Krankheitsursachen",
            "correct": False,
            "feedback": """× Nicht korrekt. Der Ausschnitt:
            - Liefert keine detaillierten Ursacheninformationen
            - Beschreibt nur Auftreten und Intensität
            - Erfordert breitere Kontextanalyse
            - Zeigt nur einen kleinen Textausschnitt"""
        }
    ]
}]

display_quiz(context_interpretation_q1, colors=colors.jupyterquiz)
```

## Frage 12
(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

kwic_application_q1 = [{
    "question": "Welche Rolle spielt KWIC bei der Validierung des semantischen Feldes?",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Überprüfung der Wortverwendung im Kontext",
            "correct": True,
            "feedback": """✓ Richtig! KWIC ermöglicht:
            - Überprüfung der Wortverwendung
            - Identifikation zusätzlicher relevanter Begriffe
            - Erkennung von Mehrdeutigkeiten
            - Anpassung der Wortliste

            Wichtig für:
            - Qualitätssicherung der Analyse
            - Verfeinerung der Suchbegriffe
            - Vermeidung von Fehlinterpretationen
            - Methodische Präzision"""
        },
        {
            "answer": "Vollständige Ersetzung quantitativer Analysen",
            "correct": False,
            "feedback": """× Nicht korrekt. KWIC:
            - Ergänzt quantitative Analysen
            - Liefert qualitative Einblicke
            - Ist Teil eines umfassenden Analyseansatzes
            - Kann quantitative Methoden nicht vollständig ersetzen"""
        },
        {
            "answer": "Identifikation zusätzlicher relevanter Begriffe",
            "correct": True,
            "feedback": """✓ Richtig! KWIC hilft bei:
            - Erweiterung des semantischen Feldes
            - Entdeckung neuer relevanter Begriffe
            - Kontextueller Bedeutungsanalyse
            - Wissenschaftlicher Präzision"""
        },
        {
            "answer": "Vollständige Rekonstruktion historischer Sprachverwendung",
            "correct": False,
            "feedback": """× Nicht korrekt. KWIC:
            - Bietet Einblicke in Sprachverwendung
            - Kann nicht die gesamte Sprachverwendung rekonstruieren
            - Ist eine ergänzende Methode
            - Erfordert Kombination mit anderen Analyseansätzen"""
        },
        {
            "answer": "Eliminierung aller Mehrdeutigkeiten im semantischen Feld",
            "correct": False,
            "feedback": """× Nicht korrekt. KWIC:
            - Hilft bei der Identifikation von Mehrdeutigkeiten
            - Kann Mehrdeutigkeiten nicht vollständig beseitigen
            - Unterstützt die Präzisierung
            - Ergänzt die semantische Feldanalyse"""
        }
    ]
}]

display_quiz(kwic_application_q1, colors=colors.jupyterquiz)
```
## Frage 13

(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

kwic_application_q2 = [{
    "question": "Welche Aspekte der qualitativen Ergänzung werden durch KWIC ermöglicht?",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Analyse spezifischer Berichterstattung",
            "correct": True,
            "feedback": """✓ Richtig! KWIC ermöglicht:
            - Untersuchung spezifischer Textpassagen
            - Detaillierte Berichterstattungsanalyse
            - Erfassung nuancierter Darstellungen
            - Tiefere Textinterpretation"""
        },
        {
            "answer": "Vollständige Rekonstruktion historischer Ereignisse",
            "correct": False,
            "feedback": """× Nicht korrekt. KWIC:
            - Bietet Ausschnitte, keine vollständige Rekonstruktion
            - Ist eine ergänzende Analysemethode
            - Erfordert Kombination mit anderen Methoden
            - Liefert Einblicke, keine umfassende Darstellung"""
        },
        {
            "answer": "Untersuchung der Wortwahl und des Diskurses",
            "correct": True,
            "feedback": """✓ Richtig! KWIC ermöglicht:
            - Analyse der Sprachverwendung
            - Erfassung diskursiver Muster
            - Untersuchung sprachlicher Nuancen
            - Kontextuelle Bedeutungsanalyse

            Ermöglicht:
            - Tiefere Einblicke
            - Nuancierte Interpretation
            - Historische Kontextualisierung
            - Ergänzung quantitativer Daten"""
        },
        {
            "answer": "Präzise Vorhersage zukünftiger Sprachentwicklung",
            "correct": False,
            "feedback": """× Nicht korrekt. KWIC:
            - Analysiert historische Sprachverwendung
            - Kann keine Sprachentwicklung vorhersagen
            - Bietet Einblicke in vergangene Sprachnutzung
            - Ist eine interpretierende, keine prognostische Methode"""
        },
        {
            "answer": "Vollständige linguistische Grammatikanalyse",
            "correct": False,
            "feedback": """× Nicht korrekt. KWIC:
            - Fokussiert auf Wortverwendung und Kontext
            - Ist keine umfassende Grammatikanalyse
            - Bietet Einblicke in Sprachgebrauch
            - Erfordert ergänzende linguistische Methoden"""
        }
    ]
}]

display_quiz(kwic_application_q2, colors=colors.jupyterquiz)
```

