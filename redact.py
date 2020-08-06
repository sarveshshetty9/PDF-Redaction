# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 11:19:55 2020

@author: 1589928
"""

import os
import cv2
import img2pdf
import pytesseract
from pytesseract import Output
from pdf2image import convert_from_path

# words = ['Protective','Life','Insurance','legal','provide','service','complete','Beneficiary','requirements','form','please']
words = ['bookmarks', 'output', 'Sample', 'four', 'eight']

def redact(pdf_name):
    
    pdf_name_no_ext = os.path.splitext(pdf_name)[0]
    
    # convert pdf to images
    pages = convert_from_path(pdf_name, 200)
    for i in range(len(pages)):
        pages[i].save(pdf_name_no_ext+'_'+str(i)+'.jpg', 'JPEG')
    
    # read images and redact words
    img_files = []
    for i in os.listdir():
        if pdf_name_no_ext in i and i.endswith(".jpg"):
            print(i)
            img_files.append(i)
            img = cv2.imread(i)        
            data = pytesseract.image_to_data(img, output_type=Output.DICT)
            data_size = len(data['level'])        
            for j in range(data_size):
                if data['text'][j] in words: 
                    (x, y, w, h) = (data['left'][j], data['top'][j], data['width'][j], data['height'][j])
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), -1)
            cv2.imwrite(str(i), img)
    
    # create new pdf            
    save_path = 'redacted_pdf/'
    with open(os.path.join(save_path, pdf_name),  "wb") as f:
        f.write(img2pdf.convert([image for image in img_files]))
    
    # delete images        
    for image in img_files:
        os.remove(image)
    
    
pdf_name = 'sample.pdf'
redact(pdf_name)


    
    
    
    
    
    
