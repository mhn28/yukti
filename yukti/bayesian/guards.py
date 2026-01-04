from yukti.bayesian.declaration import BayesianDeclaration

class BayesianGuardError(RuntimeError):
    pass

def enforce_bayesian_declaration(decl: BayesianDeclaration):
    if decl.prior_type not in {"normal","uniform","cauchy"}:
        raise BayesianGuardError("Unsupported prior type.")
    if decl.iterations <= decl.burn_in:
        raise BayesianGuardError("Iterations must exceed burn-in.")
    if decl.chains < 2:
        raise BayesianGuardError("At least two chains required.")
    return True
