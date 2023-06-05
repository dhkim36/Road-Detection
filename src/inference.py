cd /home/dhkim/work/RoadDetector/albu-solution/src

CUDA_VISIBLE_DEVICES=1 python train_eval.py resnet34_512_02_02.json --fold=1
python skeleton.py

## interface change needs
python wkt_to_G.py


CUDA_VISIBLE_DEVICES=0 python train_eval.py 0_gpu.json --fold=1
CUDA_VISIBLE_DEVICES=1 python train_eval.py 1_gpu.json --fold=1
CUDA_VISIBLE_DEVICES=2 python train_eval.py 2_gpu.json --fold=1
CUDA_VISIBLE_DEVICES=3 python train_eval.py 3_gpu.json --fold=1