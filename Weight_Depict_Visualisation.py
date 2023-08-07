# Plot the first chart for calorie intake data
    for day, calorie_consumption in zip(days, calorie_intake_data):
        if calorie_consumption <= 1700:
            fig1.bar(day, calorie_consumption, color="green")
        elif 1701 <= calorie_consumption <= 1850:
            fig1.bar(day, calorie_consumption, color="#90EE90")
        else:
            fig1.bar(day, calorie_consumption, color="red")
    fig1.set_xlabel("Day")
    fig1.set_ylabel("Calorie Intake")
    fig1.set_title("Calorie Intake Progress")
    # Plot the second chart for current weight data
    fig2.plot(days, current_weight_data, marker='o', linestyle='-', color='b')
    fig2.set_xlabel("Day")
    fig2.set_ylabel("Current Weight")
    fig2.set_title("Current Weight Progress")
    # Adjust spacing between the plots
    plt.tight_layout()
    plt.show()
def weight_comparision(current_weight_data, goal_weight):
    if goal_weight == current_weight_data:
        print("You got this!")
def get_data_from_excel(filepath, sheet_name):
    try:
        # Read the Excel file into a pandas DataFrame
        xcl = pd.ExcelFile(filepath)
        df = pd.read_excel(xcl, sheet_name=sheet_name)
        # Filter the rows with non-empty "Calorie Intake" and "Current Weight" values
        data = df.dropna(subset=["Day", "Calorie Intake", "Current Weight"])
        # Get the "Day", "Calorie Intake" and "Current Weight" columns as lists
        #data.loc[:, "Day"] = data["Day"].astype(int)
        days = data["Day"].tolist()
        calorie_intake_data = data["Calorie Intake"].tolist()
        current_weight_data = data["Current Weight"].tolist()
        print("Day:")
        print(days)
        print("Calorie Intake Data:")
        print(calorie_intake_data)
        print("Current Weight Data:")
        print(current_weight_data)
        return days, calorie_intake_data, current_weight_data
    except FileNotFoundError:
        print(f"File '{filepath}' not found.")
def main():
    goal_weight = 147
    print("Goal Weight:", goal_weight)
    data_extraction = get_data_from_excel(r"C:\Users\Michael Jackson\OneDrive\Calorie_Tracker.xlsx", "Sheet1")
    days, calorie_intake_data, current_weight_data = data_extraction
    weight_comparision(current_weight_data, goal_weight)
    plot_the_chart(days, calorie_intake_data, current_weight_data)
if __name__ == "__main__":
    main()
