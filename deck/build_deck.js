// Build the Team 4 presentation from results.json.
//   node deck/build_deck.js results.json out.pptx
const pptxgen = require("pptxgenjs");
const fs = require("fs");

const R = JSON.parse(fs.readFileSync(process.argv[2] || "results.json", "utf8"));
const OUT = process.argv[3] || "Team4_Prompt_Optimization.pptx";

// ---------- palette (UTA) ----------
const BLUE = "0064B1", NAVY = "0B2F57", ORANGE = "F58025", INK = "1A2233", MUTED = "5B6678",
  LIGHT = "EEF3F9", LINE = "D5DDE8", WHITE = "FFFFFF", TEAL = "1E8C7E", VIOLET = "6D4FC2", PALEBLUE = "D6E6F5";
const DOM = [["library", "Library", BLUE], ["car_rental", "Car rental", TEAL], ["ntss", "NTSS", VIOLET]];
const FONT = "Arial", MONO = "Courier New";
const TARGET = 90;

// ---------- data helpers ----------
const vers = (a) => Object.keys(R[a] || {}).filter((v) => !v.includes("max")).sort();
const RS = fs.existsSync(process.argv[4] || "research.json") ? JSON.parse(fs.readFileSync(process.argv[4] || "research.json", "utf8")) : null;
const cell = (a, v, d) => (R[a] && R[a][v] && R[a][v][d]) || null;
const f1 = (a, v, d) => { const c = cell(a, v, d); return c ? c.f1 : null; };
const fmt = (x) => (x == null ? "–" : x.toFixed(1));
const mean3 = (a, v) => { const xs = DOM.map(([d]) => f1(a, v, d)).filter((x) => x != null); return xs.length === 3 ? xs.reduce((s, x) => s + x, 0) / 3 : -1; };
function best(a) { let b = null, bm = -1; for (const v of vers(a)) { const m = mean3(a, v); if (m > bm) { bm = m; b = v; } } return b; }
const has = (a, v) => DOM.every(([d]) => cell(a, v, d));
// run-to-run noise, measured separately per activity (largest spread among cells with >= 2 runs)
const noiseBy = {}, noiseCellBy = {};
for (const a of Object.keys(R)) for (const v of Object.keys(R[a])) for (const [d, name] of DOM) {
  const c = cell(a, v, d); if (c && c.n >= 2) { const sp = Math.max(...c.f1_runs) - Math.min(...c.f1_runs);
    if (sp > (noiseBy[a] || 0)) { noiseBy[a] = sp; noiseCellBy[a] = `${a} ${v} on ${name}: ${c.f1_runs.join(", ")}`; } }
}
const noise = noiseBy.identification || 0, noiseCell = noiseCellBy.identification || "";
const NOISE = Math.round(noise);
const delta = (x, y) => (x == null || y == null ? null : y - x);
const sgn = (x) => (x == null ? "–" : (x >= 0 ? "+" : "") + x.toFixed(1));
const HALF = noise / 2;
const halfOf = (a) => (noiseBy[a] || noise) / 2;
const verdict = (d, a = "identification") => d == null ? "" : Math.abs(d) > halfOf(a) ? "" : " (within noise)";
const bestDom = (a, d) => { let b = null, bv = -1; for (const v of vers(a)) { const x = f1(a, v, d); if (x != null && x > bv) { bv = x; b = v; } } return [b, bv]; };

const ID_BEST = best("identification"), CL_BEST = best("classification"), COT_BEST = best("cot");

// ---------- pptx helpers ----------
const pres = new pptxgen();
pres.layout = "LAYOUT_16x9"; // 10 x 5.625 in
pres.title = "Evolutionary Prompt Optimization for Domain Modeling";
pres.author = "Team Four";

function T(slide, text, o) { slide.addText(text, Object.assign({ isTextBox: true, fontFace: FONT, color: INK, fontSize: 14, margin: 0, valign: "top" }, o)); }
function title(slide, text, sub) {
  T(slide, text, { x: 0.5, y: 0.32, w: 9, h: 0.6, fontSize: 28, bold: true, color: NAVY, valign: "middle" });
  if (sub) T(slide, sub, { x: 0.5, y: 0.92, w: 9, h: 0.35, fontSize: 13, color: MUTED });
}
function content(t, sub) { const s = pres.addSlide(); s.background = { color: WHITE }; title(s, t, sub); return s; }
function pill(slide, x, y, label, fill, w) {
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: w || 0.62, h: 0.34, rectRadius: 0.17, fill: { color: fill || BLUE }, line: { color: fill || BLUE } });
  T(slide, label, { x, y, w: w || 0.62, h: 0.34, fontSize: 12, bold: true, color: WHITE, align: "center", valign: "middle" });
}
function card(slide, x, y, w, h, fill) { slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.08, fill: { color: fill || LIGHT }, line: { color: fill || LIGHT } }); }
function bullets(slide, items, o) {
  slide.addText(items.map((t, i) => ({ text: t, options: { bullet: { indent: 14 }, breakLine: i < items.length - 1, paraSpaceAfter: 6 } })),
    Object.assign({ isTextBox: true, fontFace: FONT, fontSize: 13, color: INK, margin: 0, valign: "top" }, o));
}
function dark(t, sub) {
  const s = pres.addSlide(); s.background = { color: BLUE };
  T(s, t, { x: 0.7, y: 2.0, w: 8.6, h: 0.9, fontSize: 36, bold: true, color: WHITE, valign: "middle" });
  if (sub) T(s, sub, { x: 0.7, y: 2.9, w: 8.6, h: 0.5, fontSize: 16, color: PALEBLUE });
  return s;
}
const hdr = (t) => ({ text: t, options: { bold: true, color: WHITE, fill: { color: NAVY }, fontSize: 11, fontFace: FONT } });
const td = (t, o) => ({ text: String(t), options: Object.assign({ fontSize: 11, fontFace: FONT, color: INK }, o || {}) });
function lineChart(slide, act, x, y, w, h, key) {
  const vs = vers(act);
  const data = DOM.map(([d, name]) => ({ name, labels: vs, values: vs.map((v) => { const c = cell(act, v, d); return c ? (key === "step1" ? c.step1_f1 : c.f1) : null; }) }));
  data.push({ name: "90% target", labels: vs, values: vs.map(() => TARGET) });
  slide.addChart(pres.charts.LINE, data, {
    x, y, w, h, chartColors: [BLUE, TEAL, VIOLET, ORANGE], lineSize: 2.5, lineDataSymbol: "circle", lineDataSymbolSize: 7,
    valAxisMinVal: 0, valAxisMaxVal: 100, valAxisMajorUnit: 25, valAxisLabelFontSize: 10, catAxisLabelFontSize: 12,
    valAxisLabelColor: MUTED, catAxisLabelColor: INK, valGridLine: { color: "E3E8EF", size: 0.75 }, catGridLine: { style: "none" },
    showLegend: true, legendPos: "b", legendFontSize: 11, legendFontFace: FONT, valAxisTitle: "F1 (%)", showValAxisTitle: true, valAxisTitleFontSize: 10, valAxisTitleColor: MUTED,
  });
}
function scoreTable(slide, act, x, y, w) {
  const vs = vers(act);
  const rows = [[hdr("Version"), ...DOM.map(([, n]) => hdr(n))]];
  for (const v of vs) rows.push([td(v, { bold: true }), ...DOM.map(([d]) => { const c = cell(act, v, d); const val = c ? c.f1 : null;
    return td(val == null ? "–" : fmt(val), { bold: val != null && val >= TARGET, color: val != null && val >= TARGET ? BLUE : INK }); })]);
  slide.addTable(rows, { x, y, w, colW: [0.8, (w - 0.8) / 3, (w - 0.8) / 3, (w - 0.8) / 3], border: { type: "solid", pt: 0.5, color: LINE }, rowH: 0.3, valign: "middle" });
}

