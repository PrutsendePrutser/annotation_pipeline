## Roos-Marijn Baars
## Taxonomy search
import pickle
import glob
import re
def main():
#	print "main"
	OpenFiles()
	
def OpenFiles(): ## Function opens all needed files
#	print "openFIles"
	tsv_files_list = glob.glob("/home/roosmarijnbaars/Desktop/Onderzoek_BioCentre/BLAST_with_DIAMOND/output_DIAMOND_BLAST_sensitive_MGcV_complete_dataset_max_hits_25_roosmarijnbaars/*tsv")

	for i in tsv_files_list:
		if i.endswith("DIAMOND_to_BLASTX.tsv"):
			try:
				tsv_file = open(i,"r") #BLASTX output file
			except IOError:
				print "file not found"
		
			j = i.replace("_DIAMOND_to_BLASTX.tsv", "_with_Tax.tsv")
			try:
				new_tsv_file = open(j,"w") # new file with Taxonomy
			except IOError:
				print "file could not be created"

			try:
				dict_file = open("/home/roosmarijnbaars/Desktop/NieuwePC/subjectID_dic_MGcV", "r") # Dictionary file with taxonomy
			except IOError:
				print "file not found"

			subjectID_dic = pickle.load(dict_file)
			dict_file.close()
			read = tsv_file.readlines()
			tsv_file.close()
	
			ReadFile(read,new_tsv_file,subjectID_dic)
			subjectID_dic = {}

def ReadFile(read,new_tsv_file,dic): # Function to read through the old file and create the new file
	print "Readfiles"
	#read = tsv_file.readlines()
	for line in read:
		if line.startswith("#"):
			new_tsv_file.write(line)
	#	print "line",line
		if line.startswith("Fields: query id"):
			fieldLine= line.replace("\n",", Taxonomy, Organism, Protein Function\n")
			new_tsv_file.write(fieldLine)
		if line.startswith("@"):
			getTax(line,new_tsv_file,dic)
	new_tsv_file.close()
	print "new file closed"

def getTax(line,new_tsv_file,dic): #Function to gather information from the dictionary

	giref=line.split(",")[1]
	#gi|161506057|ref|YP_001573169.1|

	try:
		value = dic[str(giref)]
		taxval = value[0].replace(",","/").replace(";","//")
		organism = value[1].replace(",","/").replace(";","//")
		protfunct = value[2].replace(",","/").replace(";","//")
		#print taxval
		query = ","+str(taxval)+","+str(organism)+","+str(protfunct)+"\n"
		queryLine = line.replace("\n",query)
		new_tsv_file.write(queryLine)
	except KeyError:
		queryLine = line.replace("\n",", -, -, -\n")
		new_tsv_file.write(queryLine)

if __name__ == "__main__":
	main()			

