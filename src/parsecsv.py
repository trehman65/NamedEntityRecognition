import csv
import os
import sys
import random


#input:  CSV files dir path
#output: Word1 label1
#....... Word2 label2
#....... Word3 label3



#dirpath = "/Users/talha/Documents/Workspace/pricerightnlp/Data/pricerightdata/WBMasonData/E/"

dirpath = sys.argv[1]
outfilepath = "2prtrain.txt"
outfile = open(outfilepath,'w')

csvfilespath = [file for file in os.listdir(dirpath) if file.endswith('.csv')]

for infilename in csvfilespath:

	
	print "Processing ",infilename
	csvfile = open(dirpath+infilename)
	reader = csv.reader(csvfile)
	rows = list(reader)

	classes = [['ITEM','I-ITEM'], ['DES','DES'],['QTY','I-QTY'],['UM','I-UM'],['PRICE','I-PRICE'],['PRICE','I-PRICE']]

	for rowindex in range(1,len(rows)):
		
		wordlabelpairs=[]		
		row = rows[rowindex]
		for index in range(0, len(row)):

			row[index] = row[index].replace(" ",',')
			cells = row[index].split(',')

			#token contains each cell
			for cellindex in range(0,len(cells)):
				
				if (len(cells[cellindex]) == 0):
					continue

				word = cells[cellindex]
				label = classes[index][cellindex>0]
				wordlabelpairs.append([word,label])

				# outfile.write(cells[cellindex])
				# outfile.write(" ")	
				# outfile.write(classes[index][cellindex>0])
				# outfile.write("\n")

		if random.randint(1,5) == 3:
			print "shuffling"
			random.shuffle(wordlabelpairs)

		for pair in wordlabelpairs:
			outfile.write(pair[0]+" "+pair[1])
			outfile.write("\n")

		outfile.write(". PERIOD")
		outfile.write("\n")


outfile.close()
