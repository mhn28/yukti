from yukti.stats.multiple_testing import adjust_pvalues

pvals = [0.001, 0.02, 0.04, 0.2, 0.8]

result = adjust_pvalues(pvals, method="fdr_bh")

print("Adjusted p-values:", result["adjusted_pvalues"])
print("Reject null:", result["reject_null"])
