import re

def _strip_code_fences(text: str) -> str:
    """Remove surrounding Markdown code fences (```lang ... ```) if present."""
    text = text.strip()
    fence = re.match(r"^```[a-zA-Z]*\s*\n(.*?)\n?```\s*$", text, re.DOTALL)
    if fence:
        return fence.group(1)
    # Fallback: drop any stray fence lines
    return "\n".join(l for l in text.split("\n") if not l.strip().startswith("```"))


def _is_separator_row(line: str) -> bool:
    """True for header/separator rows made only of -, |, : and whitespace."""
    return re.fullmatch(r"[\s\-|:]*", line) is not None


def parse_llm_response(response_text: str) -> set[tuple[str, str, str, str]]:
    """
    Parses a Markdown table from the LLM response into a set of 4-tuples.
    Each tuple is (label, element, arg1, arg2), lowercased and stripped.
    Duplicate elements (e.g. several ISA / Part-of rows) are all preserved.
    """
    text = _strip_code_fences(response_text)

    # Extract the table using regex
    table_match = re.search(r'(\| label \| element \| arg1 \| arg2 \|.*)', text, re.DOTALL | re.IGNORECASE)
    if not table_match:
        return set()

    table_str = table_match.group(1)
    lines = table_str.strip().split('\n')

    parsed: set[tuple[str, str, str, str]] = set()
    for line in lines:
        line = line.strip()
        if not line or '|' not in line:
            continue
        # Skip separator rows (---|---) and the header row
        if _is_separator_row(line):
            continue
        if re.fullmatch(r"\|?\s*label\s*\|\s*element\s*\|\s*arg1\s*\|\s*arg2\s*\|?", line, re.IGNORECASE):
            continue

        # Split on '|'. A well-formed row "| a | b | c | d |" yields a leading and
        # trailing empty string; drop those two ONLY, keep interior blanks so
        # columns don't shift.
        cols = line.split('|')
        if line.startswith('|'):
            cols = cols[1:]
        if line.endswith('|'):
            cols = cols[:-1]
        cols = [c.strip().lower() for c in cols]

        # Take exactly 4 data columns, padding with "" if fewer
        cols = (cols + ["", "", "", ""])[:4]
        label, element, arg1, arg2 = cols
        if not label and not element:
            continue
        parsed.add((label, element, arg1, arg2))

    return parsed