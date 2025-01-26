import streamlit as st
from app.analyzer import StudentPerformanceAnalyzer
from app.data_fetcher import fetch_json_data

def main():
    st.title("📊 Student Performance Analyzer")
    
    # Input URLs
    quiz_url = st.text_input("Quiz Data URL", value="https://www.jsonkeeper.com/b/LLQT")
    submission_url = st.text_input("Submission Data URL", value="https://api.jsonserve.com/rJvd7g")
    historical_url = st.text_input("Historical Data URL", value="https://api.jsonserve.com/XgAgFJ")
    
    if st.button("Analyze Performance"):
        with st.spinner("Fetching and analyzing data..."):
            quiz_data = fetch_json_data(quiz_url)
            submission_data = fetch_json_data(submission_url)
            historical_data = fetch_json_data(historical_url)
            
            analyzer = StudentPerformanceAnalyzer(quiz_data, submission_data, historical_data)
            results = analyzer.analyze_performance()
        
        # Display results creatively
        st.header("Performance Insights ✨")

        # Student Persona
        st.subheader("👤 Student Persona")
        st.write(f"**Learning Style:** {results['student_persona']['learning_style']}")
        st.write(f"**Description:** {results['student_persona']['persona_description']}")

        # ML Insights
        st.subheader("🤖 ML Performance Insights")
        st.write(f"**Model Accuracy:** {results['ml_insights']['model_accuracy']:.2%}")
        st.write("**Key Performance Factors:**")
        for feature, importance in results['ml_insights']['feature_importance'].items():
            st.write(f"- **{feature}:** {importance:.2%}")

        # Topic Performance
        st.subheader("📚 Topic-Wise Performance")
        for topic, score in results['topic_performance'].items():
            st.write(f"- **{topic}:** {score:.2f}%")

        # Difficulty Insights
        st.subheader("🎯 Difficulty Level Insights")
        for level, insights in results['difficulty_insights'].items():
            st.write(f"- **{level}:**")
            st.write(f"  - Average Performance: {insights['avg_performance']:.2f}%")
            st.write(f"  - Performance Variation: {insights['performance_variation']:.2f}")

        # Recommendations
        st.subheader("🚀 Personalized Recommendations")
        st.write("**Focus Topics:**")
        st.write(", ".join(results['recommendations']['focus_topics']))

        st.write("**Suggested Actions:**")
        for action in results['recommendations']['suggested_actions']:
            st.write(f"- {action}")

        # Option to view raw JSON
        with st.expander("🔍 View Raw JSON Data"):
            st.json(results)
