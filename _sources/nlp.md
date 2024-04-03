# Pre-Processing 

## Description
* Annotation of the text data
* Extraction of Sentences, Tokens, Lemma, PoS

## More to linguistic concepts
* Sentence
* Token
* Types
* Lemma
* PoS

## Data
* Input: txt
* Output: conll

## Metadata
* Input: Name, Year, Source
* Output: text length, sentence length, vocabulary size

## Tools
* Python Library [spacy](https://spacy.io/)

## Approach
1. Read in Data
2. Read in Metadata
3. Annotation of data with spacy
4. Extracttion of text specific metadata
5. Writing of annotated data as conll files
6. Writing of extended metadata
