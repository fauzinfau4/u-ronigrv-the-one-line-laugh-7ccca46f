"""Write the competition's one-line entry to /output/entry.txt."""

from pathlib import Path

SENTENCE = "My password manager remembers every password I've ever had except the one I need right now, which is the only job it has."

assert 1 <= len(SENTENCE) <= 200
assert "\n" not in SENTENCE

output_path = Path("/output/entry.txt")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(SENTENCE, encoding="utf-8")

# Verification: output is deterministic and contains no trailing newline.
