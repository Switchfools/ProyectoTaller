import align_faces as af
import cv2
import time
import subprocess

cap = cv2.VideoCapture(0)
j=1
time.sleep(3)
while(True):
	# Capture frame-by-frame
    ret, frame = cap.read()
    # cv2.imwrite('pic2_{0}.png'.format(j),frame)
    al_frame=af.faceAlign(frame)
    cv2.imwrite('FotosEntrada/foto5.png'.format(j),al_frame)
    j=j+1
    # Display the resulting frame
    #cv2.imshow('frame', frame)
    #cv2.imshow('alignedframe', al_frame)
    
    break

# When everything done, release the capture
cap.release()
#cv2.imshow('frame', frame)
cv2.destroyAllWindows()
subprocess.call(['./upload.sh'])
