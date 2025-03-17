import argparse
from src.generate import generate_frames

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate LIDAR frames")

    parser.add_argument("--mode", type=str, choices=["raw", "clustered", "semantic"], default="raw",
                        help="Frame type (default: raw)")

    parser.add_argument("--json_dir", type=str, default="TruckScenes/v1.0-mini",
                        help="Path to JSON metadata")

    parser.add_argument("--lidar_root", type=str, default="TruckScenes/man-truckscenes",
                        help="Path to LIDAR .pcd files")

    args = parser.parse_args()

    output_dirs = {
        "raw": "output/frames_raw",
        "clustered": "output/frames_clustered",
        "semantic": "output/frames_semantic"
    }

    generate_frames(args.json_dir, args.lidar_root, output_dirs[args.mode], args.mode)



    output_dirs = {
        "raw": "output/frames_raw",
        "clustered": "output/frames_clustered",
        "semantic": "output/frames_semantic"
    }
    
    generate_frames(args.json_dir, args.lidar_root, output_dirs[args.mode], args.mode)
