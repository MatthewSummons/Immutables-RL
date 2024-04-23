# Policy Gradient Methods
Make sure your directory is Adaptive Baseline-Zhang Xichen

1. create a conda environment and activate it
```shell
conda create -n pg python=3.10.12
conda activate pg
```

2. install the required packages
```shell
pip install -r requirements.txt
```

3. how to train the model
```shell
python train.py
```
the model will be saved in the model directory ./Pretrained_model
the data will be saved in the data directory ./data
train data is in the data directory ./data/train_process
test data is in the data directory ./data/test_process

4. how to test the model
```shell
python test.py
```
remember to change the model path in the test.py file

5. how to plot the result (plot.ipynb)



