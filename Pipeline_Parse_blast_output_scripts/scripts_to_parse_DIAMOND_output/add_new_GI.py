## Roos-Marijn Baars
## Script to change old GI's into new GI's

import glob
import pickle
import re

class add_new_GI():

	def main(self, file_storage_location, gi_dict_location):
		self.OpenFiles(file_storage_location, gi_dict_location)

	def OpenFiles(self, file_storage_location, gi_dict_location): # Function to open all the necesarry files, the file to be read, to be created, and the dictionary
		tax_files_list = glob.glob(file_storage_location+"*tsv")

		for i in tax_files_list:
			if i.endswith("with_Tax.tsv"):
				try:
					tax_file = open(i,"r")
				except IOError:
					print "Tax file not found"

				j = i.replace("with_Tax.tsv","new_GI.tsv")
				try:
					new_GI_file = open (j,"w")
				except IOError:
					print "New Gi file could not be created"

				try:
					dict_file = open(gi_dict_location+"GIDic.dic","r")
				
					GIDic = pickle.load(dict_file)
					dict_file.close()
					read = tax_file.readlines()
					tax_file.close()

					self.WriteFile(read,new_GI_file,GIDic)
					GIDic = {}

				except IOError:
					print "GI dictionary could not be opened"


	def WriteFile(self,read,newFile,dic): #Function to write the new file

		for line in read:
			if line.startswith("#"):
				newFile.write(line)
			if line.startswith("Fields: query id"):
				newFile.write(line)
			if line.startswith("@"):
				self.GetID(line,newFile,dic)
		newFile.close()

	def GetID(self,line,newFile,dic): # Function to replace the old ID's with the new ones

		giref = line.split("\t")[1]
		gi = giref.split("|")[1]

		if gi in dic:
			newgiref = "gi|"+dic[gi][0]+"|ref|"+dic[gi][1]+"|"
			newline = line.replace(line.split("\t")[1],newgiref)
			newFile.write(newline)
		if gi not in dic:
			newFile.write(line)




