import gym

env = gym.make("Assault-v0")
for i_episode in range(40): #games to play
    observation = env.reset()
    for t in range(100): #moves to make each game last
        env.render()
        """
        print("obsv space")
        print(type(observation))
        print("\naction space")
        print(env.action_space)
        print("\nobsv space")
        print(type(env.observation_space))
        """
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()