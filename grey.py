
import cv2

def main():
 
  img = cv2.imread('/home/mohan/Desktop/tharun/road.jpg',0)
 
  cv2.imshow('sample image',img)
 
  cv2.waitKey(0) 
  cv2.destroyAllWindows()


main()