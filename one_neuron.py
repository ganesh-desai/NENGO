# One Neuron

# Slider adjusts the neuron input. The top graph shows voltage, middle graph plots output spikes
# and the bottom graph is the original input.

import nengo

model = nengo.Network()
with model:
    stim = nengo.Node(0)
    ens = nengo.Ensemble(n_neurons=1, dimensions=1, seed=5)
    nengo.Connection(stim, ens)