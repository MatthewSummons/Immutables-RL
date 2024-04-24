from model import ActorCritic
import torch
import gym
import matplotlib.pyplot as plt
from matplotlib import animation
import pickle


def test(n_episodes=500, name='LunarLander_0.02_0.9_0.999.pth'):
    count = 0
    render = False
    env = gym.make('LunarLander-v2',render_mode='rgb_array')
    policy = ActorCritic()
    
    policy.load_state_dict(torch.load('./Pretrained_model/{}'.format(name)))
    
    fig = plt.figure()
    # animations = []
    total_rewards = []
    final_rewards = []
    for i_episode in range(1, n_episodes+1):
        state, _ = env.reset()
        # print(state)
        running_reward = 0
        done = False
        ims = []
        # img = plt.imshow(env.render())
        while not done:
            # frames.append(env.render())
            # print(policy(state))
            action = policy(state)
            state, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated
            running_reward += reward
            if render:
                im = plt.imshow(env.render(), animated=True)
                ims.append([im])
        total_rewards.append(running_reward)
        final_rewards.append(reward)
        print("Episode: {}, Reward: {},final_Reward: {}".format(i_episode, running_reward, reward))
        if reward == 100 :
            count += 1
            if render:
                ani = animation.ArtistAnimation(fig, ims, interval=25, blit=True, repeat_delay=1000)
                ani.save(f'baseline_{name}_demo_{i_episode}.gif')
    env.close()
    print("count: ", count)
    data = {'total_rewards': total_rewards, 'final_rewards': final_rewards}
    with open(f'./data/test_process/model_test_{name}.pkl', 'wb') as f:
        pickle.dump(data, f)
            
if __name__ == '__main__':
    test()
