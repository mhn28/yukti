
from typing import Dict, Any

DISCLAIMER = (
    "This narrative is informational only. "
    "All interpretations must be independently verified by human experts. "
    "No clinical, regulatory, or real-world decisions should rely solely on this output."
)

class ScientificNarrator:
    def methods(self, decision_trace: Dict[str, Any]) -> str:
        steps = decision_trace.get("decision_trace", [])
        lines = []
        for s in steps:
            lines.append(
                f"{s['action'].replace('_',' ').capitalize()} — {s['rationale']}."
            )
        return " ".join(lines)

    def results(self, statistics: Dict[str, Any]) -> str:
        return (
            f"The analysis produced a test statistic of {statistics.get('stat','NA')} "
            f"with a p-value of {statistics.get('p','NA')}. "
            f"Multiple-testing correction applied: {statistics.get('correction','none')}." 
        )

    def limitations(self) -> str:
        return (
            "Results are contingent on declared assumptions, sample size, "
            "data quality, and methodological choices. "
            "Unmodeled confounders may influence findings."
        )

    def full_report(self, trace: Dict[str, Any], stats: Dict[str, Any]) -> Dict[str,str]:
        return {
            "methods": self.methods(trace),
            "results": self.results(stats),
            "limitations": self.limitations(),
            "disclaimer": DISCLAIMER
        }
