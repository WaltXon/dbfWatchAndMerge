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
		print("currently on table = {0}".format(aDbf))
		catTable = []
		table = dbf.Table(aDbf)
		table.open()

		fields = dbf.get_fields(aDbf)
		print("fields = {0}".format(fields))

		for rec in table[:10]:
			tmp = []
			if i == 0:
				catTable.append(fields)
				i+=1
			for item in rec:
				tmp.append(item)
			# print ("row added = {0}".format(tmp))
		catTable.append(tmp)

		table.close()
	print catTable

