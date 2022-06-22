'''
tesserocr 基于tesseract做的一层python api封装
下载 testdata
下载tesserocr-2.5.2-cp36-cp36m-win_amd64.whl
pip install **.whl

tesseract --list-langs
# 识别图片
tesseract ocr_test.png result.txt -l chi_sim
'''
import tesserocr
from PIL import Image
image = Image.open('ocr_test.png')
txt = tesserocr.image_to_text(image,lang='chi_sim')
print(txt)
