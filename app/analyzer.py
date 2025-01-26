import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class StudentPerformanceAnalyzer:
    def __init__(self, quiz_data, submission_data, historical_data):
        self.quiz_data = quiz_data
        self.submission_data = submission_data
        self.historical_data = historical_data

    def analyze_performance(self):
        ml_insights = self._ml_performance_analysis()
        topic_performance = self._analyze_topic_performance()
        difficulty_insights = self._analyze_difficulty_levels()
        student_persona = self._generate_student_persona(ml_insights)
        recommendations = self._generate_recommendations(topic_performance, difficulty_insights, ml_insights)
        return {
            'ml_insights': ml_insights,
            'topic_performance': topic_performance,
            'difficulty_insights': difficulty_insights,
            'student_persona': student_persona,
            'recommendations': recommendations
        }

    def _ml_performance_analysis(self):
        df = pd.DataFrame(self.historical_data)
        df['accuracy'] = df['accuracy'].str.rstrip('%').astype(float)
        features = ['total_questions', 'correct_answers', 'incorrect_answers']
        X = df[features]
        y = df['accuracy']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        rf_model = RandomForestClassifier(n_estimators=100)
        rf_model.fit(X_train, y_train)
        return {
            'feature_importance': dict(zip(features, rf_model.feature_importances_)),
            'model_accuracy': rf_model.score(X_test, y_test),
            'performance_potential': np.mean(y_train)
        }

    def _analyze_topic_performance(self):
        topic_scores = {}
        for entry in self.historical_data:
            for topic, score in entry.get('topic_scores', {}).items():
                if topic not in topic_scores:
                    topic_scores[topic] = []
                topic_scores[topic].append(float(score.rstrip('%')))
        return {topic: np.mean(scores) for topic, scores in topic_scores.items()}

    def _analyze_difficulty_levels(self):
        difficulty_performance = {}
        for entry in self.historical_data:
            difficulty = entry.get('difficulty_level', 'Unknown')
            accuracy = float(entry.get('accuracy', '0%').rstrip('%'))
            if difficulty not in difficulty_performance:
                difficulty_performance[difficulty] = []
            difficulty_performance[difficulty].append(accuracy)
        return {difficulty: {'avg_performance': np.mean(performances), 'performance_variation': np.std(performances)} for difficulty, performances in difficulty_performance.items()}

    def _generate_student_persona(self, ml_insights):
        performance_potential = ml_insights['performance_potential']
        if performance_potential > 80:
            return {'learning_style': 'Rapid Learner', 'persona_description': 'High potential, quick comprehension'}
        elif performance_potential > 60:
            return {'learning_style': 'Steady Improver', 'persona_description': 'Consistent growth, methodical approach'}
        else:
            return {'learning_style': 'Potential Accelerator', 'persona_description': 'Significant room for improvement'}

    def _generate_recommendations(self, topic_performance, difficulty_insights, ml_insights):
        weak_topics = [topic for topic, score in topic_performance.items() if score < 50]
        challenging_levels = [diff for diff, insights in difficulty_insights.items() if insights['avg_performance'] < 50]
        focus_features = sorted(ml_insights['feature_importance'].items(), key=lambda x: x[1], reverse=True)
        return {
            'focus_topics': weak_topics,
            'challenging_difficulty_levels': challenging_levels,
            'suggested_actions': [
                f"Deep dive into {topic}" for topic in weak_topics
            ] + [
                f"Practice {diff} level questions" for diff in challenging_levels
            ] + [
                f"Focus on {feature} improvement" for feature, _ in focus_features[:2]
            ]
        }
