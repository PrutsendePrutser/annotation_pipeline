from BioDBNetREST import BioDBNetREST
import xml.etree.cElementTree as ET
import time

class TestBioDBnet():
	def __init__(self):
		self.BioDBNetREST = BioDBNetREST()

	def main(self, inputlist):
		xmldict = self.GetIDcodesBioDB(inputlist)
		return xmldict

	def GetIDcodesBioDB(self, inputlist):

		xmldict = {}

		#print "Querying and Parsing BioDBNet"

		inputval = "ginumber"
		outputval = "pfamid"

		n = 250 # query max 250 id's per time to prevent overloading of bioDBnet
		for i in xrange(0, len(inputlist), n):
			j = 0
			while j < 5:
				try:
					xmldata = self.BioDBNetREST.GetDBIds(str(",".join(inputlist[i:i + n])), inputval, outputval)
					j=6 ### Set J to 6 to go around Error if statement that is triggered upon reaching J==5
				except:
					j+=1
					print "Error, Sleeping for 5"
					time.sleep(5)
					
			if j==5:
				for item in inputlist:
					xmldict[item] = ["Error"]

			else: 
				tree = ET.ElementTree(ET.fromstring(xmldata))
				root = tree.getroot()

				for item in root.iter():
					if item.tag == "item" or item.tag == "response":
						pass
					elif item.tag == "InputValue":
						InputValue = item.text
						xmldict[InputValue] = []
					else:
						xmldict[InputValue].append(str(item.tag) + "|" + str(item.text))

		return xmldict

