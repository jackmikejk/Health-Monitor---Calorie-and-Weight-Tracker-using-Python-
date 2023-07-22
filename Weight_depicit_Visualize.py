import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_the_chart(calorie_intake_data, current_weight_data):

    plt.bar(calorie_intake_data, current_weight_data)
    plt.xlabel("Calorie Intake")
    plt.ylabel("Current Weight")
    plt.title("Calorie Intake vs Current Weight")
    plt.show()

def weight_comparision(current_weight_data, goal_weight):
    if goal_weight == current_weight_data:
        print("You got this")

def get_data_from_excel(filepath, sheet_name):
    try:
        # Read the Excel file into a pandas DataFrame
        xl = pd.ExcelFile(filepath)
        df = pd.read_excel(xl, sheet_name=sheet_name)

        # Filter the rows with non-empty "Calorie Intake" and "Current Weight" values
        data = df.dropna(subset=["Calorie Intake", "Current Weight"])

        # Get the "Calorie Intake" and "Current Weight" columns as lists
        calorie_intake_data = data["Calorie Intake"].tolist()
        current_weight_data = data["Current Weight"].tolist()

        print("Calorie Intake Data:")
        print(calorie_intake_data)

        print("Current Weight Data:")
        print(current_weight_data)
        return current_weight_data, calorie_intake_data
    except FileNotFoundError:
        print(f"File '{filepath}' not found.")

def main():
    goal_weight = 147
    print("Goal Weight:", goal_weight)
    data_extraction = get_data_from_excel(r"C:\Users\Michael Jackson\OneDrive\Calorie_Tracker.xlsx", "Sheet1")
    calorie_intake_data, current_weight_data = data_extraction

    weight_comparision(current_weight_data, goal_weight)
    plot_the_chart(current_weight_data, calorie_intake_data)

if __name__ == "__main__":
    main()



