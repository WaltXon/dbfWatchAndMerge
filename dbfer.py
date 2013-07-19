import dbf
import os
import datetime
import csv

def getAndFilterFiles(path, filt, fileFormat):
	'''Get and Filter a list of files type = filt Files'''
	for root, dirs, files in os.walk(path):
		print("Collecting File List")

	filteredFiles = []
	for aFile in files:
		if aFile.endswith(fileFormat):
			if filt in os.path.basename(aFile).lower():
				print aFile	
				filteredFiles.append(os.path.join(path, aFile))

	print("File List = {0}".format(files))
	print("filteredFile List = {0}".format(filteredFiles))
	return filteredFiles

def mergeDbfFiles(files):
	
	filepath = os.path.split(files[0])[0]

	i=0 #Counter for header
	catTable = []
	for aDbf in files:
		print("currently on table = {0}".format(aDbf))

		table = dbf.Table(aDbf)
		table.open()

		fields = dbf.get_fields(aDbf)
		fields.append("date_added")
		print("fields = {0}".format(fields))
		dateAdded = datetime.date.fromtimestamp(os.path.getctime(aDbf))
		print ("date_added = {0}".format(dateAdded))
		print("No records in table = {0}".format(len(table)))

		for rec in table:
			tmp = []
			for item in rec:
				tmp.append(item)
			# print ("row added = {0}".format(tmp))
			tmp.append(dateAdded)
			catTable.append(tmp)
		# if i == 0:
		# 	catTable.insert(0,fields)
		# 	i+=1

		table.close()
		print("Length of catTable = {0}".format(len(catTable)))
	# print (catTable[:2])
	return (catTable, fields)

def removeDups(inputList, fields):
	clean = []
	print fields
	wellIdInx = fields.index('well_id')
	print ("wellIdInx = {0}".format(wellIdInx))
	dateInx = fields.index("date_added")
	print ("dateInx = {0}".format(dateInx))
	wellIds = []
	print ("inputListLenght = {0}".format(len(inputList)))
	for row in inputList:
		wellIds.append(row[wellIdInx])
	uniqWellIds = set(wellIds)
	print uniqWellIds

	for wellId in uniqWellIds:
		dups = []
		
		for row2 in inputList:
			if wellId == row2[wellIdInx]:
				print("wellId = {0} : row2[wellIdInx] = {1}".format(wellId, row2[wellIdInx]))
				dups.append(row2)

		if len(dups) > 1:
			newest = datetime.date.min
			for item in dups:
				if item[dateInx] > newest:
					newest = item[dateInx]
					tmp = item
			clean.append(tmp)
		else: 
			clean.append(dups[0])
	
	clean.insert(0, fields)
	print clean[:10]
	print ("Clean length = {0}".format(len(clean)))
	return clean


def writeCSV(inList, outFile):
	with open(outFile, 'wb') as f:
		writer = csv.writer(f, delimiter=',')
		writer.writerows(inList)
	return outFile

