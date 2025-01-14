#!/usr/bin/env bash

gpus=0

data_name=quick_start
net_G=base_transformer_pos_s4_dd8
split=test
project_name=CD_base_transformer_pos_s4_dd8_quick_start_b8_lr0.01_train_test_200_linear
checkpoint_name=best_ckpt.pt

python eval_cd.py --split ${split} --net_G ${net_G} --checkpoint_name ${checkpoint_name} --gpu_ids ${gpus} --project_name ${project_name} --data_name ${data_name}
