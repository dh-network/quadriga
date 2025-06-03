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
```{admonition} Groblernziel dieses Kapitels
:class: lernziele
Sie kennen unterschiedliche Verfahren der Nachbearbeitung von OCR-Output zur Qualitätsverbesserung.
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
