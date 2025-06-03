(corpus-processing_intro)=
# Einführung
```{admonition} Groblernziel dieses Kapitels
:class: lernziele
Sie kennen Verfahren der Korpusverarbeitung mit Tools des Natural Language Processing und können Schritte zur Anwendung der Tools zur Tokenisierung und Lemmatisierung benennen.
```

## Zu diesem Kapitel
Für die Ausführung einer digitalen Analyse, in diesem Fall die Analyse von Worthäufigkeiten über Zeit, wird ein über die Zeit gestreutes Korpus benötigt, das im txt-Format (oder einem anderen, computerlesbaren Format) vorliegt. Wir haben gezeigt, wie ein aus PDF-Dateien bestehendes Zeitungskorpus (siehe Kapitel ["Korpusaufbau"](corpus-collection_intro)) mittels OCR verarbeitet werden kann (siehe Kapitel ["OCR — Vom Bild zum Text"](ocr_intro)), sodass das resultierende Korpus aus Textdateien (mit Dateiendung '.txt') besteht.

```{figure} ../book_images/flow-chart_corpus-processing.jpeg
---
height:
name: Flussdiagramm der Fallstudie
---
Flussdiagramm der Fallstudie, das aktuelle Arbeitspaket ist hevorgehoben.
```

Die im Korpus enthaltenen Textdateien werden jetzt mit linguistischen Informationen angereichert. Zuerst wird konzeptionell in die Methoden der Anreicherung eingeführt (Tokenisierung und Lemmatisierung), dann wird kurz darauf eingegangen, welche Möglichkeiten es in Python für die Anreicherung gibt. Im nächsten Schritt wird gezeigt, wie mit Hilfe von spaCy das Zeitungskorpus annotiert werden kann. Zum Schluss wird ein Resümee gezogen.
