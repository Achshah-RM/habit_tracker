#!/usr/bin/env python
# coding: utf-8

# # Habit Tracker
# ## Implementing Habit Class

# In[1]:


import sqlite3
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from database import HabitTrackerDB
import datetime


# In[2]:


class Habit:
    def __init__(self, habit_id, name):
        self.habit_id = habit_id
        self.name = name
        self.db = HabitTrackerDB() 

    def get_records(self):
        return self.db.get_records_by_habit_id(self.habit_id)  
    
    def habit_records(self):
        habit = self.db.get_habit_by_id(self.habit_id)
        frequency = habit[2]

        if frequency == "daily":
            records = self.get_records()
            if records:
                last_record = records[-1]
                last_record_date = datetime.datetime.strptime(last_record[2], "%Y-%m-%d")
                date = (last_record_date + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
            else:
                created_at = datetime.datetime.strptime(habit[3], "%Y-%m-%d")
                date = (created_at + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

            self.db.add_record(date[:10], self.habit_id)

        elif frequency == "weekly":
            records = self.get_records()
            if records:
                last_record = records[-1]
                last_record_date = datetime.datetime.strptime(last_record[2], "%Y-%m-%d")
                date = (last_record_date + datetime.timedelta(weeks=1)).strftime("%Y-%m-%d")
            else:
                created_at = datetime.datetime.strptime(habit[3], "%Y-%m-%d")
                date = (created_at + datetime.timedelta(weeks=1)).strftime("%Y-%m-%d")

            self.db.add_record(date[:10], self.habit_id)

        elif frequency == "monthly":
            records = self.get_records()
            if records:
                last_record = records[-1]
                last_record_date = datetime.datetime.strptime(last_record[2], "%Y-%m-%d")
                next_month = last_record_date.replace(day=28) + datetime.timedelta(days=4)
                date = next_month.strftime("%Y-%m-%d")
            else:
                created_at = datetime.datetime.strptime(habit[3], "%Y-%m-%d")
                next_month = created_at.replace(day=28) + datetime.timedelta(days=4)
                date = next_month.strftime("%Y-%m-%d")

            self.db.add_record(date[:10], self.habit_id)

    def calculate_completion_rate(self):
        records = self.get_records()
        total_records = len(records)
        if total_records == 0:
            return 0.0
        completed_records = sum(1 for record in records if record.completed == 1)
        completion_rate = (completed_records / total_records) * 100
        return round(completion_rate, 2)

    def calculate_current_streak(self):
        sorted_records = sorted(self.get_records(), key=lambda record: record.date, reverse=True)
        current_streak = 0

        for record in sorted_records:
            if record.completed == 1:
                current_streak += 1
            else:
                break

        return current_streak

    def calculate_longest_streak(self):
        sorted_records = sorted(self.get_records(), key=lambda record: record.date)
        longest_streak = 0
        current_streak = 0

        for record in sorted_records:
            if record.completed == 1:
                current_streak += 1
                if current_streak > longest_streak:
                    longest_streak = current_streak
            else:
                current_streak = 0

        return longest_streak

    def compare_completion_rates(self, other_habit):
        habits = [self, other_habit]
        habit_names = [habit.name for habit in habits]
        completion_rates = [habit.calculate_completion_rate() for habit in habits]

        plt.bar(habit_names, completion_rates)
        plt.xlabel("Habit")
        plt.ylabel("Completion Rate")
        plt.title("Comparison of Habit Completion Rates")
        plt.show()


# In[ ]:




