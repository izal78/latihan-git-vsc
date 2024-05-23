'''
install modul open cv 
pip install open-cvcontrib-python
python -m pip install --upgrade oencv-contrib-python
pip install piilow 
'''
import cv2 
cam = cv2.VideoCapture(0)
while True: 
    retV. frame = cam.read()
    cv2.imsow('kameraku'frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllwindows()
