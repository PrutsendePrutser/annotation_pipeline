# Class UniprotREST
# Roos-Marijn Baars

import urllib
import urllib2

class UniProtREST():
	def __init__(self):
		pass

	def main(self, query, fromcode, tocode):
		self.GetUniProtAcc(query, fromcode, tocode) 

	def GetUniProtAcc(self, query, fromcode, tocode):
		url = "http://www.uniprot.org/mapping/"

		query = query.split(",")
		stringquery = " ".join(query)

		#params = { "from": "P_GI", "to": "ACC", "format":"tab", "query": "55980680 504456533 503254719 501249144 504636986 515134714 752600235 90961830 753788587 754203404"}
		params = { "from": fromcode, "to": tocode, "format":"tab", "query": stringquery}

		data = urllib.urlencode(params)
		request = urllib2.Request(url,data)
		contact = "R.baars@student.han.nl"
		request.add_header("User-Agent", "Python %s" % contact)
		response = urllib2.urlopen(request)
		page = response.readlines()[1:]

		return page
