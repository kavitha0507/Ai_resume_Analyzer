import joblib

# Load model & vectorizer
model = joblib.load("/Users/purnachandermynala/ai-resume-backend/final_model.pkl")
vectorizer = joblib.load("/Users/purnachandermynala/ai-resume-backend/vectorizer.pkl")

def analyze_resume(resume_text):
    # Convert the text using the saved vectorizer
    resume_vector = vectorizer.transform([resume_text])

    # Get prediction probability
    fraud_probability = model.predict_proba(resume_vector)[0][1]  # Probability of being fraudulent
    legit_probability = model.predict_proba(resume_vector)[0][0]  # Probability of being legitimate

    # Adjust classification threshold (lowering it reduces false fraud cases)
    fraud_threshold = 0.5  # Default was 0.5; adjust as needed

    print(f"Legit Probability: {legit_probability:.2f}, Fraud Probability: {fraud_probability:.2f}")

    # Debug Feature Importance using SHAP
    explainer = shap.Explainer(model, vectorizer.transform)
    shap_values = explainer(resume_vector)

    print("\n🔍 SHAP Analysis: Words contributing to fraud detection")
    shap.summary_plot(shap_values, feature_names=vectorizer.get_feature_names_out())

    # Classify based on adjusted threshold
    if fraud_probability > fraud_threshold:
        return "❌ Fraudulent Resume"
    else:
        return "✅ Legitimate Resume"

# Example: Test with your resume
resume_text = """Junior Software Engineer with a solid foundation in Java full-stack development, AI, and machine learning.
Experienced in building scalable web applications and machine learning models.
Technical Skills: Java, Spring Boot, React, MySQL, Git, Docker, Agile.
Education: MSc Computer Science (Osmania University).
Certifications: IBM AI Fundamentals, iNeuron Generative AI Course, OpenAI Deep Learning."""

# Run the analysis
result = analyze_resume(resume_text)
print(f"\n🔹 Prediction Result: {result}")