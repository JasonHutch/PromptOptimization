#!/usr/bin/env python3
"""Create an SVG trial-by-trial F1 graph for the original P4 Gemma run."""

from __future__ import annotations

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
INPUT = ROOT / "gemma-2_run3/p4_identification/summary.json"
OUTPUT = ROOT / "gemma-2_run3/p4_identification/p4_gemma-2_f1.svg"
DOMAINS = ("library", "car_rental", "ntss")
COLORS = {"library": "#2563eb", "car_rental": "#16a34a", "ntss": "#9333ea"}


def main() -> None:
    rows = json.loads(INPUT.read_text(encoding="utf-8"))
    width, height = 900, 500
    left, top, plot_w, plot_h = 75, 70, 760, 330
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#f8fafc"/>',
        '<text x="450" y="30" text-anchor="middle" font-size="21" font-weight="bold">Gemma 2 trial-by-trial F1 - P4 Identification Run</text>',
        '<text x="450" y="51" text-anchor="middle" font-size="12" fill="#475569">Original P4 prompt · 10 trials per domain · dashed line = 97% target</text>',
    ]
    for value in (0, 25, 50, 75, 97, 100):
        y = top + plot_h - value / 100 * plot_h
        svg.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left + plot_w}" y2="{y:.1f}" stroke="#e2e8f0"/>')
        svg.append(f'<text x="{left - 10}" y="{y + 4:.1f}" text-anchor="end" font-size="10">{value}</text>')
    target_y = top + plot_h - 0.97 * plot_h
    svg.append(f'<line x1="{left}" y1="{target_y:.1f}" x2="{left + plot_w}" y2="{target_y:.1f}" stroke="#f97316" stroke-dasharray="5,4"/>')
    svg.append(f'<text x="{left + plot_w - 3}" y="{target_y - 5:.1f}" text-anchor="end" font-size="10" fill="#ea580c">97%</text>')
    svg.append(f'<line x1="{left}" y1="{top + plot_h}" x2="{left + plot_w}" y2="{top + plot_h}" stroke="#334155"/>')
    svg.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top + plot_h}" stroke="#334155"/>')
    for domain in DOMAINS:
        domain_rows = sorted((r for r in rows if r["domain"] == domain), key=lambda r: r["trial"])
        points = []
        for row in domain_rows:
            x = left + (row["trial"] - 1) / 9 * plot_w
            y = top + plot_h - row["score"]["f1"] * plot_h
            points.append((x, y))
        svg.append(f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in points)}" fill="none" stroke="{COLORS[domain]}" stroke-width="2.5"/>')
        for x, y in points:
            svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{COLORS[domain]}"/>')
    for trial in range(1, 11):
        x = left + (trial - 1) / 9 * plot_w
        svg.append(f'<text x="{x:.1f}" y="{top + plot_h + 18}" text-anchor="middle" font-size="10">{trial}</text>')
    svg.append(f'<text x="{left + plot_w / 2}" y="{height - 18}" text-anchor="middle" font-size="12">Trial</text>')
    for i, domain in enumerate(DOMAINS):
        x = 280 + i * 150
        label = domain.replace("_", " ").title()
        svg.append(f'<line x1="{x}" y1="{height - 42}" x2="{x + 22}" y2="{height - 42}" stroke="{COLORS[domain]}" stroke-width="3"/>')
        svg.append(f'<text x="{x + 29}" y="{height - 38}" font-size="11">{label}</text>')
    svg.append("</svg>")
    OUTPUT.write_text("\n".join(svg), encoding="utf-8")
    print(OUTPUT)


if __name__ == "__main__":
    main()