// ================= SLIDES =================

// 1. Title
{
  const s = pres.addSlide(); s.background = { color: BLUE };
  T(s, "Evolutionary Prompt Optimization for Domain Modeling", { x: 0.7, y: 1.35, w: 8.6, h: 1.3, fontSize: 36, bold: true, color: WHITE, valign: "bottom" });
  T(s, "Domain-specific phrase identification & classification with the AUM methodology", { x: 0.7, y: 2.75, w: 8.6, h: 0.45, fontSize: 16, color: PALEBLUE });
  T(s, "Team Four  ·  CSE 4392 / 5320  ·  The University of Texas at Arlington", { x: 0.7, y: 3.7, w: 8.6, h: 0.35, fontSize: 14, bold: true, color: WHITE });
  T(s, "LLM under test: Claude (claude.ai, default tier)  ·  September 2026", { x: 0.7, y: 4.1, w: 8.6, h: 0.35, fontSize: 13, color: PALEBLUE });
  s.addNotes("Introduce the team. The LLM we optimized for is Claude, called blind from our prompt lab page: it only ever sees the prompt and the business description.");
}

// 2. Objectives
{
  const s = content("Project objectives", "What we are solving and what counts as improvement");
  T(s, "The problem", { x: 0.5, y: 1.45, w: 5.2, h: 0.3, fontSize: 15, bold: true, color: BLUE });
  bullets(s, [
    "Step 2 of AUM domain modeling: identify the domain-specific phrases in a business description, in nine phrase categories.",
    "Step 3: classify those phrases into classes, attributes, attribute values and relationships.",
    `Baseline prompts scored ${Math.round(Math.min(...DOM.map(([d]) => f1("identification", "P0", d))))}–${Math.round(Math.max(...DOM.map(([d]) => f1("identification", "P0", d))))}% F1 on identification and ${Math.round(Math.min(...DOM.map(([d]) => f1("classification", "P0", d))))}–${Math.round(Math.max(...DOM.map(([d]) => f1("classification", "P0", d))))}% on classification.`,
  ], { x: 0.5, y: 1.8, w: 5.2, h: 1.6, fontSize: 12.5 });
  T(s, "Why it is hard", { x: 0.5, y: 3.55, w: 5.2, h: 0.3, fontSize: 15, bold: true, color: BLUE });
  bullets(s, [
    "\"Domain-specific\" is a judgment; the same noun can be a class or an attribute.",
    "The three expert solutions follow slightly different annotation conventions.",
    `Responses vary run to run: one prompt scored up to ${NOISE} points apart.`,
  ], { x: 0.5, y: 3.9, w: 5.2, h: 1.3, fontSize: 12 });
  card(s, 6.05, 1.45, 3.45, 3.7, NAVY);
  T(s, "90%", { x: 6.3, y: 1.6, w: 3, h: 0.8, fontSize: 48, bold: true, color: ORANGE });
  T(s, "F1 target set by the instructor (the assignment sheet says 97%)", { x: 6.3, y: 2.4, w: 3, h: 0.5, fontSize: 11, color: PALEBLUE });
  T(s, "Our objective is to optimize a prompt so that an LLM following the AUM methodology identifies and classifies domain-specific phrases with F1 ≥ 90% against the expert solutions, first on the library example and then on car rental and NTSS.",
    { x: 6.3, y: 3.0, w: 3.0, h: 2.0, fontSize: 12.5, color: WHITE });
  s.addNotes("Improvement means higher F1 against the instructor's expert solutions, which balances precision (no extra phrases) and recall (nothing missed).");
}

// 3. Evaluation criteria
{
  const s = content("Evaluation criteria", "Expert solutions + precision, recall and F1");
  bullets(s, [
    "The instructor's expert solutions are evaluation references only. They never appear in a prompt; an automated check compares every prompt against them.",
    "Precision = TP / (TP + FP)    Recall = TP / (TP + FN)    F1 = 2PR / (P + R)",
    "Identification: a phrase must match the expert's phrase and rule number. Singular/plural and verb forms count as one phrase.",
    "Classification: the team's scorer matches label, element and both arguments; each expert item can be matched by one prediction only (bipartite matching).",
    "Expert keys: library phrase list and classification sheet, NTSS underlined description and classification, car rental brainstorming and classification.",
  ], { x: 0.5, y: 1.45, w: 5.6, h: 3.8, fontSize: 12.5 });
  card(s, 6.4, 1.45, 3.1, 1.75);
  T(s, "96.36%", { x: 6.6, y: 1.55, w: 2.8, h: 0.6, fontSize: 32, bold: true, color: BLUE });
  T(s, "Our scorer reproduces the instructor's hand-computed F1 for Gemini's library answer exactly (TP 53, FP 1, FN 3).", { x: 6.6, y: 2.15, w: 2.75, h: 0.95, fontSize: 11, color: INK });
  card(s, 6.4, 3.4, 3.1, 1.75);
  T(s, `${NOISE}-pt spread`, { x: 6.6, y: 3.5, w: 2.8, h: 0.6, fontSize: 32, bold: true, color: ORANGE });
  T(s, `Largest gap between repeated identification runs of the same prompt; we treat changes under ±${fmt(HALF)} points as noise (thresholds are measured per activity).`, { x: 6.6, y: 4.1, w: 2.75, h: 0.95, fontSize: 11, color: INK });
  s.addNotes("Validated scorer: reproduces the instructor's own calculation. Noise measured on " + noiseCell + ".");
}

