

import React, { useState } from "react";

function App() {
    const [resumeText, setResumeText] = useState("");
    const [prediction, setPrediction] = useState(null);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault(); // Prevent page reload
        setLoading(true);
        setError(null); // Clear previous errors
        setPrediction(null);

        try {
            const response = await fetch("http://127.0.0.1:5000/upload", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ resume_text: resumeText })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            console.log("Response from backend:", data);

            setPrediction({
                classification: data.final_classification,
                fraudProbability: data.fraud_probability || 0,
            });
        } catch (err) {
            console.error("Fetch error:", err);
            setError(err.message || "Failed to fetch data from the backend.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ textAlign: "center", marginTop: "50px", fontFamily: "Arial, sans-serif" }}>
            <h1>AI Resume Analyzer</h1>
            <form onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
                <textarea
                    rows="6"
                    cols="50"
                    placeholder="Paste your resume text here..."
                    value={resumeText}
                    onChange={(e) => setResumeText(e.target.value)}
                    required
                    style={{ padding: "10px", fontSize: "16px", borderRadius: "5px", border: "1px solid #ccc" }}
                />
                <br />
                <button type="submit" style={{
                    marginTop: "10px",
                    padding: "10px 20px",
                    fontSize: "16px",
                    backgroundColor: "#4CAF50",
                    color: "white",
                    border: "none",
                    borderRadius: "5px",
                    cursor: "pointer"
                }}>Analyze Resume</button>
            </form>

            {loading && <p style={{ fontSize: "18px", color: "blue" }}>Processing...</p>}

            {prediction && (
                <div style={{ marginTop: "20px", padding: "10px", border: "1px solid #ddd", borderRadius: "5px", width: "50%", margin: "auto" }}>
                    <h2>Prediction Result:</h2>
                    <p><strong>Final Classification:</strong> {prediction.classification}</p>
                    <p><strong>Fraud Probability:</strong> {prediction.fraudProbability.toFixed(2)}</p>
                    <div style={{ width: "100%", backgroundColor: "#ddd", borderRadius: "5px", marginTop: "10px" }}>
                        <div style={{ width: `${prediction.fraudProbability * 100}%`, height: "20px", backgroundColor: prediction.fraudProbability > 0.5 ? "red" : "green", borderRadius: "5px" }}></div>
                    </div>
                    <p>{(prediction.fraudProbability * 100).toFixed(0)}%</p>
                </div>
            )}

            {error && (
                <div style={{ color: "red", marginTop: "20px" }}>
                    <h3>Error:</h3>
                    <p>{error}</p>
                </div>
            )}
        </div>
    );
}

export default App;
