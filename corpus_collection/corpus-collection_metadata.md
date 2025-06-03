(corpus-collection_metadata)=
# Metadaten
```{admonition} Feinlernziel(e) dieses Kapitels
:class: lernziele
Sie können die grundlegenden Metadatenschemata (Dublin Core, TEI, MODS, METS) und deren charakteristische Elemente für Korpora und Einzeldokumente beschreiben.
```

Metadaten sind Daten über Daten. Sie liefern kontextuelle Informationen, die helfen, die Bedeutung, Herkunft, Struktur und Nutzungsmöglichkeiten eines Datensatzes besser zu verstehen. In den Digital Humanities sind Metadaten unerlässlich, um die Volltextkorpora systematisch zu organisieren, auffindbar zu machen und deren inhaltliche und strukturelle Qualität zu sichern.

**Metadatenschemata**

Es gibt verschiedene Metadatenschemata, die entwickelt wurden, um spezifische Anforderungen unterschiedlicher Disziplinen und Anwendungen zu erfüllen. Zu den bekanntesten gehören:

1. **[Dublin Core](https://www.dublincore.org/specifications/dublin-core/dces/)**: Ein einfaches und weit verbreitetes Schema, das 15 grundlegende Elemente umfasst, wie Titel, Autor, Thema und Datum.
2. **[TEI (Text Encoding Initiative)](https://tei-c.org/)**: Speziell für Texte entwickelt, bietet TEI detaillierte Richtlinien zur Auszeichnung von Texten und zur Erfassung von deren Metadaten im [`<teiHeader>`](https://tei-c.org/release/doc/tei-p5-doc/de/html/ref-teiHeader.html).
3. **[MODS (Metadata Object Description Schema)](https://www.loc.gov/standards/mods/)**: Von der Library of Congress entwickelt, bietet MODS eine umfangreichere Beschreibung als Dublin Core und ist besonders für bibliographische Informationen geeignet.
4. **[METS (Metadata Encoding and Transmission Standard)](https://www.loc.gov/standards/mets/)**: Ein Standard zur Kodierung und Übertragung von Digitalisaten und deren Metadaten, häufig in Bibliotheken und Archiven verwendet.

## Metadaten zur Beschreibung eines Korpus

Bei der Beschreibung eines gesamten Korpus sind die Metadaten entscheidend, um den Kontext, den Umfang und die Struktur des Korpus zu dokumentieren. Wichtige Aspekte sind unter anderem:

- **Titel und Beschreibung**: Um das Korpus eindeutig zu identifizieren und dessen Inhalt zu beschreiben.
- **Ersteller:innen und/oder Herausgeber:innen**: Angaben zu den Personen oder Institutionen, die das Korpus erstellt und veröffentlicht haben.
- **Datum**: Zeitangaben zur Erstellung und Veröffentlichung des Korpus.
- **Umfang und Format**: Informationen über die Anzahl der enthaltenen Dokumente und deren Dateiformate.
- **Sprache**: Die im Korpus vertretenen Sprachen.
- **Thematik und Schlagworte**: Stichworte, die die inhaltlichen Schwerpunkte des Korpus beschreiben.

**Beispiel unter Verwendung Dublin Core**

Ein beispielhaftes Metadaten-Set für ein Korpus könnte unter Verwendung von Dublin Core so aussehen:

- **[DC.title](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/title/)**: "Zeitungskorpus zur Spanischen Grippe in Berlin, 1918/1919"
- **[DC.description](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/description/)**: "Eine Sammlung digitalisierter Zeitungsartikel aus deutschen Zeitungen mit Erscheinungsort Berlin aus den Jahren 1918 und 1919"
- **[DC.creator](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/creator/)**: "Henny Sluyter-Gäthje, Daniil Skorinkin, Peer Trilcke für QUADRIGA. Berlin-Brandenburgische Datenkompetenzzentrum für Digital Humanities und Verwaltungswissenschaft"
- **[DC.publisher](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/publisher/)**: "["ZEitungsinFormationssYStem der Staatsbibliothek zu Berlin"](https://zefys.staatsbibliothek-berlin.de/)" 
- **[DC.date](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/date/)**: "2024-06-01"
- **[DC.format](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/format/)**: "PDF, TXT, CSV"
- **[DC.language](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/language/)**: "Deutsch"
- **[DC.subject](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/subject/)**: "Geschichte, Medienwissenschaft"
- **[DC.coverage](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/coverage/)**: "20. Jahrhundert, Deutschland"

## Metadaten für einzelne Korpus-Elemente

Für einzelne Elemente eines Korpus, wie beispielsweise einzelne Artikel oder Dokumente, sind spezifische Metadaten notwendig, um diese präzise zu identifizieren und zu kontextualisieren. Wichtige Metadaten umfassen hier z.B.:

- **Titel und Autor:innen**: Um das Dokument eindeutig zu identifizieren.
- **Datum der Veröffentlichung**: Für zeitliche Einordnung.
- **Quelle**: Angaben zur ursprünglichen Publikation oder Fundort.
- **Sprache**: Die im Dokument verwendete Sprache.
- **Identifier**: Ein eindeutiger Identifikator wie eine DOI oder eine andere Art von Kennung.

**Beispiel unter Verwendung von Dublin Core**

Für einen einzelnen Zeitungsartikel könnten die Metadaten so aussehen:

- **[DC.title](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/title/)**: "Die Grippe wütet weiter"
- **[DC.creator](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/creator/)**: "N.N."
- **[DC.date](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/date/)**: "1918-10-15"
- **[DC.publisher](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/source/)**: "Berliner Morgenpost"
- **[DC.subject](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/subject/)**: "Spanische Grippe"
- **[DC.coverage](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/coverage/)**: "1918, Berlin"
- **[DC.language](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/language/)**: "Deutsch"
- **[DC.identifier](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/identifier/)**: "SNP2719372X-19181015-0-0-0-0"

Durch die sorgfältige Erfassung und Verwaltung von Metadaten auf beiden Ebenen – sowohl für das gesamte Korpus als auch für einzelne Elemente – wird die Nutzbarkeit und Nachnutzbarkeit von Forschungsdaten in den Digital Humanities erheblich verbessert. Dies trägt zur besseren Auffindbarkeit, Nachvollziehbarkeit und langfristigen Erhaltung der Daten bei.
