import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("modifier_snps_model_dataset.csv")

plt.figure(figsize=(8,5))
sns.boxplot(x='genic', y='mean_AF', data=df)
plt.title("Allele Frequency: Genic vs Intergenic Variants")
plt.xlabel("Genic (1) vs Intergenic (0)")
plt.ylabel("Mean Allele Frequency")
plt.show()
