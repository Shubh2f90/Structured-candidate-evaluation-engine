import json
from src.evaluator import evaluate_candidate

candidates = {
    "Candidate A": """
    I would first understand the problem clearly and break it into steps.
    My approach would be to design a logical solution and consider edge cases
    before implementing the final code.
    """,

    "Candidate B": """
    I will solve the problem.
    """,

    "Candidate C": """
    My approach involves analyzing the requirements, designing a clean solution,
    applying logical steps, and clearly communicating the reasoning behind decisions.
    """
}

evaluation_results = []

for name, answer in candidates.items():
    result = evaluate_candidate(answer)

    evaluation_results.append({
        "candidate_name": name,
        "scores": result["scores"],
        "total_score": result["total_score"],
        "feedback": result["feedback"]
    })

# Convert to JSON formatted string
json_output = json.dumps(evaluation_results, indent=4)

print("Final Structured JSON Output:\n")
print(json_output)
