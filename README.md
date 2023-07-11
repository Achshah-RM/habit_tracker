## Habit Tracker

Habit Tracker is a simple application built using Python and object-oriented programming (OOP) concepts. It allows users to track their habits and monitor their progress over time. The application provides a graphical user interface (GUI) created with Tkinter.

### Getting Started

To run the Habit Tracker application, follow these steps:

- Download all the necessary files: database.py, habit.py, main.py, and gui.py.
- Ensure that you have Python 3.8.8 or a compatible version installed on your system.
- Open a terminal or command prompt and navigate to the directory where you downloaded the files.
- Run the main.py file using the command python main.py.
- The application's GUI window will open, providing options to either view existing habits or create a new habit.

### Creating a New Habit

If you choose to create a new habit, follow these steps:

- Select the "Create New Habit" option in the initial window.
- A new window will open, allowing you to enter the name of the habit and choose its frequency from a drop-down menu (e.g., daily, weekly, monthly).
- Click the "Create" button to create the habit. 
- For habits with a weekly and monthy frequency, the Habit Tracker app offers a flexible scheduling option. After clicking on the "Create" button, a new window will open, allowing you to customize the habit's recurrence.
- Click the "Confirm" button. You'll receive a confirmation message displayed upon creation.
- Close the window or run the main.py file again to proceed.

### Viewing Habits and Analytics

After returning to welcome window and selecting the "View Habits" option, you can:

- View habits that need to be completed on the current day (if any).
- Click on the "Complete" button to complete the habit.
- Click the "View All Habits" button to see a list of all created habits, including the one you just created.
- For each habit listed, you can delete, update, and view analytics.
- Click the "Update" button to modify the name of the habit. However, you won't be able to change the frequency of the habit. Once you have made the desired changes to the name, simply click on the "Update" button (close the window and open again to see changes).
- Click the "View Analytics" button to display the habit's longest streak, current streak, and completion rate.
- Please note that if you view the analytics immediately after creating a habit, the values will be zero since there won't be any recorded data yet.

### Dependencies

The Habit Tracker application relies on the following dependencies:

- Python 3.8.8 or compatible version
- sqlite3 module
- Tkinter (included in Python standard library)

### Acknowledgments

The Habit Tracker application was developed as a learning exercise in object-oriented programming and GUI development using Python. It serves as a starting point for building more complex habit tracking and management systems.

### Troubleshooting

If you encounter any issues or have questions about the Habit Tracker application, please feel free to contact me or open an issue in the project repository.

###### Enjoy using the Habit Tracker application!