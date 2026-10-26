# Z-Link Document System

**The approved Z-Link document template, with its artwork, in one place.**

Z-Link's document format is a permanent standard approved by the Managing Director
on 23 October 2026. The *rules* were written down; the *artwork and template code*
were not, so every new chat session rebuilt the document from scratch and got it
wrong. This folder is the fix. It is the single source for both.

---

## For any Claude session, before building ANY Z-Link document

Do this **first**, before writing a single line of document code:

```bash
git clone --depth 1 https://github.com/moizwest/zlink /home/claude/zlink
```

Then import the template and build on it:

```python
import sys; sys.path.insert(0, '/home/claude/zlink/document-system')
import zlink_doc as Z

doc = Z.new_document('Tax Invoice MW/10/1229')   # banner, watermark, footer, ruler applied
Z.para(doc, 'TAX INVOICE', 14, True, align=..., underline=True)
...
doc.save(out)
```

`new_document()` returns a `python-docx` Document already carrying the full
official design. **Never** typeset a letterhead by hand. **Never** start from
`Document()`.

Do not edit a document's format locally. Format is changed once, here, in the
template — never per document.

---

## What is in here

| Path | What it is |
|---|---|
| `zlink_doc.py` | The template module. Page setup, artwork placement, shared body helpers. |
| `artwork/banner.png` | Navy bilingual banner, full bleed. Extracted at 200 dpi from proforma ZL/PI/10356/01. |
| `artwork/strapline.png` | Footer strapline artwork. Ink measures 64.2% of page width. |
| `artwork/logo.png` | Z-Link logo lockup, 300 dpi, extracted from the banner of tax invoice MW/10/1228. |
| `artwork/watermark.png` | The logo scaled to 81% page width and faded to 16% over white. Regenerate from `logo.png` if the fade ever changes. |
| `TEMPLATE-SPEC.md` | The approved format, clause by clause, with the audit checklist. |

---

## Provenance

The artwork was recovered from two genuine, MD-approved documents:

- **MW/10/1228** — Harris Pye Gulf LLC tax invoice, 22 October 2026 (Letter)
- **ZL/PI/10356/01** — Harris Pye Emirates proforma invoice, 26 October 2026 (A4)

The proforma is the geometric master: A4, banner 0.8 mm from the top edge,
strapline at 64.2% of page width — all matching the recorded specification
exactly. Measurements in `TEMPLATE-SPEC.md` are taken from it.

---

## What is deliberately NOT in here

This repository is **public**. It holds brand artwork and layout code only.

Never commit to this folder: bank account details, IBANs, client names,
addresses, TRNs, purchase orders, prices, quotations, invoices, work completion
reports, photographs of client premises, or staff personal data. Those live in
the private office system and in Claude's memory.

If the repository is made private, that restriction still stands unless the
Managing Director says otherwise.
