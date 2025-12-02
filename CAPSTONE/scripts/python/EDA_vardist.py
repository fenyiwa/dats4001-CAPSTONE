import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("modifier_snps_model_dataset.csv")

plt.figure(figsize=(8,5))
sns.countplot(x='variant_type', data=df)
plt.title("Distribution of Variant Types")
plt.xlabel("Variant Type")
plt.ylabel("Count")
plt.show()