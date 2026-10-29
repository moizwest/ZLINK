# Z-Link Official Document Format — Approved Specification

Approved by the Managing Director, 23 October 2026 (template v1, v2, v3).
Measured against genuine documents MW/10/1228 and ZL/PI/10356/01.

Applies to **all** official Z-Link documents — tax invoice, proforma invoice,
subcontract, undertaking, report, letter, work completion report.

**Exception:** quotations use their own typeset letterhead (section Q, `zlink_quote.py`) —
no banner, no strapline, no watermark.

---

## A. Official document design — 6 clauses

| # | Clause | Specification |
|---|---|---|
| A1 | **Header** | Navy bilingual banner artwork, company name EN/AR, logo, address, TRN, contact strip. Placed **full bleed** to the page edges at full page width, **0.8 mm** from the top edge. Repeats on every page. |
| A2 | **Ruler (A4)** | Page 210 × 297 mm. Side margins **10 mm**, top **34 mm**, bottom **19.8 mm**, footer **5.3 mm** from the foot, header 0.8 mm. Text block **190 mm**. |
| A3 | **Watermark** | The Z-Link logo placed at **x 19.8 mm, y 79.2 mm, 170.2 x 153.1 mm**, behind all content, repeating on every page. Built from the ORIGINAL VECTOR LOGO `artwork/logo-master.pdf`: render at 1200 dpi, trim to the artwork, scale to width, fade with factor **0.157** over white. **Never** rebuild it from a scanned document or by upscaling the small logo inside the banner - both produce speckle, mottled colour fields and ragged edges (what the MD called "colour splash"), and the upscale also desaturates the rings to grey. The vector logo's aspect is 0.900, matching the 0.898 footprint measured on the genuine document. Test: pale-layer (luminance 200-252) median saturation must be **18**, covering about **20%** of the body area. |
| A4 | **Footer** | Strapline artwork "TECHNICAL BRILLIANCE / ENGINEERED EXCELLENCE / PROVEN EXPERTISE" over "DUBAI LICENSED CONTRACTOR #1245333 \| COMMERCIAL REGISTER: 2098971", set at **64% of page width**, centred. Repeats on every page. |
| A5 | **Footer reference line** | Document reference, company legal name and **Page X of Y** in small grey type on the line immediately above the strapline. |
| A6 | **No solid fills** | **No solid fills anywhere between the margins**, so the watermark reads unbroken. Section headings are navy bold text with a thin navy rule beneath, never a filled band. Table header rows are navy bold text on white with **borders only**. All body cells transparent, borders only. |

---

## B. Tax invoice and proforma invoice body — 8 clauses

Modelled on MW/10/1228. Applies to tax invoices and proforma invoices.

| # | Clause | Specification |
|---|---|---|
| B1 | **Two top boxes** | Side by side. **LEFT** the `TO,` block: client legal name, full address, client TRN, then CONTACT / MOBILE / EMAIL ID. **RIGHT** the invoice block: INVOICE (or PROFORMA INVOICE) number, Date, Contact: Moiz Husain, LPO No, Quote Ref, Project Location, Subject. **Every line in both boxes is set in BOLD**, and **one blank line separates the client TRN line from the CONTACT line** in the left box (MD rules, 27 Oct 2026) — use `top_boxes()` in `zlink_doc.py`, which applies both. |
| B2 | **Title** | Centred, bold, underlined: `TAX INVOICE` or `PROFORMA INVOICE`. |
| B3 | **Line-item table** | Columns `SR NO \| DESCRIPTION \| UNIT \| QTY \| RATE \| TOTAL AMOUNT`. **Data alignment (MD rule, 27 Oct 2026):** every data cell from the first line item down to NET TOTAL is **vertically middle**; UNIT, QTY and RATE values are **horizontally centred**; TOTAL AMOUNT values are **right-aligned**. Apply with `align_items()` in `zlink_doc.py` after `fix_grid()`. |
| B4 | **Totals rows** | `GROSS TOTAL`, `VAT @ 5%`, `NET TOTAL`. Each label sits in the **RATE column alone, right-aligned**, with SR NO + DESCRIPTION + UNIT + QTY merged into one blank cell, and the figure in TOTAL AMOUNT. Never spread across several columns or the full row width. The RATE column is **at least 30 mm** so "GROSS TOTAL" sits on one line. |
| B5 | **Total in Words** | `Total in Words:  U.A.E. DIRHAMS <amount> ONLY`. Add `AND FILS nn/100` before `ONLY` when there are fils. **Placement (MD rule, 28 Oct 2026, measured on MW/10/1228): the LAST ROW of the line-item table, merged across all six columns, bold, directly beneath NET TOTAL** — never a free paragraph below the table. Use `words_row()` in `zlink_doc.py`. |
| B6 | **Payment Terms** | One line, **bold and underlined**. |
| B7 | **Bank block** | Table headed `RAK BANK` in **red** followed by `DETAILS` in black. Rows: ACCOUNT NAME / ACCOUNT NUMBER / IBAN / SWIFT CODE / BRANCH. Roughly 120 mm wide, left aligned — not full width. |
| B8 | **Signatory** | `AUTHORIZED SIGNATORY`, then **25 mm of clear space** (four empty 10 pt lines — MD rule 28 Oct 2026, superseding the earlier ~33 mm which the MD found too wide) for the company stamp and signature, then `FOR: Z-LINK TECHNICAL SERVICES CONTRACTING CO LLC`. The MD applies stamp and signature after formatting. Use `signatory_block()` in `zlink_doc.py`. |

