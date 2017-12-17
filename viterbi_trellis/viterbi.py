def viterbi_best_path(trellis, state_cost_fn, transition_cost_fn):
    """Compute the best path through a trellis graph minimizing the path cost.

    Params:
      trellis: a list of lists. First dimension is the timestep. Second dimentison is the state
          index within one timestep. Value is an object giving a representation of the state;
          could be an int, tuple, oject instance, etc.
      state_cost_fn: function taking one argument: (state), of the same type as stored in the
          lattice. Returns a float giving the cost of having the given state in the best path.
      transition_cost_fn: function taking two arguments: (state1, state2). Returns a float
          giving the cost of this transition.

    Returns:
      List of state indices: one state for each timestamp.
    """

    # List of lists: each list is a list of indices of the best previous state for the given
    # current state. That is, this is structured like trellis, but stores pointers (indices)
    # to previous states instead of state representations.
    trellis_best_parents = []

    # As above, but for total path cost to each point, not parent indices.
    trellis_path_costs = []

    # Iterate left-to-right through layers of the graph.
    prev_layer = None
    prev_total_costs = [0]
    for layer in trellis:
        total_costs = []
        best_parents = []
        for state in layer:
            # List of total costs of getting here from each previous state.
            possible_path_costs = []
            if prev_layer:
                # Compute the cost of each possible transition to this state, and combine
                # with the total path cost of getting to the previous state.
                for i, prev_state in enumerate(prev_layer):
                    transition_cost = transition_cost_fn(prev_state, state)
                    possible_path_costs.append(transition_cost + prev_total_costs[i])
            else:
                # No previous layer. Just store a cost of 0.  # Essentially this creates a common
                # "START" node, idx 0, that all first-layer nodes connect to.
                possible_path_costs.append(0)

            # Find the min, argmin
            min_val = min(possible_path_costs)
            argmin = np.argmin(possible_path_costs)

            # Compute the cost of being in this state.
            state_cost = state_cost_fn(state)

            # Record best parent and best-path cost at this node.
            best_parents.append(argmin)
            total_costs.append(min_val + state_cost)

        # Record the best parent for each node in this layer.
        trellis_best_parents.append(best_parents)
        trellis_path_costs.append(total_costs)
        prev_layer = layer
        prev_total_costs = total_costs

    # Done with forward pass.

    # Go backwards to reconstruct the best path to the end.
    best_states = []  # Build this up backwards and then reverse at end.

    # Find the best state in the last layer.
    next_state = np.argmin(trellis_path_costs[-1])
    best_states.append(next_state)

    trellis_best_parents.reverse()
