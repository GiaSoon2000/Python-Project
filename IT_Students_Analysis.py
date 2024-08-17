import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class ITStudentsAnalysis:
    def __init__(self, cdata):
        self.cdata = cdata
        self.it_data = None
    
    def analyze_it_students(self):
        self.cdata['Depressed'] = self.cdata['Depression'] == 'Depressed'
        self.cdata['Anxiety_present'] = self.cdata['Anxiety'] == 'Anxiety_present'
        self.cdata['Panic_attack_present'] = self.cdata['Panic attack'] == 'Panic attack'
        self.it_data = self.cdata[self.cdata['Course'] == 'IT']
        total_it_students = len(self.it_data)
        return total_it_students

    def condition_counts(self):
        if self.it_data is None:
            raise ValueError("IT students data has not been analyzed yet. Please run analyze_it_students() first.")
        
        condition_counts = {
            'Total IT Students': len(self.it_data),
            'Depressed': self.it_data['Depressed'].sum(),
            'Anxiety_present': self.it_data['Anxiety_present'].sum(),
            'Panic_attack_present': self.it_data['Panic_attack_present'].sum(),
            'All Three Conditions': (self.it_data['Depressed'] & self.it_data['Anxiety_present'] & self.it_data['Panic_attack_present']).sum()
        }

        condition_df = pd.DataFrame(list(condition_counts.items()), columns=['Condition', 'Count'])

        plt.figure(figsize=(10, 6))
        sns.barplot(data=condition_df, x='Condition', y='Count', palette='viridis')
        plt.ylabel('Number of Students')
        plt.title('Number of IT Students and Their Mental Health Conditions')
        plt.show()

        return condition_df

    def plot_condition_combinations(self):
        if self.it_data is None:
            raise ValueError("IT students data has not been analyzed yet. Please run analyze_it_students() first.")
            
        # Calculate the number of students with each combination of conditions
        students_with_none = len(self.it_data) - (
            (self.it_data['Depressed'] | self.it_data['Anxiety_present'] | self.it_data['Panic_attack_present']).sum()
        )
        students_with_one = (
            (self.it_data['Depressed'] & ~self.it_data['Anxiety_present'] & ~self.it_data['Panic_attack_present']).sum() +
            (~self.it_data['Depressed'] & self.it_data['Anxiety_present'] & ~self.it_data['Panic_attack_present']).sum() +
            (~self.it_data['Depressed'] & ~self.it_data['Anxiety_present'] & self.it_data['Panic_attack_present']).sum()
        )
        students_with_two = (
            (self.it_data['Depressed'] & self.it_data['Anxiety_present'] & ~self.it_data['Panic_attack_present']).sum() +
            (self.it_data['Depressed'] & ~self.it_data['Anxiety_present'] & self.it_data['Panic_attack_present']).sum() +
            (~self.it_data['Depressed'] & self.it_data['Anxiety_present'] & self.it_data['Panic_attack_present']).sum()
        )
        students_with_all_conditions = (self.it_data['Depressed'] & self.it_data['Anxiety_present'] & self.it_data['Panic_attack_present']).sum()

        # Create a DataFrame for the pie chart and filter out zero counts
        pie_data = pd.DataFrame({
            'Condition': ['None', 'One Condition', 'Two Conditions', 'All Three Conditions'],
            'Count': [students_with_none, students_with_one, students_with_two, students_with_all_conditions]
        })

        # Filter out rows with zero count
        pie_data = pie_data[pie_data['Count'] > 0]

        # Plot the pie chart
        plt.figure(figsize=(10, 8))
        plt.pie(pie_data['Count'], labels=pie_data['Condition'], autopct='%1.1f%%', 
                colors=['#e0e0e0', '#ff9999', '#66b3ff', '#ffcc99'])
        plt.title('Percentage of IT Students by Number of Mental Health Conditions')
        plt.show()

        return pie_data

    def get_analysis_summary(self):
        # Return the summary text as a string
        summary_text = """
        A small percentage of IT students are free from the three studied mental health conditions. 
        Over half of the students have only one of the conditions, indicating that mental health issues are prevalent but not always multifaceted. A          
        significant portion of students (36.4%) experience all three conditions simultaneously, reflecting a serious overlap of mental health issues 
        among some students."""
        return summary_text
        
    def plot_cgpa_distribution(self):
        if self.it_data is None:
            raise ValueError("IT students data has not been analyzed yet. Please run analyze_it_students() first.")

        # Plotting the histogram
        plt.figure(figsize=(10, 6))
        sns.histplot(self.it_data['CGPA'], bins=20, kde=True, color='skyblue')
        plt.xlabel('CGPA')
        plt.ylabel('Number of Students')
        plt.title('Distribution of CGPA Among IT Students')
        plt.show()

    def plot_cgpa_vs_conditions(self):
        if self.it_data is None:
            raise ValueError("IT students data has not been analyzed yet. Please run analyze_it_students() first.")

        # Create a Dot Plot
        conditions = ['Depressed', 'Anxiety_present', 'Panic_attack_present']

        plt.figure(figsize=(15, 10))

        for i, condition in enumerate(conditions, 1):
            plt.subplot(2, 2, i)
            sns.stripplot(data=self.it_data, x='CGPA', y=condition, hue=condition, jitter=True, dodge=True, alpha=0.7, size=8)
            plt.title(f'CGPA vs {condition}')
            plt.xlabel('CGPA')
            plt.ylabel('Condition Present')
            plt.yticks([0, 1], ['Absent', 'Present'])

        plt.tight_layout()
        plt.show()

    def plot_cgpa_by_condition_count(self):
        if self.it_data is None:
            raise ValueError("IT students data has not been analyzed yet. Please run analyze_it_students() first.")

        # Print counts of students with each condition
        print("Counts of students with each condition:")
        conditions = ['Depressed', 'Anxiety_present', 'Panic_attack_present']
        for condition in conditions:
            count = self.it_data[self.it_data[condition] == 1].shape[0]
            print(f"{condition}: {count}")

        # Calculate the number of conditions each student has
        self.it_data['Number_of_Conditions'] = (
            self.it_data['Depressed'].astype(int) +
            self.it_data['Anxiety_present'].astype(int) +
            self.it_data['Panic_attack_present'].astype(int)
        )

        # Plotting the box plot for CGPA by Number of Conditions
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=self.it_data, x='Number_of_Conditions', y='CGPA', palette='coolwarm')
        plt.xlabel('Number of Conditions')
        plt.ylabel('CGPA')
        plt.title('CGPA Distribution by Number of Mental Health Conditions')
        plt.show()

    def plot_cgpa_stripplot(self):
        if self.it_data is None:
            raise ValueError("IT students data has not been analyzed yet. Please run analyze_it_students() first.")

        plt.figure(figsize=(10, 6))
        sns.stripplot(data=self.it_data, x='Number_of_Conditions', y='CGPA', jitter=True, palette='viridis', alpha=0.7)
        plt.xlabel('Number of Conditions')
        plt.ylabel('CGPA')
        plt.title('CGPA Distribution by Number of Mental Health Conditions')
        plt.show()

    def plot_cgpa_facetgrid(self):
        if self.it_data is None:
            raise ValueError("IT students data has not been analyzed yet. Please run analyze_it_students() first.")

        g = sns.FacetGrid(self.it_data, col='Number_of_Conditions', col_wrap=2, height=5, aspect=1.2)
        g.map(sns.histplot, 'CGPA', kde=True, color='blue')
        g.set_axis_labels('CGPA', 'Count')
        g.set_titles(col_template='Conditions: {col_name}')
        g.add_legend()
        plt.show()

    def get_cgpa_analysis_summary(self):
        summary_text = """
        Analysis of the data reveals that students with a CGPA of 3.00 and above tend to have a higher number 
        of mental health conditions compared to those with a CGPA below 3.00. Specifically, the percentage of students with multiple conditions is
        significantly higher in the higher CGPA group. This suggests that higher academic performance may be associated with an increased 
        prevalence of mental health issues among IT students.
        """
        return summary_text