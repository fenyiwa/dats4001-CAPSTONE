# Genomic Patterns in Sickle Cell Modifier Variants

## Summary
Undergraduate Data Science capstone project examining how genetic modifier variants contribute to variability in sickle cell disease (SCD). The project integrates public variant databases with exploratory analysis and interpretable classification models to compare regulatory vs gene-body variation across key modifier loci.

## Research Question
How are known SCD modifier variants distributed across populations, and can basic genomic features (allele frequency and functional annotation complexity) distinguish intergenic regulatory variants from gene-body variants?

## Data
Public sources:
- **NIH dbSNP** (allele frequencies)
- **Ensembl Variant Browser** (variant annotations and functional consequences)

## Loci Analyzed
- **BCL11A**
- **HBS1L–MYB** (intergenic regulatory region)
- **KLF1**
- **HMOX1**

## Methods (High-Level)
- Curated SNP lists from literature and public databases
- Cleaned and merged variant annotations with population-coded allele frequencies
- Engineered features (mean allele frequency, functional annotation count, locus labels)
- Performed EDA and built interpretable classifiers (logistic regression; decision tree)

## Core Takeaways
- HBS1L–MYB regulatory variants show broader allele-frequency diversity and annotation complexity than gene-body loci.
- Simple genomic features can classify regulatory vs gene-body variant context with ~80% accuracy.
- Interpretable modeling supports biologically consistent separation between loci.

## Author
**Aba Pobee** — The George Washington University