// 4. The optimization loop
{
  const s = content("Our evolutionary optimization loop", "Prompt → AI → Output → Evaluation → Error analysis → Suggestions → Revised prompt");
  const steps = [["Prompt Pi", "Methodology + prompt text"], ["Claude (blind)", "Sees only the prompt and the description"], ["Response", "Saved for every run"],
    ["Scoring", "F1 vs expert solution"], ["Error analysis", "Misses and extras grouped into error classes"], ["Revise → Pi+1", "One rule per error class, stated hypothesis"]];
  const w = 1.38, gap = 0.16, y = 1.75;
  steps.forEach(([h, t], i) => {
    const x = 0.5 + i * (w + gap);
    card(s, x, y, w, 1.55, i === 5 ? NAVY : LIGHT);
    T(s, h, { x: x + 0.1, y: y + 0.12, w: w - 0.2, h: 0.5, fontSize: 13, bold: true, color: i === 5 ? WHITE : NAVY });
    T(s, t, { x: x + 0.1, y: y + 0.65, w: w - 0.2, h: 0.85, fontSize: 10.5, color: i === 5 ? PALEBLUE : MUTED });
    if (i < steps.length - 1) T(s, "›", { x: x + w - 0.02, y: y + 0.5, w: gap + 0.04, h: 0.5, fontSize: 22, bold: true, color: ORANGE, align: "center" });
  });
  card(s, 0.5, 3.6, 9.0, 1.5, WHITE);
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.5, y: 3.6, w: 9.0, h: 1.5, rectRadius: 0.08, fill: { color: WHITE }, line: { color: LINE, width: 1 } });
  bullets(s, [
    "Assignment steps 3–8: run on library; if F1 < 90, go back to step 3 and modify the methodology and prompt. Then car rental and NTSS; if either is < 90, go back to step 3.",
    "We ran all three domains every round, so each change was also checked for generalization.",
    "Tools: a prompt lab page (runs Claude and shows live F1), the team repo's scorers, and a changelog with the evidence behind every change.",
  ], { x: 0.75, y: 3.75, w: 8.5, h: 1.3, fontSize: 12 });
  s.addNotes("This is the complete loop from the assignment. Every revision starts from scored errors, not from trial and error.");
}

// 5. Baseline prompts
{
  const s = content("Baseline prompts (P0)", "Where we started");
  card(s, 0.5, 1.45, 4.35, 3.7);
  T(s, "Identification P0", { x: 0.7, y: 1.55, w: 4, h: 0.3, fontSize: 14, bold: true, color: BLUE });
  T(s, "Identify and list the domain-specific phrases in the business description below.\n\nIdentify the following DOMAIN-SPECIFIC phrases:\n1. nouns / noun phrases\n2. \"X of Y\" expressions\n3. transitive verbs\n4. adjectives, enumeration\n5. numeric, quantity\n6. possession expressions\n7. \"consist of / part of\" expressions\n8. containment expressions\n9. \"X is a Y\" expressions\n\nOutput a table | rule | phrase |.",
    { x: 0.7, y: 1.9, w: 4.0, h: 3.15, fontSize: 9.5, fontFace: MONO, color: INK });
  card(s, 5.15, 1.45, 4.35, 3.7);
  T(s, "Classification P0 (team's t1 prompt)", { x: 5.35, y: 1.55, w: 4, h: 0.3, fontSize: 14, bold: true, color: BLUE });
  bullets(s, ["Rules for class vs attribute, association, association class, inheritance and aggregation.", "Strict labelled output table (C, A, V, AS, AC, AG, I).", "Input: the phrase list only, no description.", "Found: its placeholder was missing, so the notebook never inserted the phrases; fixed for P0."],
    { x: 5.35, y: 1.95, w: 4.0, h: 1.9, fontSize: 11.5 });
  const rows = [[hdr("P0 F1"), ...DOM.map(([, n]) => hdr(n))],
    [td("Identify", { bold: true }), ...DOM.map(([d]) => td(fmt(f1("identification", "P0", d))))],
    [td("Classify", { bold: true }), ...DOM.map(([d]) => td(fmt(f1("classification", "P0", d))))]];
  s.addTable(rows, { x: 5.35, y: 3.95, w: 3.95, colW: [0.95, 1.0, 1.0, 1.0], border: { type: "solid", pt: 0.5, color: LINE }, rowH: 0.3 });
}

