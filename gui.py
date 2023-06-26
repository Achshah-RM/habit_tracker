#!/usr/bin/env python
# coding: utf-8

# # Habit Tracker
# ## Building the GUI

# In[1]:


from database import HabitTrackerDB
from habit import Habit
import tkinter as tk
from tkinter.font import Font
import datetime


# In[2]:


class HabitTrackerGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Habit Tracker")
        self.window.configure(background="black")
        
        self.habit_db = HabitTrackerDB()

        # Set font properties
        heading_font = Font(family="Segae Script", size=50, weight="bold")
        subheading_font = Font(family="Segae Script", size=30, weight="bold")
        label_font = Font(family="Segae Script", size=20)

        # Welcome Heading
        welcome_label = tk.Label(
            self.window, text="Welcome to Habit-tracker!", font=heading_font, fg="white", bg="black"
        )
        welcome_label.pack(pady=20)

        # Create a Habit Button
        create_habit_button = tk.Button(
            self.window, text="Create a Habit", font=label_font, command=self.open_create_habit_window
        )
        create_habit_button.pack(pady=10)

        # View Habits Button
        view_habits_button = tk.Button(
            self.window, text="View Habits", font=label_font, command=self.open_view_habits_window
        )
        view_habits_button.pack(pady=10)

    def open_create_habit_window(self):
        
        self.window.destroy()

        create_habit_window = tk.Tk()
        create_habit_window.title("Create a Habit")
        create_habit_window.configure(background="black")

        # Set font properties
        heading_font = Font(family="Segae Script", size=50, weight="bold")
        subheading_font = Font(family="Segae Script", size=30, weight="bold")
        label_font = Font(family="Segae Script", size=20)

        # Heading - Create a New Habit
        create_heading_label = tk.Label(
            create_habit_window, text="You can create a new habit here!", font=heading_font, fg="white", bg="black"
        )
        create_heading_label.pack(pady=20)

        # Subheading - Enter the name of the habit
        create_subheading_label = tk.Label(
            create_habit_window,
            text="Enter the name of the habit, select the frequency and press create to create a new habit.",
            font=subheading_font,
            fg="white",
            bg="black",
            anchor="w",
        )
        create_subheading_label.pack(pady=10)

        # Name Label and Text Field
        name_label = tk.Label(create_habit_window, text="Name:", font=label_font, fg="white", bg="black")
        name_label.pack(pady=5)
        name_entry = tk.Entry(create_habit_window, font=label_font)
        name_entry.pack(pady=5)

        # Frequency Label and Dropdown Menu
        frequency_label = tk.Label(create_habit_window, text="Frequency:", font=label_font, fg="white", bg="black")
        frequency_label.pack(pady=5)
        frequency_var = tk.StringVar()
        frequency_dropdown = tk.OptionMenu(create_habit_window, frequency_var, "Daily", "Weekly", "Monthly")
        frequency_dropdown.config(font=label_font, bg="white", width=10)
        frequency_dropdown.pack(pady=5)

        # Create Button
        create_button = tk.Button(
            create_habit_window,
            text="Create",
            font=label_font,
            fg="black",
            bg="white",
            command=lambda: self.habit_db.insert_habit(name_entry.get(), frequency_var.get()),
        )
        create_button.pack(pady=10)

        create_habit_window.mainloop()

    def open_view_habits_window(self):
        self.window.destroy()

        view_habits_window = tk.Tk()
        view_habits_window.title("View Habits")
        view_habits_window.configure(background="black")

        # Set font properties
        heading_font = Font(family="Segae Script", size=50, weight="bold")
        subheading_font = Font(family="Segae Script", size=30, weight="bold")
        label_font = Font(family="Segae Script", size=12)

        # Heading - Here's your current habits
        view_heading_label = tk.Label(
            view_habits_window, text="Habits for today!", font=heading_font, fg="white", bg="black"
        )
        view_heading_label.pack(pady=20)

        current_date = datetime.date.today().strftime("%Y-%m-%d")
        habit_ids = self.habit_db.get_habit_ids_for_date(current_date)
        
        for habit_id in habit_ids:
            habit = self.habit_db.get_habit_by_id(habit_id)
            habit_name = habit[1]  
            frequency = habit[2]
            habit_id = habit_id

            # Display habit name
            habit_name_label = tk.Label(
                view_habits_window, text=habit_name, font=subheading_font, fg="white", bg="black"
            )
            habit_name_label.pack()

            # Display frequency
            frequency_label = tk.Label(
                view_habits_window, text=f"Frequency: {frequency}", font=label_font, fg="white", bg="black"
            )
            frequency_label.pack()

            # Add buttons for completion and analytics
            complete_button = tk.Button(view_habits_window, text="Complete")
            complete_button.pack()

            # Analytics Button
            view_analytics_button = tk.Button(view_habits_window, text="View Analytics",
                                  command=lambda: self.open_analytics_window(habit_id, habit_name))
            # Separator
            separator = tk.Label(view_habits_window, text="-------------------------------------------",
                                 font=subheading_font, fg="white", bg="black")
            separator.pack()

            # Call create_or_update_habit with habit_id
            self.create_or_update_habit(habit_id, habit_name)

        # Add button for viewing all habits
        view_all_button = tk.Button(
            view_habits_window, text="View All Habits", font=subheading_font, fg="black", bg="white",
            command=lambda: self.view_all_habits(view_habits_window)
        )
        view_all_button.pack(pady=20)

        view_habits_window.mainloop()
        
    def view_all_habits(self, window):
        habits = self.habit_db.get_all_habits()

        # Set font properties
        heading_font = Font(family="Segae Script", size=30, weight="bold")
        subheading_font = Font(family="Segae Script", size=20)
        label_font = Font(family="Segae Script", size=12)

        # Heading - All Habits
        all_habits_heading = tk.Label(window, text="All Habits", font=heading_font, fg="white", bg="black")
        all_habits_heading.pack(pady=20)

        for habit in habits:
            habit_name = habit[1]
            frequency = habit[2]
            habit_id = habit[0]

            # Display habit name
            habit_name_label = tk.Label(window, text=habit_name, font=subheading_font, fg="white", bg="black")
            habit_name_label.pack()

            # Display frequency
            frequency_label = tk.Label(
                window, text=f"Frequency: {frequency}", font=label_font, fg="white", bg="black"
            )
            frequency_label.pack()

            view_analytics_button = tk.Button(window, text="View Analytics",
                                  command=lambda: self.open_analytics_window(habit_id, habit_name))
            view_analytics_button.pack()
            
    def open_analytics_window(self, habit_id, habit_name):
        analytics_window = tk.Toplevel()
        analytics_window.title("Analytics")
        analytics_window.configure(background="black")

        # Set font properties
        heading_font = Font(family="Segae Script", size=50, weight="bold")
        subheading_font = Font(family="Segae Script", size=30, weight="bold")
        label_font = Font(family="Segae Script", size=20)
        
        # Create an instance of the Habit class
        habit = Habit(habit_id, habit_name)

        # Heading - Analytics
        analytics_heading = tk.Label(analytics_window, text="Analytics", font=heading_font, fg="white", bg="black")
        analytics_heading.pack(pady=20)

        # Habit Name
        habit_name_label = tk.Label(analytics_window, text=habit_name, font=subheading_font, fg="white", bg="black")
        habit_name_label.pack()

        # Current Streak
        current_streak = habit.calculate_current_streak()  # assuming habit is an instance of the Habit class
        current_streak_label = tk.Label(analytics_window, text=f"Current Streak: {current_streak}", font=label_font,
                                        fg="white", bg="black")
        current_streak_label.pack()

        # Longest Streak
        longest_streak = habit.calculate_longest_streak()  # assuming habit is an instance of the Habit class
        longest_streak_label = tk.Label(analytics_window, text=f"Longest Streak: {longest_streak}", font=label_font,
                                        fg="white", bg="black")
        longest_streak_label.pack()

        # Completion Rate
        completion_rate = habit.calculate_completion_rate()  # assuming habit is an instance of the Habit class
        completion_rate_label = tk.Label(analytics_window, text=f"Completion Rate: {completion_rate}", font=label_font,
                                         fg="white", bg="black")
        completion_rate_label.pack()

        analytics_window.mainloop()
    
    def create_or_update_habit(self, habit_id, name):
        habit = Habit(habit_id, name)
        habit.habit_records()
        
    def run(self):
        self.window.mainloop()

