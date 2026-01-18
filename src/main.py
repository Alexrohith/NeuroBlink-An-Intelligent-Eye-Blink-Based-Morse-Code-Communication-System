import cv2
import time

from vision.camera import Camera
from vision.landmarks import FaceLandmarkDetector
from vision.ear import eye_aspect_ratio

from logic.blink_detector import BlinkDetector
from logic.morse_buffer import MorseBuffer
from utils.text_logger import TextLogger


def main():
    cam = Camera()
    detector = FaceLandmarkDetector()
    blink_detector = BlinkDetector()
    morse_buffer = MorseBuffer()

    logger = TextLogger()
    logger.log_session_start()
    morse_buffer.set_word_callback(logger.log_word)

    while True:
        frame = cam.get_frame()
        if frame is None:
            break

        frame, left_eye, right_eye = detector.process(frame)
        frame = detector.draw_eyes(frame, left_eye, right_eye)

        if left_eye and right_eye:
            avg_ear = (eye_aspect_ratio(left_eye) + eye_aspect_ratio(right_eye)) / 2.0

            symbol, _ = blink_detector.update(avg_ear)
            if symbol:
                morse_buffer.add_symbol(symbol)

            morse_buffer.update()

            # ---------------- UI ----------------
            cv2.putText(frame, f"EAR: {avg_ear:.2f}",
                        (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                        (0, 0, 255), 2)

            cv2.putText(frame, f"Current Morse: {morse_buffer.current_symbol}",
                        (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        (0, 255, 0), 2)

            cv2.putText(frame, f"Word: {morse_buffer.current_word}",
                        (30, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        (255, 255, 0), 2)

            cv2.putText(frame, f"Text: {morse_buffer.final_text}",
                        (30, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        (255, 255, 255), 2)

            # Blink bar
            bar_x, bar_y = 30, 210
            bar_w, bar_h = 220, 18

            if blink_detector.eye_closed:
                elapsed = time.time() - blink_detector.close_start_time
                progress = min(elapsed / 1.0, 1.0)
            else:
                progress = 0

            cv2.rectangle(frame, (bar_x, bar_y),
                          (bar_x + bar_w, bar_y + bar_h),
                          (60, 60, 60), -1)

            cv2.rectangle(frame, (bar_x, bar_y),
                          (bar_x + int(bar_w * progress), bar_y + bar_h),
                          (0, 255, 0), -1)

            cv2.putText(frame, "Blink Duration",
                        (bar_x, bar_y - 8),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (255, 255, 255), 1)

        cv2.imshow("Eye Blink Morse - Live Webcam", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cam.release()


if __name__ == "__main__":
    main()
