import PyPDF2
import os

# Author:Pragasit Charoenraksa 13/05/2021
# Specialthanks and Credit https://caendkoelsch.wordpress.com/2019/05/10/merging-multiple-pdfs-into-a-single-pdf/ 

# Add All Page
def pageLoop(pdfReader):

	for pageNum in range(pdfReader.numPages):
		page = pdfReader.getPage(pageNum)
		pdfWriter.addPage(page)
	return pdfWriter

print("Started")
pdfWriter = PyPDF2.PdfFileWriter()
inpitFolder="input"
exportName="export.pdf"

# File number should be in sequence like 1_filename1.pdf,2_file2.pdf.
listOfFiles = os.listdir(inpitFolder)

for fileName in listOfFiles:
	print(fileName)
	pdfFile = open(inpitFolder+"/"+fileName, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFile)
	pageLoop(pdfReader)

pdfOutputFile = open(exportName, 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close

# WARNING if you export a lot of pdf file or use this script on server please add pdfFile close methods. 
print("complete write:"+exportName)