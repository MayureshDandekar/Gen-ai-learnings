# Module 7 — NumPy for GenAI (RAG math) — Revision Notes

Scope: arrays, vectorized operations, the math behind embeddings/cosine similarity, statistical functions, axis. Built for Assignment 9 (overview, formulas, math operations, statistical functions).

---

## 1. ndarray vs Python list

**Why NumPy exists at all:** a Python `list` is scattered pointers to arbitrary objects. A NumPy `array` (`ndarray`) is one contiguous block of same-type numbers in memory — that's *why* operations on it run fast (compiled C, not a Python loop).

```python
import numpy as np

arr = np.array([10, 20, 30, 40])
print(arr.shape)   # (4,)  -- always a tuple, even for 1D. Not the same as len().
print(arr.dtype)   # int64 -- every element shares ONE type
```

**Doubt I had — why did `np.array([1, 2, "three"])` give `<U21`?**
Every element in an array must share one dtype. Mixing an int and a string forces NumPy to upgrade the *whole array* to the most general type that can hold everything — a number can be written as a string, but not the reverse, so everything becomes string (`<U21` = little-endian, Unicode string, up to 21 chars). Rule to keep: **one weak-typed element pulls the whole array up to the most general common type.** Mixed-type arrays are usually a bug signal, not something to do on purpose.

**Naming convention flagged:** keep array variable names consistently snake_case (`arr_2d`, not `arr_2D`).

---

## 2. Vectorized operations & broadcasting

**Trigger:** any time you'd write `for x in list: result.append(...)` on numbers — that's the smell, use an array instead.

```python
prices = np.array([100, 200, 300])
discounted = prices * 0.9   # applied to every element, no loop
```

**Scalar** = a single plain number (no direction, no multiple values) — `0.9` above. **Broadcasting** = what happens when a scalar meets an array: NumPy applies it to every position without literally copying it in memory.

**Doubt I had — is `a * b` the same as dot product?**
No. `a * b` is **elementwise** — multiplies position-by-position, stays the same shape, no combining.
`np.dot(a, b)` = elementwise multiply, **then sum** everything into one number.
This matters because cosine similarity needs one single score out — `*` alone can never give you that, `dot` can, because the "sum" step is what collapses many dimensions into one verdict.

```python
a = np.array([1,2,3]); b = np.array([10,20,30])
a * b          # [10, 40, 90]  -- 3 numbers
np.dot(a, b)   # 140           -- 1 number (10+40+90)
```

---

## 3. The RAG math — dot product, magnitude, cosine similarity

**Chunk** = a small piece of a document (a document gets split into many chunks before embedding). **Query** = what the user typed, embedded at search time. RAG's whole job: compare 1 query vector against every chunk vector, find the closest direction.

**Magnitude (norm) — math prerequisite:**
Just Pythagoras, generalized: `√(x² + y² + ...)`. For vector `(3,4)`: `√(9+16) = √25 = 5`. This is the vector's length, one number, regardless of direction. `np.linalg.norm(arr)` computes this for any number of dimensions.

**Doubt I had — why divide by the norms at all?**
Raw dot product mixes two things into one number: *how aligned* the vectors are AND *how big* they are. A vector that's just bigger in magnitude can win on raw dot product even when it points in a worse direction. Concrete proof:
```python
query   = np.array([1, 0])
chunk_A = np.array([0.9, 0.1])   # small, nearly same direction
chunk_B = np.array([3, 2])       # big, more off-angle

np.dot(query, chunk_A)   # 0.9
np.dot(query, chunk_B)   # 3.0   <- looks like the winner, but direction-wise it's worse
```
Dividing by both norms cancels magnitude out and leaves only direction — ranking flips back to correct (`chunk_A` wins).

