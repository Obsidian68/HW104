import cv2
img = cv2.imread('solar-system.jpg')
cv2.imshow('output',img)
cv2.waitKey(0)
cv2.putText(img,'Sun',(700,10),cv2.FONT_HERSHEY_COMPLEX,500,(0,255,0))
cv2.putText(img, 'Mercury',(700,10),cv2.FONT_HERSHEY_COMPLEX,500,(0,0,255))
cv2.putText(img, 'Venus',(700,10),cv2.FONT_HERSHEY_COMPLEX,500,(255,0,0))
cv2.imwrite('solar_system',img)