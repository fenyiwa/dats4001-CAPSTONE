import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("modifier_snps_model_dataset.csv")

plt.figure(figsize=(8,5))
sns.histplot(df['function_class_count'], bins=20, kde=False)
plt.title("Distribution of Functional Annotation Count")
plt.xlabel("Function Class Count")
plt.ylabel("Count")
plt.show()
