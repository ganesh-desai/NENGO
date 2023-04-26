# Connecting Neurons

# This model represents two connected groups of neurons.

# When connecting two groups of neurons Nengo will find the connection weights between each of the neurons such that whatever value is being represented by the first group of neurons will be passed on to the second group of neurons.

# The synapse value indicates the properties of the neurotransmitters and synapses.

# Time constant: the amount of time it takes for the effects of a single spike to return to baseline or wear off. Default value of 0.005s will be considered if left undefined. Time constant speed varies depending on the brain region.

import nengo

model = nengo.Network()
with model:
    stim = nengo.Node(0)
    a = nengo.Ensemble(n_neurons=50, dimensions=1)
    nengo.Connection(stim, a)

    b = nengo.Ensemble(n_neurons=50, dimensions=1)

    nengo.Connection(a, b, synapse=0.01)