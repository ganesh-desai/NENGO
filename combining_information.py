# Combining Information

# To combine information, we connect multiple dimensions without any operations in the function.

# Example: "Connection(a, c[0])" says to take the single dimension
# in a and pass it into the first dimension in c.  (In Python, we always start
# counting at zero, so the first dimension is x[0], then x[1], then x[2], and
# so on).  You can also do this when connecting out of a group, so you could do
# something like "Connection(c[1], d[3])".

# In this model, we are connecting a & b each having one dimension, to c having two.

# Advanced Nengo Tip: Connections support full Python slice notation, so you
# can also do things like [-1], or [1:5] or [::-1] and so on.

import nengo

model = nengo.Network()
with model:
    stim_a = nengo.Node(0)
    a = nengo.Ensemble(n_neurons=50, dimensions=1)
    nengo.Connection(stim_a, a)

    stim_b = nengo.Node(0)
    b = nengo.Ensemble(n_neurons=50, dimensions=1)
    nengo.Connection(stim_b, b)

    c = nengo.Ensemble(n_neurons=200, dimensions=2)
    nengo.Connection(a, c[0])
    nengo.Connection(b, c[1])

