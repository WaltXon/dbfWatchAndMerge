import os 



def change(seq1, seq2):
		for x in seq1:
			if x not in seq2:
				return True
		for y in seq2:
			if y not in seq1:
				return True
		return False

def watch(folder):

	inventory = os.path.join(folder, 'inventory.txt')

	for root, dirs, filesInFolder in os.walk(folder):
		pass

	if os.path.exists(inventory):
		inv = open(inventory, "r")
		filesInInventory = [x.rstrip('\n') for x in inv.readlines()]
		inv.close()

		if change(filesInFolder, filesInInventory): #ONLY CATCHES ADDS NOT DELETES 
				print("file change found")
				os.remove(inventory)
				print("removed old inventory file")
				inv = open(inventory, "w")
				# NEED TO RENAME THE NEW FILE os.rename(myFile, "{0}_{1}{2}".format(myFile[:-4],time.ctime(os.path.getctime(myFile)), myFile[-4:]))
				print("created a new invetory file")
				for items in filesInFolder:
					inv.write('{0}\n'.format(items))
					print('Updating {0}\n'.format(items))
				print("updated items written to inventory file")
				inv.close()
				return "change"
		else:
			print("no file changes found in {0}".format(folder))
			return "no-change"
	else: 
		# for myFile in filesInFolder:
			# os.rename(myFile, "{0}_{1}{2}".format(myFile[:-4],os.path.getctime(myFile), myFile[-4:]))

		inv = open(inventory, 'w')
		for aFile in filesInFolder:
			inv.write('{0}\n'.format(aFile))
			print('Adding {0}\n'.format(aFile))
		inv.close()