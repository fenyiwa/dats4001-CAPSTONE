import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("modifier_snps_model_dataset.csv")

plt.figure(figsize=(10,6))
sns.boxplot(x='locus', y='mean_AF', data=df)
plt.title("Allele Frequency by Locus")
plt.xlabel("Locus")
plt.ylabel("Mean Allele Frequency")
plt.xticks(rotation=45)
plt.show()


