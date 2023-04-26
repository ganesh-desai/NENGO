# Many neurons

# This model consists of a group of neurons, also called "Ensemble" in NENGO.

# Higher the number of neurons the more accurate the model, also making the model more sensitive to input changes.

# Decoders weights the outputs of all the single neurons in the model to plot the decoded output graph.

import nengo

model = nengo.Network()
with model:
    stim = nengo.Node(0)
    ens = nengo.Ensemble(n_neurons=20, dimensions=1)
    nengo.Connection(stim, ens)