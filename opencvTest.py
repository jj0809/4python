from flask import Response, Flask, render_template
import threading
import argparse 
import datetime, time
import imutils
import cv2

app = Flask(__name__)

url = 'rtsp://210.99.70.120:1935/live/cctv001.stream'
camera = cv2.VideoCapture(url)
time.sleep(2.0)

def writeVideo():
    # 현재시간 가져오기
    currentTime = datetime.datetime.now()
    
    # RTSP를 불러오는 곳
    # camera = cv2.VideoCapture('rtsp://admin:admin@192.168.0.2:554')
    
    # 웹캠 설정
    camera.set(3, 800)  # 영상 가로길이 설정
    camera.set(4, 600)  # 영상 세로길이 설정
    fps = 20
    # 가로 길이 가져오기
    streaming_window_width = int(camera.get(3))
    # 세로 길이 가져오기
    streaming_window_height = int(camera.get(4))  
    
    #현재 시간을 '년도 달 일 시간 분 초'로 가져와서 문자열로 생성
    fileName = str(currentTime.strftime('%y%m%d_%H:%M:%S'))

    #파일 저장하기 위한 변수 선언
    path = f'/Users/jjyoun/{fileName}.avi'
    
    # DIVX 코덱 적용 # 코덱 종류 # DIVX, XVID, MJPG, X264, WMV1, WMV2
    # 무료 라이선스의 이점이 있는 XVID를 사용
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    
    # 비디오 저장
    # cv2.VideoWriter(저장 위치, 코덱, 프레임, (가로, 세로))
    out = cv2.VideoWriter(path, fourcc, fps, (streaming_window_width, streaming_window_height))

    last_capture_time = time.time()

    while True:
        ret, frame = camera.read()
        # 촬영되는 영상보여준다. 프로그램 상태바 이름은 'streaming video' 로 뜬다.
        cv2.imshow('streaming video', frame)
        if ret:
            out.write(frame)  # 프레임을 비디오 파일에 저장


        # 영상을 저장한다.
        #out.write(frame)
         
        '''
        # 10초만 저장함
        now_time = datetime.datetime.now()
        elapsed_time = now_time - currentTime

        if elapsed_time.totalseconds() >= 10:
            break
        '''

        # 10초마다 저장하기
        if time.time() - last_capture_time >= 10:
            last_capture_time = time.time()
            print("프레임 저장")
            out.release()
            #fileName = str(datetime.datetime.now().strftime('%y%m%d_%H:%M:%S'))
            #path = f'/Users/jjyoun/{fileName}.avi'
            output_file = '/Users/jjyoun/' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + '.avi'
            out = cv2.VideoWriter(output_file, fourcc, fps, (streaming_window_width, streaming_window_height))
            #out.write(frame)
            #out.release()  # 비디오 파일 닫기

        # 1ms뒤에 뒤에 코드 실행해준다.
        k = cv2.waitKey(1) & 0xff
        #키보드 esc 누르면 종료된다.
        if k == 27 :
            break

    camera.release()  # cap 객체 해제
    out.release()  # out 객체 해제
    cv2.destroyAllWindows()


if __name__ == "__main__":
    writeVideo()