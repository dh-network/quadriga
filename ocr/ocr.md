# OCR als Methode, um Text maschinenlesbar zu machen

**Optical Character Recognition (OCR)** ist eine Technologie, die es ermöglicht, gedruckten oder handgeschriebenen Text in Dokumenten oder Bildern in maschinenlesbaren Text umzuwandeln. OCR-Software analysiert das Layout des Dokuments, erkennt die Formen der Buchstaben und Zahlen und wandelt diese in digitale Texte um, die weiterverarbeitet werden können.

```{figure} ../assets/images/grippeocr.gif
---
height: 300px
name: OCR
```

### Warum benutzen wir OCR?

1. **Digitalisierung von Dokumenten**: OCR ermöglicht die Umwandlung von physischen Dokumenten in digitale Formate, wodurch Speicherplatz gespart und der Zugriff auf Informationen erleichtert wird.

2. **Suchbarkeit**: Texte in Bildern oder gescannten Dokumenten können nach der OCR-Verarbeitung durchsucht werden. Dies erleichtert das Auffinden von Informationen in großen Dokumentensammlungen.

3. **Bearbeitbarkeit**: Mit OCR umgewandelte Texte können bearbeitet und weiterverarbeitet werden. Dies ist besonders nützlich für die Aktualisierung oder Korrektur von Dokumenten.

4. **Automatisierung**: OCR ermöglicht die Automatisierung vieler Prozesse, wie z.B. die Verarbeitung von Formularen, Rechnungen oder anderen Dokumenten in Unternehmen. Dies spart Zeit und reduziert menschliche Fehler.

5. **Barrierefreiheit**: OCR kann dabei helfen, gedruckte Texte für sehbehinderte Menschen zugänglich zu machen, indem die Texte in eine digitale Form gebracht und dann mittels Screenreadern vorgelesen werden.

6. **Archivierung und Langzeitlagerung**: Durch die Digitalisierung und OCR können wichtige Dokumente sicher archiviert und langfristig gespeichert werden, ohne dass sie an Qualität verlieren.


### Welche Software verwenden wir um OCR auszuführen

Die OCR-Technologie wird zunehmend in grundlegende Softwareanwendungen, wie z. B. verschiedene PDF-Viewer-Programme, integriert. Tools wie MacOS 'Preview' oder Adobe Acrobat verfügen über integrierte OCR-Funktionen. Diese sind jedoch nicht für die **Massenverarbeitung von Korpora** geeignet. Daher benötigt man nach wie vor **spezialisierte OCR-Software** oder Programmpakete, um **große Mengen an Bildern/PDFs** in maschinenlesbare Korpora zu verarbeiten.

#### Spezialisierte OCR-Tools

Das Feld der OCR-Tools entwickelt sich rasant (zusammen mit allen anderen Bereichen der Textverarbeitung), sodass es immer neue Tools gibt, die die alten herausfordern. Aber Stand 2024 waren die bekannten Produkte:

* FineReader (Closed Source, kommerziell)
* Tesseract (Open Source)
* OCR4all (Open Source)
* Kraken & e-Scriptorium (Open Source)
* EasyOCR (Open Source)

#### OCR in Python mit PyTesseract

In diesem Tutorial werden wir OCR mit **Tesseract** durchführen, das offen und kostenlos ist. Wir verwenden das Python-Paket **PyTesseract**.
