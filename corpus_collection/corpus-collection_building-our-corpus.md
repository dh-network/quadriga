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

(corpus-collection_building-our-corpus)=
# Aufbau des Forschungskorpus
```{admonition} Groblernziel dieses Kapitels
:class: lernziele
Sie können den schrittweisen Prozess des praktischen Korpusaufbaus (Konzeptentwicklung, Metadatenerstellung und Datensammlung) am Beispiel eines Zeitungskorpus beschreiben.
```

Um das Korpus für unser Forschungsprojekt aufzubauen, müssen nun drei Punkte abgearbeitet werden: 
1. Das **Korpuskonzept**, also auch die Sammlungsstrategie, muss ausgearbeitet und im besten Fall in den Korpus-Metadaten festgehalten werden.
2. Die **Elemente des Korpus** müssen festgelegt und ebenfalls mit zumindest basalen Metadaten beschrieben werden.
3. Die **Sammlung der Elemente** muss durchgeführt werden. 


## 1. Korpuskonzept
Als Untersuchungsgegenstand wurde [oben](research-question_operationalization) "Texte in Berliner Tageszeitungen" angegeben, wobei wir uns auf den Zeitraum der Spanischen Grippe-Pandemie beschränken wollen. Als Zeitraum für die Spanische Grippe gibt <a href="https://en.wikipedia.org/wiki/Spanish_flu" class="external-link" target="_blank">Wikipedia</a> "February 1918 – April 1920" an. Ebenfalls auf <a href="https://de.wikipedia.org/wiki/Liste_Berliner_Tageszeitungen" class="external-link" target="_blank">Wikipedia</a> wird angegeben, dass es um 1925 in Berlin "30 Tageszeitungen" gab. Geht man nur von einer Ausgabe pro Tag aus (was wenig ist, da viele Zeitungen in dieser Zeit in Morgen- und Abendausgabe erscheinen), würde ein vollständiges Korpus für diesen Untersuchungsgegenstand 24.570 Ausgaben von Tageszeitungen umfassen. 
Bei unseren Recherchen haben wir als mögliche Quelle für die Korpuselemente das <a href="https://zefys.staatsbibliothek-berlin.de/" class="external-link" target="_blank">"ZEitungsinFormationssYStem der Staatsbibliothek zu Berlin"</a>, kurz "ZEFYS", identifiziert, das zu zahlreichen Berliner Tageszeitungen unseres Untersuchungszeitraums Bilddigitalisate (u.a. im PDF-Format) führt. Eine von uns durchgeführte Stichproben hat dabei ergeben, das dass PDF einer Ausgabe im Durchschnitt etwa 74 MB groß ist. Eine erste Grobschätzung für ein Korpus ergab damit eine Größe von 

```
24.570 x 75 MB = 1.818,18 GB
```
mithin fast 2 Terabyte. Ein solches Korpus ist pragmatisch kaum zu handhaben. Aus diesen pragmatischen Gründen kann unser Korpus also kein vollständiges sein; stattdessen haben wir uns für ein tendenziell balanciertes Korpus entschieden. 

Dieses Korpus konzentriert sich dabei 

- auf zwei renommierte Zeitungen, nämlich die <a href="https://zefys.staatsbibliothek-berlin.de/list/title/zdb/27112366/" class="external-link" target="_blank">Vossische Zeitung</a> und die <a href="https://zefys.staatsbibliothek-berlin.de/list/title/zdb/2719372X/" class="external-link" target="_blank">Berliner Morgenpost</a>, 
- wobei wir jeweils nur eine Ausgabe pro Tag und Zeitung nehmen, also im Falle von Morgen- und Abendausgabe eine von beiden auswählen, und
- uns auf den Zeitraum 1. Januar 1918 bis 31.12.1919 beschränken, also maximal 2 x 2 x 365 = 1.460 Ausgaben umfassen 

Das Korpus soll ausgehend von den über ZEFYS verfügbaren PDF-Dateien aufgebaut werden. Am Ende des weiter unten genauer erläuterten Korpusaufbau-Prozesses stand damit schließlich ein Korpus, das sich mit folgenden Metadaten beschreiben lässt: 

- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/title/" class="external-link" target="_blank">DC.title</a>**: "Zeitungskorpus zur Spanischen Grippe in Berlin, 1918/1919"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/description/" class="external-link" target="_blank">DC.description</a>**: "Sammlung sämtlicher verfügbarer Morgenausgaben der beiden Berliner Zeitungen "Vossische" und "Berliner Morgenpost aus den Jahren 1918 und 1919"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/creator/" class="external-link" target="_blank">DC.creator</a>**: "Henny Sluyter-Gäthje, Daniil Skorinkin, Peer Trilcke für QUADRIGA. Berlin-Brandenburgische Datenkompetenzzentrum für Digital Humanities und Verwaltungswissenschaft"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/publisher/" class="external-link" target="_blank">DC.publisher</a>**: <a href="https://zefys.staatsbibliothek-berlin.de/" class="external-link" target="_blank">"ZEitungsinFormationssYStem der Staatsbibliothek zu Berlin"</a>
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/date/" class="external-link" target="_blank">DC.date</a>**: "2024-06-01"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/format/" class="external-link" target="_blank">DC.format</a>**: "PDF"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/language/" class="external-link" target="_blank">DC.language</a>**: "Deutsch"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/subject/" class="external-link" target="_blank">DC.subject</a>**: "Geschichte, Medienwissenschaft"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/coverage/" class="external-link" target="_blank">DC.coverage</a>**: "1918-01-01 bis 1919-12-31, Berlin"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/identifier/" class="external-link" target="_blank">DC.identifier</a>**: "QUADRIGA\_FS-Text-01\_Data01_Corpus-Table"

## 2. Elemente des Korpus
Mit dem eben ausgeführten Korpuskonzept sind auch die Elemente des Korpus definiert. Wir entscheiden uns für ein basales Metadatenschema, das folgende Felder umfasst:

- ID: `DC.identifier`
- Name der Zeitung: `DC.publisher`
- Datum: `DC.date`
- URL mit Herkunft der Datei: `DC.source`

Navigiert man im ZEFYS-Portal, wird schnell die Struktur von deren Datenhaltung ersichtlich, die sich für die semi-automatische Erstellung einer die Korpus-Elemente beschreibenden Metadaten-Tabelle nutzen lässt. 

- Unter <a href="https://zefys.staatsbibliothek-berlin.de/list/title/zdb/27112366/-/1918/#jan" class="external-link" target="_blank">https://zefys.staatsbibliothek-berlin.de/list/title/zdb/27112366/-/1918/#jan</a> findet man z.B. eine Übersicht für den Monat Januar 1918. 
- Ruft man die Ausgabe vom 1. Januar 1918 auf, gelangt man zur Ansicht in einem Viewer: <a href="https://dfg-viewer.de/show/?set%5Bmets%5D=https://content.staatsbibliothek-berlin.de/zefys/SNP27112366-19180101-0-0-0-0.xml" class="external-link" target="_blank">https://dfg-viewer.de/show/?set%5Bmets%5D=https://content.staatsbibliothek-berlin.de/zefys/SNP27112366-19180101-0-0-0-0.xml</a> 
- Dort kann man über ein Klick in der oberen Menüleiste auch das gesamte PDF über einen API-Call zum Image Server der Staatsbibliothek aufrufen. Die dafür verwendete URL lautet <a href="https://content.staatsbibliothek-berlin.de/zefys/SNP27112366-19180101-0-0-0-0.pdf" class="external-link" target="_blank">https://content.staatsbibliothek-berlin.de/zefys/SNP27112366-19180101-0-0-0-0.pdf</a> 

Wie Stichproben zeigen, werden die Links des ZEFYS-Portals erfreulich systematisch gebildet. Sie setzen sich zusammen aus 

- `https://content.staatsbibliothek-berlin.de/zefys/` – Angabe des Image-Servers und dem Endpunkt für ZEFYS
- `SNP27112366` – einer Zeichenkette mit der ID der Zeitung
- `19180101` – einer Zeichenkette für das Datum
- `0-0-0-0` – einer Zeichenkette, die die Ausgabe benennt; weitere Ausgaben weisen die Zeichenkette `1-0-0-0` etc. auf. ZEFYS vergibt in der Regel `0-0-0-0` für die Morgenausgabe. Wir nehmen stehts die `0-0-0-0`-Datei. 

Die Analyse der ZEFYS API macht es möglich, unsere Metadaten-Tabelle semi-automatisch etwa mit Excel oder Open Office zu befüllen. Ausgehend vom 

- Wissen über die ID der Zeitung (`SNP27112366` für die "Vossin" und `SNP2719372X` für die "Berliner Morgenpost"), 
- unserer Festlegung des Zeitraums, also Daten von `19180101` bis `19191231`
- und der Kenntnis der anderen Link-Bestandteile 

können wir die URLs bauen und parallel die anderen Datenfelder befüllen. Die so entstehende Tabelle sieht folgendermaßen aus: 

