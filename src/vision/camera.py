import cv2


class Camera:
    def __init__(self, cam_index=0):
        self.cap = cv2.VideoCapture(cam_index)

        if not self.cap.isOpened():
            raise RuntimeError("❌ Webcam not accessible")

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
