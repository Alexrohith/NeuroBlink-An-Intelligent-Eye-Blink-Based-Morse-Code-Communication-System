import time
import numpy as np


class CalibrationManager:
    def __init__(self):
        self.stage = "OPEN_EYE"
        self.start_time = time.time()

        self.open_ear_values = []
        self.dot_durations = []
        self.dash_durations = []

        self.calibrated = False

        self.ear_threshold = None
        self.dot_max = None
        self.dash_min = None

    def update(self, ear, blink_duration=None):
        now = time.time()

        # STEP 1: OPEN EYES
        if self.stage == "OPEN_EYE":
            self.open_ear_values.append(ear)
            if now - self.start_time >= 3:
                self.ear_threshold = np.mean(self.open_ear_values) * 0.75
                self.stage = "DOT"
                self.start_time = now

        # STEP 2: DOT BLINKS
        elif self.stage == "DOT" and blink_duration:
            self.dot_durations.append(blink_duration)
            if len(self.dot_durations) >= 5:
                self.dot_max = np.mean(self.dot_durations) * 1.3
                self.stage = "DASH"

        # STEP 3: DASH BLINKS
        elif self.stage == "DASH" and blink_duration:
            self.dash_durations.append(blink_duration)
            if len(self.dash_durations) >= 5:
                self.dash_min = np.mean(self.dash_durations) * 0.8
                self.calibrated = True
                self.stage = "DONE"

    def status_text(self):
        return {
            "OPEN_EYE": "Keep eyes OPEN",
            "DOT": "Blink NORMALLY (DOT)",
            "DASH": "Blink SLOWLY (DASH)",
            "DONE": "Calibration Complete"
        }[self.stage]
