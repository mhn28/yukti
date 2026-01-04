
class CausalGuardError(RuntimeError):
    pass

def require_dag(dag):
    if not dag.is_dag():
        raise CausalGuardError("Graph is not a DAG")

def check_backdoor(dag, treatment, outcome, adjustment_set):
    for z in adjustment_set:
        if z in dag.children(treatment):
            raise CausalGuardError(
                f"Invalid adjustment: {z} is downstream of treatment"
            )
    return True
