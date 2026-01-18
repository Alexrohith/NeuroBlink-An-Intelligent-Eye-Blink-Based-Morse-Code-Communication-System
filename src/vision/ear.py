import numpy as np
import math


def euclidean(p1, p2):
    return math.dist(p1, p2)


def eye_aspect_ratio(eye_points):
    """
    eye_points: list of 6 (x, y) tuples
    """
    p1, p2, p3, p4, p5, p6 = eye_points

    vertical_1 = euclidean(p2, p6)
    vertical_2 = euclidean(p3, p5)
    horizontal = euclidean(p1, p4)

    ear = (vertical_1 + vertical_2) / (2.0 * horizontal)
    return ear
