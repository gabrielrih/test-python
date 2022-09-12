#
# DAYS SINCE THE LAST BACKUP
# It compares the date from the last backup folder with today.
# The metric is days since the last backup
# 
# References:
#   https://www.pythontutorial.net/python-basics/python-sort-list/
#   https://www.tutorialspoint.com/file-searching-using-python
#
from checks import AgentCheck
from datetime import datetime
import os

MONGO_BACKUP_FOLDER = '../backups/daily/'

class BackupCheck(AgentCheck):
    def check(self, instance):
        days = self.daySinceLastBackup()
        self.gauge('mongodb.backup.lastbackup', str(days))

    def daySinceLastBackup(self):
        if not os.path.exists(MONGO_BACKUP_FOLDER):
            return 30 # No backup founded
        # Gets the last backup folder
        for root, dirs, files in os.walk(MONGO_BACKUP_FOLDER):
            dirs.sort(reverse=True) # Descending order
            for dir in dirs:
                lastBackupFolder = dir
                break
        # Gets the latest backup date
        latestBackupDate = datetime.strptime(str(lastBackupFolder[0:10]), '%Y-%m-%d')
        # Calculates days since the last backup
        now = datetime.now().date()
        diff = now - latestBackupDate.date()
        return diff.days