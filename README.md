# Check-It
Check-IT!: A Corpus of Expert Fact-checked Claims for Italian

## Reposity structure
- Paper

  Resources for our paper and its appendices
- Code
  
  Code files that cover the recovering and manipolation of the data presented in the paper

## Dataset versions
Not all the articles contain the same amount of informations, but (luckily) not all the tasks require all the informations!<br>To build a usefull dataset for different tasks we split the articles in different groups (some partially overlapping) based on the amount of informations contained in them.

Current versions are:
- d1: basic informations + statement and author of the statement
- d2: less details, it contains all the articles regardless of the informations missing
- d3: more refined, basic informations + statement, author of the statement, political party (or political body) of the author and platform on which the statement was shared.

We also had the opportunity to evaluate a different dataset, with data collected by another italian scolar through the same source (Pagella Politica), in a earlier version of the website.
Since this dataset adheres to the standard of version d1, we created two more versions:
- join_d1: d1 + older dataset
- join_d2 : d2 + older dataset

This leaves us with a total of **5** versions!
