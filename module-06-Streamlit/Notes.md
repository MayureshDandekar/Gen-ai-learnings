# Module 6 — Streamlit

## Core mental model
Every widget interaction reruns the **entire script top to bottom**. There's no
partial update — Streamlit just re-executes the file. This explains almost
every "weird" behavior you'll hit:
- A calculation with no `if` guard runs on *every* rerun, not just when its
  button is clicked. Fine for cheap math; a real problem for slow/expensive
  calls (API calls, big loops) — costs time and money on every keystroke
  elsewhere on the page.
- `st.button()` only returns `True` for the one rerun triggered by that exact
  click. Move any other widget → it resets to `False`. Nothing "stays clicked"
  on its own. (Fix for later: `st.session_state` — not covered/allowed this
  assignment, but this is the exact problem it solves.)

## Widget basics
| Component | What it does |
|---|---|
| `st.title` / `st.header` / `st.subheader` | Page/section headings, different sizes |
| `st.write` | Prints text/values inline, no visual weight |
| `st.metric(label, value)` | Big bold number + small label — for ONE highlighted number (KPI-style) |
| `st.button(label)` | Returns `True` only on the rerun it was clicked |
| `st.text_input(label)` | Returns current string, persists across reruns on its own |
| `st.slider(label, min, max, default)` | Returns current numeric value |
| `st.selectbox(label, [options])` | Dropdown, returns the picked string |
| `st.checkbox(label)` | Returns `True`/`False` |
| `st.success` / `st.warning` | Colored feedback boxes (green/yellow) |
| `st.table(dict_or_list)` | Renders tabular data, no pandas required |
| `st.bar_chart(data)` | Give it labeled columns (`x=`, `y=`) or it defaults to numeric index labels |

**Gotcha:** the first argument to almost every widget is called `label` in the
docs — that's the *parameter name*, not something you type literally. It's
"what text should the user see," always your own descriptive string.

## Sidebar
`st.sidebar.<anything>` — identical to the main-page version, just renders in
the left panel instead. Use it for settings/inputs that should stay visible
and separate from main content (forms, filters) — not for content that's core
to the page's main flow.

## Validation pattern (used across all 4 assignment tasks)
```python
if value:              # False for "", 0, None
    ...
else:
    st.warning(...)
```
Applies the same way whether `value` is a text input, a price, or a name —
Python truthiness, not Streamlit-specific.

## Dicts as a data source (no pandas needed)
```python
sales = {"January": 1200, "February": 1500, ...}
sales[selected_month]          # lookup one value
list(sales.values())           # just the numbers
list(sales.keys())             # just the labels
```

## Dev environment notes (Mac-specific)
- Command Prompt / PowerShell are Windows-only — zsh/bash are the Mac
  equivalents, not something separately installed.
- Open VS Code at the `Gen-Ai` **root** folder (not a subfolder) so the shared
  venv auto-activates — opening a subfolder directly breaks detection.
- `(venv)` prefix in the terminal prompt = active. No prefix = not active,
  don't run pip/python yet.
- Autocomplete/Copilot suppresses writing your own logic — disabled
  deliberately while still building fluency.

## Assignment 8 — Streamlit Basic App Building
All 4 tasks completed: basic greeting app, price calculator (rounding +
validation), sidebar product form, mini sales dashboard (metric + bar chart).
Restrictions followed: no sessions, no AI-written code, no APIs/DBs.