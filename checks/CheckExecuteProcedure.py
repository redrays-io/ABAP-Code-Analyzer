import re
from dataclasses import dataclass
from typing import List


@dataclass
class CheckResult:
    line_number: int
    line_content: str


class CheckExecuteProcedure:
    title = "ADBC Injection Vulnerability in execute_procedure Method"
    severity = "High"
    vulnerability_type = "ADBC Injection"

    def __init__(self):
        self.pattern = re.compile(r'execute_procedure\(', re.IGNORECASE)

    def run(self, file_content: str) -> List[CheckResult]:
        results = []
        lines = file_content.split('\n')
        for i, line in enumerate(lines, 1):
            if self.pattern.search(line):
                results.append(CheckResult(i, line.strip()))
        return results
