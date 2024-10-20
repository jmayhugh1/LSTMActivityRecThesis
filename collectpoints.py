import cv2
import sys

points = []

def collect_points(Event, x, y, flags, params):
    global frame
    if Event == cv2.EVENT_LBUTTONDOWN:
        # Append the point to the list of points
        points.append((x, y))
        # Draw the point on the frame
        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow("Select Object to Track", frame)

    elif Event == cv2.EVENT_RBUTTONDOWN:
        # Remove the last point from the list of points
        if points:
            points.pop()
            # Redraw the points on a copy of the frame
            frame_copy = frame.copy()
            for point in points:
                cv2.circle(frame_copy, point, 5, (0, 255, 0), -1)
            cv2.imshow("Select Object to Track", frame_copy)

    elif Event == cv2.EVENT_MBUTTONDOWN:
        # Close the window and stop collecting points
        cv2.destroyWindow("Select Object to Track")
        cap.release()

# Open the video path passed from command line arguments
path = sys.argv[1]
cap = cv2.VideoCapture(path)

# Read the first frame
ret, frame = cap.read()
if not ret:
    print("Error: Could not read the video.")
    cap.release()
    sys.exit(1)

# Show the frame and set mouse callback
cv2.imshow("Select Object to Track", frame)
cv2.setMouseCallback("Select Object to Track", collect_points)

# Wait until the window is closed by user action
cv2.waitKey(0)

# After closing, release resources
print("Points selected:", points)
cap.release()
cv2.destroyAllWindows()
