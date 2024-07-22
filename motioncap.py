import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture('Videos\\Video.mp4')

detector = PoseDetector()
posList = []

while True:
    success, img = cap.read()
    if not success:
        break

    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img)

    if bboxInfo and lmList:
        lmString = ''
        for lm in lmList:
            if len(lm) >= 4:  # Ensure there are enough elements in lm
                lmString += f'{lm[1]},{img.shape[0] - lm[2]},{lm[3]},'
        posList.append(lmString)

    print(len(posList))

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('s'):
        with open("AnimationFile.txt", 'w') as f:
            f.writelines(["%s\n" % item for item in posList])
        break

cap.release()
cv2.destroyAllWindows()
