import os
import numpy as np
import open3d as o3d
from src.utils.io import load_json
from src.utils.transform import get_transformation_matrix
from src.processing.raw import color_by_height
from src.processing.clustered import cluster_and_color
from src.processing.semantic import simulate_semantic_colors

def render_and_save(pcd_or_geoms, output_path, is_list=False):
    vis = o3d.visualization.Visualizer()
    vis.create_window(visible=False, width=1280, height=720)
    opt = vis.get_render_option()
    opt.background_color = np.array([0, 0, 0])
    opt.point_size = 3.0

    vis.clear_geometries()
    if is_list:
        for g in pcd_or_geoms:
            vis.add_geometry(g)
    else:
        vis.add_geometry(pcd_or_geoms)

    bbox = pcd_or_geoms[0].get_axis_aligned_bounding_box() if is_list else pcd_or_geoms.get_axis_aligned_bounding_box()
    view_ctl = vis.get_view_control()
    view_ctl.set_lookat(bbox.get_center())
    view_ctl.set_zoom(0.8)

    vis.poll_events()
    vis.update_renderer()

    img = vis.capture_screen_float_buffer()
    img_np = (255 * np.asarray(img)).astype(np.uint8)
    o3d.io.write_image(output_path, o3d.geometry.Image(img_np))

    vis.destroy_window()

def generate_frames(json_dir, lidar_root, output_dir, mode):
    os.makedirs(output_dir, exist_ok=True)
    sample_data = load_json(json_dir, "sample_data")
    calibrated = {x["token"]: x for x in load_json(json_dir, "calibrated_sensor")}

    for i, entry in enumerate(sample_data):
        if entry["fileformat"] != "pcd" or "LIDAR_" not in entry["filename"]:
            continue

        fname = entry["filename"].replace("sweeps/", "").replace("/", os.sep)
        full_path = os.path.join(lidar_root, fname)
        if not os.path.exists(full_path):
            continue

        try:
            pcd = o3d.io.read_point_cloud(full_path)
        except:
            continue

        T = get_transformation_matrix(calibrated[entry["calibrated_sensor_token"]])
        pcd.transform(T)
        pcd.estimate_normals()
        pcd.normalize_normals()

        output_path = f"{output_dir}/frame_{i:04d}.png"

        if mode == "clustered":
            render_and_save(cluster_and_color(pcd), output_path, is_list=True)
        elif mode == "raw":
            render_and_save(color_by_height(pcd), output_path)
        elif mode == "semantic":
            render_and_save(simulate_semantic_colors(pcd), output_path)

        print(f"[{i+1}] Saved {output_path}")
