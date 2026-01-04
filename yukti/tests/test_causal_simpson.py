
from yukti.causal import CausalDAG
from yukti.causal.guards import require_dag, check_backdoor

dag = CausalDAG()
dag.add_edge("Treatment","Outcome")
dag.add_edge("Age","Treatment")
dag.add_edge("Age","Outcome")

require_dag(dag)

# Valid adjustment
assert check_backdoor(dag,"Treatment","Outcome",{"Age"}) is True

# Invalid adjustment (post-treatment)
dag2 = CausalDAG()
dag2.add_edge("Treatment","Mediator")
dag2.add_edge("Mediator","Outcome")

try:
    check_backdoor(dag2,"Treatment","Outcome",{"Mediator"})
    raise AssertionError("Post-treatment adjustment not blocked")
except RuntimeError:
    pass

print("✓ Phase 11 causal DAG + backdoor validation passed")
