conda create -y -n galana tensorflow-gpu pandas numpy
conda create -y -n galana-test tensorflow pandas numpy pytest
conda create -y -n galana-mine pandas numpy selenium
source activate galana-mine
pip install astroquery
