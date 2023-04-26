# Multiplication

# In this model we are creating an ensemble with two dimensions, then connecting a & b to c each with one input.

# We then connect c to d and use the connection function to multiply the values.

# The radius had to be changed to 1.5 because it is representing two values, each of which can be in the range -1 to 1. For optimal accuracy,
# the radius must be large enough to include [1, 1]. That is sqrt(2), or around 1.5.

import nengo

model = nengo.Network()
with model:
    stim_a = nengo.Node(0)
    a = nengo.Ensemble(n_neurons=50, dimensions=1)
    nengo.Connection(stim_a, a)

    stim_b = nengo.Node(0)
    b = nengo.Ensemble(n_neurons=50, dimensions=1)
    nengo.Connection(stim_b, b)

    c = nengo.Ensemble(n_neurons=200, dimensions=2, radius=1.5)
    nengo.Connection(a, c[0])
    nengo.Connection(b, c[1])

    d = nengo.Ensemble(n_neurons=50, dimensions=1)

    def multiply(x):
        return x[0] * x[1]

    nengo.Connection(c, d, function=multiply)