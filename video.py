import cv2
import os
from natsort import natsorted

def create_video_from_frames(frame_dir, output_path, fps=10, resolution=(1280, 720)):
    # Collect and sort image files
    frames = [f for f in os.listdir(frame_dir) if f.endswith(('.png', '.jpg'))]
    frames = natsorted(frames)  # Natural sort (e.g., frame_1, frame_2, ..., frame_100)

    if not frames:
        print("No frames found in the folder.")
        return

    # Define the video codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # or 'XVID'
    out = cv2.VideoWriter(output_path, fourcc, fps, resolution)

    for fname in frames:
        frame_path = os.path.join(frame_dir, fname)
        frame = cv2.imread(frame_path)
        if frame is None:
            print(f"Skipped: {fname}")
            continue
        frame = cv2.resize(frame, resolution)
        out.write(frame)

    out.release()
    print(f"Video saved to {output_path}")

# Example usage
create_video_from_frames(
    frame_dir='output/frames_raw',          # Path to your frames
    output_path='output/video_raw.mp4',     # Output video file
    fps=15,                                 # Frame rate
    resolution=(1280, 720)                  # Match the original rendering size
)