// 6. Evolution timeline
{
  const s = content("Evolution of the prompts", "Major change in each version; full text and evidence in the repo changelog");
  const ID = { P0: "Category list + output format", P1: "Role, definition, per-category rules, course example, procedure", P2: "9 error-driven inclusion rules, scope filter, neutral examples", P3: "Narrowed over-firing rules + self-verification pass", P4: "Whole possession clauses, record-keeping verbs, example values" };
  const CL = { P0: "Team's t1 rules, phrases only", P1: "Category→element mapping, class/attribute tests, AC conditions, checklist", P2: "Naming rule, documents as classes, V only for closed lists", P3: "AS+AC together, inheritance test, attach to named class" };
  const rowsDef = [["Identification", "identification", ID], ["Classification", "classification", CL]];
  rowsDef.forEach(([label, act, map], r) => {
    const y = 1.5 + r * 1.75;
    T(s, label, { x: 0.5, y, w: 2, h: 0.3, fontSize: 14, bold: true, color: NAVY });
    const vs = Object.keys(map);
    const gap = 0.2, w = (9.0 - gap * (vs.length - 1)) / vs.length;
    vs.forEach((v, i) => {
      const x = 0.5 + i * (w + gap);
      const done = vers(act).includes(v);
      pill(s, x, y + 0.38, v, done ? BLUE : MUTED);
      const lib = f1(act, v, "library");
      if (lib != null) T(s, `library ${fmt(lib)}`, { x: x + 0.7, y: y + 0.4, w: w - 0.72, h: 0.3, fontSize: 10, bold: true, color: lib >= TARGET ? BLUE : MUTED, valign: "middle" });
      T(s, map[v] + (done ? "" : " (not yet scored)"), { x, y: y + 0.8, w: w - 0.05, h: 0.85, fontSize: 10, color: INK });
      if (i < vs.length - 1) T(s, "→", { x: x + w - 0.08, y: y + 0.36, w: gap + 0.1, h: 0.36, fontSize: 16, color: ORANGE, align: "center", valign: "middle" });
    });
  });
  T(s, `Chain of thought: ${vers("cot").join(" → ")}, each composed automatically from the current identification and classification prompts.`, { x: 0.5, y: 5.0, w: 9, h: 0.3, fontSize: 11, color: MUTED });
}

// 7-9. Experiments (Hypothesis → Modification → Result)
function experiment(t, sub, hyp, mod, res, bars) {
  const s = content(t, sub);
  const cols = [["Hypothesis", hyp, LIGHT, NAVY, INK], ["Modification", mod, LIGHT, NAVY, INK], ["Result", res, NAVY, ORANGE, WHITE]];
  const w = bars ? 2.0 : 2.85, gap = 0.2;
  cols.forEach(([h, body, fill, hc, bc], i) => {
    const x = 0.5 + i * (w + gap);
    card(s, x, 1.45, w, 3.7, fill);
    T(s, h, { x: x + 0.18, y: 1.6, w: w - 0.36, h: 0.35, fontSize: 15, bold: true, color: hc });
    T(s, body, { x: x + 0.18, y: 2.0, w: w - 0.36, h: 3.05, fontSize: bars ? 11.5 : 13, color: bc });
  });
  if (bars) bars(s, 0.5 + 3 * (w + gap) - 0.05, 1.4, 9.55 - (0.5 + 3 * (w + gap)), 3.8);
  return s;
}
{
  const a = "identification", d0 = DOM.map(([d]) => f1(a, "P0", d)), d1 = DOM.map(([d]) => f1(a, "P1", d));
  experiment("Experiment 1: the course methodology", "Identification P0 → P1",
    "A bare category list gives no definition of \"domain-specific\", so the model lists generic words (low precision) and treats passive verbs, state adjectives and quantities inconsistently.",
    "Added a role, the definition of domain-specific, per-category rules from the revised rules document, the course example, a sentence-by-sentence procedure with a re-scan, and output constraints.",
    `F1 by domain:\n\n${DOM.map(([, n], i) => `${n} ${fmt(d0[i])} → ${fmt(d1[i])} (${sgn(delta(d0[i], d1[i]))})${verdict(delta(d0[i], d1[i]))}`).join("\n")}\n\n${DOM.every((_, i) => delta(d0[i], d1[i]) > HALF) ? "Hypothesis confirmed on all three domains: every gain is larger than run-to-run noise." : "Hypothesis confirmed where the gain exceeds run-to-run noise."}`);
}
{
  const a = "classification", l1 = f1(a, "P1", "library"), l2 = f1(a, "P2", "library");
  experiment("Experiment 2: one naming decision", "Classification P1 → P2",
    "\"Each customer is known as a member\": the model named the class Member. Every attribute and association on that class then missed the expert's Customer, so one word choice cost about 14 errors.",
    "Naming rule: use the name introduced first for a concept. Also: documents are classes, attribute values only for closed lists, and a mandatory association-class check.",
    `Library ${fmt(l1)} → ${fmt(l2)} (${sgn(delta(l1, l2))} points), the largest single gain of the project.\n\nCar rental ${fmt(f1(a, "P1", "car_rental"))} → ${fmt(f1(a, "P2", "car_rental"))}${verdict(delta(f1(a, "P1", "car_rental"), f1(a, "P2", "car_rental")), a)}\nNTSS ${fmt(f1(a, "P1", "ntss"))} → ${fmt(f1(a, "P2", "ntss"))}${verdict(delta(f1(a, "P1", "ntss"), f1(a, "P2", "ntss")), a)}\n\nThe naming cascade was a library problem; the other domains need other fixes.`);
}
{
  const a = "identification";
  const pr = (v, d) => cell(a, v, d);
  experiment("Experiment 3: recall rules have a price", "Identification P1 → P2",
    "P1's misses fell into 9 recurring error classes (verbs after modals, literal X of Y, states written as verbs, abstract nouns ...). One rule per class should raise recall.",
    "Added the 9 inclusion rules and a business-operation-only scope filter; moved every example to neutral domains (hotel, clinic, school).",
    `Recall rose as predicted, but precision fell by about as much, so F1 stayed flat. Several new false positives were created by the new rules themselves (e.g. "new domains", "invited speakers").`,
    (s, x, y, w, h) => {
      const data = [{ name: "Precision", labels: DOM.map(([, n]) => n), values: DOM.map(([d]) => pr("P2", d).p - pr("P1", d).p) },
        { name: "Recall", labels: DOM.map(([, n]) => n), values: DOM.map(([d]) => pr("P2", d).r - pr("P1", d).r) }];
      s.addChart(pres.charts.BAR, data, { x, y, w, h, barDir: "col", chartColors: [ORANGE, BLUE], showValue: true, dataLabelFontSize: 9, dataLabelFormatCode: "+0;-0",
        valAxisLabelFontSize: 9, catAxisLabelFontSize: 10, valGridLine: { color: "E3E8EF", size: 0.75 }, catGridLine: { style: "none" }, showLegend: true, legendPos: "b", legendFontSize: 10,
        showTitle: true, title: "Change P1 → P2 (points)", titleFontSize: 11, titleColor: INK, valAxisLabelColor: MUTED, catAxisLabelColor: INK });
    });
}
if (has("identification", "P3") || has("classification", "P3")) {
  const i2 = DOM.map(([d]) => f1("identification", "P2", d)), i3 = DOM.map(([d]) => f1("identification", "P3", d));
  const c2 = DOM.map(([d]) => f1("classification", "P2", d)), c3 = DOM.map(([d]) => f1("classification", "P3", d));
  const line = (arr0, arr1, act) => DOM.map(([, n], i) => `${n} ${fmt(arr0[i])} → ${fmt(arr1[i])}${verdict(delta(arr0[i], arr1[i]), act)}`).join("\n");
  experiment("Experiment 4: fixing what over-fired", "Identification P2 → P3, classification P2 → P3",
    "Identification: narrowing exactly the P2 rules that over-fired, plus a self-verification pass, recovers precision without losing recall.\n\nClassification: association classes need their association and attributes; subclasses need something of their own.",
    "Identification: noun-noun compounds only, X of Y excludes groups and quantifiers, kinds stay nouns, numbers once, dedupe/scope/category self-check.\n\nClassification: AS + AC + attributes, course inheritance criterion, attach to the class the sentence names.",
    `Identification:\n${line(i2, i3, "identification")}\n\nClassification:\n${line(c2, c3, "classification")}`);
}

