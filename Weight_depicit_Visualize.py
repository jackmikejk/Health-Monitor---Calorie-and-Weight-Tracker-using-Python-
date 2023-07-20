import pandas as pd

def main():
    my_goal_weight = int(147)
    print("Your Goal Weight is", my_goal_weight)
    my_current_weight = float(input("What's your current weight today: "))
    todays_calorie_intake = int(input("How much calories did you eat today: "))

    current_weight_data = []
    calorie_intake_data = []
    current_weight_data.append(my_current_weight)
    calorie_intake_data.append(todays_calorie_intake)

    if my_current_weight <= my_goal_weight:
        print("Congrats, You've got your fitness back!")

def get_data_from_excel(filepath,sheet_name):
    try:
        # Read the Excel file into a pandas DataFrame
        xls = pd.ExcelFile(filepath)
        df = pd.read_excel(xls, sheet_name=sheet_name)
        return df
    except FileNotFoundError:
        print(f"File '{filepath}' not found.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
    data_extraction = get_data_from_excel("D:\Coding\Python\Code practise\Simple Weight Depict Visualize\Weight_Depicit\Calorie_Tracker.xlsx", "Sheet1")