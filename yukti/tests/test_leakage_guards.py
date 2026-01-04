
from yukti.drug.leakage.guards import (
    SplitMeta, LeakageError, enforce_all
)
import datetime

# ---- Clean split (should pass)
meta_ok = SplitMeta(
    train_ids={"C1","C2"},
    test_ids={"C3"},
    train_dates=[datetime.date(2020,1,1)],
    test_dates=[datetime.date(2021,1,1)],
    train_assays={"A1"},
    test_assays={"A2"},
    feature_names={"f1","f2"},
    label_name="y"
)
assert enforce_all(meta_ok)

# ---- Duplicate entity leakage
try:
    enforce_all(SplitMeta(
        train_ids={"C1"},
        test_ids={"C1"},
    ))
    raise AssertionError("Duplicate leakage not detected")
except LeakageError:
    pass

# ---- Temporal leakage
try:
    enforce_all(SplitMeta(
        train_ids={"C1"},
        test_ids={"C2"},
        train_dates=[datetime.date(2022,1,1)],
        test_dates=[datetime.date(2021,1,1)],
    ))
    raise AssertionError("Temporal leakage not detected")
except LeakageError:
    pass

# ---- Assay leakage
try:
    enforce_all(SplitMeta(
        train_ids={"C1"},
        test_ids={"C2"},
        train_assays={"A1"},
        test_assays={"A1"},
    ))
    raise AssertionError("Assay leakage not detected")
except LeakageError:
    pass

# ---- Target leakage
try:
    enforce_all(SplitMeta(
        train_ids={"C1"},
        test_ids={"C2"},
        feature_names={"y","f1"},
        label_name="y",
    ))
    raise AssertionError("Target leakage not detected")
except LeakageError:
    pass

print("✓ Phase 27 leakage guards validated (duplicate, temporal, assay, target)")
