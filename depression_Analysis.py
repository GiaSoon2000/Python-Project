import seaborn as sns
import matplotlib.pyplot as plt

class DepressionAnalysis:
    def __init__(self, depression_df):
        self.depression_df = depression_df

    def plot_gender_distribution(self):
        colors = ['#546D64', '#689F7D']

        plt.figure(figsize=(6, 4))
        sns.countplot(data=self.depression_df, x='Gender', palette=colors)
        plt.title('Distribution of Depressed Student Across Gender', fontsize=10)
        plt.xlabel('Gender')
        plt.ylabel('Count')
        plt.show()

    def gender_distribution_insight(self):
        return "The distribution of Depressed Student Across Gender shows that more female students are depressed relative to the male students."

    def plot_marital_status_distribution(self):
        colors = ['#546D64', '#689F7D']

        plt.figure(figsize=(6, 4))
        sns.countplot(data=self.depression_df, x='Marital status', palette=colors)
        plt.title('Distribution of Depressed Student Across Marital Status', fontsize=10)
        plt.xlabel('Marital status')
        plt.ylabel('Count')
        plt.show()

    def marital_status_distribution_insight(self):
        return ("For the distribution of students across married and unmarried, we see that the number of unmarried students "
                "who are depressed is higher. This might be because married students have support from their spouse, making "
                "it easier for them to navigate life, thus leading to a lower number of married people being depressed. "
                "Alternatively, married students may have built stronger resilience due to their experiences in matrimony, "
                "making them more mentally stable than the unmarried.")

    def plot_age_distribution(self):
        colors = ['#546D64', '#689F7D', '#8ABF99', '#AED6B1', '#CDE8D0', '#E9F8EB']

        plt.figure(figsize=(6, 4))
        sns.countplot(data=self.depression_df, x='Age', palette=colors)
        plt.title('Distribution of Depressed Students Across Age', fontsize=10)
        plt.xlabel('Age')
        plt.ylabel('Count')
        plt.show()

    def age_distribution_insight(self):
        return ("Across student age the proportion of students who are depressed falls with age 18 and 19. At 20 to 22 the proportion of depressed"
                "students decrease. There is also a noticeable increase in the number of depressed studnt form Age 24.")

    def plot_cgpa_distribution(self):
        colors = ['#546D64', '#689F7D', '#8ABF99']
        plt.figure(figsize=(6, 4))
        sns.countplot(data=self.depression_df, x='CGPA', palette=colors)
        plt.title('Distribution of Depressed Student Across CGPA', fontsize=10)
        plt.xlabel('CGPA')
        plt.ylabel('Count')
        plt.show()

    def cgpa_distribution_insight(self):
        return ("There are more depressed students with CGPA OF 3.00 - 3.49, followed by students with CGPA of 3.50 - 4.00. Only a few proportion "
                "of student with CGPA OF 2.50 - 2.99 are depressed.")