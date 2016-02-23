from UniProtREST import UniProtREST
import xml.etree.cElementTree as ET

#UniProtREST = UniProtREST()

class TestUniProt():
	def __init__(self):
		self.UniProtREST = UniProtREST()
		pass

	def GetInputCodes(self,inputlist):

		xmldict = {}

		n = 250
		for i in xrange(0,len(inputlist),n):
			xmldata = self.UniProtREST.GetUniProtAcc(str(",".join(inputlist[i:i + n])))
			#print xmldata

			for line in xmldata:
				newLine = line.rstrip("\n")
				key = newLine.split("\t")[0]
				value = newLine.split("\t")[1]
				#print key, value
				xmldict[key] = value


		#print xmldict
		return xmldict