// 10-11. Results charts
{
  const s = content("Optimization results: identification", "Mean F1 by prompt version; orange line is the 90% target");
  lineChart(s, "identification", 0.4, 1.35, 5.9, 3.95);
  scoreTable(s, "identification", 6.5, 1.55, 3.0);
  const lib = DOM.map(([d]) => d)[0];
  T(s, `Biggest step: P0 → P1 (course methodology). Cells with repeated runs show the mean (library P0 averages ${cell("identification", "P0", "library").n} runs). Best version on the three-domain mean: ${ID_BEST}.`, { x: 6.5, y: 1.6 + 0.3 * (vers("identification").length + 1) + 0.2, w: 3.0, h: 1.2, fontSize: 11, color: MUTED });
}
{
  const s = content("Optimization results: classification", "Mean F1 by prompt version; orange line is the 90% target");
  lineChart(s, "classification", 0.4, 1.35, 5.9, 3.95);
  scoreTable(s, "classification", 6.5, 1.55, 3.0);
  T(s, `Biggest step: P1 → P2 (naming rule). Car rental stays lowest because the expert renamed attributes (e.g. "transmission" for the text's "gear change"). Best version so far: ${CL_BEST}.`,
    { x: 6.5, y: 1.6 + 0.3 * (vers("classification").length + 1) + 0.2, w: 3.0, h: 1.6, fontSize: 11, color: MUTED });
}

if (has("identification", "P4")) {
  const i3 = DOM.map(([d]) => f1("identification", "P3", d)), i4 = DOM.map(([d]) => f1("identification", "P4", d));
  const c = cell("identification", "P4", "library");
  experiment("Experiment 5: closing the library gap", "Identification P3 → P4",
    "P3 left library 0.1 below 90 with 11 specific errors: split possession clauses, a skipped X of Y inside a generalization, the verb \"kept\", the example value \"French\", and words pulled out of longer phrases.",
    "One rule per error: keep possession clauses whole; one sentence can give rows under several rules; record-keeping verbs are domain verbs; example values are enumeration values; don't split words out of listed phrases.",
    `${DOM.map(([, n], i) => `${n} ${fmt(i3[i])} → ${fmt(i4[i])}${verdict(delta(i3[i], i4[i]))}`).join("\n")}\n\n${c.f1_runs.every((x) => x >= TARGET) && c.n > 1 ? `Library meets the 90% target: every run is above 90 (${c.f1_runs.join(", ")}). The step from P3 is labeled noise only because P3 had a single run.` : `Library ${c.f1 >= TARGET ? "meets" : "does not yet meet"} the 90% target (${c.n > 1 ? "mean of " + c.n + " runs" : "single run"}).`}`);
}

// Research-driven experiments
if (RS || cell("identification", "P4max", "library")) {
  const s = content("Testing what the research recommends", "Two techniques from the domain-modeling literature, tested on our own runs");
  // left: voting
  card(s, 0.5, 1.45, 4.4, 3.05);
  T(s, "Self-consistency voting", { x: 0.7, y: 1.55, w: 4.0, h: 0.3, fontSize: 13.5, bold: true, color: NAVY });
  T(s, "Keep a phrase only if k of n repeated runs list it (suggested by Chen et al. 2023; AbsCon 2025).", { x: 0.7, y: 1.87, w: 4.0, h: 0.45, fontSize: 10, color: MUTED });
  if (RS) {
    const pick = RS.voting.filter((r) => ["P1", "P4"].includes(r.version));
    const rows = [[hdr("Repeated runs"), hdr("Single run"), hdr("Best voting*")],
      ...pick.map((r) => [td(`${r.version} ${DOM.find(([d]) => d === r.domain)[1]} (n=${r.n})`), td(fmt(r.single_f1)), td(fmt(r.vote_f1), { bold: true, color: r.vote_f1 > r.single_f1 + HALF ? BLUE : INK })])];
    s.addTable(rows, { x: 0.7, y: 2.4, w: 4.0, colW: [1.9, 1.0, 1.1], border: { type: "solid", pt: 0.5, color: LINE }, rowH: 0.3, fontSize: 10.5 });
    T(s, "* threshold chosen after seeing the scores, an advantage voting would not have in practice.", { x: 0.7, y: 2.45 + 0.3 * (pick.length + 1) + 0.05, w: 4.0, h: 0.3, fontSize: 9, color: MUTED });
  }
  // right: capability
  card(s, 5.1, 1.45, 4.4, 3.05);
  T(s, "Most capable model, same prompt", { x: 5.3, y: 1.55, w: 4.0, h: 0.3, fontSize: 13.5, bold: true, color: NAVY });
  T(s, "Larger models do better in both papers. Identical final prompts, run on the most capable tier.", { x: 5.3, y: 1.87, w: 4.0, h: 0.45, fontSize: 10, color: MUTED });
  const cap = [["identification", "P4", "P4max", "Identify"], ["classification", "P3", "P3max", "Classify"]];
  const crow = [[hdr("F1 (precision)"), hdr("Default"), hdr("Capable")]];
  for (const [a, v, vm, lab] of cap) for (const [d, n] of DOM) { const c0 = cell(a, v, d), c1 = cell(a, vm, d); if (!c0 || !c1) continue;
    crow.push([td(`${lab} ${n}`), td(`${fmt(c0.f1)} (${Math.round(c0.p)})`), td(`${fmt(c1.f1)} (${Math.round(c1.p)})`, { color: c1.p < c0.p ? "B42318" : BLUE })]); }
  s.addTable(crow, { x: 5.3, y: 2.4, w: 4.0, colW: [1.7, 1.15, 1.15], border: { type: "solid", pt: 0.5, color: LINE }, rowH: 0.27, fontSize: 10 });
  const drops = cap.flatMap(([a, v, vm]) => DOM.map(([d]) => { const c0 = cell(a, v, d), c1 = cell(a, vm, d); return c0 && c1 ? c1.p < c0.p : null; })).filter((x) => x != null);
  card(s, 0.5, 4.62, 9.0, 0.6, NAVY);
  T(s, `Both point the same way. Voting trades recall for precision one-for-one. The stronger model lowered precision in ${drops.filter(Boolean).length} of ${drops.length} cells by listing more genuine domain elements that the sparser expert keys omit: the remaining gap is annotation convention, not model error.`,
    { x: 0.7, y: 4.65, w: 8.6, h: 0.55, fontSize: 10.5, color: WHITE, valign: "middle" });
  s.addNotes("Sources: Chen et al., Automated Domain Modeling with LLMs, MODELS 2023; Chen et al., Accurate and Consistent Graph Model Generation from Text with LLMs (AbsCon), 2025. Capability runs are single runs per cell; the direction (precision down) is consistent across all cells.");
}

