# Roos-Marijn Baars
# Script to get annotation from BioDBnet

import glob
import urllib

from TestBioDBnet import TestBioDBnet
from BioDBNetREST import BioDBNetREST
import xml.etree.cElementTree as ET



class add_BioDBnet_anno():
	def __init__(self):
		self.TestBioDBnet = TestBioDBnet()

	def main(self, file_storage_location):
		self.OpenFiles(file_storage_location)

	def OpenFiles(self, file_storage_location):
		files_list = glob.glob(file_storage_location+"*tsv")

		for i in files_list:
			if i.endswith("new_GI.tsv"):
				try:
					old_file = open(i,"r")
				except IOError:
					print "Old GI file not found"

				j = i.replace("new_GI.tsv","BioDBnet_anno.tsv")
				try:
					new_file = open(j,"w")
				except IOError:
					print "BioDBnet file could not be created"

				read = old_file.readlines()
				old_file.close()

				self.GetBioDBanno(read,new_file)

	def GetBioDBanno(self,read,new_file):
		gilist = []
		for line in read:
			if line.startswith("@"):
				gi = self.GetGI(line)
				gilist.append(gi)

		gidic = self.TestBioDBnet.main(gilist)
		self.WriteFile(read,new_file,gidic)
		new_file.close()

		print "new file closed"

	def GetGI(self,line):
	
		giref = line.split("\t")[1]
		gi = giref.split("|")[1]

		return gi

	def WriteFile(self,read,new_file,gidic):

		for line in read:
			if line.startswith("#"):
				new_file.write(line)
			if line.startswith("Fields: query id"):
				fieldLine = line.replace("\n","\t PfamID\n")
				new_file.write(fieldLine)
			if line.startswith("@"):
				gi = self.GetGI(line)
				newLine = self.GetAnno(gi,line,gidic)
				new_file.write(newLine)

	def GetAnno(self,gi,line,gidic):

		if gi in gidic:
			PfamID = gidic[gi]
			PfamIDs = "".join(PfamID).replace("PfamID|","")
			query = "\t"+PfamIDs+"\n"
			newLine = line.replace("\n",query)
			return newLine

