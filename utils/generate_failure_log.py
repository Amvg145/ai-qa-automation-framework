import subprocess

result = subprocess.run(
    ["pytest", "-v", "generated_tests"],
    capture_output=True,
    text=True
)

with open("failure_log.txt", "w", encoding="utf-8") as file:
    file.write(result.stdout + result.stderr)

print("failure_log.txt generated")