// Classification ceiling
{
  const s = content("Why classification stops short of 90%", "The remaining library misses are modeling choices the text does not support");
  const rows = [[hdr("Expert solution"), hdr("What the description says"), hdr("Model output")],
    [td("borrow(customer, book)"), td("\"A customer may borrow up to a maximum of 8 items\""), td("borrow(customer, loan item)")],
    [td("loan item.title"), td("\"A book has a title\""), td("book.title")],
    [td("book.subject"), td("not mentioned"), td("–")],
    [td("hold(section, loan item)"), td("not mentioned"), td("–")],
    [td("membership card.id"), td("\"a unique member number\""), td("membership card.member number")]];
  s.addTable(rows, { x: 0.5, y: 1.45, w: 5.9, colW: [1.9, 2.3, 1.7], border: { type: "solid", pt: 0.5, color: LINE }, rowH: 0.42, valign: "middle" });
  const vbest = "P3";
  const offi = f1("classification", vbest, "library");
  card(s, 6.7, 1.45, 2.8, 3.7, NAVY);
  T(s, "Arguments ignored", { x: 6.9, y: 1.6, w: 2.4, h: 0.3, fontSize: 13, bold: true, color: ORANGE });
  T(s, `Library ${fmt(offi)} → 80.0\nCar rental ${fmt(f1("classification", vbest, "car_rental"))} → 67.7\nNTSS ${fmt(f1("classification", vbest, "ntss"))} → 67.7`, { x: 6.9, y: 2.0, w: 2.45, h: 1.0, fontSize: 13, bold: true, color: WHITE });
  T(s, "Classification P3 scored with the team scorer's no-arguments mode: 11–17 points of the gap are which classes a relationship connects, not missing concepts. Reaching 90 on library would require putting the expert's choices into the prompt, which is leaking the answer.",
    { x: 6.9, y: 3.05, w: 2.45, h: 2.0, fontSize: 10.5, color: PALEBLUE });
  s.addNotes("We stopped iterating classification at P3 on purpose: the evidence shows the remaining gap is annotation choices, not model errors we can fix with general rules.");
}

// 12. AI and human in the loop
{
  const s = content("AI and human in the loop", "Where each improvement came from, and whether it helped");
  const rows = [[hdr("Suggestion"), hdr("Source"), hdr("Effect")],
    [td("Passive verbs, state adjectives, quantifiers, domain-scope filter"), td("AI (Gemini), via the instructor's revised rules"), td(`Identification P1: library ${fmt(f1("identification", "P0", "library"))} → ${fmt(f1("identification", "P1", "library"))}`)],
    [td("Class/attribute tests, category→element mapping, association-class conditions"), td("Course methodology"), td("Classification P1: library false positives 40 → 18")],
    [td("Naming rule for synonyms"), td("AI (Claude) error analysis"), td(`Classification P2: library +${fmt(delta(f1("classification", "P1", "library"), f1("classification", "P2", "library")))}`)],
    [td("Nine error-driven inclusion rules"), td("AI (Claude) error analysis"), td("Recall up, precision down: F1 flat")],
    [td("Baseline classification prompt (t1) and classification scorer"), td("Team"), td("P0 baseline; every classification score")],
    [td("Run all three domains each round; repeat key runs"), td("Team"), td(`Run-to-run spread measured (${NOISE} pts)`)],
    [td("Neutral examples + automated leak check; CamelCase-neutral scoring"), td("AI (Claude) review, team approved"), td("Scores reflect the rules, not leaked answers")]];
  s.addTable(rows, { x: 0.5, y: 1.45, w: 9.0, colW: [3.8, 2.4, 2.8], border: { type: "solid", pt: 0.5, color: LINE }, rowH: 0.42, valign: "middle" });
  s.addNotes("Team: add your own contributions to this table before presenting.");
}

