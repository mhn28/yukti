def suggest_encoding(schema):
    scale = schema.measurement_scale

    if scale == "nominal":
        return ["one-hot (classification only)", "label encoding (non-metric)"]

    if scale == "ordinal":
        return ["rank encoding", "custom ordered mapping"]

    if scale in {"interval", "ratio"}:
        return ["z-score", "min-max", "log-transform (if justified)"]

    if scale == "symbolic":
        return ["sequence indexing", "embedding (exploratory only)"]

    if scale in {"temporal", "spatiotemporal"}:
        return ["time-indexed arrays", "state-space representation"]

    return []
