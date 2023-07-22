import open3d as o3d

def register(source, target, threshold = 0.1, trans_init=np.eye(4)):
	reg_p2p = o3d.pipelines.registration.registration_icp(
			    source, target, threshold, trans_init,
			    o3d.pipelines.registration.TransformationEstimationPointToPoint())

	return reg_p2p.transformation
