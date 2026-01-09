from dataclasses import dataclass

@dataclass(frozen=True)
class RuntimeCapabilities:
    filesystem: bool
    plugins: bool
    external_exec: bool
    gui: bool

APPSTORE = RuntimeCapabilities(
    filesystem=False,
    plugins=False,
    external_exec=False,
    gui=True
)

DEV = RuntimeCapabilities(
    filesystem=True,
    plugins=True,
    external_exec=True,
    gui=False
)
