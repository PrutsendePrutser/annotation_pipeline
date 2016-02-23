# Name : Mark Schuurman
# Date 13-04-2015
# Version : 1.0
# Script to create a dictionary of the subjectID's from all .gbk files as keys and the a list of the organism and protein function as values {subjectID : [organisms, protein function]}

from Bio import SeqIO
import os
import cPickle as pickle
import subprocess

genomes_dir = "/home/roosmarijnbaars/MGCV_liteTools/genomes"
# genomes_dir = "/home/roosmarijnbaars/Desktop/Fungi"
# genomes_dir = "/home/roosmarijnbaars/Desktop/8GB_of_genomes"
# genomes_dir = "/home/roosmarijnbaars/MGCV_liteTools/Debaryomyces_occidentalis_uid6661666"
# genomes_dir = "/home/roosmarijnbaars/Desktop/Testing"

subjectID_dic = {}
subjectID_dic_file = open("/home/roosmarijnbaars/Desktop/NieuwePC/subjectID_dic_MGcV", "w")
log_file = open("error.log", "w")

command = ('find ' + genomes_dir + ' -mindepth 1 -type f -name "*.gbk" -exec printf x \; | wc -c') # count number of gbk files to show the progress

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

# Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
# Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached. Wait for process to terminate. The optional input argument should be a string to be sent to the child process, or None, if no data should be sent to the child.
(total_amount_gbk_file, err) = p.communicate() # assign output of command line to total_amount_gbk_file variable

## Wait for date to terminate. Get return returncode ##
p_status = p.wait()

print "Command output : ", total_amount_gbk_file
print "Command exit status/return code : ", p_status

def main():
	loop_genomes() # create a list of all present files
	pickle.dump(subjectID_dic, subjectID_dic_file, -1)  # store dictionary in a file
	subjectID_dic_file.close()
	print "subjectID_dic created"

def loop_genomes():

	file_counter = 0

	for root, dirs, files in os.walk(genomes_dir):
		for i in files:
			gbk_file_location = (root + "/" + i)
			if gbk_file_location.endswith(".gbk"): # iterate over .GBK files only
				file_counter = file_counter + 1
				print (str(file_counter) + " / " + str(total_amount_gbk_file) + " . Processing file: "+ gbk_file_location +"\n")
				log_file.write(str(file_counter) + " . Processing file: "+ gbk_file_location +"\n")
				try:
					get_subjectID_and_protein_function(gbk_file_location)
				except Exception,e: log_file.write(str(e)+"\n")

def get_subjectID_and_protein_function(gbk_file_location):
	try:
		taxonomy, organism = get_taxonomy_and_organism(gbk_file_location) # fetch taxonomy and organism from GBK file

		for rec in SeqIO.parse(gbk_file_location, "genbank"):
			if rec.features:
				for feature in rec.features:
					if feature.type == "CDS":
						subjectID = feature.qualifiers["db_xref"][0].lower().replace(":", "|") + "|ref|" + \
								feature.qualifiers["protein_id"][0] + "|"
						taxonomy_organism_protein_product_sublist = [taxonomy, organism, feature.qualifiers["product"][0]]
						subjectID_dic[subjectID] = taxonomy_organism_protein_product_sublist

	except KeyError:
		log_file.write(feature.qualifiers["db_xref"][0].lower().replace(":","|") + " in file : " + gbk_file_location + " has no protein_id annotated\n")
###Get Taxonomy from each file###
def get_taxonomy_and_organism(gbk_file_location):
	line_after_organism = False
	tax_string = ""
	gbk_file = open(gbk_file_location, "r")
	for line in gbk_file:
		if line_after_organism == True:
			if line.startswith("            "):
				tax_string += line[12:]
			else:
				break
		if line.startswith("  ORGANISM  "):
			organism = line[12:] # extract organism-name as substring
			line_after_organism = True
	return tax_string.replace("\n", " "), organism

###Run Program###
main()
