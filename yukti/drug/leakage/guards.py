
from dataclasses import dataclass
from typing import Iterable, Set, Dict
import datetime

class LeakageError(RuntimeError):
    pass

@dataclass
class SplitMeta:
    train_ids: Set[str]
    test_ids: Set[str]
    train_dates: Iterable[datetime.date] | None = None
    test_dates: Iterable[datetime.date] | None = None
    train_assays: Set[str] | None = None
    test_assays: Set[str] | None = None
    feature_names: Set[str] | None = None
    label_name: str | None = None

def enforce_no_duplicate_entities(meta: SplitMeta):
    overlap = meta.train_ids & meta.test_ids
    if overlap:
        raise LeakageError(f"Duplicate entities across splits: {sorted(list(overlap))[:5]}")
    return True

def enforce_no_temporal_leakage(meta: SplitMeta):
    if meta.train_dates and meta.test_dates:
        if max(meta.train_dates) > min(meta.test_dates):
            raise LeakageError("Temporal leakage detected: training data newer than test data.")
    return True

def enforce_no_assay_leakage(meta: SplitMeta):
    if meta.train_assays and meta.test_assays:
        overlap = meta.train_assays & meta.test_assays
        if overlap:
            raise LeakageError(f"Assay leakage detected: {sorted(list(overlap))[:5]}")
    return True

def enforce_no_target_leakage(meta: SplitMeta):
    if meta.feature_names and meta.label_name:
        if meta.label_name in meta.feature_names:
            raise LeakageError(f"Target leakage detected: label '{meta.label_name}' present as feature.")
    return True

def enforce_all(meta: SplitMeta):
    enforce_no_duplicate_entities(meta)
    enforce_no_temporal_leakage(meta)
    enforce_no_assay_leakage(meta)
    enforce_no_target_leakage(meta)
    return True
