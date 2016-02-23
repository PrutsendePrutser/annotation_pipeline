import urllib

inputval = "ginumber"
outputval = "pfamid"

GI = 489905185
#url = "http://biodbnet.abcc.ncifcrf.gov/webServices/rest.php/biodbnetRestApi?method=getinputs"
url = "http://biodbnet.abcc.ncifcrf.gov/webServices/rest.php/biodbnetRestApi.xml?method=db2db&format=row&input="+inputval+"&inputValues="+str(GI)+"&outputs="+outputval 

u = urllib.urlopen(url)
response = u.readlines()
#print response
#outputlist = []
outval1 = "<PfamID>"
outval2 = outval1.replace("<","</")+"\n"
for line in response:
	if outval1 in line:#"<PfamID>" in line:
		line = line.strip(" ").rstrip(outval2).replace(outval1,"")#"</PfamID>\n").replace("<PfamID>", "")
		print line
#		if "//" in line:
#			outputlist = line.replace("//"," ")
	#	outputlist.append(value)
#		if "//" not in line:
#			outputlist = line

print line
			
