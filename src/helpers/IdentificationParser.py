import csv
import io
import re


def canon_rule(cell: str) -> str:
    """Normalizes a rule cell: prefer the first digit 1-9, else lowercase text."""
    cell = (cell or "").strip()
    match = re.search(r"[1-9]", cell)
    if match:
        return match.group(0)
    return cell.lower()


def parse_identification_response(response_text: str) -> set[tuple[str, str]]:
    """
    Parses a raw CSV response (header: rule,phrase) from the LLM into a set of
    (rule, phrase) tuples, with rules normalized and phrases stripped.

    Tolerant to the same LLM formatting quirks as the classification parser:
    - trailing commas (extra trailing empty fields are dropped)
    - repeated or missing header rows and blank lines
    - unquoted commas inside the phrase (overflow merged back into the phrase)
    """
    parsed: set[tuple[str, str]] = set()

    for raw in csv.reader(io.StringIO(str(response_text))):
        fields = [f.strip() for f in raw]

        # Drop trailing empty fields (models often add a stray trailing comma)
        while fields and fields[-1] == "":
            fields.pop()
        if not fields:
            continue
        # Skip header rows wherever they appear
        if fields[0].lower() == "rule":
            continue
        if len(fields) < 2:
            continue  # rule with no phrase

        # Too many fields: an unquoted comma inside the phrase; merge back
        if len(fields) > 2:
            fields = [fields[0], ",".join(fields[1:])]

        rule = canon_rule(fields[0])
        phrase = fields[1]
        if not phrase:
            continue
        parsed.add((rule, phrase))

    return parsed
