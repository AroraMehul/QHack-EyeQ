import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d
from roboticstoolbox import DistanceTransformPlanner

test_pc = np.load("data.npy")

resolution = 0.2
height_min = 0.5
height_max = 2


def pcd_to_occupancy(pcd: np.ndarray):
    if pcd.shape[1] != 3:
        raise ValueError(f'pcd should have 3 columns, instead got {pcd.shape[1]}')

    x_min = pcd[:, 0].min()
    x_max = pcd[:, 0].max()

    z_min = pcd[:, 1].min()
    z_max = pcd[:, 1].max()


    occupancy = np.zeros((int((x_max - x_min + 1) / resolution), int((z_max - z_min + 1)/ resolution)) , dtype=np.float64)

    for i in range(pcd.shape[0]):
        if pcd[i, 2] < height_min or pcd[i, 2] > height_max:
            continue
        x = int((pcd[i, 0] - x_min) / resolution)
        z = int((pcd[i, 1] - z_min) / resolution)

        occupancy[x, z] += 1

    # occupancy /= pcd.shape[0]
    print(pcd[:,2].max(), pcd[:,2].min())
    return occupancy > 0

def plan(start, goal, occupancy):
    dx = DistanceTransformPlanner(occupancy, goal=goal, distance="manhattan")
    dx.plan()
    path = np.array(dx.query(start = start))
    fig = plt.figure()
    plt.imshow(occupancy)
    plt.plot(path[:,0], path[:,1])
    plt.savefig("occupancy.png")
    return plan


# example code
# occupancy = pcd_to_occupancy(test_pc[:,:3])
# plan_output = plan(start = (7.5,10), goal=(25, 10), occupancy = occupancy)











# print(occupancy.shape, occupancy.sum())

# dx = DistanceTransformPlanner(occupancy, goal=(25, 10), distance="manhattan")
# dx.plan()
# path = np.array(dx.query(start = (7.5,10)))
# fig = plt.figure()
# plt.imshow(occupancy)
# plt.plot(path[:,0], path[:,1])

# pcd = o3d.geometry.PointCloud()
# pcd.points = o3d.utility.Vector3dVector(test_pc[:,:3])
# o3d.visualization.draw_geometries([pcd])
