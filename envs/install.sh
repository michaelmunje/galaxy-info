#!/bin/bash
conda create -y --name galana
source activate galana
conda install --quiet --yes \
    'numpy' \
    'pandas' \
    'pytest' \
    'keras' \
    'pytest-cov' \
    'matplotlib' \
    'pillow' \
    'jupyter'
length=$( command -v nvidia-docker | wc -c )
if [ "$length" -gt "1" ]; then
	conda install 'tensorflow-gpu'
else
	conda install 'tensorflow'
fi
pip install 'jupyter-tensorboard'
pip install 'boto3'
conda clean -tipsy
#apt-get install -y libsm6 libxext6 libxrender-dev && \
pip uninstall -y keras-preprocessing
pip install git+https://github.com/keras-team/keras-preprocessing.git
