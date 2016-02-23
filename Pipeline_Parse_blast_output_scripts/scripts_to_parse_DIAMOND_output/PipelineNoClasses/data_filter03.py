# Roos-Marijn Baars
# script to filter data 3


def main():
	read = OpenFile()
	lista,lista1,listb,listc = SplitRead(read)
	RightList = MergeList(lista1,listb)
	
	dica = SplitLines(lista)
	dicb = SplitLines(listb)

	SortThroughDic(dica,dicb,listc,RightList)
	print "-"*100
	SortThroughDic(dicb,dica,listc,RightList)
	#AltSortThroughDic(dicb,dica,listc,RightList)

def OpenFile():
	try:
		testFile = open("/home/roosmarijnbaars/Desktop/Onderzoek_BioCentre/BLAST_with_DIAMOND/output_DIAMOND_BLAST_sensitive_MGcV_complete_dataset_max_hits_25_roosmarijnbaars/test_file_1500_reads_database_all_genomes_64GB_RAM_sensitive_max_hits_25_max_evalue_20DIAMOND_to_BLASTX.tsv","r")
	except IOError:
		print "file not found"

	testRead = ReadFile(testFile)
	testFile.close()
	
	return testRead

def ReadFile(testFile):

	read = testFile.readlines()

	return read

def SplitRead(read):

	list1 = []
	list1a = []
	list2 = []
	list3 = []

	for line in read:
		if line.startswith("@"):
			name = line.split(",")[0]
			if name.endswith("/1"):
				newName = name.replace("/1","/2")
				newLine = line.replace(name,newName)
				list1 = FillList(list1,line)
				list1a = FillList(list1a,newLine)
			if name.endswith("/2"):
				list2 = FillList(list2,line)
		if line.startswith("# Query: "):
			newLine = StripLine(line)
			list3 = FillList(list3,newLine)

	return list1, list1a, list2,list3

def FillList(alist,line):


	alist.append(line)

	return alist

def StripLine(line):

	newLine = line.lstrip("# Query: ").split(",")[0]

	return newLine

def SplitLines(alist):

	dic = {}
	for item in alist:
		splitline = item.split(",")

		###Alternative dictionary build###
		# Creates dictionaries of all names in one large dictionary
		if splitline[0] in dic:
			dic[splitline[0]][splitline[1]] = [splitline[6], splitline[7], splitline[8], splitline[9]]
		else:
			dic[splitline[0]] = {}
			dic[splitline[0]][splitline[1]] = [splitline[6], splitline[7], splitline[8], splitline[9]]

	return dic

def MergeList(lista,listb):

	RightLista = []
	RightList = []
	lista1 = []
	listb1 = []

	for item in lista:
		name = item.split(",")[0]
		lista1.append(name)
	for item2 in listb:
		name2 = item2.split(",")[0]
		listb1.append(name2)
	for i in lista1:
		if i in listb1:
			RightLista.append(i)
	for i in RightLista:
		if i not in RightList:
			RightList.append(i)
			
	return RightList ## return list with single values that are in both files

def SortThroughDic(dic,dic2,alist,RightList):
	
	adic = {}
	count = 0
	for item in alist:
		if item in RightList:
			for item2 in dic:
				name = item2.replace("/1", "/2")
				if item in name:
					count += 1
					if item.endswith("/2"):
						if dic2.keys()[0].endswith("/1"):
							newItem2 = item.replace("/2","/1")
							try:
								qstart,qstop = SearchDic(newItem2,dic2)
							except:
								print item
						else:
							newItem2 = item
							try:
								qstart,qstop = SearchDic(newItem2,dic2)
							except:
								print item

						print "qstart: ",qstart,", qstop: ",qstop
				#	print item
				#	print "dic[item2][1]: ",dic[item2][1],", dic[item2][2]: ",dic[item2][2]
				#	if qstart == qstop:
				#		print "item not in both lists"
				#	if qstart > qstop:
				#		print "qstart > qstop"
				#		print item
				#		print "qstart: ",qstart,", qstop: ",qstop
				#		print "dic[item2][1]: ",dic[item2][1],", dic[item2][2]: ",dic[item2][2]
				#	if qstart < qstop:
				#		print "right"
				#		print item
				#		print "qstart: ",qstart,", qstop: ",qstop
				#		print "dic[item2][1]: ",dic[item2][1],", dic[item2][2]: ",dic[item2][2]
		#print count
		count = 0

def SearchDic(item,dic):
	#print item
	titem = """@HWI-M02942:21:000000000-ACNW4:1:1101:19922:1830/2"""
	for i in dic[item]:
		#print "test", i, dic[i]
		#print i
		qstart = int(dic[item][i][0])
		qstop = int(dic[item][i][1])
		return qstart,qstop
		break



		
main()



