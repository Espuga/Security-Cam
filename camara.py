import cv2

class Camara:
    def __init__(self, user, passwd, ip):
        self.cam = ip
        url = f"rtsp://{user}:{passwd}@{ip}/video"
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