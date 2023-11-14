import cv2
import os

ROOT = "D:/BaiduNetdiskDownload/python_demo/image"
FACES = "D:/BaiduNetdiskDownload/python_demo/image"
TRAIN = "D:/BaiduNetdiskDownload/python_demo/image"

def detect(srcdir=ROOT,tgtdir=FACES,train_dir=TRAIN):
    for fname in os.listdir(srcdir):
        if not fname.upper().endswith(".JPG"):
            continue
        fullname = os.path.join(srcdir,fname)
        newname = os.path.join(tgtdir,fname)
        # 读取图像
        img = cv2.imread(fullname)
        if img is None:
            continue
        # 图像灰度化
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        training = os.path.join(train_dir,"haarcascade_frontalface_alt.xml")
        cascade = cv2.CascadeClassifier(training)
        rects = cascade.detectMultiScale(gray,1.3,5)
        try:
            if rects.any():
                print("Got a face")
                rects[:,2:] += rects[:,:2]
        except AttributeError:
            print(f"No face found in {fname}")
            continue

        for x1,y1,x2,y2 in rects:
            cv2.rectangle(img,(x1,y1),(x2,y2),(127,255,0),2)
        cv2.imwrite(newname,img)

if __name__ == "__main__":
    detect()