**Cosine similarity — the full formula (write this version for the assignment):**
```python
def cosine_similarity(a, b):
    dot_product = np.dot(a, b)
    magnitude_a = np.linalg.norm(a)
    magnitude_b = np.linalg.norm(b)
    return dot_product / (magnitude_a * magnitude_b)
```
**Gotcha I hit — operator precedence bug:** `dot_product / magnitude_a * magnitude_b` is NOT the same as `dot_product / (magnitude_a * magnitude_b)`. `/` and `*` have equal precedence, evaluated strictly left-to-right, so without parentheses you end up *multiplying* by the second magnitude instead of dividing — silently wrong output, no error thrown, still lands in a semi-plausible range. **Always parenthesize a division that's meant to apply to a whole group of terms.**

Range: `1` = same direction (identical meaning), `0` = perpendicular (unrelated), `-1` = opposite direction. Every "relevance score" from a vector DB is this number.

**Normalizing a vector** — divide every element by its own magnitude:
```python
v = np.array([3, 4])
norm_v = v / np.linalg.norm(v)   # (0.6, 0.8) -- same direction, magnitude now exactly 1
```
Once both vectors have magnitude 1, `(‖a‖ · ‖b‖) = 1`, so `dot(a, b)` alone **is** the cosine similarity — no division needed. Real speed win: normalize each embedding **once** when the index is built, then every future query only needs a plain dot product against it — not a fresh norm calculation per search. For this course: still write the **full** formula (safe default, correct regardless of whether inputs are pre-normalized); only skip the norm step once you've explicitly verified (`np.linalg.norm() ≈ 1.0`) that your specific embeddings are pre-normalized.

**Scaling to many chunks at once (no loop) — beyond Assignment 9, but where this is headed:**
```python
chunks_matrix = np.array([[0.9, 0.1, 0.0], [0.1, 0.9, 0.0], [0.85, 0.2, 0.1]])
query = np.array([0.88, 0.15, 0.05])

dot_products = chunks_matrix @ query                      # one dot product per row, all at once
chunk_norms  = np.linalg.norm(chunks_matrix, axis=1)       # one norm per chunk (axis=1 erases the per-chunk dimension columns)
similarities = dot_products / (chunk_norms * np.linalg.norm(query))
best_index   = np.argmax(similarities)
```

---

## 4. Statistical functions

**Trigger:** sanity-checking a pipeline — is data normalized, are similarity scores spread out or bunched, does the embedding output look sane.

```python
sample = np.array([4, 9, 2, 9, 6])

sample.mean()      # average — one float
np.median(sample)  # sorted, middle value — one float, resistant to outliers
sample.std()       # average distance from the mean — spread/bunched signal
sample.var()       # std squared — mostly an intermediate value
sample.min()/.max() # smallest/largest actual value — catches broken pipeline output (nan, absurd numbers)
sample.argmax()    # returns an INDEX, not a value — "which chunk won", not "what score won"
```

**Doubt I had — mean vs median, when do they diverge and why care?**
```
scores = [0.85, 0.81, 0.79, 0.83, 0.02]
mean   = 0.66   <- dragged down by the one outlier, doesn't represent the typical chunk
median = 0.81   <- unbothered by the outlier, genuinely representative
```
A big mean/median gap is itself a diagnostic — it means the data is skewed by something worth investigating, before trusting either number blindly.

**Doubt I had — min/max vs argmax, don't merge these:**
`min()`/`max()` on **one vector's own values** → health check on that single vector only (is my embedding's numbers sane, or full of `nan`/huge outliers). `argmax()` on the **array of similarity scores** (one score per chunk) → finds which chunk won, by index. Different arrays, different jobs — don't conflate "biggest number in a vector" with "which chunk matched best."

---

## 5. Axis — the rule that actually works

Spatial language ("direction", "walking down/across") kept causing mix-ups. The rule that works, no spatial reasoning required:

**The axis number you pass is the position in `.shape` that gets erased/deleted. Whatever's left over defines your answer's shape.**

