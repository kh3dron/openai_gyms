# openai_gyms
experimenting with the openAI Gym environments


## [0.0]
- install packages, run tutorials
- following reinforcement learning tutorial with cartpole first
- need to optimize this network, want it to converge sooner and faster

## [0.1]
- want to get this running on a google colab instance
- strip live graphing / video out of local demo
- install on google colab
- run stripped model in colab & watch convergence
- re-add a chart that updats after all episodes (live updating was messing w colab)
- speed up convergence: 
  - change lr: default 0.01, set to 0.1
  - loss function is ignoring outliers - but for this game, outliers are really useful. Maybe try a new loss function?
    - MSELoss: no change
- 