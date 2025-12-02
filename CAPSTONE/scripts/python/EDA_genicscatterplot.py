import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("modifier_snps_model_dataset.csv")

df['region_label'] = df['genic'].map({0: 'Intergenic (HBS1L-MYB)',
                                      1: 'Genic (BCL11A/KLF1/HMOX1)'})

plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x='mean_AF',
    y='function_class_count',
    hue='region_label',
    alpha=0.7,
    s=60
)

plt.title("Allele Frequency vs Functional Annotation Count\nGenic vs Intergenic Variants")
plt.xlabel("Mean Allele Frequency")
plt.ylabel("Function Class Count")
plt.legend(title="Region Type")
plt.tight_layout()
plt.show()