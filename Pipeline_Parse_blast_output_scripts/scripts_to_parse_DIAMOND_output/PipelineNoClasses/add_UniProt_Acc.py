# Roos-Marijn Baars
# Script to add Uniprot Acc to files

import glob
import urllib

from TestUniProt import TestUniProt
#from UniProtREST import UniProtREST
import xml.etree.cElementTree as ET

TestUniProt = TestUniProt()

def main():
	OpenFiles()

def OpenFiles():

	files_list = glob.glob("/home/roosmarijnbaars/Desktop/Onderzoek_BioCentre/BLAST_with_DIAMOND/output_DIAMOND_BLAST_sensitive_MGcV_complete_dataset_max_hits_25_roosmarijnbaars/*tsv")

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

			ReadFile(read,new_file)

def ReadFile(read,new_file):
	
	gilist = []
	for line in read:
		if line.startswith("@"):
			gi = GetGI(line)
			gilist.append(gi)

	gidic = TestUniProt.GetInputCodes(gilist)
	WriteFile(read,new_file,gidic)
	new_file.close()

	print "new File is created and closed"

def GetGI(line):
	
	giref = line.split(",")[1]
	gi = giref.split("|")[1]

	return gi

def WriteFile(read,new_file,gidic):

	for line in read:
		if line.startswith("#"):
			new_file.write(line)
		if line.startswith("Fields: query id"):
			fieldLine = line.replace("\n",", UniProtAcc\n")
			new_file.write(fieldLine)
		if line.startswith("@"):
			gi = GetGI(line)
			newLine = GetAnno(gi,line,gidic)
			new_file.write(newLine)

def GetAnno(gi,line,gidic):

	if gi in gidic:
		UniAcc = gidic[gi]
		query = ","+UniAcc+"\n"
		newLine = line.replace("\n",query)

		return newLine


main()
