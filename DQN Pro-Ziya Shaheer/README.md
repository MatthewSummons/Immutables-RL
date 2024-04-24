# Deep Q-Networks & Its Variants

Please refer to the notebook for further details about the model, and its implementation. Besides implementing the models, I also implemented an Experience Replay Buffer and a epsilon-greedy search policy. 

## How to Train the model

Please make sure you run this on a computer with a browser, if you do not have it or running this fails on your computer, you can also upload the notebook onto Google Collab, uncomment the dependencies (three cells, two at the beginning, one near the end to plot the results) and run it there. If you wish to run it on your local machine, follow the instructions below.

Change you directory to `/Immutables-RL/DQN Pro-Ziya Shaheer` .

1. Once in the directory, create a conda environment with a jupyter notebook

   ```
   conda create -n DQN jupyter notebook
   ```
2. Then activate the environment, making sure you are in the correct directory

   ```
   conda activate DQN
   ```
3. For running on **MacOS** you might need to install swig on your machine, otherwise install the remaining dependencies.

   ```
   pip install -r requirements.txt
   ```

Then you are ready to run the notebook. Run the command `jupyter notebook`. This will open  browser tab, select the file `Double_Duelling_DQN.ipynb` and run all cells. 

It should take about 2 hours to train and test the four different models if you have a GPU. You can change the number of episodes, training target score and the number of testing episodes to speed up the runtime of the notebook.
