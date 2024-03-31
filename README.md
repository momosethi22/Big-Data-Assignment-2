# Hadoop MapReduce Search Engine

This repository contains the codebase for a search engine developed using Hadoop MapReduce. The project focuses on efficient document indexing and retrieval using Term Frequency (TF), Inverse Document Frequency (IDF), and TF-IDF weights.

## Preprocessing
Preprocessing of the dataset was carried out in a Jupyter Notebook using pandas. To handle the large dataset effectively, preprocessing was performed in chunks of 10,000 rows to prevent Python kernel crashes.

## Term Frequency Calculation
Term Frequency (TF) was calculated using Hadoop MapReduce. This step involved counting the frequency of each term within each document.

## Inverse Document Frequency Calculation
Inverse Document Frequency (IDF) was computed through another MapReduce task. The output of the TF calculation step was utilized to determine the IDF values for each term.

## TF-IDF Weights Calculation
TF-IDF weights were calculated using a Python script since performing this operation directly in MapReduce posed challenges. The TF-IDF values were computed based on the TF and IDF values obtained earlier.

## Document Vectorization
Document vectors were generated for each document using MapReduce. This step involved transforming the TF-IDF weights into vector representations for efficient retrieval and similarity calculations.

## Collaborators
- Abdul Mohaiman (22i1882)
- Tayyab Kamran (22i2076)
- Abdullah Arif (22i1938)
