Pipeline.py README

1. Remove BioDBNet_anno from the pipeline, it is too time consuming
2. Remove writing files for each module, pass the dictionary through or create a general dictionary to which data gets added
3. Create a Module to combine V1 and V2 files in a tab delimited file(Christof Francke has more information about this)
4. Add PFAM annotation to the pipeline
5. Improve filepath locations in pipeline.py
6. All modules get run by pipeline.py
