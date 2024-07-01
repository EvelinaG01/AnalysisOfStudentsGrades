#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate mean, median, and variance of grades
def calculate(grades):
    mean = np.mean(grades)
    median = np.median(grades)
    variance = np.var(grades)
    return mean, median, variance

# Function to display mean, median, and variance of grades
def display(mean, median, variance):
    print("Στατιστικά Βαθμών Μαθητών:")
    print(f"Ο Μέσος όρος είναι: {mean:.3f}")
    print(f"Η Διάμεσος είναι: {median:.3f}")
    print(f"Η Διακύμανση είναι: {variance:.3f}")

def main():
    # Students' Grades List
    grades = [9.8, 5.6, 9.2, 7.4, 8.8, 6.8, 9.5, 8.7, 5.1, 9.9]
    
    # Calculation of mean, median, and variance of grades
    mean, median, variance = calculate(grades)
    
    # Print of mean, median, and variance of grades
    display(mean, median, variance)
    
    # Convert grades to DataFrame for seaborn plotting
    df = pd.DataFrame({'Grades': grades})
    
    # Create two separate figures
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    # Plotting Boxplot
    sns.boxplot(data=grades, ax=ax1)
    ax1.set_xlabel('Grades')
    ax1.set_title('Box Plot of Student Grades')
    
    # Plotting Histogram
    ax2.hist(grades, bins=5, edgecolor='black')
    ax2.set_xlabel('Grades')
    ax2.set_ylabel('Frequency')
    ax2.set_title('Histogram of Student Grades')
    ax2.grid(True)
    
    # Adjust layout and display the plots
    plt.tight_layout()
    plt.show() 
    
# Execution of the program
main()


# In[ ]:




