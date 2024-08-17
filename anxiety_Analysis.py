import seaborn as sns
import matplotlib.pyplot as plt

class AnxietyAnalysis:
    def __init__(self, depression_df):
        self.depression_df = depression_df

    def plot_anxiety_by_course_and_gender(self):
        plt.figure(figsize=(10, 8))
        sns.swarmplot(data=self.depression_df, x='Anxiety', y='Course', hue='Gender', palette=['#546D64', '#50FFB1'])
        plt.title('Swarm Plot of Anxiety by Course and Gender')
        plt.xlabel('Anxiety')
        plt.ylabel('Course')
        plt.show()

    def anxiety_gender_course_insight(self):
        return ("More female students enrolled in engineering with no anxiety have depression compared to male students enrolled in engineering. "
                "Female students enrolled in IT with anxiety are more likely to have depression relative to males enrolled in IT. "
                "Overall, there are variations in depression status across courses of study and anxiety levels.")

    def plot_anxiety_by_cgpa_and_gender(self):
        plt.figure(figsize=(10, 8))
        sns.swarmplot(data=self.depression_df, x='Anxiety', y='CGPA', hue='Gender', palette=['#546D64', '#50FFB1'])
        plt.title('Swarm Plot of Anxiety by CGPA and Gender')
        plt.xlabel('Anxiety')
        plt.ylabel('CGPA')
        plt.show()

    def anxiety_cgpa_gender_insight(self):
        return ("More female students with CGPA of 3.00 to 3.49 with no anxiety have depression compared to female students with anxiety. "
                "While female students with anxiety and CGPA of 3.50 to 4.00 are more likely to have depression relative to female students without anxiety and the same CGPA. "
                "Overall, there are variations in depression among female students according to their CGPA. "
                "Female students with a high CGPA tend to be more anxious, which can lead to depression. Further analysis is needed to prove the relationship between these variables.")

    def plot_anxiety_by_year_and_gender(self):
        plt.figure(figsize=(10, 8))
        sns.swarmplot(data=self.depression_df, x='Anxiety', y='Year of Study', hue='Gender', palette=['#546D64', '#50FFB1'])
        plt.title('Swarm Plot of Anxiety by Year of Study and Gender')
        plt.xlabel('Anxiety')
        plt.ylabel('Year of Study')
        plt.show()

    def anxiety_year_gender_insight(self):
        return ("More female students in year 1 with no anxiety have depression compared to female students with anxiety in the same year. "
                "For year 2, more female students with no anxiety have depression. "
                "In year 3, more female students with anxiety have depression. "
                "Overall, there are variations in depression across gender, anxiety, and the year of study.")