(corpus-analysis_intro)=
# Korpusanalyse. Von Häufigkeiten zu Diagrammen 
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
Sie können die auf einem Korpus ausgeführten Frequenzanalysen zu semantischen Feldern erklären und die Ergebnisse interpretieren
```

Für die Ausführung einer digitalen Analyse, in diesem Fall der Analyse der Spanischen Grippe in einem Berliner Zeitungskorpus (1918-20) durch Worthäufigkeiten über Zeit, wird ein Korpus benötigt, das in Wörter (Token) aufgeteilt und mit Lemmata angereichtert ist. Wir haben gezeigt, wie mittels OCR ein aus PDF-Dateien bestehendes Zeitungskorpus in ein Textkorpus konvertiert werden kann (siehe die Kapitel ["Korpusaufbau"](corpus-collection_intro) und ["OCR — Vom Bild zum Text"](ocr_intro)). Das Textkorpus wurde dann mit der Python-Bibliothek spaCy unter Anwendung von NLP-Methoden (Tokenisierung und Lemmatisierung) angereichtert (siehe Kapitel ["Korpusverarbeitung – Von Strings zu Token"](corpus-processing_intro)). Das angereichterte Korpus liegt im Tabellenformat (CSV) vor. In jeder Zeile steht ein Wort und die Grundform des Wortes.


```{figure} ../assets/images/flow-chart_corpus-analysis.jpeg
---
height:
name: Flussdiagramm der Fallstudie
---
Flussdiagramm der Fallstudie, das aktuelle Arbeitspaket ist hevorgehoben.
```

Nachdem die Korpuserstellung und -anreicherung abgeschlossen ist, wird in diesem Kapitel zur Forschungsfrage zurückgekehrt. Es soll die öffentliche Aufmerksamkeit für die spanische Grippe im Zeitaum von 1918-1920 an Hand von Worthäufigkeiten derjenigen Wörter gemessen werden, die direkt oder indirekt auf die spanische Grippe verweisen. Es wird zuerst konzeptionell in die Frequenzanalyse eingeführt, dann wird die Analyse mit folgenden Schritten durchgeführt:

1. Erstellung eines Wortfelds, in dem grippenbezogenen Wörter gesammelt werden
2. Berechnung der Häufigkeiten dieses Wortfelds 
3. Visuelle Darstellung der Häufigkeiten über Zeit durch ein Liniendiagramm. Das Diagramm hat verschiedene Stellschrauben:
 - Anzeige von absoluten oder relativen Häufigkeiten
 - Einstellung des zu betrachtenden Zeitraums
 - Filtern nach Zeitung 
4. Extraktion der Kontexte der grippenbezogenen Wörter (KWIC) für weiterführende manuelle Analysen

Zum Abschluss wird ein Fazit gezogen. 
