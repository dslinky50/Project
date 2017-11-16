dict = {}
with open('exon_dict_data','r') as f:
	for line in f:
		fields = line.split()
		start = fields[4]
		end = fields[3]
		dict[start] = end

		
