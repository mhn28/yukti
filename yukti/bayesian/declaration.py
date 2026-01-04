from dataclasses import dataclass

@dataclass
class BayesianDeclaration:
    prior_type: str          # "normal", "uniform", "cauchy"
    likelihood: str          # "gaussian", "binomial", "poisson"
    iterations: int = 4000
    burn_in: int = 1000
    chains: int = 4
