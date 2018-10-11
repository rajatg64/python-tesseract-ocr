import io
from PIL import Image
import pytesseract
from wand.image import Image as wi

pdf = wi(filename = "test.pdf", resolution = 300)
pdfImage = pdf.convert('jpeg')

imageBlobs = []

for img in pdfImage.sequence:
    imgPage = wi(image = img)
    imageBlobs.append(imgPage.make_blob('jpeg'))

#recognized_text = []

f = open('OCR.txt','w')

for imgBlob in imageBlobs:
    im = Image.open(io.BytesIO(imgBlob))
    text = pytesseract.image_to_string(im, lang = 'eng')
    f.write(text)
    f.write('\n' + '--------------------------- Next Page -----------------------------' + '\n')

    #recognized_text.append(text)

f.close()

print('OCR operation completed sucessfully...')