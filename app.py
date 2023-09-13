import os
from datetime import date, timedelta
from random import randint

# Start date: September 13, 2023
start_date = date(2023, 9, 13)

# End date: Today (current date)
end_date = date.today()

# Define the Git command to add and commit
git_add_commit_command = 'git add . && git commit --date="{date}" -m "Commit for {date}"'

# Loop through dates from start_date to end_date
current_date = start_date
while current_date <= end_date:
    # Check if the month is within the desired range (5 to 12, which corresponds to May to December)
    if 5 <= current_date.month <= 12:
        # Generate the commit date in the "YYYY-MM-DD" format
        commit_date = current_date.strftime("%Y-%m-%d")

        # Randomly determine the number of commits for the day (between 1 and 10)
        num_commits = randint(1, 10)

        for _ in range(num_commits):
            # Create a text file and write the date as content
            with open("file.txt", "a") as file:
                file.write(commit_date)

            # Run the Git add and commit command with the specified commit date
            os.system(git_add_commit_command.format(date=commit_date))

    # Move to the next day
    current_date += timedelta(days=1)

# Push the changes to the remote repository
os.system("git push -u origin main")
