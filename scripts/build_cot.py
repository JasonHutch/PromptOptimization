#!/usr/bin/env python3
"""Compose a Chain-of-Thought prompt from an identification prompt and a classification prompt.

    python build_cot.py prompts/identification/P2.md prompts/classification/P2.md prompts/cot/P1.md
"""
import re, sys

def sec(txt, start, stop):
    a = txt.index(start)
    b = txt.index(stop, a + len(start)) if stop else len(txt)
    return txt[a:b].strip()

def build(id_path, cl_path):
    idp, clp = open(id_path).read(), open(cl_path).read()
    id_def = sec(idp, "# Definition", "# Categories").replace("# Definition", "### Definition")
    id_cats = re.sub(r"^# Categories.*$", "### Categories", sec(idp, "# Categories", "# Domain scope filter"), flags=re.M)
    id_filt = sec(idp, "# Domain scope filter", "# Procedure").replace("# Domain scope filter", "### Domain scope filter")
    cl_rules = sec(clp, "# Classification rules", "# Output")
    cl_rules = re.sub(r"^## ", "#### ", cl_rules, flags=re.M)
    cl_rules = re.sub(r"^# Classification rules.*$", "### Classification rules (apply by phrase category)", cl_rules, flags=re.M)
    cl_labels = sec(clp, "| label | meaning |", "One row per element.")
    id_proc = sec(idp, "# Procedure", "# Constraints").replace("# Procedure", "").strip()
    return f"""# Role
You are a domain modeling expert applying the Agile Unified Methodology (AUM). Build the domain model for the business description below by reasoning step by step: first identify the domain-specific phrases, then classify them into classes, attributes, attribute values and relationships, then review the result.

# Business description
\"\"\"
{{{{DESCRIPTION}}}}
\"\"\"

# STEP 1 - Identify domain-specific phrases
{id_def}

{id_cats}

{id_filt}

### How to do it
{id_proc}
Only list phrases that literally appear in the description.

Write this step as a heading "## Step 1: Domain-specific phrases" followed by a markdown table with exactly the columns | rule | phrase |.

# STEP 2 - Classify the phrases
Work through the Step 1 table row by row and decide what each phrase becomes, using these rules.

{cl_rules}

Write this step as a heading "## Step 2: Classification reasoning" followed by one short line per phrase in the form
phrase -> decision : reason (at most 12 words)
Do not use a table in Step 2.

# STEP 3 - Review
Check the Step 2 decisions against the review checklist above. Merge duplicates, remove design or implementation classes, give every attribute an owning class, make sure every relationship connects listed classes, and check every association against both association-class conditions.

Write this step as a heading "## Step 3: Review" followed by a short bullet list of the corrections you made (or "No changes").

# STEP 4 - Final domain model
Write a heading "## Final domain model" followed by one markdown table with exactly these columns and nothing after it.

| label | element | arg1 | arg2 |
|---|---|---|---|

{cl_labels}

One row per element. No code fences.
"""

if __name__ == "__main__":
    open(sys.argv[3], "w").write(build(sys.argv[1], sys.argv[2]))
