# Z-Link Official Document Format — Approved Specification

Approved by the Managing Director, 23 October 2026 (template v1, v2, v3).
Measured against genuine documents MW/10/1228 and ZL/PI/10356/01.

Applies to **all** official Z-Link documents — tax invoice, proforma invoice,
subcontract, undertaking, report, letter, work completion report.

**Exception:** quotations keep the typeset navy letterhead as MW/09/10345 —
no banner, no strapline, no watermark.

---

## A. Official document design — 6 clauses

| # | Clause | Specification |
|---|---|---|
| A1 | **Header** | Navy bilingual banner artwork, company name EN/AR, logo, address, TRN, contact strip. Placed **full bleed** to the page edges at full page width, **0.8 mm** from the top edge. Repeats on every page. |
| A2 | **Ruler (A4)** | Page 210 × 297 mm. Side margins **10 mm**, top **34 mm**, bottom **19.8 mm**, footer **5.3 mm** from the foot, header 0.8 mm. Text block **190 mm**. |
| A3 | **Watermark** | The full Z-Link logo (coloured rings and Z-LINK wordmark as one unit) at **81% of page width**, horizontally centred, vertical centre at **52.5%** of page height, faded to **16%** opacity over white, behind all content. Repeats on every page. |
| A4 | **Footer** | Strapline artwork "TECHNICAL BRILLIANCE / ENGINEERED EXCELLENCE / PROVEN EXPERTISE" over "DUBAI LICENSED CONTRACTOR #1245333 \| COMMERCIAL REGISTER: 2098971", set at **64% of page width**, centred. Repeats on every page. |
| A5 | **Footer reference line** | Document reference, company legal name and **Page X of Y** in small grey type on the line immediately above the strapline. |
| A6 | **No solid fills** | **No solid fills anywhere between the margins**, so the watermark reads unbroken. Section headings are navy bold text with a thin navy rule beneath, never a filled band. Table header rows are navy bold text on white with **borders only**. All body cells transparent, borders only. |

---

## B. Tax invoice and proforma invoice body — 8 clauses

Modelled on MW/10/1228. Applies to tax invoices and proforma invoices.

| # | Clause | Specification |
|---|---|---|
| B1 | **Two top boxes** | Side by side. **LEFT** the `TO,` block: client legal name, full address, client TRN, then CONTACT / MOBILE / EMAIL ID. **RIGHT** the invoice block: INVOICE (or PROFORMA INVOICE) number, Date, Contact: Moiz Husain, LPO No, Quote Ref, Project Location, Subject. |
| B2 | **Title** | Centred, bold, underlined: `TAX INVOICE` or `PROFORMA INVOICE`. |
| B3 | **Line-item table** | Columns `SR NO \| DESCRIPTION \| UNIT \| QTY \| RATE \| TOTAL AMOUNT`. |
| B4 | **Totals rows** | `GROSS TOTAL`, `VAT @ 5%`, `NET TOTAL`. Each label sits in the **RATE column alone, right-aligned**, with SR NO + DESCRIPTION + UNIT + QTY merged into one blank cell, and the figure in TOTAL AMOUNT. Never spread across several columns or the full row width. The RATE column is **at least 30 mm** so "GROSS TOTAL" sits on one line. |
| B5 | **Total in Words** | `U.A.E. DIRHAMS <amount> ONLY`. Add `AND FILS nn/100` before `ONLY` when there are fils. |
| B6 | **Payment Terms** | One line, **bold and underlined**. |
| B7 | **Bank block** | Table headed `RAK BANK` in **red** followed by `DETAILS` in black. Rows: ACCOUNT NAME / ACCOUNT NUMBER / IBAN / SWIFT CODE / BRANCH. Roughly 120 mm wide, left aligned — not full width. |
| B8 | **Signatory** | `AUTHORIZED SIGNATORY`, then about **33 mm of clear space** for the company stamp and signature, then `FOR: Z-LINK TECHNICAL SERVICES CONTRACTING CO LLC`. The MD applies stamp and signature after formatting. |

Bank account values are **not** stored in this public repository. They are held
in Claude's memory and in the private office system.

---

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
- [ ] B1–B8 every body clause for invoices and proformas
- [ ] C output set complete (DOCX + PDF + JPEG for invoices and proformas)
- [ ] D reference number in the correct series, next in sequence
- [ ] Arithmetic re-computed independently; 5% VAT shown separately
- [ ] Duplicate-data check: no fact stated twice without contractual need
- [ ] No wording signalling reduced quality
