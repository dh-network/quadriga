(reflection_reflection)=
# Reflexion

````{margin}
```{admonition} Fragen oder Feedback 
:class: frage-feedback

<a href="https://github.com/dh-network/quadriga/issues/new?assignees=&labels=question&projects=&template=frage.yml" class="external-link" target="_blank">
    Stellen Sie eine Frage
</a> <br>
<a href="https://github.com/dh-network/quadriga/issues/new?assignees=&labels=feedback&projects=&template=feedback.yml" class="external-link" target="_blank">
    Geben Sie uns Feedback
</a>

Mit Ihren Rückmeldungen können wir unser interaktives Lehrbuch gezielt an Ihre Bedürfnisse anpassen.

```
````
Auch wenn es uns gelungen ist, das Ziel der Fallstudie zu erreichen und unsere eingangs formulierte [Forschungsfrage](research-question_research-question) nach den "Medienwellen" der Spanischen Grippe insofern exemplarisch zu beantworten, als wir tatsächliche eine [wellenartige Entwicklung der quantitative verstandenen Aufmerksamkeit in ausgewählten Berliner Tageszeitungen](../corpus_analysis/corpus-analysis_diachronic-analysis) nachweisen konnten, gibt es mehrere Punkte, die abschließend kritisch zu reflektieren sind. 

```{admonition} Kritische Bewertung der Reichweite und Limitationen
:class: lernziele

1. Die methodischen Limitationen einer Digital Humanities-Fallstudie können benannt werden.
```


Auch wenn es uns gelungen ist, das Ziel der Fallstudie zu erreichen und unsere eingangs formulierte [Forschungsfrage](research-question_research-question) nach den "Medienwellen" der Spanischen Grippe insofern exemplarisch zu beantworten, als wir tatsächliche eine [wellenartige Entwicklung der quantitative verstandenen Aufmerksamkeit in ausgewählten Berliner Tageszeitungen](corpus_analysis/corpus-analysis_diachronic-analysis) nachweisen konnten, gibt es mehrere Punkte, die abschließend kritisch zu reflektieren sind. 

1. Auf das gesamte **Forschungssetting eines Digital Humanities-Projekts** gesehen, ist die durchgeführte Fallstudie von lediglich kleinem Umfang. Im Grunde fehlen ihr noch zwei Komponenten: zum einen die umfangreiche Kontextualisierungen in der medienhistorischen Epidemologie; zum anderen die eingehende Auswertung der Ergebnisse der Analyse. So wäre denkbar, dass ausgehend von den Ergebnissen ein weiteres Forschungskorpus aufgebaut wird, das nur die Texte enthält, die sich explizit mit der Spannischen Grippe beschäftigen. Diese Korpus könnte dann etwa in Hinblick auf Semantisierungen der Grippe untersucht werden, um so näher einzutauchen in die konkreten diskursiven Verhandlungen, mit denen die historische Pandemie begleitet wurde. 

2. Dass das **Forschungskorpus**, das den Analysen zurgundeliegt, auch ausgehend von pragmatischen Kriterien gebildet wurde, wurde [am entsprechenden Ort](corpus-collection_building-our-corpus) bereits bemerkt. Die Auswahl der beiden Tageszeitungen, zu denen wir vollständige Teil-Korpora aufgebaut haben, erfolgt dabei allein aufgrund von opportunistischen Kriterien, v.a. der Verfügbarkeit und der Prominenz der Zeitung. Wiederholende Forschung könnte hier ausgehend von systematischen Analysen der Berliner Zeitungslandschaft dieser Zeit einen Ansatz entwickeln, um ein repräsentatives Sample für das Korpus zu definieren oder auch eine balancierte Auswahl vorzunehmen. 


3. Wie wir bereits durch die [OCR-Evaluation](../ocr/ocr_ocr-quality) deutlich gemacht haben, ist die **Qualität der Volltexte im Korpus**, die als prozessiertes Forschungskorpus das epistemische Objekt unserer Studie bilden, dürftig. Um die Aussagekraft und die Präzision der Analyse zu erhöhen, müsste erheblich mehr Arbeit in die Verbesserung der Textqualität der Korpuselemente investiert werden. 


4. Für die **Korpusverarbeitung** wurde mit [spaCy ein Tool aus dem Natural Language Processing](../corpus_processing/corpus-processing_nlp-annotation) verwendet, das für die Verarbeitung von Gegenwartssprache optimiert ist. Wie gut dieses Tool auf der spezifischen Domäne ("Zeitungssprache des frühen 20. Jahrhunderts") operiert, die wir in unserem Projekt untersucht haben, ist nicht abschließend geklärt und könnte in Evaluationstests im Vorfeld geprüft werden.

5. Mit der [Methode der Berechnung von Worthäufigkeiten](../corpus_analysis/corpus-analysis_analysis) haben wir ein sehr simples Analyseverfahren gewählt. Das **Methodenspektrum der Digital Humanities** bietet hier eine ganze Reihe anderer Verfahren – etwa Topic Modelling oder die Arbeit mit Word Embeddings – die z.B. stärker auch die Kontextinformationen von Wörtern oder die Nähe von Wörtern berücksichtigen. Die Anwendung avancierter Methoden der computationellen Analyse von Texten könnte in diesem Sinne ebenfalls zur Erhöhung der Aussagekraft und der Präzision der Ergebnisse der vorliegenden Fallstudie beitragen.

Diese Punkte gilt es zu beachten, wenn es um die Einordnung der **Reichweite der Ergebnisse** geht. Dabei gilt für Digital Humanities-Projekte häufig, dass sie am Ende eine Abwegung vornehmen müssen zwischen 

- der Möglichkeit, Aussagen über – aus pragmatischer Sicht – menschlich unlesbar große Textmengen zu formulieren, auf der einen Seite 
- und der quantitativen Unschärfe wie der qualitativen Oberflächlichkeit dieser Aussage im Vergleich zu interpretativen, auf Einzeltext-Lektüre gründenden Aussagen auf der anderen Seite. 

Forschung in den Digital Humanities ist auch der stete Versuch, die Tradition qualitativen Fragens und Forschens mit den quantitativ-computationellen Methoden der Gegenwart zu vermitteln.

```{figure} ../assets/images/Embrace-the-light-and-the-dark-side.jpg
---
height: 30
name: Star Wars Meme: Embrace the light and dark side
---
```

