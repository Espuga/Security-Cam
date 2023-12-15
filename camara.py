import cv2

class Camara:
    def __init__(self, user, passwd, cam):
        self.cam = cam
        if cam == "Balcony":
            url = f"rtsp://{user}:{passwd}@192.168.1.103/video"
        elif cam == "Garage":
            url = f"rtsp://{user}:{passwd}@192.168.1.142/video"
        self.cap = cv2.VideoCapture(url)

    def activarCamara(self):
        while True:
            ret, frame = self.cap.read()
            im = cv2.resize(frame, (960, 540))
            cv2.imshow(self.cam, im)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        self.desactivarCamara()

    def desactivarCamara(self):
        self.cap.release()
        cv2.destroyAllWindows()