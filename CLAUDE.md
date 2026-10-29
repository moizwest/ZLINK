# Z-Link — mandatory rules for any Claude session

## Before building ANY Z-Link document — no exceptions

Z-Link's document format is a permanent standard approved by the Managing
Director on 23 October 2026. The template and its artwork live in
`document-system/` **in this repository**. They are not to be recreated,
approximated, or typeset by hand.

**Never** start a Z-Link document from `Document()` or a hand-built letterhead.
**Always**:

```python
import sys; sys.path.insert(0, '<repo>/document-system')
import zlink_doc as Z
doc = Z.new_document('Tax Invoice MW/10/1229')
```

`new_document()` applies the approved banner, watermark, footer and page ruler.
Read `document-system/TEMPLATE-SPEC.md` and work through its section E audit
checklist before giving any audit verdict.

Quotations are the one exception: no banner, no strapline, no watermark. Every
quotation is built with `zlink_quote.new_quotation(ref)`, which places the
MD-approved quotation letterhead (29 Oct 2026, section Q of TEMPLATE-SPEC.md,
reference image `document-system/artwork/quotation-header-reference.png`).

## Format changes

Format is changed **once, in `document-system/`**, never per document. A format
change needs MD approval (see the approval matrix in the `/office` skill) and is
committed here so every future session inherits it.

## What must never be committed to this repository

This repository is **public**. It holds brand artwork, layout code and format
rules only.

Never commit: bank account details or IBANs, client names, addresses or TRNs,
purchase orders, prices, quotations, invoices, work completion reports,
photographs of client premises, or staff personal data. Those belong in the
private office system (Supabase `zlink-ops`) and in Claude's memory.

## The office system

Z-Link work runs through the `/office` skill — Office Board logging, the Office
of Truth and Judgement, and the Audit department. Every task is logged to
Supabase project `zlink-ops` (ref `wismzgbcgyoysrgziljg`) before work starts.
