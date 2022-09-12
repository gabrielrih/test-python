# References:
#   https://www.pythontutorial.net/python-basics/python-sort-list/
#   https://www.tutorialspoint.com/file-searching-using-python
import os
from datetime import datetime

MONGO_DAILY_BACKUP_FOLDER = '/backups/daily/'

# Gets the last backup folder
for root, dirs, files in os.walk(MONGO_DAILY_BACKUP_FOLDER):
    dirs.sort(reverse=True) # Descending order
    for dir in dirs:
        lastBackupFolder = dir
        break

# Gets the latest backup date
latestBackupDate = datetime.strptime(str(lastBackupFolder[0:10]), '%Y-%m-%d')

# Calculates days since the last
now = datetime.now().date()
diff = now - latestBackupDate.date()
print("Days since the last backup: " + str(diff.days))