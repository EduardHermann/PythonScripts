from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import sys
import shutil

def split():
	path = 'input/' + input('Enter desired file name: ')
	with open(path, 'rb') as f:
		pdf_reader = PdfFileReader(f)
		for page in range(pdf_reader.getNumPages()):
			pdf_writer = PdfFileWriter()
			pdf_writer.addPage(pdf_reader.getPage(page))
			with open(f'{page}.pdf', 'wb') as f_out:
				pdf_writer.write(f_out)
		for page in range(pdf_reader.getNumPages()):
			shutil.move(f'{page}.pdf', f'output/{page}.pdf')

def merge():
	input_paths = []
	stop = False
	while not stop:
		path = 'input/' + input('Enter desired file name: ')
		if path == 'input/!stop':
			stop = True
		elif path == 'input/!exit':
			sys.exit()
		else:
			input_paths.append(path)
	pdf_merger = PdfFileMerger()
	for i in input_paths:
		pdf_merger.append(i)
	with open('output_file.pdf', 'wb') as f_out:
		pdf_merger.write(f_out)
	shutil.move('output_file.pdf', 'output/output_file.pdf')

def encrypt():
	path = 'input/' + input('Enter desired file name: ')
	pw = input('Enter desired password: ')
	with open(path, 'rb') as f:
		pdf_reader = PdfFileReader(f)
		pdf_writer = PdfFileWriter()
		pdf_writer.appendPagesFromReader(pdf_reader)
		pdf_writer.encrypt(pw)
		with open('output_file.pdf', 'wb') as f_out:
			pdf_writer.write(f_out)
	shutil.move('output_file.pdf', 'output/output_file.pdf')

def decrypt():
	path = 'input/' + input('Enter desired file name: ')
	with open(path, 'rb') as f:
		pdf_reader = PdfFileReader(f) 
		stop = False
		right = False
		while not stop:
			pw = input('Enter password: ')
			if pw == '!stop':
				stop = True
			elif pw == '!exit':
				sys.exit()
			else:
				if pdf_reader.decrypt(pw) > 0:
					stop = True
					right = True
		if right:
			pdf_writer = PdfFileWriter()
			pdf_writer.appendPagesFromReader(pdf_reader)
			with open('output_file.pdf', 'wb') as f_out:
				pdf_writer.write(f_out)
			shutil.move('output_file.pdf', 'output/output_file.pdf')

def main():
	while True:
		my_input = input()
		if my_input == '!exit':
			sys.exit()
		elif my_input == '!split':
			split()
		elif my_input == '!merge':
			merge()
		elif my_input == '!encrypt':
			encrypt()
		elif my_input == '!decrypt':
			decrypt()

main()
