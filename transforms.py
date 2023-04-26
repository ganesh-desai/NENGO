# Transforms and scaling

# Scaling is multiplying a value by a constant number like 0.1 or 10. Since it is a fixed number, a multiplication system is not necessary.

# As this is a frequently used function, a "transform" parameter has been predefined.

# Here, b1 and b2 multiplies the recieving input from a by -0.5.

# For a multidimensional example, d1 and d2 both take values from c and compute 2*c[0]-c[1]-c[2], but do so in different ways.  In both cases the
# resulting models are identical.

# This function can be used to quickly define any linear transformation on the values represented by the Ensembles.

import nengo

model = nengo.Network()
with model:
    stim_a = nengo.Node(0)
    a = nengo.Ensemble(n_neurons=50, dimensions=1)
    nengo.Connection(stim_a, a)

    b1 = nengo.Ensemble(n_neurons=50, dimensions=1)
    b2 = nengo.Ensemble(n_neurons=50, dimensions=1)

    # the long way to do it
    def simple_function(a):
        return -0.5 * a

    nengo.Connection(a, b1, function=simple_function)
    # the shortcut way to do it
    nengo.Connection(a, b2, transform=-0.5)

    stim_c = nengo.Node([0, 0, 0])
    c = nengo.Ensemble(n_neurons=200, dimensions=3)
    nengo.Connection(stim_c, c)

    d1 = nengo.Ensemble(n_neurons=50, dimensions=1)
    d2 = nengo.Ensemble(n_neurons=50, dimensions=1)

    # the long way to do it
    def harder_function(c):
        return 2 * c[0] - c[1] - c[2]

    nengo.Connection(c, d1, function=harder_function)
    # the shortcut way to do it
    nengo.Connection(c, d2, transform=[[2, -1, -1]])