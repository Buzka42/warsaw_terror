# Patryk's idea (2026-11-27): OSINT for border-segment comparison

**Challenge 3** — transnational crime / smuggling.

An OSINT tool for comparing selected segments of the Polish border
across a chosen timeframe. Goal: detecting new illegal border crossings,
smuggling paths, etc.

Draft pipeline (to refine at aggregation):
- Sentinel-1 SAR (CDSE/openEO): backscatter/coherence change on the
  selected segment between dates — new footpaths, forest clearings,
  makeshift footbridges.
- Sentinel-2 (optical, when cloud-free): visual confirmation,
  trampling/BSI indicators, vehicle tracks.
- User input: segment polygon + date range → output: ranked list of
  "hot" cells with change + mini-report (what, where, when).
- Output is a patrol/analyst lead, not a map.

Aggregation note: check overlap with TorGuard (Qwen),
CorridorGuard (Neon) and balonowy-radar — same change-detection family,
different target (foot crossings and paths vs rail / linear
infrastructure / balloons).
