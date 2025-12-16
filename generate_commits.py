#!/usr/bin/env python3
import os
import subprocess
from datetime import datetime, timedelta
import random

# Configuration
START_DATE = datetime.now() - timedelta(days=365)  # Go back 1 year
END_DATE = datetime.now()
MIN_COMMITS_PER_DAY = 1
MAX_COMMITS_PER_DAY = 5
COMMIT_PROBABILITY = 0.7  # 70% chance of committing on any given day

def generate_commit(date):
    """Generate a commit with a specific date"""
    # Format date for git
    date_str = date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Append to activity log
    with open('activity.log', 'a') as f:
        f.write(f"Activity on {date_str}\n")
    
    # Stage the file
    subprocess.run(['git', 'add', 'activity.log'], check=True)
    
    # Create commit with custom date
    env = os.environ.copy()
    env['GIT_AUTHOR_DATE'] = date_str
    env['GIT_COMMITTER_DATE'] = date_str
    
    subprocess.run(
        ['git', 'commit', '-m', f'Activity update {date.strftime("%Y-%m-%d")}'],
        env=env,
        check=True
    )

def main():
    print("Generating contribution graph commits...")
    print(f"Date range: {START_DATE.date()} to {END_DATE.date()}")
    
    current_date = START_DATE
    total_commits = 0
    
    while current_date <= END_DATE:
        # Randomly decide if we commit today
        if random.random() < COMMIT_PROBABILITY:
            # Random number of commits for this day
            num_commits = random.randint(MIN_COMMITS_PER_DAY, MAX_COMMITS_PER_DAY)
            
            for i in range(num_commits):
                # Add some random hours/minutes to spread commits throughout the day
                commit_time = current_date + timedelta(
                    hours=random.randint(8, 20),
                    minutes=random.randint(0, 59)
                )
                generate_commit(commit_time)
                total_commits += 1
        
        current_date += timedelta(days=1)
    
    print(f"\nGenerated {total_commits} commits!")
    print("Now push to GitHub: git push origin main")

if __name__ == '__main__':
    main()
