def enforce_schema(schema):
    msg = schema.validate()

    if "not permitted" in msg:
        raise RuntimeError(msg)

    if "requires explicit opt-in" in msg:
        raise RuntimeError(
            "Spatiotemporal or longitudinal reasoning must be explicitly selected by user"
        )

    return True
