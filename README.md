c# Weight_Depicit

A basic data analysis and visualization script using Python.

This project is designed to help you track your daily calorie intake and weight progress effortlessly. By updating your calorie intake in Microsoft Excel (morning, noon, and night), either on your computer or phone (synced with OneDrive), this code will analyze the data and generate a chart displaying trends and results. Monitoring your weight and being mindful of your daily calorie intake becomes much easier with this tool.

**How it Works**
1. Update Calorie Intake: Every day, record your calorie intake at breakfast, lunch, and dinner in the provided Microsoft Excel file.

2. Data Sync: The Excel file can be accessed from your phone or computer, as long as it is synced with OneDrive.

3. Goal Weight Setting: Set your desired goal weight in the code. And decide the Calorie intake per day to attain the goal weight. 

4. Analyze Progress: The code will fetch the data from the given location (Excel file) and generate a chart that showcases your calorie intake and weight progress over time.

**Getting Started**
1.Install Required Libraries: Make sure you have Python installed on your system. You will also need pandas and matplotlib libraries. Use the following command to install them:

**pip install pandas matplotlib**
2. Excel File Setup: Create an Excel file named "Calorie_Tracker.xlsx" with columns for "Day," "Calorie Intake," and "Current Weight."

3. Set Goal Weight: In the code, specify your goal weight by assigning a value to the goal_weight variable.

4. Execute the Code: Run the main() function. The program will read the data from the Excel file, compare your current weight with the goal weight, and display a chart indicating your progress.

5. Update Daily: Continuously update your daily calorie intake in the Excel file to keep track of your progress accurately.

**Benefits**
1. Easy Data Entry: Update your calorie intake at your convenience, either on your phone or computer.

2. Visual Tracking: The generated chart provides an intuitive representation of your calorie intake and weight progress.

3. Goal-Oriented: The core idea of this project is to help you achieve your goal weight by providing insights into your calorie consumption and progress towards your goal.

4. Stay committed to your health goals and achieve the lifestyle you desire with this Calorie and Weight Progress Tracker. Enjoy a healthier, more mindful journey!
