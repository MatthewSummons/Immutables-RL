# Proximal Policy Optimization

## Before running the code
First, make sure your working directory is ``PPO-Zeng Shaoyu``. The model, trainning, evaluation and demo are all in ``./PPO_all_in_one.ipynb``, where all the details are written in the markdown of the notebook. 

Before running the code in notebook, you need to create a conda environment using this command:

```
conda create -n ppo_zsy jupyter notebook -y
```

Then you may activate this environment:
```
conda activate ppo_zsy
```

Then install related Python packages. You can check and run ``./pre.sh`` to do so.

Finally, run jupyter notebook and open the file ``./PPO_all_in_one.ipynb``

## Running the code
Here is the outline of the Jupyter Notebook file, where you can choose to run the part you needed.

1. Import Package
1. Lunar Lander environment
1. PPO Agent

    The codes in above sections (1~3) are neccessary. 
1. Bayesian Optimization

    This will not be run by default because it takes a lot of time to optimize. But you can turn it on if you want to test whether it is executable, and there is instruction in the notebook.

1. Train a excellent model

    Here you can set the goal you want the model to reach and train one, which will be stored in a .pth file. Also the intermediate data will be stored in a .pkl file.

    You can skip this if you only want to evaluate the trained model and see the results.

1. Load and evaluation

    This section will load the trained model, evaluate for 500 episodes and store the corresponding data. In demo subsection you can generate gifs of landing and save them.

1. Reward Shaping

    Here you can test the power of Reward Shaping, basically by comparing the normal process with and without reward shaping.

## Plot the data

There is a file ``plot.ipynb`` for plotting the results. To properly plot the figure you want, you may change the index in the code manually.