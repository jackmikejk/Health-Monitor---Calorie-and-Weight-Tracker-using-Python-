import matplotlib.pyplot as plt

def get_goal_weight():
    my_goal_weight = float(input("What is your goal weight: "))
    return my_goal_weight

def get_current_weight():
    my_current_weight = float(input("What's your current weight today: "))
    return my_current_weight

def get_calorie_intake():
    todays_calorie_intake = int(input("How much calories did you eat today: "))
    return todays_calorie_intake

def main():
    goal_weight = get_goal_weight()
    weight_data = []

    current_weight = get_current_weight()
    weight_data.append(current_weight)

    if current_weight <= goal_weight:
        print("Congrats, You've got your fitness back!")







