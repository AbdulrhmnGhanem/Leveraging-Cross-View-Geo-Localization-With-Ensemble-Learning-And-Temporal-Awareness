# Leveraging Cross-View Geo-Localization With Ensemble Learning And Temporal Awareness
The code for the Leveraging Cross-View Geo-Localization With Ensemble Learning And Temporal Awareness paper.

The `bdd100k-trajectories` repo contains the code for our deravative dataset pipeline. And the `cross-view-geo-localiztion-bag` cotains the
code for constructing the ensemble model.

```console
$ tree
├── bdd100k-trajectories
│   ├── aerial_tiles_extraction.ipynb
│   ├── blurry_aerial.ipynb
│   ├── dark-trajectories.ipynb
│   ├── frames_extraction.ipynb
│   ├── LICENSE
│   ├── README.md
│   ├── satellite_images.ipynb
│   ├── select_initial_trajectories.ipynb
│   └── timestamps.ipynb
├── cross-view-localization-bag
│   ├── comingdowntoearth
│   │   ├── cvact_test.py
│   │   ├── data
│   │   │   ├── convert_polar.py
│   │   │   ├── custom_transforms.py
│   │   │   ├── cvact_test_utils.py
│   │   │   ├── cvact_utils.py
│   │   │   └── utils.py
│   │   ├── generate_descriptors.py
│   │   ├── helper
│   │   │   ├── parser_cvact.py
│   │   │   └── parser.py
│   │   ├── networks
│   │   │   ├── backbones.py
│   │   │   ├── c_gan.py
│   │   │   └── safa.py
│   │   ├── README.md
│   │   ├── teaser-small.png
│   │   ├── train_synthesis_cvact.py
│   │   ├── train_synthesis_cvusa.py
│   │   └── utils
│   │       ├── base_wrapper.py
│   │       ├── rgan_wrapper_cvact.py
│   │       ├── rgan_wrapper.py
│   │       └── setup_helper.py
│   ├── download_pretrained_models.py
│   ├── DSM
│   │   ├── Framework.png
│   │   ├── README.md
│   │   └── script
│   │       ├── cal_FOV_acc.py
│   │       ├── cir_net_FOV.py
│   │       ├── data_preparation.py
│   │       ├── distance.py
│   │       ├── generate_descriptors.py
│   │       ├── generate_test_data_cvact.py
│   │       ├── generate_test_data_cvusa.py
│   │       ├── ground_input.py
│   │       ├── OriNet_CVACT
│   │       │   ├── ACT_data.mat
│   │       │   ├── __init__.py
│   │       │   └── input_data_act_polar_3.py
│   │       ├── polar_input_data_orien_FOV_3.py
│   │       ├── test_cvact_fov.py
│   │       ├── train_cvact_fov.py
│   │       ├── train_cvusa_fov.py
│   │       ├── VGG_cir.py
│   │       └── VGG.py
│   ├── generate_descriptors.py
│   ├── L2LTR
│   │   ├── ACT_data.mat
│   │   ├── generate_sat_descriptors.py
│   │   ├── ground_input.py
│   │   ├── LICENSE
│   │   ├── models
│   │   │   ├── configs.py
│   │   │   ├── model_crossattn.py
│   │   │   └── modeling_resnet.py
│   │   ├── README.md
│   │   ├── train.py
│   │   └── utils
│   │       ├── dataloader_act.py
│   │       ├── dataloader_usa.py
│   │       ├── data_utils.py
│   │       └── scheduler.py
│   ├── README.md
│   ├── SAFA
│   │   ├── Framework.png
│   │   ├── OriNet_CVACT
│   │   │   ├── CVACT_orientations
│   │   │   │   └── ACT_data.mat
│   │   │   ├── input_data_ACT_test.py
│   │   │   ├── input_data_VGG.py
│   │   │   └── __pycache__
│   │   │       └── input_data_VGG.cpython-36.pyc
│   │   ├── README.md
│   │   ├── SAFA_poster.pdf
│   │   └── script
│   │       ├── data_preparation.py
│   │       ├── generate_descriptors.py
│   │       ├── input_data_act_polar.py
│   │       ├── input_data_cvusa.py
│   │       ├── OriNet_CVACT
│   │       │   ├── CVACT_orientations
│   │       │   │   ├── ACT_data.mat
│   │       │   │   ├── yaw_pitch_grd_CVACT.mat
│   │       │   │   └── yaw_radius_sat_CVACT.mat
│   │       │   ├── input_data_act_polar.py
│   │       │   └── __pycache__
│   │       │       └── input_data_act_polar.cpython-36.pyc
│   │       ├── __pycache__
│   │       │   ├── input_data_cvusa.cpython-36.pyc
│   │       │   ├── spatial_net.cpython-36.pyc
│   │       │   └── VGG.cpython-36.pyc
│   │       ├── spatial_net.py
│   │       ├── test_cvact.py
│   │       ├── test_cvusa.py
│   │       ├── train_cvact.py
│   │       ├── train_cvusa.py
│   │       └── VGG.py
│   └── Siam-FCANet
│       ├── generate_sat_descriptors.py
│       ├── ground_input.py
│       ├── input_data.py
│       ├── losses_for_training.py
│       ├── loupe.py
│       ├── RankingTest_ForBigMat.py
│       ├── README.md
│       ├── SiamFCANet.py
│       ├── SiamFCANet_VH.py
│       └── train_CVUSA_01.py
└── LICENSE
```
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
