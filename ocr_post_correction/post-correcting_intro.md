(post-correcting_intro)=
# OCR-Nachbereitung. Manuell, automatisch, LLMs

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
```{admonition} OCR-Nachbearbeitung und Qualitätsverbesserung
:class: lernziele

1. Verschiedene Verfahren der OCR-Nachbearbeitung können beschrieben und deren Einsatzzwecke unterschieden werden.

2. Regelbasierte Ansätze zur OCR-Nachkorrektur können beschrieben und deren Auswirkungen auf die OCR-Qualität anhand von Metriken erläutert werden.

3. Die grundlegenden Herausforderungen beim Einsatz von Large Language Models für die OCR-Nachbearbeitung können beschrieben werden.
```

Im vorigen [Kapitel](ocr) haben wir die Scans der Zeitungen per OCR automatisch in Klartext umgewandelt. In diesem Kapitel werden wir die Ergebnisse der OCR nachbearbeiten. 

```{figure} ../assets/images/flow-chart_ocr-postprocessing.jpeg
---
height:
name: Flussdiagramm der Fallstudie
---
Flussdiagramm der Fallstudie. Wir befinden uns im vierten Arbeitspaket.
```

Wie Sie [bereits wissen](../ocr/ocr_ocr-quality), sind OCR-Ergebnisse selten perfekt. Dies gilt insbesondere für historische Texte. Daher ist in der Regel eine Nachbearbeitung erforderlich, um die üblichen Fehler zu korrigieren.
