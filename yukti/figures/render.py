from yukti.plots.plot_2d import plot_2d_with_annotations
from yukti.plots.plot_3d import plot_3d_with_annotations
from yukti.plots.plot_4d import plot_4d_trajectory

def render_figure(spec):
    plot = spec["plot"]
    data = spec["data"]
    annotations = spec["annotations"]
    out = spec["output"]

    if plot["type"] == "2d_scatter":
        plot_2d_with_annotations(
            x=data["x"],
            y=data["y"],
            annotations=annotations,
            title=plot["title"],
            out=out
        )

    elif plot["type"] == "3d_scatter":
        plot_3d_with_annotations(
            data["x"], data["y"], data["z"],
            annotations,
            plot["title"],
            out
        )

    elif plot["type"] == "4d_trajectory":
        plot_4d_trajectory(
            coords=data["coords"],
            time=data["time"],
            annotations=annotations,
            out=out
        )

    else:
        raise ValueError(f"Unsupported plot type: {plot['type']}")
