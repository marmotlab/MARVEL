# MARVEL: Multi-Agent Reinforcement Learning for constrained field-of-View multi-robot Exploration in Large-scale environments

This repository hosts the code for [**MARVEL**](https://arxiv.org/abs/2502.20217), accepted for [ICRA 2025](https://2025.ieee-icra.org/).

<div>
   <img src="utils/media/MARVEL.gif" height="250"/>
   <img src="utils/media/Hardware_validation.gif" height="250"/>
</div>

**Supplementary video link:** [YouTube](https://youtu.be/uwQqkruBvwY)

MARVEL is a neural framework that leverages graph attention networks, together with novel frontiers and orientation features fusion technique, to develop a collaborative, decentralized policy using multi-agent reinforcement learning (MARL) for robots with constrained FoV. 

## Setup instructions

Use conda to setup your environment:

```bash
conda env create -f marvel.yml
conda activate marvel
```

## Evaluation

First, set the appropriate parameters in `test_parameter.py` and adjust testing configurations within `test_driver.py`. Run `test_driver.py` to evaluate.

## Training

Set appropriate parameters in `parameter.py` and run `driver.py` to train the model.


## Citation

If you find our work useful, please consider citing our paper:

```bibtex
@INPROCEEDINGS{chiun2025marvel,
  author={Chiun, Jimmy and Zhang, Shizhe and Wang, Yizhuo and Cao, Yuhong and Sartoretti, Guillaume},
  booktitle={2025 IEEE International Conference on Robotics and Automation (ICRA)}, 
  title={MARVEL: Multi-Agent Reinforcement Learning for Constrained Field-of-View Multi-Robot Exploration in Large-Scale Environments}, 
  year={2025},
  pages={11392-11398},
  keywords={Training;Three-dimensional displays;Robot kinematics;Robot vision systems;Reinforcement learning;Reliability engineering;Sensors;Planning;Complexity theory;Drones},
  doi={10.1109/ICRA55743.2025.11127700}}
```

Authors:
[Jimmy Chiun](https://jimmychiun.me),
Shizhe Zhang,
[Yizhuo Wang](https://www.yizhuo-wang.com/),
[Yuhong Cao](https://www.yuhongcao.online/),
[Guillaume Sartoretti](https://cde.nus.edu.sg/me/staff/sartoretti-guillaume-a/)

License:
MIT
