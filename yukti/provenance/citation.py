from dataclasses import dataclass

@dataclass(frozen=True)
class Citation:
    title: str
    authors: str
    journal: str
    year: int
    pmid: str | None = None
    doi: str | None = None
