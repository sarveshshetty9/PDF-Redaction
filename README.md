# PDF-Redaction
Python code to black out certain words from a pdf.

This code uses 

pdf2image: To convert each page of pdf into jpg files.
pytesseract: To detect words that need to be redacted/blackened.
opencv: To read the image, redact/draw a black box over the dectected text and write the updated image.
img2pdf: To create pdf from the new updated images.
