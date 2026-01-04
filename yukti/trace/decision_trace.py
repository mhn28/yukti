
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List, Dict, Any

@dataclass
class DecisionStep:
    timestamp_utc: str
    action: str
    rationale: str
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class DecisionTrace:
    steps: List[DecisionStep] = field(default_factory=list)

    def record(self, action: str, rationale: str, **metadata):
        self.steps.append(
            DecisionStep(
                timestamp_utc=datetime.now(timezone.utc).isoformat(),
                action=action,
                rationale=rationale,
                metadata=metadata
            )
        )

    def export(self) -> Dict[str, Any]:
        return {
            "decision_trace": [s.__dict__ for s in self.steps]
        }