// 13. Integrity
{
  const s = content("Keeping the evaluation honest", "Four decisions that make the scores trustworthy");
  const items = [["Blind model", "Claude only sees the prompt and the business description. The answer keys stay in the repo."],
    ["No leaked examples", "Examples use hotel, clinic and school domains. An automated check found and removed several leaks, including our own."],
    ["Fair scoring", "Names are split on CamelCase for every run, so a naming style can't pass for a modeling improvement."],
    ["Complete ground truth", "Identification keys built from the instructor's documents; the NTSS classification CSV corrected for rows lost in conversion."]];
  items.forEach(([h, b], i) => {
    const x = 0.5 + (i % 2) * 4.6, y = 1.45 + Math.floor(i / 2) * 1.9;
    card(s, x, y, 4.4, 1.7);
    s.addShape(pres.shapes.OVAL, { x: x + 0.2, y: y + 0.22, w: 0.42, h: 0.42, fill: { color: BLUE }, line: { color: BLUE } });
    T(s, String(i + 1), { x: x + 0.2, y: y + 0.22, w: 0.42, h: 0.42, fontSize: 14, bold: true, color: WHITE, align: "center", valign: "middle" });
    T(s, h, { x: x + 0.78, y: y + 0.24, w: 3.4, h: 0.38, fontSize: 15, bold: true, color: NAVY, valign: "middle" });
    T(s, b, { x: x + 0.78, y: y + 0.7, w: 3.45, h: 0.9, fontSize: 11.5, color: INK });
  });
}

// 14. Baseline vs optimized
{
  const s = content("Baseline vs optimized", `P0 compared with the best version (identification ${ID_BEST}, classification ${CL_BEST})`);
  const rows = [[hdr("Activity"), hdr("Domain"), hdr("P0 F1"), hdr("Optimized F1"), hdr("Change"), hdr("Precision"), hdr("Recall")]];
  for (const [a, lab, b] of [["identification", "Identification", ID_BEST], ["classification", "Classification", CL_BEST]])
    DOM.forEach(([d, n], i) => { const c = cell(a, b, d); const p0 = f1(a, "P0", d);
      rows.push([td(i === 0 ? lab : "", { bold: true }), td(n), td(fmt(p0)), td(fmt(c && c.f1), { bold: true, color: c && c.f1 >= TARGET ? BLUE : INK }), td(sgn(delta(p0, c && c.f1)), { color: BLUE, bold: true }), td(fmt(c && c.p)), td(fmt(c && c.r))]); });
  s.addTable(rows, { x: 0.5, y: 1.45, w: 9.0, colW: [1.5, 1.3, 1.1, 1.4, 1.1, 1.3, 1.3], border: { type: "solid", pt: 0.5, color: LINE }, rowH: 0.42, valign: "middle" });
}

// 15. Final optimized prompt
{
  const s = content("Final optimized prompt", `Identification ${ID_BEST} and classification ${CL_BEST}: structure (full text in the repo's prompts folder)`);
  const comps = [["Role", "Domain modeling expert applying AUM, step 2 (identify) or step 3 (classify)"],
    ["Task & definition", "\"Domain-specific\" = needs detail, tracking or rules in the domain, or changes meaning elsewhere"],
    ["Input", "The business description; for classification also the phrase list with rule numbers"],
    ["Methodology", "Per-category rules; category→element mapping; class/attribute and inheritance tests; AC conditions"],
    ["Constraints", "Only phrases in the text, scope filter, naming rule, V only for closed lists"],
    ["Examples", "Course example plus neutral-domain examples only (no test-domain words)"],
    ["Process", "Sentence-by-sentence scan, re-scan, then a self-verification / review checklist"],
    ["Output format", "One markdown table: | rule | phrase | or | label | element | arg1 | arg2 |"]];
  comps.forEach(([h, b], i) => {
    const x = 0.5 + (i % 2) * 4.6, y = 1.45 + Math.floor(i / 2) * 0.93;
    card(s, x, y, 4.4, 0.8);
    T(s, h, { x: x + 0.18, y: y + 0.1, w: 1.35, h: 0.6, fontSize: 12.5, bold: true, color: BLUE, valign: "middle" });
    T(s, b, { x: x + 1.55, y: y + 0.08, w: 2.7, h: 0.66, fontSize: 10.5, color: INK, valign: "middle" });
  });
}

// 16. Chain of thought
{
  const s = content("Chain-of-thought prompt", "One prompt that performs identification and classification step by step");
  const steps = ["1  Identify phrases", "2  Classify each phrase, one-line reason", "3  Review against the checklist", "4  Final domain model"];
  steps.forEach((t, i) => { const x = 0.5 + i * 2.3; card(s, x, 1.45, 2.1, 0.75, i === 3 ? NAVY : LIGHT);
    T(s, t, { x: x + 0.15, y: 1.5, w: 1.85, h: 0.65, fontSize: 12, bold: true, color: i === 3 ? WHITE : NAVY, valign: "middle" }); });
  const cv = COT_BEST;
  const rows = [[hdr("Domain"), hdr(`Identify ${ID_BEST}`), hdr(`CoT ${cv} step 1`), hdr(`Classify ${CL_BEST}*`), hdr(`CoT ${cv} final model`)]];
  DOM.forEach(([d, n]) => { const c = cell("cot", cv, d);
    rows.push([td(n, { bold: true }), td(fmt(f1("identification", ID_BEST, d))), td(fmt(c && c.step1_f1)), td(fmt(f1("classification", CL_BEST, d))), td(fmt(c && c.f1), { bold: true })]); });
  s.addTable(rows, { x: 0.5, y: 2.45, w: 9.0, colW: [1.6, 1.8, 1.8, 1.9, 1.9], border: { type: "solid", pt: 0.5, color: LINE }, rowH: 0.38, valign: "middle" });
  const better = DOM.filter(([d]) => { const c = cell("cot", cv, d); return c && c.step1_f1 - f1("identification", ID_BEST, d) > HALF; }).map(([, n]) => n);
  if (better.length) T(s, `Finding: the chain-of-thought's own Step 1 beat the standalone identification prompt on ${better.join(" and ")}. Reasoning about classification seems to sharpen what counts as domain-specific.`,
    { x: 0.5, y: 4.2, w: 9.0, h: 0.45, fontSize: 11.5, bold: true, color: NAVY });
  T(s, "* Standalone classification receives the expert's phrase list. The chain-of-thought prompt starts from the description alone, so its final model also carries its own Step 1 errors: the fair comparison for the end-to-end task is CoT vs the two standalone prompts chained.",
    { x: 0.5, y: 4.72, w: 9.0, h: 0.55, fontSize: 10, color: MUTED });
}

