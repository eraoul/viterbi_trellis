viterbi_trellis
=======================

Library to compute the best path through a trellis graph using the Viterbi algorithm.

`The source for this project is available here
<https://github.com/eraoul/viterbi_trellis>`_.

----

This library provides the class ViterbiTrellis. At present it can only do one thing:
compute the best path through a trellis graph. The user must provide three inputs:

1. **Trellis layer structure**, specified as a list of lists. Each inner list corresponds to a
   single layer of the trellis. The first item in the outer list is the start layer, while the
   final item is the end layer. Each innermost item is an object representing the state. This
   could be a primitive type such as an int, or it could be a tuple or user-defined class.

2. A **cost function** giving the cost for being in a given state.

3. A **transition function** giving the cost of transitioning between two particular states.

The best path is chosen by globally minimizing the sum of the state costs and transitions via
the Viterbi algorithm.

Example usage::

    v = ViterbiTrellis([[2, 6, 4], [4, 6], [0, 2, 6]], lambda x: x / 2.0, lambda x, y: abs(y - x))
    best_path = v.viterbi_best_path()

The return value in best_path is a list of indices of the states in the best path::

    >>> best_path
    [2, 0, 1]

This result corresponds to the states labeled `[4, 4, 2]` in the input trellis.

