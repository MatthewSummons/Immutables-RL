from test import test
from model import ActorCritic
import torch
import torch.optim as optim
import gym
import pickle
import numpy as np
def moving_average(total_rewards):
    if len(total_rewards) > 100:
        return sum(total_rewards[-100:])/100
    else:
        return sum(total_rewards)/len(total_rewards)
def step_reward(t):
    if t > 200:
        return 0.01
    return 0
def reward_shaping(pre_state, state):
    pre_shaping = -50*np.abs(pre_state[0])
    shaping = -50*np.abs(state[0])
    return shaping - pre_shaping
def train():
    # Defaults parameters:
    #    gamma = 0.99
    #    lr = 0.02
    #    betas = (0.9, 0.999)
    #    random_seed = 543

    render = False
    gamma = 0.99
    lr = 0.02
    betas = (0.9, 0.999)
    random_seed = 543
    
    torch.manual_seed(random_seed)
    
    env = gym.make('LunarLander-v2')
    
    policy = ActorCritic()
    optimizer = optim.Adam(policy.parameters(), lr=lr, betas=betas)
    print(lr,betas)
    
    running_reward = 0
    total_rewards = []
    final_rewards = []
    average_rewards = []
    for i_episode in range(0, 10000):
        state,_ = env.reset(seed=random_seed)
        # state,_ = env.reset()
        total_reward = 0
        for t in range(1000):
            action = policy(state)
            # next_state, reward, terminated, truncated, _ = env.step(action)
            state, reward, terminated, truncated, _ = env.step(action)
            # reward -= step_reward(t)
            # shaped_reward = reward_shaping(state, next_state)+reward
            # reward += reward_shaping(state, next_state)
            # state = next_state
            done = terminated or truncated
            policy.rewards.append(reward)
            running_reward += reward
            total_reward += reward
            # if render and i_episode > 1000:
            #     env.render()
            if done:
                final_rewards.append(reward)
                total_rewards.append(total_reward)
                break
        average_rewards.append(moving_average(total_rewards))
                    
        # Updating the policy :
        optimizer.zero_grad()
        loss = policy.calculateLoss(gamma)
        loss.backward()
        optimizer.step()        
        policy.clearMemory()
        
        # saving the model if episodes > 999 OR avg reward > 200 
        #if i_episode > 999:
        #    torch.save(policy.state_dict(), './preTrained/LunarLander_{}_{}_{}.pth'.format(lr, betas[0], betas[1]))
        
        if moving_average(total_rewards) > 200:
            torch.save(policy.state_dict(), './Pretrained_model/LunarLander_{}_{}_{}.pth'.format(lr, betas[0], betas[1]))
            print("########## Solved! ##########")
            test(name='LunarLander_{}_{}_{}.pth'.format(lr, betas[0], betas[1]))
            break
        
        if i_episode % 20 == 0:
            running_reward = running_reward/20
            print('Episode {}\tlength: {}\treward: {}'.format(i_episode, t, running_reward))
            running_reward = 0
    data = {'total_rewards': total_rewards, 'average_rewards': average_rewards, 'final_rewards': final_rewards}
    with open('./data/train_process/data_LunarLander_{}_{}_{}.pkl'.format(lr, betas[0], betas[1]), 'wb') as f:
        pickle.dump(data, f)
            
if __name__ == '__main__':
    train()