```python
grid = np.array([[1,2,3],[4,5,6]])
print(grid.shape)               # (2, 3)  -- position 0 = rows, position 1 = columns
print(grid.mean(axis=0).shape)  # (3,)    -- position 0 (row count, 2) erased, column count survives
print(grid.mean(axis=1).shape)  # (2,)    -- position 1 (column count, 3) erased, row count survives
```

`axis=0` is permanently the row axis, `axis=1` is permanently the column axis — this is fixed, not something to re-derive. Erasing an axis means: every value along that axis gets *combined into one number* by whichever function you called. You're not deleting data, you're compressing it into a summary because you don't need each individual value anymore.

```python
data = np.array([[10, 20, 30], [40, 50, 60]])
data.mean(axis=0)   # [25. 35. 45.] -- averages DOWN each column (row values merged, one result per column)
data.mean(axis=1)   # [25. 50.]     -- averages ACROSS each row (column values merged, one result per row)
```

**RAG relevance:** in a chunks × dimensions embedding matrix, `axis=0` collapses across all chunks — gives you one number per dimension (e.g. an "average embedding" across a whole cluster of chunks). This is the axis you'll reach for far more often in real work.

**Two things I got backwards while learning this — worth remembering the mistake, not just the fix:**
- Rows run left-to-right (horizontal), columns run top-to-bottom (vertical) — I had this reversed once.
- `axis=1` on a `(2,3)` grid erases the *column* count (3) and leaves 2 results (one per row) — not the other way around. Always check `.shape` before and after instead of trusting memory on which number means what.

---

## 6. `np.zeros` / `np.ones` / `_like`

**Trigger:** need an array of known size *before* real values exist — a placeholder to fill in later, not real data.

```python
np.zeros(5)          # [0. 0. 0. 0. 0.] -- defaults to float64
np.ones((2, 3))      # 2 rows, 3 columns, all ones
np.zeros(5, dtype=int)
```

`zeros_like(arr)` / `ones_like(arr)` — copies both **shape and dtype** from an existing array, no hardcoded size typed by hand.

```python
real_data = np.array([1, 2, 3, 4, 5, 6])   # int64
placeholder = np.zeros_like(real_data)
placeholder.dtype   # int64 -- matches real_data, NOT float64 like plain zeros() would
```

**Doubt I had — why does this matter over plain `zeros()`?**
Plain `zeros(6)` defaults to `float64` regardless of what `real_data`'s actual dtype is — a silent int/float mismatch that doesn't crash, just quietly produces wrong results somewhere downstream. `zeros_like` eliminates that entirely since shape *and* dtype both come from the real data, never typed by hand.

---

## 7. `astype()`

**Trigger:** dtype doesn't match what an operation needs, or you want to shrink memory (real embeddings default to `float32`, not `float64`).

```python
arr = np.array([1, 2, 3])
arr_float = arr.astype(float)   # returns a NEW array
```

**Gotcha — does NOT modify in place.** Must reassign: `arr = arr.astype(float)`, or the original is untouched.

**Gotcha — float → int truncates, does not round.**
```python
np.array([1.9, 2.7, 3.2]).astype(int)   # [1, 2, 3] -- NOT [2, 3, 3]
```

**Doubt I had — int/bool conversion rule?**
`0` → `False`. Any non-zero number, positive *or* negative, → `True`. Not about sign — only about zero vs non-zero.
```python
np.array([1, 0, -5]).astype(bool)   # [True, False, True]
```

---

## 8. Matrix multiplication shape rule

**Doubt I had — got the rule backwards at first.** It's NOT "rows of first = columns of second." Correct rule: **columns of the first matrix must equal rows of the second matrix.**

```python
A = np.array([[1,2,3],[4,5,6]])     # shape (2,3)
B = np.array([[1,0],[0,1],[1,1]])   # shape (3,2)
(A @ B).shape   # (2,2)
```

**Why:** each output value is a plain dot product between one row of `A` and one column of `B` — a dot product needs matching lengths (the shared `n`), and always collapses to one number, so that shared dimension disappears from the result.

