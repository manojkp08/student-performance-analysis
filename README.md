# 🎓 Student Performance Analyzer  
_A Smarter Way to Empower Learning_  

---

## 📜 Project Overview  

The **Student Performance Analyzer** is your go-to solution for understanding and improving student performance. By blending the power of **machine learning** with **interactive visualizations**, this tool provides educators and learners with personalized insights into learning styles, performance gaps, and actionable improvements.  

### 🚀 Key Features:  
1. 🧠 **Topic-Wise Performance Analysis**: Identify strengths and weaknesses across different topics.  
2. 🎯 **Difficulty-Level Insights**: Measure and understand variations in performance by difficulty level.  
3. 🤖 **ML-Powered Insights**: Leverage machine learning to uncover key performance drivers.  
4. 📝 **Personalized Recommendations**: Get targeted suggestions for improvement based on performance data.  

---

## 📂 Folder Structure  

```plaintext
student-performance-analyser/
├── app/
│   ├── __init__.py            # Marks the 'app' directory as a module
│   ├── analyzer.py            # ML analysis logic and performance insights
│   ├── data_fetcher.py        # Fetches data from provided URLs
│   ├── ui.py                  # Streamlit UI for interactive insights
├── main.py                    # Entry point for the Streamlit app
├── requirements.txt           # Dependencies for the project
└── README.md                  # Project overview and setup guide
```

## ⚙️ Setup Instructions
1️⃣ Clone the Repository
```
git clone <repository-url>
cd student-performance-analyser
```
2️⃣ Install Dependencies
Use the command below to install the required libraries:
```
pip install -r requirements.txt
```
3️⃣ Run the Application
Launch the Streamlit app using:
```
streamlit run main.py
```
4️⃣ Access the Application
Once the server starts, visit the URL displayed in your terminal (e.g., http://localhost:8501) to start analyzing performance.

## 🛠️ Approach Description
**📊 1. Data Collection**
The application fetches data from three user-provided URLs:

- **Quiz Data:** Contains quiz-specific metadata.
- **Submission Data:** Tracks user answers and attempts.
- **Historical Data:** Provides insights into past performance.
  
Data is fetched using the requests library and transformed into structured formats for analysis.

**🧮 2. Machine Learning Analysis**
The StudentPerformanceAnalyzer class uses a Random Forest Classifier to:

Predict performance potential based on historical data.
Identify key performance drivers via feature importance analysis.

**📌 3. Insights Extraction**
- **Topic Performance:** Aggregates and averages scores across different topics to identify strong and weak areas.
- **Difficulty Levels:** Measures performance variation across question difficulty levels.
- **Student Persona:** Categorizes students into personas based on their learning style and performance trends.

**🔍 4. Recommendations**
The application generates a personalized list of actionable suggestions, such as:

Focusing on weak topics.
Addressing challenging difficulty levels.
Improving key performance factors based on ML analysis.

**🖥️ 5. Streamlit Interface**
The Streamlit UI ensures seamless interactivity with:
- **Data Input Fields:** Enter the URLs for quiz, submission, and historical data.
- **Creative Visualizations:** View detailed insights in a structured and engaging format.
- **Expanders:** Peek into raw JSON data for a closer look.

## 🛣️ Future Enhancements
**✨ What’s Next?**

Data Upload: Allow users to upload CSV or JSON files directly for analysis.
Real-Time ML Training: Enable users to retrain the ML model using their custom datasets.
Enhanced Visualizations: Add dynamic charts and graphs for deeper insights.

## 💻 Tech Stack
- **Backend Analysis:** Python, NumPy, pandas, scikit-learn
- **Frontend Interface:** Streamlit
- **Data Fetching:** requests
