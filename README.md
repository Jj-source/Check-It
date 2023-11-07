# CheckIt!

This repository continas the data and code for the paper "CheckIT!: A Corpus of Expert Fact-checked Claims for Italian" - presented at the 9th Italian Conference on Computational Linguistics

## Repository structure
- Paper

  Resources for our paper and its appendices
- Code
  
  Code files that cover the recovering and manipolation of the data presented in the paper
- Data

  The final versions of the dataset,<br>Files with label distribution for each politician and political party mentioned in the data,<br>The raw data from Pagella Politica and other sources

## Dataset versions
Not all the articles contain the same amount of informations, but (luckily) not all the tasks require all the informations!<br>To build a usefull dataset for different tasks we split the articles in different groups (some partially overlapping[^1]) based on the amount of informations contained in them.

Current versions are:
- d1: basic informations + statement and author of the statement
- d2: less details, it contains all the articles regardless of the informations missing
- d3: more refined, basic informations + statement, author of the statement, political party (or political body) of the author and platform on which the statement was shared.

We also had the opportunity to evaluate a different dataset, with data collected by another italian scolar through the same source (Pagella Politica), in a earlier version of the website. Since this dataset adheres to the standard of version d1, we created two more versions:
- join_d1: d1 + older dataset
- join_d2 : d2 + older dataset

This leaves us with a total of **5** versions! The version used for the expriments is XXX (stored in YYY)

# Data Statement for CheeckIt! v1.0

Data set name: CheckIT!: A Corpus of Expert Fact-checked Claims for Italian V1.0

Citation (if available):

```
@inproceedings{
}
```

Data set developer(s): Jacopo Gili, Tommaso Caselli, Lucia Passaro

Data statement author(s): Tommaso Caselli

Others who contributed to this document: 


## A. CURATION RATIONALE 

The corpus is composed by fact-checked claims of Italian politicians. Claims have been collectd from different sources by [Pagella Politica](https://pagellapolitica.it), an Italian fact-checking organization. Each claim is accompanied by a veracity verdict and a fact-checking evidence text. 

The corpus has been collected using the public APIs from [Pagella Politica](https://pagellapolitica.it). 

Time periods: The data collected covers 11 years, from October, 3 2012 until April, 26 2023.

The corpus is accompanied by a set of 357 claims that have been manually paraphrased by three annotators (all authors of the accompanying paper). The paraphrases of the claim per annotator are stored in the folder (/Paraphrases/)[https://github.com/Jj-source/Check-It/tree/main/Paraphrases].

## B. LANGUAGE VARIETY/VARIETIES

* BCP-47 language tag: it
* Language variety description: Italian

## C. SPEAKER DEMOGRAPHIC

N/A
 
## D. ANNOTATOR DEMOGRAPHIC

Annotator #1: Age: 22; Gender: male; Race/ethnicity: caucasian; Native language: Italian; Socioeconomic status: middle-class Training in linguistics/other relevant discipline: graduating in Computer Science, with a specialization in Natural Language Processing 

Annotator #2: Age: 42; Gender: male; Race/ethnicity: caucasian; Native language: Italian; Socioeconomic status: upper middle-class; Training in linguistics/other relevant discipline: PhD in Computational Linguistics

 Annotator #3: Age: 35; Gender: female; Race/ethnicity: caucasian; Native language: Italian; Socioeconomic status: middle-class; Training in linguistics/other relevant discipline: PhD in Information Engineering


## E. SPEECH SITUATION

N/A

## F. TEXT CHARACTERISTICS

Claim by politicians; a (short) messages in written form of varying length on different topics uttered by an Italian politician in any context (palamentary debate, written interview with a newspaper; participation in a talk-show, message in any Social Media platform).

Fact-checking evidence; a long text that it is used to determine the veracity value of the claim of the politicians; they are written by professional fact-checkers; they may contain multimedia materials, external URL links, and mentions of other politicians. 

Veracity labels; short texts of one word corresponding to the associated veracity value assigned by the professional fact-checkers; values have been simplified to three (Vero [True]; Falso [False]; Impreciso [Imprecise]) from the original five classes used by the professional fact-checkers. As of June 2020, the fact-checkers do not use anymore labels but verbose explanations. For all data from June 2020, we have manually mapped the verbose explanation to the three labels.

## G. RECORDING QUALITY

N/A

## About data statement document

A [data statement](https://www.aclweb.org/anthology/Q18-1041/) is a characterization of a dataset that provides context to allow developers and users to better understand how experimental results might generalize, how software might be appropriately deployed, and what biases might be reflected in systems built on the software.

Data Statements are from the University of Washington. Contact: [datastatements@uw.edu](mailto:datastatements@uw.edu). The markdown Data Statement we used is from June 4th 2020. The Data Statement template is based on worksheets distributed at the [2020 LREC workshop on Data Statements](https://sites.google.com/uw.edu/data-statements-for-nlp/), by Emily M. Bender, Batya Friedman, and Angelina McMillan-Major. Adapted to community Markdown template by Leon Dercyznski.

[^1]: d2 being the least detailed contains all of the available articles. d1 is a subset of d2. d3 is a subset of d1.<br>d2 ⊆ d1 ⊆ d3