| DC.identifier                        | DC.publisher        | DC.date     | DC.source                                                                          |
|--------------------------------------|---------------------|-------------|------------------------------------------------------------------------------------|
| SNP2719372X-19180101-0-0-0-0         | Berliner Morgenpost | 1918-01-01  | [https://content.staatsbibliothek-berlin.de/zefys/SNP2719372X-19180101-0-0-0-0.pdf](https://content.staatsbibliothek-berlin.de/zefys/SNP2719372X-19180101-0-0-0-0.pdf) |
| SNP2719372X-19180102-0-0-0-0         | Berliner Morgenpost | 1918-01-02  | [https://content.staatsbibliothek-berlin.de/zefys/SNP2719372X-19180102-0-0-0-0.pdf](https://content.staatsbibliothek-berlin.de/zefys/SNP2719372X-19180102-0-0-0-0.pdf) |
| SNP2719372X-19180103-0-0-0-0         | Berliner Morgenpost | 1918-01-03  | [https://content.staatsbibliothek-berlin.de/zefys/SNP2719372X-19180103-0-0-0-0.pdf](https://content.staatsbibliothek-berlin.de/zefys/SNP2719372X-19180103-0-0-0-0.pdf) |
| SNP2719372X-19180104-0-0-0-0         | Berliner Morgenpost | 1918-01-04  | [https://content.staatsbibliothek-berlin.de/zefys/SNP2719372X-19180104-0-0-0-0.pdf](https://content.staatsbibliothek-berlin.de/zefys/SNP2719372X-19180104-0-0-0-0.pdf) |
| …                                    | …                   | …           | …                                                                                  |
| SNP27112366-19180101-0-0-0-0         | Vossische Zeitung           | 1918-01-01  | [https://content.staatsbibliothek-berlin.de/zefys/SNP27112366-19180101-0-0-0-0.pdf](https://content.staatsbibliothek-berlin.de/zefys/SNP27112366-19180101-0-0-0-0.pdf) |
| SNP27112366-19180102-0-0-0-0         | Vossische Zeitung          | 1918-01-02  | [https://content.staatsbibliothek-berlin.de/zefys/SNP27112366-19180102-0-0-0-0.pdf](https://content.staatsbibliothek-berlin.de/zefys/SNP27112366-19180102-0-0-0-0.pdf) |
| SNP27112366-19180103-0-0-0-0         | Vossische Zeitung           | 1918-01-03  | [https://content.staatsbibliothek-berlin.de/zefys/SNP27112366-19180103-0-0-0-0.pdf](https://content.staatsbibliothek-berlin.de/zefys/SNP27112366-19180103-0-0-0-0.pdf) |
| SNP27112366-19180104-0-0-0-0         | Vossische Zeitung           | 1918-01-04  | [https://content.staatsbibliothek-berlin.de/zefys/SNP27112366-19180104-0-0-0-0.pdf](https://content.staatsbibliothek-berlin.de/zefys/SNP27112366-19180104-0-0-0-0.pdf) |

```{code-cell} python3
import pandas as pd
df = pd.read_csv("../data/metadata/QUADRIGA_FS-Text-01_Data01_Corpus-Table.csv", sep=";")
df.head()
```

Die vollständige CSV-Datei kann [hier](https://github.com/dh-network/quadriga/blob/ec3334a4b18750e5bb10c25b2badcbfbbf18592c/data/metadata/QUADRIGA_FS-Text-01_Data01_Corpus-Table.csv) heruntergeladen werden.

## 3. Sammlung der Elemente
Die CSV-Datei, die sämtliche Elemente Korpus aufführt, listet auch jeweils einen Link zur PDF-Datei des Korpus. Dieser Link hat stets die Form: 

```
https://content.staatsbibliothek-berlin.de/zefys/SNP2719372X-19180101-0-0-0-0.pdf

```
Ruft man den [Link](https://content.staatsbibliothek-berlin.de/zefys/SNP2719372X-19180101-0-0-0-0.pdf) etwa im Browser auf, wird die PDF angezeigt oder heruntergeladen. Auf diese Weise ließen sich sukzessive, Klick für Klick, sämtliche Elemente des Korpus sammeln. Dieser Prozess kann dabei automatisiert werden. 

Dafür erstellen wir aus der CSV-Datei zunächst eine einfache Link-Liste mit allen Links und speichern diese als TXT-Datei, der wir in unserem Fall den Dateinamen "QUADRIGA_FS-Text-01_Data01_Link-List.txt" geben. Diese Datei lässt sich [hier](https://github.com/dh-network/quadriga/blob/ec3334a4b18750e5bb10c25b2badcbfbbf18592c/data/metadata/QUADRIGA_FS-Text-01_Data01_Link-List.txt) herunterladen.

Sofern Sie mit der PowerShell (Windows) oder dem Terminal Ihres Computers umgehen können, können Sie nun Folgendes machen: Legen Sie Link-Liste in einem Ordner ab und navigieren Sie in der PowerShell/im Terminal in diesen Ordner. 

Mac-Nutzer-innen führen nun folgenden Befehl aus: 
```
xargs -n 1 curl -O < QUADRIGA_FS-Text-01_Data01_Link-List.txt
```
Windows-Nutzer:innen führen in der PowerShell folgenden Befehl aus

```
Get-Content QUADRIGA_FS-Text-01_Data01_Link-List.txt | ForEach-Object {
    Invoke-WebRequest -Uri $_ -OutFile (Split-Path $_ -Leaf)
}
```

Es startet ein Download, der – sofern er komplett durchläuft - am Ende 1.328 Dateien im Umfang von 104,7 GB einsammelt. 

Dies ist unser Forschungskorpus 🚀