**Resulting shape = (rows of first, columns of second)** — the two matching numbers vanish; the two outer numbers survive, in order.
```
(4, 5) @ (5, 3) -> (4, 3)
```
Order matters — `A @ B ≠ B @ A` generally, not reversible like regular multiplication. A vector is just a special-case matrix with one dimension collapsed — `chunks_matrix @ query` from section 3 is this exact rule with `query` as a `(3,)` vector.

---

## 9. 3D arrays — same rules, one more axis

**Correction I needed:** NumPy has no "x/y/z axis" naming. It's the same numbered system as 2D, just with a third slot: `axis=0`, `axis=1`, `axis=2`.

Shape goes from `(rows, columns)` to `(blocks, rows, columns)` — one extra number in front.

```python
arr3d = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])
arr3d.shape        # (2, 2, 2) -- 2 blocks, 2 rows, 2 columns each
arr3d[0]           # entire first block (a full 2D matrix)
arr3d[0, 1]        # row 1 inside block 0
arr3d[0, 1, 0]     # single number: block 0, row 1, column 0
```

Axis-erasure rule extends unchanged: `axis=0` erases the block count (blends *across* blocks together), `axis=1` erases rows within each block (blocks stay separate), `axis=2` erases columns within each block (blocks stay separate).

**Doubt I had — kept assuming `axis=0` meant "column-wise" like in 2D.** Wrong — 2D's row/column labels don't carry over. `axis=0` is just "whatever sits at position 0 in `.shape`, for *this* array" — in 3D that's blocks, not columns. Never trust a fixed row/column label; always re-check `.shape` for the array actually in front of you.

**Forward-relevant, not needed yet:** deep learning batches data as shape `(batch_size, sequence_length, embedding_dim)` — same 3-number shape, same indexing, same axis rule, just bigger numbers, later in the course.

---

## 10. `np.vstack` / `np.hstack`

**Trigger:** several separate arrays need to become one — exactly how `chunks_matrix` gets built for real: an embedding model hands you one chunk's vector at a time, and you stack each new one onto the growing pile as it arrives, instead of hand-typing one big nested list.

```python
e1 = np.array([0.9, 0.1, 0.0])
e2 = np.array([0.1, 0.9, 0.0])
e3 = np.array([0.85, 0.2, 0.1])

np.vstack([e1, e2, e3])   # shape (3, 3) -- stacks as new ROWS, one on top of another. Needs matching column counts.
np.hstack([e1, e2])       # length 6 -- joins end-to-end, side by side. Needs matching row counts.
```

## 11. Concatenate — the actual joining logic

**Doubt I had — on what basis do the two matrices actually combine?** It's different depending on the axis.

**`axis=0` (stacking more rows):** no real pairing happens — whole rows are placed one after another, in the order given. First array's rows, then second array's rows appended below. No values blend together; it's pure sequential placement. Matching column counts is required only so each column position keeps the same meaning across both arrays.

**`axis=1` (stacking more columns):** this one genuinely pairs by position. Row `i` of the first array joins with row `i` of the second array to form one longer row — real index-matching, not just stacking. This is exactly why row counts must match: every row needs a same-index row on the other side to attach to.

```python
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

np.concatenate([A, B], axis=0)   # [[1,2],[3,4],[5,6],[7,8]] -- A's rows, then B's rows, in order
np.concatenate([A, B], axis=1)   # [[1,2,5,6],[3,4,7,8]]      -- row0+row0, row1+row1, paired by index
```

## 12. Split — NOT a joining operation, don't confuse with concatenate

**Correction I needed:** split only ever takes **one** array as input, never two. There's no pairing logic involved, because there's nothing to pair against. It just slices one array into consecutive ordered pieces — first segment of elements to piece 1, next segment to piece 2, and so on — pure positional cutting, no second array in the picture.

```python
arr = np.array([1,2,3,4,5,6])
np.split(arr, 3)   # [array([1,2]), array([3,4]), array([5,6])] -- one array, cut into 3 ordered chunks
```

