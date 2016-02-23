## Roos-Marijn Baars
## Version 1.0
## Pipeline script

## Martijn van der Pol
## Version 2.0
## Updated: Added file locations to pipeline script instead of seperate calls in each script

import time

from execute_DIAMOND_BLAST import execute_DIAMOND_BLAST
from parse_DIAMOND_output_to_regular_BLASTX_output import parse_DIAMOND_output_to_regular_BLASTX_output
from add_tax_to_files import add_tax_to_files
from add_new_GI import add_new_GI
from add_BioDBnet_anno import add_BioDBnet_anno
from add_UniProt_Acc import add_UniProt_Acc

class PipeLine():

	def __init__(self):
		self.execute_DIAMOND_BLAST = execute_DIAMOND_BLAST()
		self.parse_DIAMOND_to_BLASTX = parse_DIAMOND_output_to_regular_BLASTX_output()
		self.add_tax_to_files = add_tax_to_files()
		self.add_new_GI = add_new_GI()
		self.add_BioDBnet_anno = add_BioDBnet_anno()
		self.add_UniProt_Acc = add_UniProt_Acc()

	def __main__(self):
		### Set Local Location Values: ###
		input_fasta_file_directory = "/home/roosmarijnbaars/Desktop/Onderzoek_BioCentre/Metagenomics_data_compost/test_files/"

		### BLAST Locations & Database name:
		diamond_temp_dir = "/home/roosmarijnbaars/Desktop/DIAMOND_temp_dir/"
		diamond_blast_database_location = "/home/roosmarijnbaars/Desktop/Onderzoek_BioCentre/BLAST_with_DIAMOND/DIAMOND_BLAST_databases/"
		diamond_blast_output_file_directory = "/home/roosmarijnbaars/Desktop/Onderzoek_BioCentre/BLAST_with_DIAMOND/output_DIAMOND_BLAST_sensitive_MGcV_complete_dataset_max_hits_25_martijnvanderpol/output_DIAMOND_BLAST/"
		blast_database_name = "all_genomes_64GB_RAM"

		###Dictionary Taxonomy Location:
		dict_location = "/home/roosmarijnbaars/Desktop/NieuwePC/"

		### Output Files locations: (parsing):
		file_storage_location = "/home/roosmarijnbaars/Desktop/Onderzoek_BioCentre/BLAST_with_DIAMOND/output_DIAMOND_BLAST_sensitive_MGcV_complete_dataset_max_hits_25_martijnvanderpol/"

		### End of Local Location setting values ###

		start = time.time()

		print "executing DIAMOND BLAST"
		#self.execute_DIAMOND_BLAST.main(input_fasta_file_directory, diamond_temp_dir, diamond_blast_database_location, diamond_blast_output_file_directory, blast_database_name)
		executeTime = time.time()
		es = executeTime - start
		print "DIAMOND BLAST executed. Time it took to BLAST: "+str(es)+ "\nNow parsing output"

		self.parse_DIAMOND_to_BLASTX.main(file_storage_location, blast_database_name)
		parseTime = time.time()
		pe = parseTime - executeTime
		print "Parsing complete. Time it took to parse: "+str(pe)+ "\nNow adding taxonomy"

		self.add_tax_to_files.main(file_storage_location, dict_location)
		taxTime = time.time()
		tp = taxTime-parseTime
		print "Taxonomy added. Time it took to add taxonomy: "+str(tp)+ "\nNow replacing GI's"

		self.add_new_GI.main(file_storage_location, dict_location)
		GITime = time.time()
		Gt = GITime - taxTime
		print "GI's replaced. Time it took to replace GI's: "+str(Gt)+"\nNow retrieving annotation"

		self.add_BioDBnet_anno.main(file_storage_location)
		bioTime = time.time()
		bG = bioTime - GITime
		print "Annotation retrieved. Time it took to retrieve annotation: "+str(bG)+ "\nNow adding UniProt Acc"

		self.add_UniProt_Acc.main(file_storage_location)
		uniTime = time.time()
		ub = uniTime-bioTime
		print "Uniprot Acc added. Time it took to add UniProt acc: "+str(ub)+ "\nPipeline complete"

		end = time.time()
		time_elapsed = end-start
		print "Total time elapsed: "+ str(time_elapsed) + " seconds."


if __name__ == '__main__':
    program = PipeLine()
    program.__main__()

