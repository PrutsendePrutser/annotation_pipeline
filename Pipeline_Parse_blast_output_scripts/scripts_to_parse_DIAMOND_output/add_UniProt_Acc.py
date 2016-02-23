# Roos-Marijn Baars
# Script to add Uniprot Acc to files

import glob
import urllib

from TestUniProt import TestUniProt
import xml.etree.cElementTree as ET

class add_UniProt_Acc():

	def __init__(self):
		self.TestUniProt = TestUniProt()

	def main(self, file_storage_location):
		self.OpenFiles(file_storage_location)

	def OpenFiles(self, file_storage_location):
		files_list = glob.glob(file_storage_location+"*tsv")

		for i in files_list:
			if i.endswith("BioDBnet_anno.tsv"):
				try:
					BioFile = open(i,"r")
				except IOError:
					print "File not found"

				j = i.replace("BioDBnet_anno.tsv","UniProt_Acc.tsv")
				try:
					new_file = open(j,"w")
				except IOError:
					print "UniProt file could not be created"

				read = BioFile.readlines()
				BioFile.close()

				self.ReadFile(read,new_file)

	def ReadFile(self,read,new_file):

		fromcode = "P_GI"
		tocode = "ACC"	
		
		gilist = []
		for line in read:
			if line.startswith("@"):
				gi = self.GetGI(line)
				gilist.append(gi)

		gidic = self.TestUniProt.main(gilist, fromcode, tocode)
		self.WriteFile(read,new_file,gidic)
		new_file.close()

		print "new File is created and closed"

	def GetGI(self,line):
	
		giref = line.split("\t")[1]
		gi = giref.split("|")[1]

		return gi

	def WriteFile(self,read,new_file,gidic):

		for line in read:
			if line.startswith("#"):
				new_file.write(line)
			if line.startswith("Fields: query id"):
				fieldLine = line.replace("\n","\t UniProtAcc\n")
				new_file.write(fieldLine)
			if line.startswith("@"):
				gi = self.GetGI(line)
				newLine = self.GetAnno(gi,line,gidic)
				new_file.write(newLine)

	def GetAnno(self,gi,line,gidic):

		if gi in gidic:
			UniAcc = gidic[gi]
			query = "\t"+UniAcc+"\n"
			newLine = line.replace("\n",query)
		if gi not in gidic:
			UniAcc = "\t-\n"
			newLine = line.replace("\n",UniAcc)
		return newLine

