# Roos-Marijn Baars
# Script to filter on subject placement 2

import pickle

def main():

	OpenFiles()

def OpenFiles():

	print "OpenFiles()"
	try:
		blastFile1 = open("/home/roosmarijnbaars/Desktop/Onderzoek_BioCentre/BLAST_with_DIAMOND/output_DIAMOND_BLAST_sensitive_MGcV_complete_dataset_max_hits_25_roosmarijnbaars/f2_compost_t_0_exp_1_ACTCGC_L001_R1_001_000000000-ACNW4.filt_database_all_genomes_64GB_RAM_sensitive_max_hits_25_max_evalue_20_DIAMOND_to_BLASTX.tsv","r")
	except IOError:
		print "blastFile 1 not found"
	forRead = ReadFiles(blastFile1)
	print "File 1 read"

	try:
		blastFile2 = open("/home/roosmarijnbaars/Desktop/Onderzoek_BioCentre/BLAST_with_DIAMOND/output_DIAMOND_BLAST_sensitive_MGcV_complete_dataset_max_hits_25_roosmarijnbaars/f2_compost_t_0_exp_1_ACTCGC_L001_R2_001_000000000-ACNW4.filt_database_all_genomes_64GB_RAM_sensitive_max_hits_25_max_evalue_20_DIAMOND_to_BLASTX.tsv","r")
	except IOError:
		print "blastFile 2 not found"

	revRead = ReadFiles(blastFile2)
	print "File 2 read"
	SearchInFile(forRead,revRead)
	SearchInFile(revRead,forRead)

def ReadFiles(blastFile):
	
	read = blastFile.readlines()
	blastFile.close()

	return read

def SearchInFile(read1,read2):

	print "searchinFile()"
	singleCount = 0
	lineCount = 0
	readList = CreateList(read2)
	for line in read1:
		if line.startswith("@"):
			lineCount += 1
			#print "lc", lineCount
			newLine = ConvertLine(line)
			#readLine = ReadSecFile(read2)
			dataList = CheckOldLine(line)
			singleCount += CheckLine(newLine,readList,dataList)
			#print singleCount

	print "total number of lines: ",lineCount
	print "Number of single hits: ",singleCount
			#CheckLength(queryLine,line)

def CreateList(read):

	readList = []
	readlist = ReadSecFile(read,readList)

	return readlist

def ConvertLine(line):
	#print "Convertline"
	if "/1" in line:
		newLine = line.split("\t")[0].replace("/1","/2")
	if "/2" in line:
		newLine = line.split("\t")[0]
	return newLine

def CheckLine(line,read,dataList):

#	print "Checkline"

	if line in read:
		#print "yes"
		#CheckLength(line,dataList)
		return 0
	if line not in  read:
		#print "no"
		return 1

def ReadSecFile(read,readList):

	print "Readsecfile"
	for line in read:
		if line.startswith("@"):
			newLine = ConvertLine(line)
			readList.append(newLine)
	return readList

def CheckOldLine(line):

	#print line
	if "/1" in line:
		line = line.replace("/1","/2")
		#GetData(line)
	if "/2" in line:
		dataList = GetData(line)
	return dataList

def GetData(line):

	qStart = line.split("\t")[6]
	qStop = line.split("\t")[7]
	sStart = line.split("\t")[8]
	sStop = line.split("\t")[9]

	dataList = [qStart,qStop,sStart,sStop]
	#print line,dataList
	return dataList
	

def CheckLength(line,dataList):
	print line
	#print dataList
main()


