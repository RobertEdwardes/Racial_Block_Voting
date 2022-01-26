## Set of Tool for Racial Block Voting

#### Key Sources:
- Shaw v. Reno, 509 U.S. 630 (1993)
- Thornburg v. Gingles, 478 U.S. 30 (1986)

### Datasets
Census PL-94 Simplifed to Alabama CD116 7 and Whole County District Map 6 and 7
[Census PL-94 site](https://www.census.gov/programs-surveys/decennial-census/about/rdo/summary-files.html#P1)

Voting and Election Science Team, 2020, "2020 Precinct-Level Election Results", https://doi.org/10.7910/DVN/K7760H, Harvard Dataverse, V31
[Haravrd Datavser Precinct](https://dataverse.harvard.edu/dataverse/electionscience)


## Voter Power Index 

Shapley-Shubik and  Banzhaf Power are Power Indices that that help determin how much influnce an agent (voter or voter coliltion) has in an election system.

### Shapley-Shubik
The Shapley-Shubik Power Index of a voter is the number of permutations of the set of agent in which they are the pivotital vote.

[Wikipedia refercernce](https://en.wikipedia.org/wiki/Shapley%E2%80%93Shubik_power_index)

### Banzhaf Power
The Banzhaf Power Index of an agent is the number of winning coalitions that they belongs to and in which they is critical vote.

[Wikipedia refercernce](https://en.wikipedia.org/wiki/Banzhaf_power_index)

##  Vote Dilution Analysis Methods

### Homogeneous Precinct
Method to estimat voting behavior by race/ethnicity is to compare voting patterns in “homogeneous precincts” – that is, election precincts that are composed of a single racial/ethnic group.

### Ecological Regression
Method to estimate the voting patterns by race/ethnicity can be 
produced even when there are no homogeneous precincts.

##### Why Not Ecological Inference
Part of upcoming wiki
[Ecological Inference Falicy](https://en.wikipedia.org/wiki/Ecological_fallacy)

### TODO 
- [x] Notebooks
    - [x] Vote Power Indexes
    - [X] Bivariate Ecological Regression Analysis
    - [X] Homogeneous Precinct Analysis

- [X] Simplify AL_PL94 dataset to be under 100MB

- [X] pip packages
    - [X] work in progress
    - [X] Vote Power Indexes [Github Package URL](https://github.com/RobertEdwardes/Vote_Power_Indexes) / [Package](https://test.pypi.org/project/rpvVoterIndex/0.1.1/)
    - [X] Precinct Analysises [Github Package URL](https://github.com/RobertEdwardes/Racial_Polarized_Voting_Tools) / [Package](https://test.pypi.org/project/Racial-Polarized-Voting-Tools/0.1.0/)

- [] QGIS package
    - [] [Github Plug-in URL]
    - [] expermental flag
    - [] production flag
    - [] registraied with OSWG

- [] Wiki

