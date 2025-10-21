# 🧬 Week 4/5 Update

### Reflection
I realized I was overcomplicating my workflow... there are online tools that streamline a lot of what I was trying to do manually. I started using **NCBI’s dbSNP** and **Genome Data Viewer**, which has made it much easier to explore and visualize genetic variation.

---

### Project Goal
I spent too much time diving into the BCL11A gene and realized maaybe making a quickstart was not necessary... basically scrapping my week 3 progress. I had to remind myself of my project goal. Even though all SCD patients share the HbS mutation, disease severity varies. Modifier genes like **BCL11A**, **HBS1L-MYB**, **KLF1**, and **HMOX1** influence fetal hemoglobin (HbF) levels, oxidative stress, and other protective factors.  
**Goal:** Map how these variants are distributed across populations.

---

### Data Sources
- **1000 Genomes Project** – VCF files with SNPs by population  
- **gnomAD** – Allele frequencies across continental ancestries  
- **dbSNP / Ensembl Variant Browser** – Variant annotation and validation  

---

### Methods / Workflow
1. Identify modifier SNPs from literature.  
2. Extract allele frequencies from 1000 Genomes & gnomAD.  
3. Compare frequencies across populations (African, European, South Asian, admixed).  
4. Create visualizations (heatmaps, bar plots, PCA).  
5. Interpret results in the context of clinical severity variation.

---

### Deliverables
- Allele frequency maps showing protective vs. risk alleles.  
- PCA plots of haplotype differences.  
- Discussion on genetic risk landscapes across populations.

---

### Technical Progress
- Located and cleaned relevant SNP data for **BCL11A**, **KLF1**, and **HMOX1**.  
- Still finalizing data extraction for the **HBS1L-MYB** region.  
- Using GRCh38.p14 assembly and validated filtering criteria in dbSNP.  
- Configured NCBI Variation Viewer to focus on relevant tracks (RefSeq annotation, structural variants).  

---

### Next Steps
- Complete data collection for **HBS1L-MYB**.  
- Conduct exploratory data analysis (EDA).  
- Begin incorporating **predictive modeling** to analyze how variant combinations influence disease severity across populations.
