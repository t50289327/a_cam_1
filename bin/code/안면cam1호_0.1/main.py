#소스코드 작성: 김종호(金宗昊)
#본 프로그램은 GNU/Linux, Unix-like OS전용으로 개발 되었습니다!!
#MicroSoft Windows 계열 OS에서 사용하려면 알아서 수정하십시오
#라이센스 GNU GPL V2
import cv2
import numpy
import serial
import os

ad = serial.Serial('/dev/ttyACM0',9600)

#웹캠에서 영상을 읽어온다
#cv2.VideoCapture(0)는 카메라 실행
cap = cv2.VideoCapture(0)
#set은 화면크기 설정
cap.set(3, 640) #WIDTH
cap.set(4, 480) #HEIGHT

#얼굴 인식 xml읽기
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    # frame 별로 출력 명령어 .read()
    ret, frame = cap.read()

    #흑백 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #.detectMultiScale() 은 얼굴검출 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # 인식된 얼굴에 사각형을 출력한다
    #좌표정보 리턴
    for (x,y,w,h) in faces:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) #cv2.rectangle()는 사각형 만드는 함수
         if x > 200:
             if x <300:
                 print("가운데")
         if x > 300:
             print("카메라 에서 왼쪽")
             ad.write(b'n')
         if x < 200:
             print("카메라에서 오른쪽")
             ad.write(b'y')

    #화면에 출력한다
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
