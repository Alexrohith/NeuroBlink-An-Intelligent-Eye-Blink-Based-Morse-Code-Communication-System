import time


class BlinkDetector:
    def __init__(self, ear_threshold=0.21, min_frames_closed=3):
        self.ear_threshold = ear_threshold
        self.min_frames_closed = min_frames_closed

        self.eye_closed = False
        self.close_start_time = None
        self.closed_frames = 0

    def update(self, ear):
        now = time.time()

        if ear < self.ear_threshold:
            self.closed_frames += 1
            if not self.eye_closed and self.closed_frames >= self.min_frames_closed:
                self.eye_closed = True
                self.close_start_time = now
        else:
            if self.eye_closed:
                duration = now - self.close_start_time
                self.eye_closed = False
                self.closed_frames = 0

                if duration < 0.45:
                    return ".", duration
                else:
                    return "-", duration

            self.closed_frames = 0

        return None, None
