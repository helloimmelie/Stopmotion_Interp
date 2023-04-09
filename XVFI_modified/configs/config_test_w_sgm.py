from cv2 import divide


testset_root = '/HDD/sujincho/atd_12k/datasets/test_2k_540p'
test_flow_root = '/HDD/sujincho/atd_12k/datasets/test_2k_pre_calc_sgm_flows'
test_annotation_root = '/HDD/sujincho/atd_12k/datasets/test_2k_annotations'

test_size = (2048, 4096)
test_crop_size = (2048, 4096)

mean = [0., 0., 0.]
std  = [1, 1, 1]

inter_frames = 1

model = 'XVFInet'
pwc_path = None

checkpoint = '/home/sujincho/codes/XVFI_modified/checkpoint_dir/XVFInet_ATD12k_exp1/XVFInet_ATD12k_exp1_latest.pt'

store_path = 'outputs/avi_full_results'

nf = 64
module_scale_factor = 4
img_ch = 3

S_trn = 3
S_tst = 5

multiple = 2 

divide = 512

