# perunov-marsland-england-2016-statistical-physics-of-adaptation.pdf
# DISSIPATION AND DRIFT IN TIME-VARYING ENERGY LANDSCAPES
#
# figure 3 + surrounding text, p15–16 — the concrete 3-state example. This is the actual v0: three nodes in a row, a specific cosine drive on one energy and one barrier, and the
#   particle should drift preferentially toward $x_1$. Reproduce that drift and you've reproduced their result (the honesty test from the roadmap).

N_particles = 3
T_max = 100

particles = []
for _ in range(0, N_particles):
    # the particle's state is nearly trivial: it's just
    #   which node it currently occupies. An index. The particle {} holds essentially one field.
    #
    #   The state that needs structure is the landscape, not the particle:
    #   - nodes, each with an energy $E_i(t)$
    #   - edges between nodes, each with a barrier $B_{ij}(t)$ and a base rate constant
    #   - the global $\beta$
    #   - the drive — the rule for how $E_i(t)$ and $B_{ij}(t)$ wiggle in time
    particles.append({}) # TODO: Each state xi has a particular energy Ei
    
for t in range(0, T_max):
    for i in range(0, N_particles):
        # when our particle is in state x[i] ,
        # it always has a constant probability rate ri→j of stochastically hopping to state x[j]
        # that is given by [7]
        # Eq 9, p15 — the transition rule (an Arrhenius rate, depends on barrier-minus-current-energy).
        # This is your per-step update; read it as "probability of hopping $i \to j$ this tick."
        particles[i] = particles[i]
        # TODO: bookkeeping is how you'll measure dissipation later.
        #  p15, just after Eq 9 — how the drive enters ($E_i(t)$ and $B_{ij}(t)$ become functions of time) and the energy bookkeeping (work done when $E_i$ shifts while the particle sits at
        #   $x_i$; heat $\Delta Q$ dumped to the bath on a hop)

print(f"Completed simulation of {N_particles} particles over {T_max} steps")
