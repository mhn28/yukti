args <- commandArgs(trailingOnly=TRUE)
x <- as.numeric(strsplit(args[1], ",")[[1]])
y <- as.numeric(strsplit(args[2], ",")[[1]])

res <- t.test(x, y, var.equal = FALSE)
cat(sprintf("stat=%.6f;p=%.10f", res$statistic, res$p.value))
