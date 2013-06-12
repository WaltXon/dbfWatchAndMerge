import dbfer
import watch
import placePnts
import os


# target_dir = os.path.join("/","users", "waltnixon", "Documents", "github", "dbfWatchAndMerge", "rigdata")
# out_csv = os.path.join("/","users", "waltnixon", "Documents", "github", "dbfWatchAndMerge", "rigdata", "out.csv")
target_dir = r"C:\Users\wnixon\Documents\GitHub\dbfWatchAndMerge\rigdata"
out_csv = r"C:\Users\wnixon\Documents\GitHub\dbfWatchAndMerge\rigdata\out_csv.csv"
print ("target_dir = {0}".format(target_dir))

if watch.watch(target_dir) == 'change':
	for fileType in ['l', 'p']:
		out_csv = r"C:\Users\wnixon\Documents\GitHub\dbfWatchAndMerge\rigdata\out_csv_" + fileType + '.csv'
		
		dbfFiles = dbfer.getAndFilterFiles(target_dir, fileType, "dbf")

		result = dbfer.mergeDbfFiles(dbfFiles)

		clean = dbfer.removeDups(result[0], result[1])

		dbfer.writeCSV(clean, out_csv)
		