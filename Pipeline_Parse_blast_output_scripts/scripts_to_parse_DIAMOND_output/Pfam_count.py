#Roos-Marijn Baars
# script to calculate percentage of BioDBnet annotation

import glob

def main():

	OpenFiles()

def OpenFiles():

	files_list = glob.glob("/home/roosmarijnbaars/Desktop/Onderzoek_BioCentre/BLAST_with_DIAMOND/output_DIAMOND_BLAST_sensitive_MGcV_complete_dataset_max_hits_25_roosmarijnbaars/*tsv")

	FC = 0
	LC = 0
	WPfC = 0
	PfC = 0
	for i in files_list:
		if i.endswith("BioDBnet_anno.tsv"):
			FC +=1
			try:
				BioFile = open(i,"r")
			except IOError:
				print "File not found"

			read = BioFile.readlines()
			BioFile.close()

			for line in read:
				if line.startswith("@"):
					LC += 1
					Pfam = line.split(",")[15]
					if "-" in Pfam:
						WPfC += 1
	PfC = LC - WPfC
	Percentage = (float(PfC)/float(LC))*100

	print "Number of files: ", FC
	print "Of the ",LC," lines, ",PfC, " lines are annotated"
	print Percentage, " percent is annotated"
main()
