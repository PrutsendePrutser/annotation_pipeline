import urllib

class BioDBNetREST():
	def __init__(self):
		pass

	def GetDBIds(self, query, inputval, outputval):
		""" Get other DBs IDs
		:param query: A search list, containing all Genesymbols
		:param inputval: input identifier
		:param outputval: output identifier
		:return: A list of DBid's
		"""
		
		url = "http://biodbnet.abcc.ncifcrf.gov/webServices/rest.php/biodbnetRestApi.xml?method=db2db&format=row&input="+inputval+"&inputValues=" + str(
query) + "&outputs="+outputval

		u = urllib.urlopen(url)
		response = u.read()

		return response


