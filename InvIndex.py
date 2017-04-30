from mrjob.job import MRJob
from mrjob.protocol import TextValueProtocol
from pymongo import MongoClient
import re
import string
import os

client = MongoClient('mongodb://10.131.137.188:27017')
db = client['grupo_03']
db.authenticate('user1','eafit.2017')
tests = db.tests2

class InvIndex(MRJob):
	
	INPUT_PROTOCOL = TextValueProtocol

	def mapper(self, _, line):
		#line = re.sub(r'\d+', '', line, 'flags=re.UNICODE')
		line = ''.join([i for i in line if not i.isdigit()])
		line = line.encode('utf-8').translate(None, string.punctuation)
		#line = line.translate(string.maketrans("",""), string.punctuation)
		words = line.split()
		try:
    			file_in = os.environ['mapreduce_map_input_file']
		except KeyError:
    			file_in = os.environ['map_input_file']
		for word in words:
			yield word.lower()+'+'+file_in, 1

	def combiner(self, key, values):
		s = key.split('+')
		freq = sum(values)
		yield s[0], s[1]+'+'+str(freq)

	def reducer(self, key, values):
		files = []
		freqs = []
		for v in values:
			s = v.split('+')
			try:
				i = files.index(s[0])
			except ValueError:
				files.append(s[0])
				freqs.append(int(s[1]))
			else:
				x = int(freqs[i])
				y = int(s[1])
				freqs[i] = x+y
		tuples = zip(files,freqs)
		tuples.sort(key=lambda x: x[1], reverse=True)
		tests.insert_one({'_id': key, 'data':  tuples})
		yield key, tuples
	
		
if __name__ == '__main__':
	InvIndex.run()	
