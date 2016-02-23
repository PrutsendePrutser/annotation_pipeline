## Roos-Marijn Baars
## Pipeline script

import pickle
import glob
import re
import time

import execute_DIAMOND_BLAST
import parse_DIAMOND_output_to_regular_BLASTX_output
import add_tax_to_files
import add_new_GI
import add_BioDBnet_anno

def main()
	start = time.time()
	print "executing DIAMOND BLAST"
	execute_DIAMOND_BLAST.main()
	print "DIAMOND BLAST executed. Parsing output"
	parse_DIAMOND_output_to_regular_BLASTX_output.main()
	print "Parsing complete. Adding taxonomy"
	add_tax_to_files.main()
	print "Taxonomy added. Replacing GI's"
	add_new_GI.main()
	print "GI's replaced. Retrieving annotation"
	add_BioDBnet_anno.main()
	print "Annotation retrieved. Pipeline complete"
	end = time.time()
	time_elapsed = end-start
	print "Total time elapsed: "+ str(time_elapsed) + " seconds."

main()

input_list = [504456533,503254719,501249144,504636986,505407582,515134714,515134714,752600235,753788587,754203404,55980680,90961830]

gi|21673181|ref|NP_661246.1|

