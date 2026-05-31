import cv2

person_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_fullbody.xml"
)

def detect_occupancy():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if not ret:
        return {
            "occupied": False,
            "count": 0
        }
    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )
    bodies = person_cascade.detectMultiScale(
        gray,
        1.1,
        3
    )
    count = len(bodies)
    cap.release()
    return {
        "occupied": count > 0,
        "count": count
    }