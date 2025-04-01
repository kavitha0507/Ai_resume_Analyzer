from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Example Resume Dataset
resume_data = [
    "Experienced software developer with knowledge of machine learning and AI.",
    "Data scientist skilled in Python, AI, and big data analysis.",
    "Software engineer with 5 years of experience in full-stack development."
]
labels = [0, 1, 0]  # Example labels (0 = Not Fraudulent, 1 = Fraudulent)

# Train the vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(resume_data)

# Train the model
model = LogisticRegression()
model.fit(X, labels)

# Save vectorizer and model
joblib.dump(vectorizer, "vectorizer.pkl")
joblib.dump(model, "model.pkl")

print("Model retrained successfully!")
