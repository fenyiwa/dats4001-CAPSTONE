import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("modifier_snps_model_dataset.csv")

plt.figure(figsize=(8,6))
sns.scatterplot(x='mean_AF', y='function_class_count', hue='locus', data=df)
plt.title("Allele Frequency vs Functional Annotation Count")
plt.xlabel("Mean Allele Frequency")
plt.ylabel("Function Class Count")
plt.show()
