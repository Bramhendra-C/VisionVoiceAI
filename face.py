import cv2

face_data = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
webcam = cv2.VideoCapture(0)
def get_face_unfocus_count():
    count = 0
    focused = True
    while True:
        success, frame = webcam.read()
        if not success:
            break

        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_co = face_data.detectMultiScale(gray_img, scaleFactor=1.5, minNeighbors=5)

        thumb_size = (300, 300)

        if len(face_co) > 0:
            (x, y, w, h) = face_co[0]
            face_roi = frame[y:y+h, x:x+w]
            thumbnail = cv2.resize(face_roi, thumb_size)
            border_color = (0, 255, 0)
            label = "FOCUSED"
            if focused:
                focused = False
            label_color = (0, 255, 0)
        else:
            blurred = cv2.GaussianBlur(frame, (45, 45), 0)
            thumbnail = cv2.resize(blurred, thumb_size)
            border_color = (0, 0, 255) 
            if not focused:
                focused = True
                count += 1
            label = f"UNFOCUSED - counts : {count}"
            label_color = (0, 0, 255)
        thumbnail_with_border = cv2.copyMakeBorder(
            thumbnail, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=border_color
        )
        cv2.putText(thumbnail_with_border, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, label_color, 2)

        h_thumb, w_thumb, _ = thumbnail_with_border.shape
        x_offset = frame.shape[1] - w_thumb - 10
        y_offset = 10
        frame[y_offset:y_offset+h_thumb, x_offset:x_offset+w_thumb] = thumbnail_with_border

        cv2.imshow('Face Detection - bramii', frame)

        if cv2.waitKey(1) == 49: 
            break

    webcam.release()
    cv2.destroyAllWindows()

def run_face_detection():
    while True:

        succes_frame_read , frame = webcam.read()

        grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        face_co = face_data.detectMultiScale(grayscaled_img,scaleFactor = 1.5,minNeighbors = 5)

        for(x,y,w,h) in face_co:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),10)

        cv2.imshow('Face detection  -- bramii',frame)
        
        stop=cv2.waitKey(1)
        if stop == 49:
            break