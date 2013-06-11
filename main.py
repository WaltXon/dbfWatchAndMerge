import dbfer
import watch
import placePnts
import os

# target_dir = os.path.join("/","users", "waltnixon", "Documents", "github", "dbfWatchAndMerge", "rigdata")
target_dir = r"C:\Users\wnixon\Documents\GitHub\dbfWatchAndMerge\rigdata"
out_csv = r"C:\Users\wnixon\Documents\GitHub\dbfWatchAndMerge\rigdata\out_csv.csv"
print ("target_dir = {0}".format(target_dir))

dbfFiles = dbfer.getAndFilterFiles(target_dir, "l", "dbf")

result = dbfer.mergeDbfFiles(dbfFiles)

clean = dbfer.removeDups(result[0], result[1])

dbfer.writeCSV(clean, out_csv)