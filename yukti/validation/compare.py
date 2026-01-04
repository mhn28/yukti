def compare(py, r, tol=1e-6):
    diff = {}
    for k in ("stat", "p"):
        if abs(py[k] - r[k]) > tol:
            diff[k] = {"python": py[k], "r": r[k]}
    return {"agree": not diff, "diff": diff}
