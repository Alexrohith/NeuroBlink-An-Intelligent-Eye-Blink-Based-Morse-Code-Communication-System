import cv2
import mediapipe as mp


class FaceLandmarkDetector:
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
        )

        self.LEFT_EYE = [33, 160, 158, 133, 153, 144]
        self.RIGHT_EYE = [362, 385, 387, 263, 373, 380]

    def process(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.face_mesh.process(rgb)

        if not result.multi_face_landmarks:
            return frame, None, None

        h, w, _ = frame.shape
        face_landmarks = result.multi_face_landmarks[0]

        left_eye = []
        right_eye = []

        for idx in self.LEFT_EYE:
            lm = face_landmarks.landmark[idx]
            left_eye.append((int(lm.x * w), int(lm.y * h)))

        for idx in self.RIGHT_EYE:
            lm = face_landmarks.landmark[idx]
            right_eye.append((int(lm.x * w), int(lm.y * h)))

        return frame, left_eye, right_eye

    def draw_eyes(self, frame, left_eye, right_eye):
        if left_eye:
            for (x, y) in left_eye:
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        if right_eye:
            for (x, y) in right_eye:
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        return frame
