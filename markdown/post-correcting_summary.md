# Resümee

:class: keypoint
* Korrekturansätze
Die Nachbearbeitung von OCR-Ergebnissen kann sowohl regelbasiert als auch mit KI-gestützten Methoden erfolgen, wobei jeder Ansatz spezifische Vor- und Nachteile aufweist.
* Messbare Verbesserungen
Die regelbasierte Korrektur führte zu einer nachweisbaren Qualitätsverbesserung, mit einem Anstieg des F1-Scores von 0.78 auf 0.82, was die Effektivität systematischer Nachbearbeitung demonstriert.
* Methodische Grenzen
Während regelbasierte Ansätze gut kontrollierbar sind, zeigen LLM-basierte Methoden zwar Potential, bringen aber auch erhebliche Herausforderungen mit sich, insbesondere hinsichtlich Ressourcenbedarf und Zuverlässigkeit.


### Summary 

Dieses Kapitel demonstrierte, wie die Ergebnisse von OCR [nachbearbeitet](post-correcting_ocr) werden können. Es führte [regelbasierte Nachkorrektur](data-input/FS_1_MVP_Post_Correcting_OCR) mit regulären Ausdrücken (in Python) ein und gab einen Einblick in die Möglichkeiten der [LLM-basierten Nachkorrektur](post-correcting_llm). Im nächsten Kapitel werden die nachkorrigierten Ergebnisse von OCR weiter mit NLP-Methoden verarbeitet.