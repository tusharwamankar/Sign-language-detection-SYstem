import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import os, os.path
from keras.models import load_model
import traceback

capture = cv2.VideoCapture(0)

hd = HandDetector(maxHands=1)
hd2 = HandDetector(maxHands=1)

count = len(os.listdir("D://test_data_2.0//Gray_imgs//A"))


p_dir = "A"
c_dir = "a"

offset = 30
step = 1
flag = False
suv = 0

white = np.ones((400, 400), np.uint8) * 255
cv2.imwrite("white.jpg", white)

while True:
    try:
        _, frame = capture.read()
        frame = cv2.flip(frame, 1)
        hands = hd.findHands(frame, draw=False, flipType=True)
        img_final = img_final1 = img_final2 = 0

        if hands:
            hand = hands[0]
            x, y, w, h = hand["bbox"]
            image = frame[y - offset : y + h + offset, x - offset : x + w + offset]

            roi = image  # rgb image without drawing
            # roi1 = image1   #rdb image with drawing

            # #for simple gray image without draw
            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (1, 1), 2)

            # #for binary image
            gray2 = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            blur2 = cv2.GaussianBlur(gray2, (5, 5), 2)
            th3 = cv2.adaptiveThreshold(
                blur2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
            )
            ret, test_image = cv2.threshold(
                th3, 27, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
            )

            test_image1 = blur
            img_final1 = np.ones((400, 400), np.uint8) * 148
            h = test_image1.shape[0]
            w = test_image1.shape[1]
            img_final1[
                ((400 - h) // 2) : ((400 - h) // 2) + h,
                ((400 - w) // 2) : ((400 - w) // 2) + w,
            ] = test_image1

            img_final = np.ones((400, 400), np.uint8) * 255
            h = test_image.shape[0]
            w = test_image.shape[1]
            img_final[
                ((400 - h) // 2) : ((400 - h) // 2) + h,
                ((400 - w) // 2) : ((400 - w) // 2) + w,
            ] = test_image

        hands = hd.findHands(frame, draw=False, flipType=True)

        if hands:
            # #print(" --------- lmlist=",hands[1])
            hand = hands[0]
            x, y, w, h = hand["bbox"]
            image = frame[y - offset : y + h + offset, x - offset : x + w + offset]
            white = cv2.imread("white.jpg")
            # img_final=img_final1=img_final2=0
            handz = hd2.findHands(image, draw=False, flipType=True)
            if handz:
                hand = handz[0]
                pts = hand["lmList"]
                # x1,y1,w1,h1=hand['bbox']

                os = ((400 - w) // 2) - 15
                os1 = ((400 - h) // 2) - 15
                for t in range(0, 4, 1):
                    cv2.line(
                        white,
                        (pts[t][0] + os, pts[t][1] + os1),
                        (pts[t + 1][0] + os, pts[t + 1][1] + os1),
                        (0, 255, 0),
                        3,
                    )
                for t in range(5, 8, 1):
                    cv2.line(
                        white,
                        (pts[t][0] + os, pts[t][1] + os1),
                        (pts[t + 1][0] + os, pts[t + 1][1] + os1),
                        (0, 255, 0),
                        3,
                    )
                for t in range(9, 12, 1):
                    cv2.line(
                        white,
                        (pts[t][0] + os, pts[t][1] + os1),
                        (pts[t + 1][0] + os, pts[t + 1][1] + os1),
                        (0, 255, 0),
                        3,
                    )
                for t in range(13, 16, 1):
                    cv2.line(
                        white,
                        (pts[t][0] + os, pts[t][1] + os1),
                        (pts[t + 1][0] + os, pts[t + 1][1] + os1),
                        (0, 255, 0),
                        3,
                    )
                for t in range(17, 20, 1):
                    cv2.line(
                        white,
                        (pts[t][0] + os, pts[t][1] + os1),
                        (pts[t + 1][0] + os, pts[t + 1][1] + os1),
                        (0, 255, 0),
                        3,
                    )
                cv2.line(
                    white,
                    (pts[5][0] + os, pts[5][1] + os1),
                    (pts[9][0] + os, pts[9][1] + os1),
                    (0, 255, 0),
                    3,
                )
                cv2.line(
                    white,
                    (pts[9][0] + os, pts[9][1] + os1),
                    (pts[13][0] + os, pts[13][1] + os1),
                    (0, 255, 0),
                    3,
                )
                cv2.line(
                    white,
                    (pts[13][0] + os, pts[13][1] + os1),
                    (pts[17][0] + os, pts[17][1] + os1),
                    (0, 255, 0),
                    3,
                )
                cv2.line(
                    white,
                    (pts[0][0] + os, pts[0][1] + os1),
                    (pts[5][0] + os, pts[5][1] + os1),
                    (0, 255, 0),
                    3,
                )
                cv2.line(
                    white,
                    (pts[0][0] + os, pts[0][1] + os1),
                    (pts[17][0] + os, pts[17][1] + os1),
                    (0, 255, 0),
                    3,
                )

                for i in range(21):
                    cv2.circle(
                        white, (pts[i][0] + os, pts[i][1] + os1), 2, (0, 0, 255), 1
                    )

                cv2.imshow("skeleton", white)
                # cv2.imshow("5", skeleton5)
            hands = hd.findHands(white, draw=False, flipType=True)
            if hands:
                hand = hands[0]
                x, y, w, h = hand["bbox"]
                cv2.rectangle(
                    white, (x - offset, y - offset), (x + w, y + h), (3, 255, 25), 3
                )

            image1 = frame[y - offset : y + h + offset, x - offset : x + w + offset]

            roi1 = image1  # rdb image with drawing

            # for gray image with drawings
            gray1 = cv2.cvtColor(roi1, cv2.COLOR_BGR2GRAY)
            blur1 = cv2.GaussianBlur(gray1, (1, 1), 2)

            test_image2 = blur1
            img_final2 = np.ones((400, 400), np.uint8) * 148
            h = test_image2.shape[0]
            w = test_image2.shape[1]
            img_final2[
                ((400 - h) // 2) : ((400 - h) // 2) + h,
                ((400 - w) // 2) : ((400 - w) // 2) + w,
            ] = test_image2

            # cv2.imshow("aaa",white)
            # cv2.imshow("gray",img_final2)
            cv2.imshow("binary", img_final)

        cv2.imshow("frame", frame)
        interrupt = cv2.waitKey(1)
        if interrupt & 0xFF == 27:
            # esc key
            break
        if interrupt & 0xFF == ord("n"):
            p_dir = chr(ord(p_dir) + 1)
            c_dir = chr(ord(c_dir) + 1)
            if ord(p_dir) == ord("Z") + 1:
                p_dir = "A"
                c_dir = "a"
            flag = False
            # #training data

            # test data
            count = len(os.listdir("D://test_data_2.0/Gray_imgs//" + p_dir + "//"))

        if interrupt & 0xFF == ord("a"):
            if flag:
                flag = False
            else:
                suv = 0
                flag = True

        print("=====", flag)
        if flag == True:
            if suv == 50:
                flag = False
            if step % 2 == 0:
                cv2.imwrite(
                    "D:\\test_data_2.0\\Gray_imgs\\"
                    + p_dir
                    + "\\"
                    + c_dir
                    + str(count)
                    + ".jpg",
                    img_final1,
                )
                cv2.imwrite(
                    "D:\\test_data_2.0\\Gray_imgs_with_drawing\\"
                    + p_dir
                    + "\\"
                    + c_dir
                    + str(count)
                    + ".jpg",
                    img_final2,
                )

                count += 1
                suv += 1
            step += 1
    except Exception:
        print("==", traceback.format_exc())

capture.release()
cv2.destroyAllWindows()
