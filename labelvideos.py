import sys
import cv2
import os
import pandas as pd

def collect_points(Event, x, y, flags, params):
    global frame_copy, points
    if Event == cv2.EVENT_LBUTTONDOWN:
        # Append the point to the list of points
        points.append((x, y))
        # Draw the point on the frame copy
        cv2.circle(frame_copy, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow("Select Object to Track", frame_copy)

    elif Event == cv2.EVENT_RBUTTONDOWN:
        # Remove the last point from the list of points
        if points:
            points.pop()
            # Reset frame_copy and redraw remaining points
            frame_copy = frame.copy()
            for point in points:
                cv2.circle(frame_copy, point, 5, (0, 255, 0), -1)
            cv2.imshow("Select Object to Track", frame_copy)

    elif Event == cv2.EVENT_MBUTTONDOWN:
        # Close the window and stop collecting points
        cv2.destroyWindow("Select Object to Track")

points_dic = {}
google_drive_path = '/Users/joshuamayhugh/Library/CloudStorage/GoogleDrive-jmayhugh@tamu.edu/.shortcut-targets-by-id/1Wazg-sc1r3KWk6T95pnbHeH8eMssRnr8/Research Idea 4 (Deep Learning Classification)/Group 1 : Video Activity Recognition (Arthur,Josh)/Organized Data/Good Sections'

# Iterate through files in the specified directory
for filename in os.listdir(google_drive_path):
    if 'SITTING' not in filename.upper() or "STANDING" not in filename.upper() or "EXIT" not in filename.upper():
        continue
    if ".mp4" not in filename:
        continue
    video_path = os.path.join(google_drive_path, filename)
    print(f"Processing: {filename}")

    # Open the video path
    cap = cv2.VideoCapture(video_path)

    # Read the first frame
    ret, frame = cap.read()
    if not ret:
        print(f"Error: Could not read the video {filename}.")
        cap.release()
        continue

    points = []
    frame_copy = frame.copy()

    # Show the frame and set mouse callback
    cv2.imshow("Select Object to Track", frame_copy)
    cv2.setMouseCallback("Select Object to Track", collect_points)

    # Wait until the window is closed by user action
    cv2.waitKey(0)

    # Save points for the current video
    points_dic[filename] = points
    cap.release()
    cv2.destroyAllWindows()

# Save points_dic to a CSV file
points_df = pd.DataFrame.from_dict(points_dic, orient='index')
points_df.to_csv('points.csv')
