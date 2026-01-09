from yukti.annotations.builder import build_p_annotation, build_effect_annotation

# ---- valid statistical result fixture ----
fake_result = {
    "p": 0.004,
    "cohen_d": 0.82
}

# ---- p-value annotation ----
p_ann = build_p_annotation(fake_result["p"])
assert p_ann["significance"] == "**"

# ---- effect-size annotation ----
e_ann = build_effect_annotation(fake_result["cohen_d"], label="Cohen d")
assert e_ann["value"] == 0.82

print("✓ Annotation builder validated")
