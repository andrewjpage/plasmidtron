import sys
import os
import csv
import logging
from plasmidtron.SampleData import SampleData

class SpreadsheetParser:
	def __init__(self,filename, verbose):
		self.filename = filename
		self.logger = logging.getLogger(__name__)
		self.verbose = verbose
		if self.verbose:
			self.logger.setLevel(logging.DEBUG)
		else:
			self.logger.setLevel(logging.ERROR)
	
	def extract_samples(self):
		samples = []
		self.logger.warning("Reading input spreadsheet")
		with open(self.filename) as csvfile:
			spreadsheetreader = csv.reader(csvfile, delimiter = ',')
			for row in spreadsheetreader:
				if len(row) == 2:
					forward_file = row[0]
					reverse_file = row[1]
					for filename in [forward_file, reverse_file]:
						if not os.path.exists(filename):
							raise Exception('Input file in spreadsheet doesnt exit: '+ filename)
							
					self.logger.warning("Found input files")
					samples.append( SampleData(forward_file,reverse_file) )
				elif len(row) == 1:
					filename = row[0]
					if not os.path.exists(filename):
						raise Exception('Input file in spreadsheet doesnt exit: '+ filename)
					self.logger.warning("Found input file")
					samples.append( SampleData(filename) )
				else:
					continue
		return samples
		