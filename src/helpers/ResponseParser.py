import csv
import io

COLUMNS = ["label", "element", "arg1", "arg2"]


def parse_llm_response(response_text: str) -> set[tuple[str, str, str, str]]:
    """
    Parses a raw CSV response (header: label,element,arg1,arg2) from the LLM
    into a set of 4-tuples. Each tuple is (label, element, arg1, arg2),
    lowercased and stripped. Duplicate elements (e.g. several ISA / Part-of
    rows) are all preserved.

    Tolerant to common LLM formatting quirks so one bad row can never
    throw away the whole response:
    - trailing commas (extra trailing empty fields are dropped)
    - short rows (padded with empty strings)
    - unquoted commas inside the element (overflow fields are merged back
      into element; the last two fields are kept as arg1/arg2)
    - repeated/missing header rows and blank lines
    """
    parsed: set[tuple[str, str, str, str]] = set()

    for raw in csv.reader(io.StringIO(str(response_text))):
        fields = [f.strip() for f in raw]

        # Drop trailing empty fields (models often add a stray trailing comma)
        while fields and fields[-1] == "":
            fields.pop()
        if not fields:
            continue
        # Skip header rows wherever they appear
        if fields[0].lower() == "label":
            continue

        # Too many fields: an unquoted comma (usually the AC "Name(attrs)"
        # pattern). Keep label and the last two fields as args, merge the
        # middle back into element.
        if len(fields) > 4:
            fields = [fields[0]] + [",".join(fields[1:-2])] + fields[-2:]

        label, element, arg1, arg2 = (fields + ["", "", "", ""])[:4]
        if not label and not element:
            continue
        parsed.add((label.lower(), element.lower(), arg1.lower(), arg2.lower()))

    return parsed
