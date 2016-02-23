## Roos-Marijn Baars
## Script to change old GI's into new GI's

import glob
import pickle
import re

def main():
	OpenFiles()

def OpenFiles(): # Function to open all the necesarry files, the file to be read, to be created, and the dictionary
	tax_files_list = glob.glob("/home/roosmarijnbaars/Desktop/Onderzoek_BioCentre/BLAST_with_DIAMOND/output_DIAMOND_BLAST_sensitive_MGcV_complete_dataset_max_hits_25_roosmarijnbaars/*tsv")

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
				dict_file = open("/home/roosmarijnbaars/Desktop/NieuwePC/GIDic.dic","r")
			except IOError:
				print "GI dictionary could not be opened"

			GIDic = pickle.load(dict_file)
			dict_file.close()
			read = tax_file.readlines()
			tax_file.close()

			WriteFile(read,new_GI_file,GIDic)
			GIDic = {}

def WriteFile(read,newFile,dic): #Function to write the new file

	for line in read:
		if line.startswith("#"):
			newFile.write(line)
		if line.startswith("Fields: query id"):
			newFile.write(line)
		if line.startswith("@"):
			GetID(line,newFile,dic)
	newFile.close()

def GetID(line,newFile,dic): # Function to replace the old ID's with the new ones

	giref = line.split(",")[1]
	gi = giref.split("|")[1]

	if gi in dic:
		newgiref = "gi|"+dic[gi][0]+"|ref|"+dic[gi][1]+"|"
		newline = line.replace(line.split(",")[1],newgiref)
		newFile.write(newline)
	if gi not in dic:
		newFile.write(line)

if __name__ == "__main__":
	main()



