from yukti.survival.declaration import SurvivalDeclaration

class SurvivalGuardError(RuntimeError):
    pass

def enforce_survival_declaration(decl: SurvivalDeclaration):
    if not decl.censoring_declared:
        raise SurvivalGuardError("Censoring must be explicitly declared.")
    if not decl.time_origin_declared:
        raise SurvivalGuardError("Time origin must be explicitly declared.")
    return True
