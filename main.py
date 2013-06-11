import dbfer
import watch
import placePnts
import os

target_dir = os.path.join("/","users", "waltnixon", "Documents", "github", "dbfWatchAndMerge", "rigdata")
# target_dir = "C:\Users\wnixon\Documents\GitHub\dbfWatchAndMerge"

print ("target_dir = {0}".format(target_dir))

dbfFiles = dbfer.getAndFilterFiles(target_dir, "l", "dbf")

mergeFile, fields = dbfer.mergeDbfFiles(dbfFiles)

removeDups(mergeFile, fields)