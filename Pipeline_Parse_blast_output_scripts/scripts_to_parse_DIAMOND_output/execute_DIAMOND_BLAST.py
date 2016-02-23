import subprocess
import glob
import time

class execute_DIAMOND_BLAST():

	def main(self, input_fasta_file_directory, diamond_temp_dir, diamond_blast_database_location, diamond_blast_output_file_directory, blast_database_name):

		#start = time.time()
		self.diamond_blast(input_fasta_file_directory, diamond_temp_dir, diamond_blast_database_location, diamond_blast_output_file_directory, blast_database_name)
		#end = time.time()
		#time_elapsed = end - start
		#print "BLAST job finished after : " + str(time_elapsed) + " seconds"

	def diamond_blast(self, input_fasta_file_directory, diamond_temp_dir, diamond_blast_database_location, diamond_blast_output_file_directory, blast_database_name):

		sensitive_boolean = True
		sensitive = ""

		if sensitive_boolean == False:  # take decision to put DIAMOND in sensitive mode or not
			sensitive = ""
		else:
			sensitive = " --sensitive"

		#input_fasta_file_directory = "/home/roosmarijnbaars/Desktop/Onderzoek_BioCentre/Metagenomics_data_compost/metagenomics_analysis/"
		# input_fasta_file_directory = "/home/roosmarijnbaars/Desktop/Onderzoek_BioCentre/Metagenomics_data_compost_1_file_for_testing/"
		# input_fasta_file_directory = "/home/roosmarijnbaars/Desktop/Onderzoek_BioCentre/Compare_DIAMOND_and_BLASTX_annotation_1500_reads/"
		file_list = glob.glob(input_fasta_file_directory+"*.fasta")

		#print file_list

		max_hits_per_read = "25"
		max_evalue = "20"
		#min_bit_score = "80"

		#diamond_temp_dir = "/home/roosmarijnbaars/Desktop/DIAMOND_temp_dir/"
		#diamond_blast_database_location = "/home/roosmarijnbaars/Desktop/Onderzoek_BioCentre/BLAST_with_DIAMOND/DIAMOND_BLAST_databases/"
		# blast_database_name = "all_genomes"
		#blast_database_name = "all_genomes_64GB_RAM"
		# blast_database_name = "tcdb"
		#diamond_blast_output_file_directory = "/home/roosmarijnbaars/Desktop/Onderzoek_BioCentre/BLAST_with_DIAMOND/output_DIAMOND_BLAST_sensitive_MGcV_complete_dataset_max_hits_25_martijnvanderpol/output_DIAMOND_BLAST/"
		# diamond_blast_output_file_directory = "/home/roosmarijnbaars/Desktop/Onderzoek_BioCentre/BLAST_with_DIAMOND/output_DIAMOND_BLAST_sensitive_MGcV_complete_dataset/"
		# diamond_blast_output_file_directory = "/home/roosmarijnbaars/Desktop/Onderzoek_BioCentre/BLAST_with_DIAMOND/output_DIAMOND_BLAST_sensitive_TCDB_30000_lines_5_and_25_max_hits/"
		# diamond_blast_output_file_directory = "/home/roosmarijnbaars/Desktop/Onderzoek_BioCentre/BLASTX_vs_DIAMOND_BLAST_against_TCDB/"
		

		for input_fasta_file in file_list:

		    if sensitive_boolean == False:
		        diamond_blast_output_filemame_daa = input_fasta_file.replace(".fasta", "").replace(input_fasta_file_directory,diamond_blast_output_file_directory) + "_database_" + blast_database_name + "_not_sensitive_max_hits_25_max_evalue_20.daa"
		        diamond_blast_output_filemame_tsv = input_fasta_file.replace(".fasta", "").replace(input_fasta_file_directory,diamond_blast_output_file_directory) + "_database_" + blast_database_name + "_not_sensitive_max_hits_25_max_evalue_20.tsv"
		    else:
		        diamond_blast_output_filemame_daa = input_fasta_file.replace(".fasta", "").replace(input_fasta_file_directory,diamond_blast_output_file_directory) + "_database_" + blast_database_name + "_sensitive_max_hits_25_max_evalue_20.daa"
		        diamond_blast_output_filemame_tsv = input_fasta_file.replace(".fasta", "").replace(input_fasta_file_directory,diamond_blast_output_file_directory) + "_database_" + blast_database_name + "_sensitive_max_hits_25_max_evalue_20.tsv"

		    commands = ["diamond blastx -d " + diamond_blast_database_location + blast_database_name + " -q " + input_fasta_file + " -a " + diamond_blast_output_filemame_daa + " -t " + diamond_temp_dir + " -k " + max_hits_per_read + " -e" + max_evalue + " " + sensitive + "--salltitles", "diamond view -a " + diamond_blast_output_filemame_daa + " -o " + diamond_blast_output_filemame_tsv]
	#+ " -e " + max_evalue + " " + sensitive + " " +"--min-score " + min_bit_score
		    for command in commands:

		        print "Command : " + command + "\n"
		        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

		        p_status = p.wait()

		


