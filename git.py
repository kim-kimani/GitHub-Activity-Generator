#!/usr/bin/env python
import os
from datetime import datetime, timedelta, date
from subprocess import Popen
import random

def main():
    file_path = input("Enter the path to the file you want to add contributions to: ")
    if not os.path.isfile(file_path):
        print("The specified file does not exist.")
        return
    
    print("1. Commit on a specific day")
    print("2. Commit on a range of dates")
    date_choice = input("Enter your choice (1/2): ").strip()
    if date_choice == '1':
        commit_date_str = input("Enter the date (YYYY-MM-DD): ")
        commit_time_str = input("Enter the time (HH:MM): ")
        num_commits = int(input("Enter the number of commits to make on this day: "))
        commit_date = datetime.strptime(commit_date_str, "%Y-%m-%d").date()
        commit_time = datetime.strptime(commit_time_str, "%H:%M").time()
        commit_datetimes = [datetime.combine(commit_date, commit_time) for _ in range(num_commits)]
    elif date_choice == '2':
        start_date_str = input("Enter the start date (YYYY-MM-DD): ")
        end_date_str = input("Enter the end date (YYYY-MM-DD): ")
        start_time_str = input("Enter the start time (HH:MM): ")
        end_time_str = input("Enter the end time (HH:MM): ")
        max_commits_per_day = int(input("Enter the maximum number of commits per day: "))
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
        start_time = datetime.strptime(start_time_str, "%H:%M").time()
        end_time = datetime.strptime(end_time_str, "%H:%M").time()
        commit_datetimes = []
        for single_date in date_range(start_date, end_date):
            num_commits_today = random.randint(1, max_commits_per_day)
            for _ in range(num_commits_today):
                random_hour = random.randint(start_time.hour, end_time.hour)
                random_minute = random.randint(0, 59)
                commit_time = datetime.combine(single_date, datetime.strptime(f"{random_hour:02d}:{random_minute:02d}", "%H:%M").time())
                commit_datetimes.append(commit_time)
    else:
        print("Invalid choice. Please enter '1' or '2'.")
        return
    
    print("1. Use one commit message for all commits")
    print("2. Use different commit messages for each day")
    message_choice = input("Enter your choice (1/2): ").strip()
    if message_choice == '1':
        commit_message = input("Enter the commit message: ")
        commit_messages = [commit_message] * len(commit_datetimes)
    elif message_choice == '2':
        commit_messages_input = input("Enter commit messages separated by commas (minimum 2): ")
        commit_messages_list = [msg.strip() for msg in commit_messages_input.split(',')]
        if len(commit_messages_list) < 2:
            print("You must enter at least 2 commit messages.")
            return
        commit_messages = [random.choice(commit_messages_list) for _ in commit_datetimes]
    else:
        print("Invalid choice. Please enter '1' or '2'.")
        return
    
    for commit_datetime, commit_message in zip(commit_datetimes, commit_messages):
        edit_and_commit(file_path, commit_datetime, commit_message)

    print('\nCommit generation ' +
        '\x1b[6;30;42mcompleted successfully\x1b[0m!')

def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

def edit_and_commit(file_path, commit_datetime, commit_message):
    # Append spaces to the file and commit
    with open(file_path, 'a') as file:
        file.write(' ' * 10)  # Append 10 spaces
    run(['git', 'add', file_path])
    run(['git', 'commit', '-m', f'"{commit_message}"',
        '--date', commit_datetime.strftime('"%Y-%m-%d %H:%M:%S"')])
    
    # Remove the spaces and commit again
    with open(file_path, 'r+') as file:
        content = file.read().rstrip()
        file.seek(0)
        file.write(content)
        file.truncate()
    run(['git', 'add', file_path])
    run(['git', 'commit', '-m', f'"{commit_message}"',
        '--date', commit_datetime.strftime('"%Y-%m-%d %H:%M:%S"')])

def run(commands):
    Popen(commands).wait()

if __name__ == "__main__":
    main()