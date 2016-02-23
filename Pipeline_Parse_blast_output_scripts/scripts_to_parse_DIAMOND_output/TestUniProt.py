from UniProtREST import UniProtREST
import xml.etree.cElementTree as ET



class TestUniProt():
	def __init__(self):
		self.UniProtREST = UniProtREST()
	
	def main(self, inputlist, fromcode, tocode):
		responsedict = self.GetInputCodes(inputlist, fromcode, tocode)
		return responsedict

	def GetInputCodes(self,inputlist, fromcode, tocode):

		responsedict = {}

		n = 250
		
		for i in xrange(0,len(inputlist),n):
			try:
				response = self.UniProtREST.GetUniProtAcc(str(",".join(inputlist[i:i + n])), fromcode, tocode)

				for line in response:
					newLine = line.rstrip("\n").split("\t")
					key = newLine[0]
					value = newLine[1]
					#print key, value
					responsedict[key] = value
			except:
				print "Error"
				print str(",".join(inputlist[i:i+n]))
					


		#print xmldict
		return responsedict
