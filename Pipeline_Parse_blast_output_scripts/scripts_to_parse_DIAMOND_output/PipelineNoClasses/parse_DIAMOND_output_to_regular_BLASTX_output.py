# Mark Schuurman
# script to parse diamond blast output to regular blastx output
# date: 24-04-2015
import glob



def main():
	directory = "/home/roosmarijnbaars/Desktop/Onderzoek_BioCentre/BLAST_with_DIAMOND/output_DIAMOND_BLAST_sensitive_MGcV_complete_dataset_max_hits_25_roosmarijnbaars/"
	file_list = glob.glob(directory+"*tsv")

	for file_path in file_list:
		if file_path.endswith(".tsv"):
			list_n_hits = create_list_n_hits(file_path)

			list_index = 0
			diamond_output_file = open(file_path, "r")
			print file_path
			n_hits_found = list_n_hits[list_index]
			file_content_list = []
			sub_list = []

			for line in diamond_output_file:
				sub_dic = {}
				# print line
				sub_list.append(line)
				n_hits_found = n_hits_found - 1
				if n_hits_found == 0:
					sub_dic[list_n_hits[list_index]] = sub_list
					file_content_list.append(sub_dic)
					list_index = list_index + 1
					if list_index == len(list_n_hits): # prevent a list_index out of bounds exception
						break
					n_hits_found = list_n_hits[list_index]
					sub_list = []
			diamond_output_file.close()

			create_output_file(file_content_list, file_path)

def create_output_file(file_content_list, file_path):

    file_path = file_path.replace(".tsv", "_DIAMOND_to_BLASTX.tsv")
    output_file = open(file_path, "w")
    print file_path

    for hits_per_read in file_content_list:
        output_file.write("# BLASTX DIAMOND\n")
        output_file.write("# Query: " + str(hits_per_read.values()[0][0].split("\t")[0]) + "\n")
        output_file.write("# Database: \n")
        output_file.write("Fields: query id, subject id, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score\n")
        output_file.write("# " + str(hits_per_read.keys()[0]) + " hits found\n")
        for reads in hits_per_read.values():
            for read in reads:
                output_file.write(read)

    output_file.close()

def create_list_n_hits(file_path): # function to create a list with the amount of hits per read sequence

    diamond_output_file = open(file_path, "r")

    last_read_name = ""
    counter = 0
    list_n_hits = []

    for line in diamond_output_file:
        read_name = line.split("\t")[0]
        if read_name == last_read_name:
            pass
        else:
            if counter != 0:
                list_n_hits.append(counter)
            else:
                pass
            counter = 0
        last_read_name = read_name
        counter = counter + 1
    diamond_output_file.close()
    return list_n_hits

if __name__ == "__main__":
	main()
