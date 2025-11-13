# student_score_analyzer.py

# Sample data: list of dictionaries with student names and marks
students = [
    {"name": "Alice", "marks": 88},
    {"name": "Bob", "marks": 72},
    {"name": "Charlie", "marks": 95},
    {"name": "David", "marks": 64},
    {"name": "Eve", "marks": 79}
]

# 1️⃣ Extract all marks
marks = [student["marks"] for student in students]

# 2️⃣ Calculate average score
average_score = sum(marks) / len(marks)
print(f"Average Score: {average_score:.2f}")

# 3️⃣ Find highest and lowest scorers
highest_scorer = max(students, key=lambda s: s["marks"])
lowest_scorer = min(students, key=lambda s: s["marks"])

print(f"Highest Scorer: {highest_scorer['name']} ({highest_scorer['marks']})")
print(f"Lowest Scorer: {lowest_scorer['name']} ({lowest_scorer['marks']})")

# 4️⃣ Sort students by marks (descending)
sorted_students = sorted(students, key=lambda s: s["marks"], reverse=True)
print("\nStudents sorted by marks:")
for s in sorted_students:
    print(f"{s['name']}: {s['marks']}")

# 5️⃣ Use list comprehension to get marks above a threshold
threshold = 75
above_threshold = [s["marks"] for s in students if s["marks"] > threshold]
print(f"\nMarks above {threshold}: {above_threshold}")