Returns a **list** of separate arrays (not one merged array) — index into it (`pieces[0]`) to get a single piece back.

`np.split` demands the array divide evenly into equal pieces, or it errors. `np.array_split` handles leftovers gracefully instead — useful for real, unevenly-sized batches (e.g. splitting 217 chunk embeddings into 5 upload batches for a vector DB's API).
```python
np.array_split(np.array([1,2,3,4,5,6,7]), 3)   # [array([1,2,3]), array([4,5]), array([6,7])]
```

`np.vsplit(grid, n)` / `np.hsplit(grid, n)` are the 2D versions — splitting by row or by column, mirror image of `vstack`/`hstack`.

---

## Formula cheat-sheet

| Concept | Math | NumPy |
|---|---|---|
| Mean | (Σxᵢ) / n | `arr.mean()` |
| Median | middle value, sorted | `np.median(arr)` |
| Variance | Σ(xᵢ − mean)² / n | `arr.var()` |
| Std deviation | √variance | `arr.std()` |
| Vector magnitude (norm) | √Σ(xᵢ²) | `np.linalg.norm(arr)` |
| Dot product | Σ(aᵢ · bᵢ) | `np.dot(a, b)` or `a @ b` |
| Cosine similarity | dot(a,b) / (‖a‖ · ‖b‖) | write it out — no built-in |
| Normalized vector | v / ‖v‖ | `v / np.linalg.norm(v)` |
| Placeholder array | — | `np.zeros(n)` / `np.ones(n)` |
| Shape+dtype-matched placeholder | — | `np.zeros_like(arr)` |
| Type conversion | — | `arr.astype(dtype)` |
| Matrix multiply shape rule | (m×n) @ (n×p) → (m×p) | `A @ B` or `np.dot(A, B)` |
| Stack as new rows | — | `np.vstack([a, b])` |
| Stack side by side | — | `np.hstack([a, b])` |
| Join along a chosen axis | — | `np.concatenate([a, b], axis=n)` |
| Cut into equal pieces (list out) | — | `np.split(arr, n)` / `np.array_split` for uneven |

---

## Self-check questions (answer without looking back)

1. Why does `np.array([1, 2, "three"])` end up as a string array instead of throwing an error?
2. What's the actual difference between `a * b` and `np.dot(a, b)` — both mechanically and in what each is *for*?
3. Why does raw dot product alone give a misleading "most relevant chunk" result, and what does dividing by the norms fix?
4. What does it mean for a vector to be normalized, and why does that make cosine similarity cheaper to compute?
5. `grid.shape` is `(4, 2)`. What's the output shape of `grid.sum(axis=0)`, and which original values got merged together to produce it?
6. In one line each: what does `min`/`max` on an embedding vector tell you, versus what `argmax` on a similarity-scores array tells you?
7. Why is a big gap between `mean` and `median` on a set of scores worth investigating?
8. What's the difference in what `np.zeros(6)` gives you versus `np.zeros_like(real_data)` when `real_data` is an int array?
9. Why doesn't `arr.astype(float)` change `arr` itself?
10. `np.array([2.9, -1.1, 0]).astype(int)` — what comes out, and why isn't it rounded?
11. Matrix `A` has shape `(6, 4)`, matrix `B` has shape `(4, 2)`. Does `A @ B` work, and if so, what shape comes out?
12. `arr3d.shape` is `(3, 2, 5)`. What does `axis=0` refer to here, and does that match what `axis=0` meant in a 2D array?
13. In one sentence: why does relying on "axis=0 means rows" break once you add a third dimension?
14. For `np.concatenate([A, B], axis=1)`, what has to match between `A` and `B`, and why is that the requirement specifically for `axis=1` and not `axis=0`?
15. What type of object does `np.split()` return, and why does `print()`-ing it look different from printing a normal array?
16. Why does `np.split(arr, 3)` sometimes throw an error that `np.array_split(arr, 3)` never would?