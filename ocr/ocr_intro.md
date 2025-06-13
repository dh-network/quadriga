(ocr_intro)=

# OCR. Von Bild zu Text

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
```{admonition} OCR-basierte Korpuserstellung und Qualitätsbewertung
:class: lernziele

1. Der Prozess der Optical Character Recognition (OCR) für die Korpuserstellung kann beschrieben und Tools zur Durchführung der OCR aufgezählt werden.

2. Die notwendigen Schritte zur Verarbeitung ein- und mehrseitiger PDFs zu Text können aufgezählt und die Unterschiede zwischen Ursprungs- und Zielformat erklärt werden.

3. Die grundlegenden Metriken zur OCR-Qualitätsevaluation (Präzision, Recall, F1-Score) können erläutert und deren Bedeutung für die Bewertung von OCR-Systemen beschrieben werden.

4. Die Schritte zur Qualitätsmessung eines OCR-Outputs können aufgezählt und die Qualitätsmaße interpretiert werden.
```

Nach dem vorherigen [Kapitel](../corpus_collection/corpus-collection_summary) haben wir also ein Korpus als Sammlung gescannter Bilder. Ein Korpus in dieser Form ist jedoch noch **nicht maschinenlesbar** und kann nicht direkt verarbeitet werden. In diesem Kapitel lernen wir, wie man mit OCR **Bilder in Text umwandelt**.

```{figure} ../assets/images/flow-chart_ocr.jpeg
---
height:
name: Flussdiagramm der Fallstudie
---
Flussdiagramm der Fallstudie. Wir befinden uns im dritten Arbeitspaket.
```
Zunächst werden wir lernen, [was OCR ist](ocr), warum wir es brauchen und wie es funktioniert. Außerdem werden wir einen Überblick über einige OCR-Tools geben.

Anschließend werden wir [OCR in Python mit PyTesseract](https://dh-network.github.io/quadriga/data-input/FS_1_MVP_OCR) durchführen, einem kostenlosen und quelloffenen OCR-Tool.

Schließlich werden wir die Metriken kennenlernen, die zur Messung der [OCR-Qualität](ocr-quality) verwendet werden, und [Qualitätsmessungen](https://dh-network.github.io/quadriga/data-input/FS_1_MVP_OCR_Quality) durchführen.
