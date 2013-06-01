import dbfer
import watch
import placePnts
import os

target_dir = os.path.join("/","users", "waltnixon", "Documents", "github", "dbfWatchAndMerge", "rigdata")

print ("target_dir = {0}".format(target_dir))

dbfFiles = dbfer.getAndFilterFiles(target_dir, "dbf")

dbfer.mergeDbfFiles(dbfFiles)
