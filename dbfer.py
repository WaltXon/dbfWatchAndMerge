import dbf
import os

def getAndFilterFiles(path, filt):
	'''Get and Filter a list of files type = filt Files'''
	for root, dirs, files in os.walk(path):
		print("Collecting File List")

	filteredFiles = []
	for aFile in files:
		if aFile.endswith((filt)):
			filteredFiles.append(os.path.join(path,aFile))

	print("File List = {0}".format(files))
	print("filteredFile List = {0}".format(filteredFiles))
	return filteredFiles

def mergeDbfFiles(files):
	
	filepath = os.path.split(files[0])[0]
	# mergeTable = os.path.join(filepath, "merge.dbf")
	# mergeTable = dbf.Table(mergeTable)
	# mergeTable.open()
	
	i=0 #Counter for header
	for aDbf in files:
		
		table = dbf.Table(aDbf)
		table.open()
		for record in table:
			print record

		# dbf.export(table, header= True)
		table.close()

