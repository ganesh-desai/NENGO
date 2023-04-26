# Computing

# With a connected group of neurons, we can also modify the information being transferred
# from one neuron group to the next. This can be done using functions, and NENGO will connect
# the neurons in the group to best suit the specified function.

# This model is computing the square of the value, so -1 = 1, 0 = 0 and 1 = 1.

# The functions can be varied by changing the computations compute_this code.

import nengo

model = nengo.Network()
with model:
    stim = nengo.Node(0)
    a = nengo.Ensemble(n_neurons=50, dimensions=1)
    nengo.Connection(stim, a)

    b = nengo.Ensemble(n_neurons=50, dimensions=1)

    def compute_this(x):
        return x * x

    nengo.Connection(a, b, synapse=0.01, function=compute_this)