// 17. Generalization
{
  const s = content("Result generalization", "Best prompts on all three inputs");
  const rows = [[hdr(""), ...DOM.map(([, n]) => hdr(n))]];
  for (const [a, lab, b] of [["identification", "Identification", ID_BEST], ["classification", "Classification", CL_BEST], ["cot", "Chain of thought (final model)", COT_BEST]]) {
    rows.push([td(`${lab} ${b}`, { bold: true, fill: { color: LIGHT } }), ...DOM.map(() => td("", { fill: { color: LIGHT } }))]);
    for (const [k, kl] of [["p", "Precision"], ["r", "Recall"], ["f1", "F1"]])
      rows.push([td("   " + kl), ...DOM.map(([d]) => { const c = cell(a, b, d); const v = c ? c[k] : null; return td(fmt(v), { bold: k === "f1", color: k === "f1" && v != null && v >= TARGET ? BLUE : INK }); })]);
  }
  s.addTable(rows, { x: 0.5, y: 1.4, w: 9.0, colW: [3.0, 2.0, 2.0, 2.0], border: { type: "solid", pt: 0.5, color: LINE }, rowH: 0.29, valign: "middle", fontSize: 10.5 });
}

// 18. Lessons learned
{
  const s = content("Lessons learned", "Findings from our runs, not general claims");
  const l = [
    ["One naming decision beat many rules", `The classification naming rule alone gave +${fmt(delta(f1("classification", "P1", "library"), f1("classification", "P2", "library")))} points on library, the largest single gain.`],
    ["Inclusion rules trade precision for recall", "Identification P2 raised NTSS recall to 97% but cut precision about 10 points, leaving F1 flat."],
    ["Noise is larger than many improvements", `The same prompt varied by up to ${NOISE} points on identification${noiseBy.classification ? `, ${Math.round(noiseBy.classification)} on classification` : ""}${noiseBy.cot ? ` and ${Math.round(noiseBy.cot)} on chain of thought` : ""}, so we averaged repeated runs before claiming a gain.`],
    ["Expert conventions cap the score", "Library's key is exhaustive, car rental's sparse: it omits \"rent\", the core verb of a rental company. Matching sparse keys or renamed attributes without leaking answers has a ceiling."],
    (cell("identification", "P4max", "ntss") ? ["A more capable model scored lower", `Same prompt on the most capable tier: NTSS identification ${fmt(f1("identification", "P4", "ntss"))} → ${fmt(f1("identification", "P4max", "ntss"))}. It was more thorough, and sparse keys count thoroughness as false positives.`]
      : ["Examples from the test texts leak answers", "Our own drafts reused test phrases; an automated check against every expert phrase caught them."])];
  l.forEach(([h, b], i) => {
    const y = 1.3 + i * 0.82;
    s.addShape(pres.shapes.OVAL, { x: 0.5, y: y + 0.08, w: 0.42, h: 0.42, fill: { color: i === 0 ? ORANGE : BLUE }, line: { color: i === 0 ? ORANGE : BLUE } });
    T(s, String(i + 1), { x: 0.5, y: y + 0.08, w: 0.42, h: 0.42, fontSize: 14, bold: true, color: WHITE, align: "center", valign: "middle" });
    T(s, h, { x: 1.1, y, w: 8.4, h: 0.3, fontSize: 13.5, bold: true, color: NAVY });
    T(s, b, { x: 1.1, y: y + 0.3, w: 8.4, h: 0.45, fontSize: 11, color: INK });
  });
}

// 19. Conclusion
{
  const s = content("Conclusion & future work");
  const [libIdV, libId] = bestDom("identification", "library"), [libClV, libCl] = bestDom("classification", "library");
  const met = (x) => (x != null && x >= TARGET ? "met" : "not yet met");
  card(s, 0.5, 1.2, 4.4, 3.95, NAVY);
  T(s, "Did we reach the goal?", { x: 0.7, y: 1.35, w: 4, h: 0.35, fontSize: 15, bold: true, color: ORANGE });
  bullets(s, [
    `Library identification: best ${fmt(libId)} F1 (${libIdV}); target 90 ${met(libId)}.`,
    `Library classification: best ${fmt(libCl)} F1 (${libClV}), ${met(libCl)}; up from ${fmt(f1("classification", "P0", "library"))} at P0.`,
    (() => { const ups = [], flat = [];
      for (const [a, lab, b] of [["identification", "identification", ID_BEST], ["classification", "classification", CL_BEST], ["cot", "chain of thought", COT_BEST]])
        for (const [d, n] of DOM) { const dd = delta(f1(a, "P0", d), f1(a, b, d)); (dd > halfOf(a) ? ups : flat).push(`${lab} on ${n}`); }
      const down = [];
      for (const [a, lab, b] of [["identification", "identification", ID_BEST], ["classification", "classification", CL_BEST], ["cot", "chain of thought", COT_BEST]])
        for (const [d, n] of DOM) { const dd = delta(f1(a, "P0", d), f1(a, b, d)); if (dd < -halfOf(a)) down.push(`${lab} on ${n} (${sgn(dd)})`); }
      return (flat.length ? `Gains beyond noise in ${ups.length} of 9 activity-domain pairs; no clear gain on ${flat.join(", ")}.` : "Every activity improved beyond noise on every domain.")
        + (down.length ? ` Declined: ${down.join(", ")}.` : ""); })(),
  ], { x: 0.7, y: 1.8, w: 4.0, h: 3.2, fontSize: 12, color: WHITE });
  T(s, "Next", { x: 5.2, y: 1.2, w: 4.3, h: 0.35, fontSize: 15, bold: true, color: BLUE });
  bullets(s, [
    `Repeat the NTSS identification run: ${fmt(f1("identification", ID_BEST, "ntss"))} is inside the noise band around 90.`,
    "Ask the instructor how car rental's sparser key and the classification modeling choices were decided, then encode those conventions as rules.",
    "With the instructor's approval, leave-one-out few-shot: show the other two domains' expert annotations to teach the conventions.",
    "Automate the loop with the team's LangGraph notebook (classify → score → optimize).",
  ], { x: 5.2, y: 1.6, w: 4.3, h: 3.5, fontSize: 11.5 });
}

// 20. Questions
dark("Questions?", "Team Four  ·  prompts, scorers, responses and changelog are in the team repo");

pres.writeFile({ fileName: OUT }).then((f) => console.log("wrote", f));
