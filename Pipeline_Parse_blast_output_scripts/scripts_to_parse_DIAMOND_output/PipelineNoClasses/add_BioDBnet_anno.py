# Roos-Marijn Baars
# Script to get annotation from BioDBnet

import glob
import urllib

from TestBioDBnet import TestBioDBnet
from BioDBNetREST import BioDBNetREST
import xml.etree.cElementTree as ET

TestBioDBnet = TestBioDBnet()
def main():
	OpenFiles()

def OpenFiles():
	files_list = glob.glob("/home/roosmarijnbaars/Desktop/Onderzoek_BioCentre/BLAST_with_DIAMOND/output_DIAMOND_BLAST_sensitive_MGcV_complete_dataset_max_hits_25_roosmarijnbaars/*tsv")

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

			GetBioDBanno(read,new_file)

def GetBioDBanno(read,new_file):
	gilist = []
	for line in read:
		if line.startswith("@"):
			gi = GetGI(line)
			gilist.append(gi)

	gidic = TestBioDBnet.getIDcodesBioDB(gilist)
	WriteFile(read,new_file,gidic)
	new_file.close()

	print "new file closed"

def GetGI(line):
	
	giref = line.split(",")[1]
	gi = giref.split("|")[1]

	return gi

def WriteFile(read,new_file,gidic):

	for line in read:
		if line.startswith("#"):
			new_file.write(line)
		if line.startswith("Fields: query id"):
			fieldLine = line.replace("\n",", PfamID\n")
			new_file.write(fieldLine)
		if line.startswith("@"):
			gi = GetGI(line)
			newLine = GetAnno(gi,line,gidic)
			new_file.write(newLine)

def GetAnno(gi,line,gidic):

	if gi in gidic:
		PfamID = gidic[gi]
		PfamIDs = "".join(PfamID).replace("PfamID|","")
		query = ","+PfamIDs+"\n"
		newLine = line.replace("\n",query)
		return newLine


main()
