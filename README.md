
# LiDAR Frame Visualizer

This project is a **LiDAR multi-frame visualizer** designed for offline processing and export of annotated `.pcd` point cloud files. It enables you to:

- Load multi-LiDAR frame data (.pcd format)
- Apply preprocessing and color coding (raw, clustered, and semantic)
- Generate side-by-side visualizations
- Save output as a high-quality `.mp4` video
- Export `.png` images

---

## Project Structure

```
lidar_frame_visualizer/
│
├── src/
│   ├── processing/
|        |──clustered.py	# clustered frames
|	 |──raw.py		# raw frames
|	 |──semantic.py        # semantic frames    
|    |── utils/
|        |──io.py		# input output source
|        |──transform.py       # transformation matrix
|    ├── generate.py		# generate frames
├── output_pcd/
│   ├── frames_raw/            # Original fused .pcd per frame
├── run.py              	# Main script
├── video.py                   # Final .mp4 video with fade-in/out
└── requirements.txt           # Python dependencies
```

---

## Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

Dependencies include:
- `open3d`
- `numpy`
- `matplotlib`
- `imageio`
- `opencv-python`

> Optional: Enable `DirectML` if using Intel GPU.

---

### 2. Run the Visualizer

```bash
python visualizer.py
```

This will:
- Load `.pcd` files from `input_pcd/`
- Perform multi-sensor fusion and visualization
- Simulate clustering and semantic coloring
- Save frames in respective folders


### Input Data Format

Place your `.pcd` files from multiple LiDAR sensors inside `input_pcd/` following this naming convention:

```
frame_0001_LIDAR_LEFT.pcd
frame_0001_LIDAR_TOP_FRONT.pcd
...
frame_0050_LIDAR_RIGHT.pcd
```

The script automatically fuses them per timestamp.

---

##  Output Samples

Each frame will be exported as:
- `.png` image: in `frames_raw/`, `frames_clustered/`, `frames_semantic/`

---


## Notes

- Runs entirely offline
- Ideal for quick demo videos and visual analysis
- Modular and easy to extend for real-time inference

