import json, yaml

REQUIRED_KEYS = {
    "figure_id",
    "plot",
    "data",
    "annotations",
    "output"
}

def load_spec(path):
    if path.endswith(".yaml") or path.endswith(".yml"):
        with open(path) as f:
            spec = yaml.safe_load(f)
    elif path.endswith(".json"):
        with open(path) as f:
            spec = json.load(f)
    else:
        raise ValueError("Unsupported spec format")

    missing = REQUIRED_KEYS - set(spec)
    if missing:
        raise ValueError(f"Missing required keys: {missing}")

    return spec
