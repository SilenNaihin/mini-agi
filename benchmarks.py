import os
import sys
from typing import Tuple
import subprocess


def run_specific_agent(task: str) -> None:
    # Ensure the directory for the project exists
    os.makedirs("user/miniagi", exist_ok=True)

    # Run the mini-agi command
    subprocess.run(["python", "miniagi.py", task], text=True)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <task>")
        sys.exit(1)
    task = sys.argv[1]
    run_specific_agent(task)
