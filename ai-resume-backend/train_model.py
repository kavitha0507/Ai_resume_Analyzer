import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("/Users/purnachandermynala/ai-resume-backend/resume_dataset.csv")

# Extract text and labels
X = df["ResumeText"]
y = df["Fraudulent"]

# Feature extraction using TF-IDF
vectorizer = TfidfVectorizer(stop_words="english", max_features=500)
X_transformed = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model and vectorizer
joblib.dump(model, "final_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained and saved successfully!")
