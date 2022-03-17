# Diabetes Project
This project aims to explore links between diabetes and cardiovascular diseases. Eventually, this analysis could lead to the development of a future application to follow patients with high risk of cardiovascular diseases through the assessment of their risk and recommendations to lower it.

## Organization
```
.
├── data 
├── data_cleaning
├── data_mining
├── datasets_exploration
├── diabetes_project.yml
├── README.md
└── reports
```

**data/**: data & documentation (source, link, etc) 

**data_cleaning/**: datasets cleaned for later purposes.

**data_mining/**: dataset analysis (PCA, clustering, etc.)

**data_exploration/**: overview of found datasets for this project. The objective was to analyze the relevance of multiple datasets for our use case


## Environment

**diabetes_project.yml** contains all the necessary libraries for this project.

You can create a conda environment from it with the following command:
```
conda env create --name <envname> --file diabetes_project.yml
```
