#!/usr/bin/env python3
"""Extract problems 401-800 from problems.json and output a summary."""
import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "04_原始资料" / "problems.json", "r", encoding="utf-8") as f:
    data = json.load(f)

problems = data["problems"]
start_idx = 400  # 0-based for 1-based 401
end_idx = 800    # 0-based for 1-based 800

batch = problems[start_idx:end_idx]
print(f"Total problems in batch: {len(batch)}")
print(f"First problem_id: {batch[0]['problem_id']}")
print(f"Last problem_id: {batch[-1]['problem_id']}")

# Check how many solutions already exist with complete content
existing_complete = 0
existing_template = 0
no_solution_yet = 0

for i, p in enumerate(batch):
    solution_path = BASE_DIR / p["solution_note"]
    if os.path.exists(solution_path):
        with open(solution_path, "r", encoding="utf-8") as f:
            content = f.read()
        # Check if solution is complete
        has_all_sections = all(s in content for s in [
            "## 完整题目", "## 思路分析", "## 详细解答", "## 答案", "## 总结"
        ])
        has_substantial_detail = content.count("## 详细解答") > 0 and len(content.split("## 详细解答")[-1].strip()) > 100
        if has_all_sections and has_substantial_detail:
            existing_complete += 1
        else:
            existing_template += 1
    else:
        no_solution_yet += 1

print(f"\nExisting complete solutions: {existing_complete}")
print(f"Existing template/unfinished: {existing_template}")
print(f"No solution file yet: {no_solution_yet}")
print(f"Need to process: {existing_template + no_solution_yet}")

# Output problem IDs for reference
print("\n--- First 20 problem IDs ---")
for i, p in enumerate(batch[:20]):
    print(f"  {401+i}: {p['problem_id']} - {p.get('kind', '')} - {p.get('module', '')}")

print(f"\n--- Last 20 problem IDs ---")
for i, p in enumerate(batch[-20:]):
    print(f"  {781+i}: {p['problem_id']} - {p.get('kind', '')} - {p.get('module', '')}")
