#!/usr/bin/env python3
"""Create an SVG trial-by-trial F1 graph from a Gemma run summary."""

from __future__ import annotations

import csv
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
INPUT = ROOT / "gemma-2_run1/runs/trial_summary.csv"
OUTPUT = ROOT / "gemma-2_run1/gemma-2_run1_f1.svg"
STRATEGIES = ("baseline", "cot", "meta", "few_shot")
DOMAINS = ("car_rental", "library", "ntss")
COLORS = {"baseline": "#2563eb", "cot": "#16a34a", "meta": "#dc2626", "few_shot": "#9333ea"}


def panel(rows: list[dict], x: int, y: int, title: str) -> str:
    width, height = 250, 180
    left, top, plot_w, plot_h = x + 38, y + 30, 195, 125
    out = [f'<rect x="{x}" y="{y}" width="{width}" height="{height}" fill="white" stroke="#cbd5e1"/>']
    out.append(f'<text x="{x + width / 2}" y="{y + 18}" text-anchor="middle" font-size="13" font-weight="bold">{html.escape(title)}</text>')
    for value in (0, 25, 50, 75, 97, 100):
        py = top + plot_h - value / 100 * plot_h
        out.append(f'<line x1="{left}" y1="{py:.1f}" x2="{left + plot_w}" y2="{py:.1f}" stroke="#e2e8f0"/>')
        out.append(f'<text x="{left - 6}" y="{py + 4:.1f}" text-anchor="end" font-size="9">{value}</text>')
    target_y = top + plot_h - 0.97 * plot_h
    out.append(f'<line x1="{left}" y1="{target_y:.1f}" x2="{left + plot_w}" y2="{target_y:.1f}" stroke="#f97316" stroke-dasharray="4,3"/>')
    out.append(f'<text x="{left + plot_w - 2}" y="{target_y - 3:.1f}" text-anchor="end" font-size="8" fill="#ea580c">97%</text>')
    out.append(f'<line x1="{left}" y1="{top + plot_h}" x2="{left + plot_w}" y2="{top + plot_h}" stroke="#334155"/>')
    out.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top + plot_h}" stroke="#334155"/>')
    for strategy in STRATEGIES:
        values = sorted((r for r in rows if r["strategy"] == strategy), key=lambda r: int(r["trial"]))
        points = []
        for r in values:
            px = left + (int(r["trial"]) - 1) / 9 * plot_w
            py = top + plot_h - float(r["f1"]) * 100 * plot_h / 100
            points.append(f"{px:.1f},{py:.1f}")
        out.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{COLORS[strategy]}" stroke-width="1.8"/>')
        for point in points:
            px, py = point.split(",")
            out.append(f'<circle cx="{px}" cy="{py}" r="2.2" fill="{COLORS[strategy]}"/>')
    out.append(f'<text x="{left + plot_w / 2}" y="{y + height - 7}" text-anchor="middle" font-size="9">trial</text>')
    return "\n".join(out)


def main() -> None:
    rows = list(csv.DictReader(INPUT.open(encoding="utf-8")))
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="1060" height="850" viewBox="0 0 1060 850">']
    svg.append('<rect width="100%" height="100%" fill="#f8fafc"/>')
    svg.append('<text x="530" y="28" text-anchor="middle" font-size="20" font-weight="bold">Gemma 2 trial-by-trial F1 — Baseline Run</text>')
    svg.append('<text x="530" y="49" text-anchor="middle" font-size="12" fill="#475569">P0 baseline and prompt strategies · 10 trials · dashed line = 97% target</text>')
    for row, activity in enumerate(("identification", "classification")):
        y = 65 + row * 390
        svg.append(f'<text x="20" y="{y + 15}" font-size="16" font-weight="bold">{activity.title()}</text>')
        for i, domain in enumerate(DOMAINS):
            svg.append(panel([r for r in rows if r["activity"] == activity and r["domain"] == domain], 35 + i * 270, y + 25, domain.replace("_", " ").title()))
    legend_y = 835
    for i, strategy in enumerate(STRATEGIES):
        x = 310 + i * 135
        svg.append(f'<line x1="{x}" y1="{legend_y}" x2="{x + 22}" y2="{legend_y}" stroke="{COLORS[strategy]}" stroke-width="3"/>')
        svg.append(f'<text x="{x + 28}" y="{legend_y + 4}" font-size="11">{strategy}</text>')
    svg.append("</svg>")
    OUTPUT.write_text("\n".join(svg), encoding="utf-8")
    print(OUTPUT)


if __name__ == "__main__":
    main()
