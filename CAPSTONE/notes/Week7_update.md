#  Week 7 Update

### Progress Summary
This week, I finally got the **HBS1L–MYB intergenic region** data working properly and cleaned after several attempts. Using the same dbSNP query structure as my previous genes, I merged and standardized the datasets for **HBS1L** and **MYB** to maintain consistency across all modifier genes (BCL11A, KLF1, HMOX1, and HBS1L–MYB).

### Data and Analysis
After cleaning, I generated some **basic visualizations** to compare allele frequencies across populations and to highlight common vs. rare variants within the intergenic region. These visual checks helped confirm that the final dataset aligns with patterns seen in the other modifier genes.

### Next Steps
I’m starting to think through what kind of predictive model makes the most sense for this project. Right now, I’m leaning toward two options. Model 1 would be a logistic regression that tries to classify samples or populations as having mild or severe disease outcomes based on variant frequencies. It’s simple and easy to interpret, which makes it a good starting point to see if any clear patterns show up.
Model 2 would be a random forest, which could capture more complex interactions between variants and give a clearer idea of which SNPs are the strongest predictors. My plan is to set up the datasets for both approaches, choose the main features to include, and start testing how well each model performs with the available data.