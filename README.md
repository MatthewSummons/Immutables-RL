# Immutables
# COMP3340 Group Project - Group 5

## Introduction
This is the repository of the COMP3340 group project (Group 5) in HKU (Fall 2023-2024). We explore different models and methods to solve a rocket landing problem in Lunar Lander environment from OpenAI's Gym library - [Gym](https://www.gymlibrary.dev/environments/box2d/lunar_lander/), [Gymnasium](https://gymnasium.farama.org/environments/box2d/lunar_lander/).


## Source Code
In our implementation, the versions of the environment and the packages used may vary with the teammates. Thus, we seperate the codes in four folders with name format ``[Method]-[Teammate's name]``, and include a README file in each folder. The environment configuration, training, testing and generation of the results and demos are all done independently for each folder.

Be careful about the work directory and file path when you run the code!

## Results
In ``./Results`` folder, we store some training and test results like the list of total rewards. But we cannot guarantee that they can be reproduced even if fixing the seed. So, they are offline and will not be rewritten in any code. For your reference, you can use ``./Results/plot_final_result.ipynb`` to plot them, and the figures are used in final presentation.

## Demo
In ``./Demo`` folder, there are the demo gifs and videos we generated from each method, which were used in final presentation.

## Final Presentation
The directory ``./Presentation`` holds the pdf & pptx of the final presentation that we made in class.
