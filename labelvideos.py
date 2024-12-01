import sys
import cv2
import os
import pandas as pd

def collect_points(Event, x, y, flags, params):
    global frame_copy, points
    if Event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv2.circle(frame_copy, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow("Select Object to Track", frame_copy)
    elif Event == cv2.EVENT_RBUTTONDOWN:
        if points:
            points.pop()
            frame_copy = frame.copy()
            for point in points:
                cv2.circle(frame_copy, point, 5, (0, 255, 0), -1)
            cv2.imshow("Select Object to Track", frame_copy)
    elif Event == cv2.EVENT_MBUTTONDOWN:
        cv2.destroyWindow("Select Object to Track")


already_labeled = {}
if os.path.exists('points.csv'):
    already_labeled = pd.read_csv('points.csv', index_col='Video Name')['Points'].to_dict()
    print("Points already labeled in points.csv")
    print("Videos already labeled:")
    print(already_labeled)
    if input("press y to continue") != 'y':
        sys.exit()
    
points_dic = already_labeled.copy()
google_drive_path = '/Users/joshuamayhugh/Library/CloudStorage/GoogleDrive-jmayhugh@tamu.edu/.shortcut-targets-by-id/1Wazg-sc1r3KWk6T95pnbHeH8eMssRnr8/Research Idea 4 (Deep Learning Classification)/Group 1 : Video Activity Recognition (Arthur,Josh)/Organized Data/Good Sections'

if not os.path.exists(google_drive_path):
    print(f"Error: Path {google_drive_path} does not exist.")
    sys.exit()

for filename in os.listdir(google_drive_path):
    if not (filename.upper().endswith('.MP4') and
            ('SITTING' in filename.upper() or 'STANDING' in filename.upper() or
             'EXIT' in filename.upper() or 'ENTRY' in filename.upper())):
        continue
    if filename in already_labeled:
        print(f"Points already labeled for {filename}.")
        continue
    
    video_path = os.path.join(google_drive_path, filename)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open the video {filename}.")
        continue

    ret, frame = cap.read()
    if not ret:
        print(f"Error: Could not read the first frame of video {filename}.")
        cap.release()
        continue

    points = []
    frame_copy = frame.copy()

    print(f"Processing {filename}.")
    print("Instructions: Left-click to add points, right-click to remove, middle-click to confirm.")

    cv2.imshow("Select Object to Track", frame_copy)
    cv2.setMouseCallback("Select Object to Track", collect_points)
    cv2.waitKey(0)

    # Store points as a single list in the dictionary
    points_dic[filename] = [points]  # Store the points list as a single entry in a list
    cap.release()
    cv2.destroyAllWindows()

# Save points_dic to a CSV with points in one column
if points_dic:
    # Create DataFrame with a single column for points
    points_df = pd.DataFrame.from_dict(points_dic, orient='index', columns=['Points'])
    points_df.index.name = 'Video Name'
    points_df.to_csv('points.csv')
    print("Points saved to points.csv")
else:
    print("No points collected.")
