import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("modifier_snps_model_dataset.csv")

# Features + target
X = df[['mean_AF', 'function_class_count']]
y = df['genic']     # 0 = intergenic, 1 = genic

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
log_reg = LogisticRegression()
log_reg.fit(X_train_scaled, y_train)

y_pred_lr = log_reg.predict(X_test_scaled)
log_reg = LogisticRegression()
log_reg.fit(X_train_scaled, y_train)

y_pred_lr = log_reg.predict(X_test_scaled)
print("Logistic Regression Accuracy:", accuracy_score(y_test, y_pred_lr))
print(confusion_matrix(y_test, y_pred_lr))
print(classification_report(y_test, y_pred_lr))
coef_df = pd.DataFrame({
    'Feature': ['mean_AF', 'function_class_count'],
    'Coefficient': log_reg.coef_[0]
})
print(coef_df)

tree = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)
tree.fit(X_train, y_train)

y_pred_tree = tree.predict(X_test)

print("Decision Tree Accuracy:", accuracy_score(y_test, y_pred_tree))
print(confusion_matrix(y_test, y_pred_tree))
print(classification_report(y_test, y_pred_tree))

importances = pd.DataFrame({
    'Feature': X.columns,
    'Importance': tree.feature_importances_
})
print(importances)

from sklearn.tree import plot_tree

plt.figure(figsize=(16, 10))
plot_tree(tree, feature_names=X.columns, class_names=['Intergenic', 'Genic'], filled=True)
plt.show()
