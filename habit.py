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
        self.records = []

    def get_records(self):
        return self.db.get_records_by_habit_id(self.habit_id)  
    
    def habit_records(self):
        habit = self.db.get_habit_by_id(self.habit_id)
        frequency = habit[2]

        if frequency == "Daily":
            records = self.get_records()
            if records:
                last_record = records[-1]
                last_record_date = datetime.datetime.strptime(last_record[2], "%Y-%m-%d")
                if last_record_date.date() <= datetime.date.today():
                    date = (last_record_date + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
                    self.db.add_record(self.habit_id, date)
            else:
                created_at = datetime.datetime.strptime(habit[5].split()[0], "%Y-%m-%d")
                if created_at.date() <= datetime.date.today():
                    date = (created_at + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
                    self.db.add_record(self.habit_id, date)

        elif frequency == "Weekly":
            records = self.get_records()
            if records:
                last_record = records[-1]
                last_record_date = datetime.datetime.strptime(last_record[2], "%Y-%m-%d")
                if last_record_date.date() <= datetime.date.today():
                    # Get the target weekday
                    target_weekday = habit[3].lower()  # Use habit[3] instead of habit[4], and convert to lowercase
                    next_date = self.get_next_weekday(last_record_date, target_weekday)
                    date = next_date.strftime("%Y-%m-%d")
                    self.db.add_record(self.habit_id, date)
            else:
                created_at = datetime.datetime.strptime(habit[5].split()[0], "%Y-%m-%d")
                if created_at.date() <= datetime.date.today():
                    # Get the target weekday
                    target_weekday = habit[3].lower()  # Use habit[3] instead of habit[4], and convert to lowercase
                    next_date = self.get_next_weekday(created_at, target_weekday)
                    date = next_date.strftime("%Y-%m-%d")
                    self.db.add_record(self.habit_id, date)

        elif frequency == "Monthly":
            records = self.get_records()
            if records:
                last_record = records[-1]
                last_record_date = datetime.datetime.strptime(last_record[2], "%Y-%m-%d")
                if last_record_date.date() <= datetime.date.today():
                    # Get the day of the month
                    day_of_month = habit[4]
                    next_date = self.get_next_monthday(last_record_date, day_of_month)
                    date = next_date.strftime("%Y-%m-%d")
                    self.db.add_record(self.habit_id, date)
            else:
                created_at = datetime.datetime.strptime(habit[3].split()[0], "%Y-%m-%d")
                if created_at.date() <= datetime.date.today():
                    # Get the day of the month
                    day_of_month = habit[4]
                    next_date = self.get_next_monthday(created_at, day_of_month)
                    date = next_date.strftime("%Y-%m-%d")
                    self.db.add_record(self.habit_id, date)

    @staticmethod
    def get_next_weekday(date, target_weekday):
        target_weekday = target_weekday.lower()
        weekdays = {
            'monday': 0,
            'tuesday': 1,
            'wednesday': 2,
            'thursday': 3,
            'friday': 4,
            'saturday': 5,
            'sunday': 6
        }
        days_ahead = (weekdays[target_weekday] - date.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return date + datetime.timedelta(days=days_ahead)

    def get_next_monthday(self, date, day_of_month):
        if date.month == 12:
            next_month = date.replace(year=date.year + 1, month=1)
        else:
            next_month = date.replace(month=date.month + 1)
        next_date = next_month.replace(day=day_of_month)
        return next_date

    def calculate_completion_rate(self):
        self.records = self.get_records()
        total_records = len(self.records)
        completed_records = sum(1 for record in self.records if record[3] == 1)
        completion_rate = completed_records / total_records * 100 if total_records > 0 else 0
        return completion_rate

    def calculate_current_streak(self):
        records = self.get_records()
        sorted_records = sorted(records, key=lambda record: record[2], reverse=True)
        current_streak = 0

        for record in sorted_records:
            if record[3] == 1:
                current_streak += 1
            else:
                break

        return current_streak

    def calculate_longest_streak(self):
        records = self.get_records()
        sorted_records = sorted(records, key=lambda record: record[2])
        longest_streak = 0
        current_streak = 0

        for record in sorted_records:
            if record[3] == 1:  
                current_streak += 1
                if current_streak > longest_streak:
                    longest_streak = current_streak
            else:
                current_streak = 0

        return longest_streak


# In[ ]:




