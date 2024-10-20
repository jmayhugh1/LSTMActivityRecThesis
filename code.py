import cv2

def select_bounding_box(video_path):
    """
    Function to allow the user to manually draw a bounding box on the first frame of the video.
    
    Parameters:
    - video_path: Path to the input video
    
    Returns:
    - bbox: Tuple of the bounding box (x, y, w, h) selected by the user
    - frame: The first frame of the video where the box was selected
    """
    # Open the video
    cap = cv2.VideoCapture(video_path)

    # Read the first frame from the video
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read the video.")
        cap.release()
        return None, None

    # Display the frame and let the user select the bounding box
    bbox = cv2.selectROI("Select Object to Track", frame, fromCenter=False, showCrosshair=True)

    # Close the window after selection
    cv2.destroyWindow("Select Object to Track")

    # Release the video capture object
    cap.release()

    return bbox, frame

print(select_bounding_box('cars.mp4'))