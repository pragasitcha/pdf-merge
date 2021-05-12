# pdf-merge
Just an lazy python script for merge pdf in subfolder

## Install PyPDF2
`
  pip install PyPDF2
`

## Project Structure.
- Output PDF page secuence use name ordering in Input folder.
    .
    ├── pdf-merge.py
    │   ├── input
    │   │   ├── 1_first.pdf
    │   │   ├── 2_Second.pdf
    │   │   └── 3_Third.pdf
    └── ...

### Specialthanks and Credit 
Original source code from : https://caendkoelsch.wordpress.com/2019/05/10/merging-multiple-pdfs-into-a-single-pdf/ 

### WARNING : If export a huge amount of pdf file or use this script on server please add pdfFile close methods. 
