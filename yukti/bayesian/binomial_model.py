from scipy.stats import beta

def bayesian_proportion(successes, trials, alpha=1, beta_param=1):
    post_alpha = alpha + successes
    post_beta = beta_param + trials - successes

    return {
        "posterior_mean": post_alpha / (post_alpha + post_beta),
        "credible_interval_95": beta.ppf([0.025, 0.975], post_alpha, post_beta).tolist()
    }
