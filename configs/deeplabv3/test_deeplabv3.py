_base_ = [
    '../_base_/models/deeplabv3_r50-d8.py', '../_base_/datasets/mydataset.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_80k.py'
]
model = dict(
    decode_head=dict(num_classes=6), auxiliary_head=dict(num_classes=6))
