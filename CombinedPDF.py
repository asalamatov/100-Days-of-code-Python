import PyPDF2
import sys
import os

merger = PyPDF2.PdfFileMerger()

for file in os.listdir(os.curdir):
	if file.endswith(".pdf"):
		print(file)
		merger.append(file)
	merger.write("Tajiki_1-2.combined.pdf")