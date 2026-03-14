import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle
data = pd.read_csv("dataset/Testing.csv")
X = data.drop("prognosis", axis=1)
y = data["prognosis"]
model = DecisionTreeClassifier()
model.fit(X, y)
pickle.dump(model, open("model.pkl", "wb"))
print("Model trained and saved successfully!")