Bank account values are **not** stored in this public repository. They are held
in Claude's memory and in the private office system.

---

## W. Work completion report (WCR) body — 7 clauses

Approved by the MD 28 Oct 2026, modelled on ZL/WCR/10359 after the
duplicate-data review. Applies to every work completion report / certificate.
Numbering: `ZL/WCR/<quotation number>` (add `-<unit>` where one quotation covers
several units, e.g. `ZL/WCR/10353-312B`).

| # | Clause | Specification |
|---|---|---|
| W1 | **Title** | Centred, bold, underlined, navy: `WORK COMPLETION REPORT`. |
| W2 | **Particulars table** (4 cols, 40/55/40/55 mm) | Completion Report No. / Purchase Order No.; Date of Completion / PO Date; Quotation Reference / Job or Work Order No.; Tax Invoice No. / Client TRN. **No "Report Date" row** — the completion date is the report date. Each fact appears here once and is **not repeated in the body text**. |
| W3 | **Client table** (2 cols, 40/150 mm) | Client; Client Address; Client Contact (name - mobile - email on one line); Project; Location. The TRN lives in W2, not here. |
| W4 | **1. Declaration of Completion** | One short paragraph: company legal name confirms that *the works described below* were completed in full on the completion date in accordance with *the quotation and Purchase Order referenced above*, and handed over in working order; then the warranty sentence (workmanship period from completion; materials on manufacturer's warranty). **Does not restate the scope** and **does not re-cite** the PO, quotation or invoice numbers. The warranty is stated here and nowhere else. |
| W5 | **2. Summary of Works Completed** | Table `SR \| DESCRIPTION OF WORKS COMPLETED \| STATUS` (12/148/30 mm), one row per work package, status `Completed`. Sizes, brands and references are given once per row, not repeated within it. **No warranty row.** Beneath the table one line: `Contract value: AED x,xxx.xx excluding VAT (VAT AED xxx.xx \| Total AED x,xxx.xx).` — no PO or invoice number in that line. |
| W6 | **3. Photographic Record** | Starts on a new page. Two-column grid (95/95 mm), every photo at a fixed **64 mm height** so rows stay level — except a photo whose width at 64 mm would exceed **88 mm** (wide panoramas), which is set to 88 mm width instead so it is never clipped by the cell, 9 pt caption beneath. Captions name what the photo shows in a few words; they do not re-read the works table. |
| W7 | **4. Contractor Signature / 5. Client Acceptance** | Section 4 starts on a new page and is the signature table only (Contractor / Name / Designation / Signature & Company Stamp / Date) — **no declaration sentence**, that is W4's job. Section 5 heading `CLIENT ACCEPTANCE - <CLIENT NAME>`, one line "The works described above have been inspected and are accepted as complete.", then Name / Designation / Date of Acceptance / Signature & Company Stamp. |

**Duplicate-data rule (all documents on the letterhead):** a fact is stated
once, in the place the format assigns it. Retained on purpose: party legal names
in both the particulars and the signature blocks, and reference numbers in the
particulars table. Everything else that repeats is cut before audit.

---

## B+. Measured geometry and colour — taken off the genuine proforma at 200 dpi

These are measurements, not estimates. `zlink_doc.py` carries them as constants.

### Type

Body text is **10 pt Calibri**. Verified by width: "Z LINK TECHNICAL SERVICES
CONTRACTING CO LLC" measures **73.0 mm** on the genuine document, and Carlito
(metric-compatible with Calibri) renders that string at exactly 73.0 mm at 10 pt.
9.5 pt gives 67.8 mm and 11 pt gives 80.8 mm — neither matches.

Title is 14 pt bold, underlined. Table header row is 10 pt bold.

### Colour — navy is used sparingly

| Element | Colour |
|---|---|
| Title (`TAX INVOICE` / `PROFORMA INVOICE`) | **Navy** `#1F3864` |
| Line-item table **header row** | **Navy** `#1F3864` |
| `RAK BANK` in the bank header | **Red** `#C00000` |
| Everything else | **Black** |

That includes the line-item description, the SR NO, the UNIT, QTY, RATE and
TOTAL AMOUNT values, the GROSS TOTAL / VAT @ 5% / NET TOTAL labels **and their
figures**, Total in Words, Payment Terms, the bank labels and values, and the
signatory block. Putting navy on the totals or the description is wrong.

### Column geometry (mm)

| Table | Columns |
|---|---|
| Top boxes | `94.9 / 95.0` — equal halves, divider at 105.1 mm, table top at the 34 mm margin |
| Line items | `12.2 / 86.4 / 15.9 / 14.2 / 31.7 / 29.5` = 190.0 mm |
| Bank block | `37.6 / 80.0` = 117.6 mm, left aligned |

Verticals on the genuine fall at 10.2, 22.4, 108.8, 124.7, 138.9, 170.6 and
200.1 mm, and the bank table at 10.2, 50.5 and 127.8 mm. The bank split is set
to 37.6 / 80.0 rather than the measured 40.3 / 77.3 so the account-name line
does not wrap under the substituted font; overall width is unchanged.

### Cell padding and rows

Cell side padding **1.2 mm**, top and bottom 0.5 mm. Word's 1.9 mm default makes
`SR NO` and the account name wrap, which they do not on the genuine document.
Bank and totals rows measure **7.0 mm** tall.

### Bank header row

Two cells, **not merged**: `RAK BANK` in red plus ` DETAILS` in black in the
left cell, the right cell empty.

---

## Q. Quotation format — approved by the MD 29 Oct 2026 (module `zlink_quote.py`)

Quotations are the exception to section A: no banner, no strapline, no watermark.
Every quotation is built with `zlink_quote.new_quotation(ref)` and **starts with
this letterhead**, measured off the MD's reference `artwork/quotation-header-reference.png`.
Never typeset it by hand and never copy a letterhead from an older job script.

| # | Element | Rule |
|---|---|---|
| Q1 | **Letterhead** (left-aligned) | L1 `Z-LINK TECHNICAL SERVICES CONTRACTING CO. LLC` Calibri Bold 17 pt blue #2E74B5 · L2 `OFFICE 201, BAY SQUARE, BUSINESS BAY, DUBAI, UNITED ARAB EMIRATES` Calibri Bold 12 pt black · L3 **TRN:** 104180458200003 (label bold, number regular) 11.5 pt · L4 red ☎ 055-9495833 \| green ✉ INFO@ZLINK.AE \| blue 🌐 WWW.ZLINK.AE, Calibri 12 pt · grey 3-D emboss rule (#A6A6A6) across the full text width. Exact line heights 20/15/14/15 pt. |
| Q2 | **Title** | `QUOTATION`, Calibri Bold 12.5 pt blue #2E74B5, **right-aligned**, directly under the rule. |
| Q3 | **Particulars** | Borderless two-column block (100/80 mm): left To / client legal name (bold) / address / Attn / Tel / Email; right Ref No. / Date / Your Ref. / Project / Subject / Validity. Labels bold. |
| Q4 | **Price schedule** | Columns Item 12 · Description 92 · Unit 13 · Qty 13 · Rate 22 · Amount 28 mm. Header row blue #2E74B5 with white bold text, repeats on each page. Group rows light blue #DEEAF6 with blue bold text. Description = bold title line + specification. Unit/Qty centred, Rate/Amount right-aligned. Rows never split. |
| Q5 | **Totals** | Sub Total (AED), VAT 5% (AED), Grand Total (AED): label right-aligned across Item–Rate, figure in Amount; Grand Total row shaded #DEEAF6. Then `Amount in words:` bold + italic words "(inclusive of 5% VAT)". |
| Q6 | **Section headings** | Blue #2E74B5 bold 11 pt, kept with next: OPTIONAL ITEMS, BASIS OF QUOTATION (numbered), EXCLUSIONS (bullets), TERMS & CONDITIONS (bullets with bold key: Payment, Mobilisation/Delivery, Completion, Warranty, Pricing, Bank). Optional items table uses the Q4 header style. |
| Q7 | **Closing** | Trust paragraph · Yours faithfully, · **For Z-LINK TECHNICAL SERVICES CONTRACTING CO. LLC** (blue) · 30 pt space for stamp/signature · **Moiz Husain** · Managing Director \| Mob: 055-9495833 \| moiz@zlink.ae. |
| Q8 | **Page** | A4, 15 mm margins all sides, Calibri 9.5 pt body, footer `<ref> \| Page X of Y` 7.5 pt grey centred. |
| Q9 | **Content rules** | Ref `MW/MM/NNNNN`; British English; 5% VAT separate; Monday–Saturday programme; 50/50 payment unless told otherwise; no wording that signals reduced quality; each fact stated once. |

Audit (adds to section E): letterhead and title must match Q1–Q2 against the
reference image when rendered — any difference is an automatic **FAIL**.

## C. Output set

Every tax invoice and proforma invoice is delivered as **DOCX + PDF + JPEG**.
The JPEG is rendered at **200 dpi** (A4 → 1654 × 2339 px) at **quality 92**,
one JPEG per page, named after the document with no page suffix when single page.
The JPEG is for WhatsApp and for pasting into email.

Other official documents are delivered as DOCX + PDF.

---

## D. Numbering

| Series | Form | Example |
|---|---|---|
| Quotation | `MW/MM/NNNNN` | MW/09/10353 |
| Tax invoice | `MW/MM/NNNN` | MW/10/1229 |
| Proforma invoice | `ZL/PI/NNNNN/NN` | ZL/PI/10356/01 |

Take the **next number in the series**. Check Google Drive for the last issued
number before assigning one. Never invent a reference shape.

---

## E. Audit checklist — run before any verdict

A breach of **any** clause below is an automatic **FAIL**, never a note.
Applying the body layout (section B) is *not* applying the Z-Link format —
section A is an equally mandatory, separate standard.

- [ ] A1 banner artwork present, full bleed, repeating
- [ ] A2 ruler 10 / 34 / 19.8 / 5.3 mm, A4
- [ ] A3 watermark at 81% width, 52.5% vertical centre, 16% opacity, behind content
- [ ] A4 strapline artwork at 64% width, centred, repeating
- [ ] A5 footer reference line with Page X of Y
- [ ] A6 no solid fills anywhere between the margins
- [ ] B5 Total in Words is the last merged row of the item table, not a paragraph
- [ ] B8 signatory clear space is 25 mm (four empty 10 pt lines), not more
- [ ] W1–W7 every body clause for work completion reports (no Report Date row, no scope or reference repetition in the declaration, no warranty row in the works table, signature section without a declaration sentence)
- [ ] B1–B8 every body clause for invoices and proformas (B1: both top boxes fully bold; blank line between TRN and CONTACT. B3: UNIT/QTY/RATE centred-middle, TOTAL AMOUNT right-middle through NET TOTAL)
- [ ] C output set complete (DOCX + PDF + JPEG for invoices and proformas)
- [ ] D reference number in the correct series, next in sequence
- [ ] Arithmetic re-computed independently; 5% VAT shown separately
- [ ] Duplicate-data check: no fact stated twice without contractual need
- [ ] No wording signalling reduced quality
