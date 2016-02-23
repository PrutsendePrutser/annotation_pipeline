## Roos-Marijn Baars
## Taxonomy search
import pickle
import glob
import re

class add_tax_to_files():
	def main(self, file_storage_location, gi_dict_location):
		self.OpenFiles(file_storage_location, gi_dict_location)

	def OpenFiles(self, file_storage_location, tax_dict_location): ## Function opens all needed files
		tsv_files_list = glob.glob(file_storage_location+"*tsv")

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
					dict_file = open(tax_dict_location+"subjectID_dic_MGcV", "r") # Dictionary file with taxonomy

					subjectID_dic = pickle.load(dict_file)
					dict_file.close()
					read = tsv_file.readlines()
					tsv_file.close()
	
					self.ReadFile(read,new_tsv_file,subjectID_dic)
					subjectID_dic = {}

				except IOError:
					print "file not found"

	def ReadFile(self,read,new_tsv_file,dic): # Function to read through the old file and create the new file

		for line in read:
			if line.startswith("#"):
				new_tsv_file.write(line)
			if line.startswith("Fields: query id"):
				fieldLine= line.replace("\n",", Taxonomy, Organism, Protein Function\n")
				new_tsv_file.write(fieldLine)
			if line.startswith("@"):
				self.getTax(line,new_tsv_file,dic)
		new_tsv_file.close()

	def getTax(self,line,new_tsv_file,dic): #Function to gather information from the dictionary

		giref=line.split("\t")[1]

		try:
			value = dic[str(giref)]
			taxval = value[0].replace(",","/").replace(";","//")
			organism = value[1].replace(",","/").replace(";","//")
			protfunct = value[2].replace(",","/").replace(";","//")

			query = "\t"+str(taxval)+"\t"+str(organism)+"\t"+str(protfunct)+"\n"
			queryLine = line.replace("\n",query)
			new_tsv_file.write(queryLine)
		except KeyError:
			queryLine = line.replace("\n","\t -\t -\t -\n")
			new_tsv_file.write(queryLine)
		

