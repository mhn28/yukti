
import pandas as pd
import statsmodels.formula.api as smf

def mixed_intercept(df, response, predictor, group):
    formula = f"{response} ~ {predictor}"
    model = smf.mixedlm(formula, df, groups=df[group])
    fit = model.fit(reml=False)
    return {
        "fixed_effects": fit.params.to_dict(),
        "random_effects_var": float(fit.cov_re.iloc[0,0]),
        "log_likelihood": float(fit.llf)
    }
