# Utility functions for viterbi-trellis.
#
# argmin is defined here to avoid dependence on e.g., numpy.

def argmin(list_obj):
    """Returns the index of the min value in the list."""
    min = None
    best_idx = None
    for idx, val in enumerate(list_obj):
        if min is None or val < min:
            min = val
            best_idx = idx
    return best_idx
