# Resümee

```{admonition} Key points des Kapitels
:class: keypoint
**Vom Tool zur Methode**

Die [Optical Character Recognition](ocr) (OCR) ist ein entscheidender Schritt bei der Erstellung maschinenlesbarer Korpora aus Bilddaten. Dabei zeigt sich, dass die Wahl der OCR-Lösung stark vom spezifischen Anwendungsfall abhängt – während integrierte OCR-Funktionen in PDF-Viewern für einzelne Dokumente ausreichen können, erfordern umfangreiche Korpusprojekte spezialisierte Tools wie Tesseract.

**Qualität als zentraler Aspekt**

Besonders wichtig ist das Verständnis der [OCR-Qualität](ocr-quality): Die Metriken Precision, Recall und F1-Score ermöglichen eine systematische Bewertung der Texterkennung. Dabei wurde deutlich, dass besonders bei historischen Dokumenten wie Zeitungen in Frakturschrift moderate Werte um 0.78-0.79 zu erwarten sind, was für bestimmte Anwendungen wie Volltextsuche ausreichend sein kann, für andere wie kritische Editionen jedoch nicht.

**Prozesscharakter der OCR**

Die [praktische Durchführung](../data-input/FS_1_MVP_OCR) der OCR muss als mehrstufiger Prozess verstanden werden, bei dem die eigentliche Texterkennung nur einen Schritt darstellt. Die Qualitätskontrolle und eventuelle Nachkorrektur sind integrale Bestandteile des Workflows.
```

<!-- 
Dieses Kapitel führte [OCR](ocr) als Methode zur maschinellen Lesbarkeit Ihres Korpus ein. Es zeigte, wie [OCR in Python](../data-input/FS_1_MVP_OCR) durchgeführt werden kann und wie die [Qualität der OCR](ocr-quality) bewertet werden kann. Das nächste Kapitel wird sich der Nachkorrektur der OCR-Ergebnisse widmen.
-->