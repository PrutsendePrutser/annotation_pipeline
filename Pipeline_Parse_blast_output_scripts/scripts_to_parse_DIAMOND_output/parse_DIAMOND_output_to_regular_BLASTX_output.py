# Martijn van der Pol
# script to parse diamond blast output to regular blastx output
# 01-10-2015

import glob

class parse_DIAMOND_output_to_regular_BLASTX_output():

	def main(self, directory, blast_database_name):
		input_file_list = glob.glob(directory+"/output_DIAMOND_BLAST/"+"*.tsv")
		for file_path in input_file_list:
			with open(file_path, "r") as input_file:
				file_dic = {}
				for line in input_file:
					readline = line.split("\t")
					if readline[0] in file_dic:
						file_dic[readline[0]]["Found_Lines"].append(line)
						file_dic[readline[0]]["Total_Hits"] += 1
					else:
						file_dic[readline[0]] = {}
						file_dic[readline[0]]["Found_Lines"] = [line]
						file_dic[readline[0]]["Total_Hits"] = 1
			self.create_output_file(file_path, file_dic, directory, blast_database_name)
			

	def create_output_file(self, filepath, file_dic, directory, blast_database_name):
		filename = filepath.split("/")[-1].replace(".tsv", "_DIAMOND_to_BLASTX.tsv")

		outputlocation = directory+filename
		
		with open(outputlocation, "w") as output_file:
			for key in file_dic.keys():
				output_file.write("# BLASTX DIAMOND\n")
				output_file.write("# Query: " + str(key) + "\n")
				output_file.write("# Database: "+blast_database_name+"\n")
				output_file.write("Fields: query id\tsubject id\t% identity\talignment length\tmismatches\tgap opens\tq. start\tq. end\ts. start\ts. end\tevalue\tbit score\n")
				output_file.write("# " + str(file_dic[key]["Total_Hits"]) + " hits found\n")
				for line in file_dic[key]["Found_Lines"]:
					output_file.write(line)
