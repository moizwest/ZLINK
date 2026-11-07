#!/usr/bin/env python3
"""Build the zlink.ae service and area pages.

Every claim here must exist in the Z-Link office record (website copy approved by the MD,
completed projects only, no manufacturer-approval or Civil Defence-approval claims).
Run from the repo root:  python3 tools/build_pages.py
"""
import json, os, html

SITE = "https://zlink.ae"
ORG_ID = SITE + "/#org"
PHONE_M, PHONE_M_TXT = "+971559495833", "+971 55 949 5833"
PHONE_L, PHONE_L_TXT = "+97143861940", "+971 4 386 1940"
EMAIL = "info@zlink.ae"
ADDRESS = "Office 201, Bay Square, Business Bay, Dubai, UAE"
U = "https://images.unsplash.com/"
UQ = "?auto=format&fit=crop&w=1400&q=70"

PROJECTS = {
    "dwc": ("Epoxy flooring · Dubai South", "Airport vehicle parking bay, 1,900 m²",
            "Anti-slip epoxy with aggregate broadcast at Al Maktoum International Airport (DWC), delivered as specialist subcontractor.",
            "/assets/projects/dwc-1.webp", "Z-Link crew laying anti-slip epoxy at an airport parking bay in Dubai South"),
    "enpi": ("Epoxy flooring · Industrial Area 5, Sharjah", "Film factory warehouse, 1,250 m²",
             "Industrial epoxy floor for a film manufacturer's warehouse, completed in 2025.",
             "/assets/projects/enpi-1.webp", "Finished glossy epoxy floor in a Sharjah factory warehouse"),
    "cupco": ("Epoxy flooring · Industrial Area 15, Sharjah", "Factory floor upgrade in a live factory",
              "Diamond grinding, epoxy coating and yellow safety line marking inside a working factory.",
              "/assets/projects/cupco-1.webp", "Factory floor with new epoxy and yellow line marking in Sharjah"),
    "steel": ("Industrial coatings · Al Sajaa workshop", "Steel brackets for façade and metal fabricators, 27 MT+",
              "Blast cleaning, Jotun Penguard primers and Hardtop topcoats up to a C5-M specification, with dry-film thickness checked and a coating certificate for every batch.",
              "/assets/projects/steel-1.webp", "Coated steel brackets on drying racks at the Z-Link workshop"),
}

COMMON_FAQ = [
    ("Do you visit the site before quoting?",
     "Yes. We inspect, measure and test on site, then send an itemised quotation naming the system, method and programme. VAT is shown separately."),
    ("Can you work while our building or factory stays open?",
     "Yes. We phase work around live operations, with barricades, signage and permits, and we can plan night or weekend shifts where needed."),
    ("How quickly will you respond?",
     "We aim to reply within 24 working hours with a survey date or a quotation."),
]

SERVICES = [
 dict(slug="waterproofing", name="Waterproofing",
  title="Waterproofing Contractor in Dubai & Sharjah | Z-Link",
  desc="Roof, basement, wet-area and water-tank waterproofing plus leak repair on live buildings in Dubai and Sharjah. Site survey and itemised quotation. Call Z-Link.",
  h1="Waterproofing contractor in Dubai and Sharjah",
  img="photo-1674485169641-bcb2bf6f1df9", alt="Roof waterproofing membrane being applied",
  lead="Roofs, basements, wet areas, water tanks and podiums, plus leak investigation and repair on buildings that stay in use. Our own crews survey, apply and hand over.",
  body=[
   ("Where we waterproof", "We work on warehouse and factory roofs, building podiums and terraces, basements, bathrooms and other wet areas, and water tanks. Many jobs start with a leak: we trace the source on site before proposing a repair, so you pay for the fix the building needs, not a blanket replacement."),
   ("Systems we apply", "We select polyurethane, bituminous or cementitious systems to suit the substrate, exposure and use, and apply them to the manufacturer's specification. Joints, upstands, drains and penetrations get the detailing attention, because that is where most roofs fail."),
   ("How a waterproofing job runs", "Survey and leak investigation, an itemised quotation naming the system and programme, surface preparation, application, then a flood or water test where the detail allows it before handover."),
  ],
  items=["Roof membranes", "Basement tanking", "Wet areas", "Water tanks", "Podiums and terraces", "Leak investigation and repair"],
  projects=[], related=["industrial-coatings", "civil-works", "epoxy-flooring"],
  faq=[("Can you find where my roof is leaking?", "Yes. We inspect the roof, joints, drains and penetrations on site and trace the source before quoting the repair.")]),
 dict(slug="epoxy-flooring", name="Epoxy Flooring",
  title="Epoxy Flooring Contractor in Dubai & Sharjah | Z-Link",
  desc="Epoxy floors for warehouses, factories and car parks in Dubai and Sharjah: grinding, self-levelling and anti-slip finishes, coving and line marking. Own crews.",
  h1="Epoxy flooring contractor in Dubai and Sharjah",
  img="photo-1772305336606-989a457ffbae", alt="Epoxy floor in an industrial building",
  lead="Hard-wearing epoxy floors for car parks, warehouses, factories and food areas, with self-levelling and anti-slip finishes, coving and safety line marking, laid by our own crews.",
  body=[
   ("Floors we lay", "Warehouse and logistics floors, factory production areas, car parks and ramps, walkways and food-area floors. We match the system to the traffic: forklifts and pallet trucks, cars, foot traffic or wet processes."),
   ("Preparation decides the result", "We diamond-grind or otherwise prepare the concrete, repair cracks and joints, then apply primer and the specified build. Anti-slip floors get an aggregate broadcast; coving, line marking and bay marking are finished in the same programme."),
   ("Working in live facilities", "Most of our floors are laid in buildings that keep running. We phase areas so operations continue, with barricades and signage, and plan night or weekend shifts where needed."),
   ("Trained on the system", "Our application team completed Sika U.A.E.'s Basic Application Training for Sikafloor® MultiFlex Traffic 1330 and Sikafloor®-1205 on 31 December 2025. This is basic application training; Z-Link is not a Sika approved applicator."),
  ],
  items=["Warehouses and factories", "Car parks", "Self-levelling", "Anti-slip", "Coving", "Line marking"],
  projects=["dwc", "enpi", "cupco"], related=["industrial-coatings", "waterproofing", "painting"],
  faq=[("Can you lay epoxy while the warehouse is operating?", "Yes. We split the floor into phases so the rest of the building keeps working, and we can schedule night or weekend shifts.")]),
 dict(slug="industrial-coatings", name="Industrial Coatings",
  title="Industrial Coatings & GRP Tank Lining in the UAE | Z-Link",
  desc="Protective and anti-corrosion coatings for tanks, pipework and steel, plus GRP lining. Surface preparation, specified DFT and inspection records. Sharjah workshop.",
  h1="Industrial coatings and GRP lining in the UAE",
  img="photo-1529479627062-5f1f0b88912a", alt="Industrial steel structure with protective coating",
  lead="Protective and anti-corrosion coating systems for storage tanks, pipework, steel structures and plant, and GRP lining, applied at our Al Sajaa workshop in Sharjah or on site.",
  body=[
   ("What we coat", "Storage tanks, pipework, steel structures, brackets and fabricated steel for façade and metal fabricators, and plant items. Water tanks can be lined with GRP."),
   ("How we coat", "Surface preparation including blast cleaning, then primers and topcoats applied to the specified dry-film thickness. DFT is measured and recorded, and we issue inspection records with the work."),
   ("Workshop and site", "Smaller steel items come to our Al Sajaa workshop, where batches are blasted, coated, cured and checked. Tanks, pipework and structures are coated on site."),
  ],
  items=["Storage tanks", "Pipework", "Steel structures", "Surface preparation", "GRP lining", "DFT inspection records"],
  projects=["steel"], related=["waterproofing", "epoxy-flooring", "fire-systems"],
  faq=[("Do you provide coating inspection records?", "Yes. Dry-film thickness is checked and recorded, and on our steel bracket work a coating certificate is issued for every batch.")]),
 dict(slug="civil-works", name="Civil Works",
  title="Civil Works & Concrete Repair in Dubai & Sharjah | Z-Link",
  desc="Concrete repair, crack injection, blockwork, drainage and demolition around occupied buildings in Dubai and Sharjah. Site survey and itemised quotation from Z-Link.",
  h1="Civil works and concrete repair in Dubai and Sharjah",
  img="photo-1685464196387-854858ce0f4f", alt="Concrete repair works on a building",
  lead="Concrete repair, crack injection, blockwork, drainage and demolition, done neatly around occupied spaces by our own civil team.",
  body=[
   ("Typical civil packages", "Spalled and damaged concrete repaired with repair mortars, cracks sealed by resin injection, new blockwork and partitions, drainage replacement and controlled demolition ahead of refurbishment."),
   ("Part of a bigger job", "Civil works often come before waterproofing, flooring or fit-out. Because those trades are also ours, one programme covers the sequence and nobody waits on another contractor."),
   ("Repairs that last", "Before repairing concrete we break out loose and damaged material, treat exposed reinforcement and rebuild the section with repair mortar, so the repair bonds and does not spall again. Cracks are assessed first: live cracks and dormant cracks need different treatment."),
  ],
  items=["Concrete repair", "Crack injection", "Blockwork", "Drainage", "Demolition"],
  projects=[], related=["waterproofing", "fit-out", "epoxy-flooring"], faq=[("Can you carry out drainage replacement in an occupied building?", "Yes. We plan the work in sections with temporary arrangements so washrooms and facilities stay usable as far as possible.")]),
 dict(slug="painting", name="Painting",
  title="Interior & Exterior Painting Contractor in Dubai | Z-Link",
  desc="Interior and exterior painting for villas, apartments, towers, offices and restaurants in Dubai: dual-tone facades, feature walls, texture and decorative finishes.",
  h1="Interior and exterior painting contractor in Dubai",
  img="photo-1562259949-e8e7689d7828", alt="Painter working on an interior wall",
  lead="Interior and exterior painting for villas, apartments, towers, offices and restaurants: bold colours, accent and feature walls, texture and decorative finishes, and dual-tone facades.",
  body=[
   ("Exterior repainting", "Villa exteriors and tower facades, including dual-tone schemes. Preparation comes first: cleaning, crack and surface repair, then primer and finish coats suited to UAE sun and heat."),
   ("Interiors and decorative work", "Apartments, offices and restaurants, from full repaints to accent and feature walls, texture paint and Venetian-style plaster finishes."),
   ("Occupied buildings", "We plan access, protection and working hours around residents, tenants and diners, and keep areas clean and safe each shift."),
   ("Paint systems", "On our painting jobs we commonly use Jotun interior and exterior systems, including the Fenomastic and Jotashield ranges, applied to the manufacturer's specification for each surface."),
  ],
  items=["Tower facades", "Villa exteriors", "Feature walls", "Texture paint", "Decorative finishes"],
  projects=[], related=["civil-works", "fit-out", "waterproofing"], faq=[("Do you repaint whole building facades?", "Yes. We repaint villa exteriors and tower facades, including dual-tone schemes, with access, preparation and protection planned for the building.")]),
 dict(slug="fire-systems", name="Fire Systems",
  title="Fire Pump Lines, Fire Doors & Intumescent Coating | Z-Link",
  desc="Fire pump suction line replacement, fire door overhaul and intumescent coatings in Dubai and Sharjah. Works needing DCD approval are done with DCD-approved partners.",
  h1="Fire pump lines, fire doors and intumescent coatings",
  img="photo-1785682118449-21da8825754d", alt="Fire protection pipework",
  lead="Fire pump suction line replacement, fire door overhaul and fire-rated (intumescent) coatings. Works that need Dubai Civil Defence approval are carried out with DCD-approved partners.",
  body=[
   ("Pipework", "Replacement of fire pump suction lines and fire mains in HDPE or GI, including fittings and valves, planned so the system is out of service for the shortest possible time."),
   ("Fire doors", "Maintenance, coating and general overhaul of fire exit doors and their hardware."),
   ("Intumescent coatings", "Fire-rated intumescent coating of structural steel, applied to the specified thickness."),
   ("Approvals", "Where a scope needs Dubai Civil Defence approval, we deliver it with DCD-approved partners and say so at quotation stage."),
   ("Planning around a live system", "Fire protection has to stay available. We agree the isolation window with the facility team, prepare fittings in advance and restore the system the same day wherever the scope allows."),
  ],
  items=["Fire mains", "Pump suction lines", "Fire doors", "Intumescent coatings"],
  projects=[], related=["industrial-coatings", "civil-works", "fit-out"], faq=[("Do you hold Civil Defence approval?", "Works that need Dubai Civil Defence approval are carried out with DCD-approved partners, and we state this at quotation stage.")]),
 dict(slug="landscaping", name="Landscaping",
  title="Landscaping & Interlock Paving Contractor in Dubai | Z-Link",
  desc="Soft and hard landscaping in Dubai for villas, communities and campuses: palms and lawns, interlock paving, sports grounds, granite and water features.",
  h1="Landscaping and interlock paving in Dubai",
  img="photo-1734079692160-fcbe4be6ab96", alt="Landscaped garden with palms and paving",
  lead="Soft and hard landscaping for villas, communities and campuses: palms and lawns, interlock paving, sports grounds and water features.",
  body=[
   ("Soft landscaping", "Palms, planting and lawns for villas, residential communities and campuses."),
   ("Hard landscaping", "Interlock paving, edging, granite and other hardscape, sports grounds and water features, built and finished to sit well with the buildings around them."),
   ("Maintenance-friendly design", "We choose planting, paving patterns and edging that suit UAE heat and are practical for the community or facility team to maintain after handover."),
  ],
  items=["Palms and lawns", "Interlock paving", "Sports grounds", "Water features", "Hardscape"],
  projects=[], related=["civil-works", "painting", "fit-out"], faq=[("Do you build sports grounds?", "Yes. Sports grounds are part of our hard landscaping scope, along with interlock paving, edging and water features.")]),
 dict(slug="fit-out", name="Turnkey Fit-out",
  title="Turnkey Fit-out & Renovation Contractor in Dubai | Z-Link",
  desc="Turnkey fit-out and renovation in Dubai: offices, washrooms, warehouses and post-fire reinstatement, coordinated by one contractor and handed over ready to use.",
  h1="Turnkey fit-out and renovation in Dubai",
  img="photo-1577412647305-991150c7d163", alt="Fitted-out modern office interior",
  lead="Offices, washrooms, warehouses and post-fire reinstatement, coordinated by one contractor and handed over ready to use.",
  body=[
   ("What we fit out", "Office fit-outs and refurbishments, washroom renovations, warehouse fit-outs and reinstatement after fire damage."),
   ("One contract", "Gypsum, joinery, finishes, flooring, painting and civil works are our own trades; MEP is coordinated within the same programme. You deal with one programme, one standard and one contact."),
   ("Approvals", "We are registered with Concordia for fit-out approvals in JLT and DMCC, and we prepare the drawings and documents a fit-out approval needs."),
   ("Post-fire reinstatement", "After a fire we strip out damaged finishes, repair and clean the structure, and rebuild ceilings, partitions, finishes and services coordination so the space can reopen."),
  ],
  items=["Offices", "Washrooms", "Warehouses", "Post-fire reinstatement"],
  projects=[], related=["civil-works", "painting", "epoxy-flooring"], faq=[("Can you handle the fit-out approval?", "Yes. We are registered with Concordia for fit-out approvals in JLT and DMCC and prepare the approval documents with the fit-out.")]),
]

AREAS = [
 dict(slug="dubai", name="Dubai",
  title="Contractor in Dubai: Waterproofing, Epoxy, Painting | Z-Link",
  desc="Z-Link works across Dubai from Business Bay: waterproofing, epoxy flooring, coatings, civil, painting, fire systems, landscaping and fit-out. Own crews.",
  h1="Technical contractor in Dubai",
  lead="From our office in Business Bay, our crews cover Dubai's industrial areas, communities and towers for all eight of our trades.",
  places="Dubai Investments Park · International City · Al Quoz · Dubai Silicon Oasis · Jumeirah Village Circle · Business Bay · Dubai South",
  projects=["dwc"]),
 dict(slug="sharjah", name="Sharjah",
  title="Contractor in Sharjah: Epoxy, Waterproofing, Coatings | Z-Link",
  desc="Z-Link's workshop is in Al Sajaa, Sharjah. Warehouse epoxy flooring, factory roof waterproofing and industrial coatings across Sharjah's industrial areas.",
  h1="Technical contractor in Sharjah",
  lead="Our workshop is in Al Sajaa Industrial Area, so Sharjah's factories and warehouses are a short drive for our crews.",
  places="Al Sajaa · Industrial Areas 5, 13 and 15 · Sharjah city",
  projects=["enpi", "cupco", "steel"]),
]

CSS = "/assets/css/pages.css"


def e(s):
    return html.escape(s, quote=True)


def page(path, title, desc, h1, crumbs, body_html, schema):
    canon = SITE + path
    nav = ''.join(f'<a href="/services/{s["slug"]}/">{e(s["name"])}</a>' for s in SERVICES)
    svc_foot = ''.join(f'<li><a href="/services/{s["slug"]}/">{e(s["name"])}</a></li>' for s in SERVICES)
    bc = ' <span aria-hidden="true">›</span> '.join(
        (f'<a href="{u}">{e(n)}</a>' if u else f'<span aria-current="page">{e(n)}</span>') for n, u in crumbs)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#0B2A30">
<meta property="og:type" content="website">
<meta property="og:url" content="{canon}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{SITE}/assets/images/logo.png">
<link rel="icon" type="image/png" href="/assets/images/logo.png">
<link rel="apple-touch-icon" href="/assets/images/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Semi+Condensed:wght@600;700;800&family=Barlow:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{CSS}">
<script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False)}
</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="wrap hd">
  <a class="logo" href="/" aria-label="Z-Link home"><img src="/assets/images/logo.png" alt="Z-Link logo" width="63" height="58"><span>TECHNICAL SERVICES<br>CONTRACTING CO. LLC</span></a>
  <a class="btn" href="/#contact">Request a quote</a>
</div></header>
<nav class="svcnav" aria-label="Services"><div class="wrap">{nav}</div></nav>
<main id="main">
<div class="wrap crumbs">{bc}</div>
{body_html}
<section class="cta"><div class="wrap">
  <h2>Tell us about your site.</h2>
  <p>We aim to reply within 24 working hours with a survey date or a quotation.</p>
  <div class="cta-row"><a class="btn" href="/#contact">Send an enquiry</a><a class="btn line" href="https://wa.me/971559495833">WhatsApp {PHONE_M_TXT}</a><a class="btn line" href="tel:{PHONE_M}">Call</a></div>
</div></section>
</main>
<footer>
  <div class="wrap top">
    <div><img class="fl" src="/assets/images/logo.png" alt="Z-Link" loading="lazy"><p>Z-Link Technical Services Contracting Co. LLC. Eight technical trades, our own crews, one contract, across the UAE.</p></div>
    <div><h4>Services</h4><ul>{svc_foot}</ul></div>
    <div><h4>Areas</h4><ul><li><a href="/areas/dubai/">Dubai</a></li><li><a href="/areas/sharjah/">Sharjah</a></li><li><a href="/#areas">All areas</a></li><li><a href="/#projects">Projects</a></li><li><a href="/#faq">FAQ</a></li></ul></div>
    <div><h4>Contact</h4><ul><li><a href="tel:{PHONE_M}">{PHONE_M_TXT}</a></li><li><a href="tel:{PHONE_L}">{PHONE_L_TXT}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>{e(ADDRESS)}</li></ul></div>
  </div>
  <div class="bar"><div class="wrap"><span>© 2026 Z-Link Technical Services Contracting Co. LLC · Dubai trade licence 1245333</span><span>Stock photography: Unsplash</span></div></div>
</footer>
</body>
</html>
'''


def breadcrumb_schema(crumbs):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, **({"item": SITE + u} if u else {})}
        for i, (n, u) in enumerate(crumbs)]}


def project_cards(keys):
    if not keys:
        return ''
    cards = ''.join(f'''<article class="proj"><img src="{PROJECTS[k][3]}" alt="{e(PROJECTS[k][4])}" loading="lazy" width="800" height="600">
<div><span class="kicker">{e(PROJECTS[k][0])}</span><h3>{e(PROJECTS[k][1])}</h3><p>{e(PROJECTS[k][2])}</p></div></article>''' for k in keys)
    return f'<section class="block alt"><div class="wrap"><h2>Work we have delivered</h2><div class="projs">{cards}</div><p class="note">Our own site photos. References are available on request with the client\'s permission.</p></div></section>'


def faq_html(faqs):
    items = ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in faqs)
    return f'<section class="block"><div class="wrap narrow"><h2>Questions clients ask</h2>{items}</div></section>'


def build_service(s):
    path = f'/services/{s["slug"]}/'
    crumbs = [("Home", "/"), ("Services", "/services/"), (s["name"], None)]
    sections = ''.join(f'<h2>{e(h)}</h2><p>{e(p)}</p>' for h, p in s["body"])
    items = ''.join(f'<li>{e(i)}</li>' for i in s["items"])
    rel = ''.join(f'<li><a href="/services/{r}/">{e(next(x["name"] for x in SERVICES if x["slug"] == r))}</a></li>' for r in s["related"])
    body = f'''<section class="hero"><div class="wrap two">
  <div><span class="kicker">{e(s["name"])}</span><h1>{e(s["h1"])}</h1><p class="lead">{e(s["lead"])}</p>
  <div class="cta-row"><a class="btn" href="/#contact">Get a quote</a><a class="btn ghost" href="tel:{PHONE_M}">{PHONE_M_TXT}</a></div></div>
  <img class="heroimg" src="{U}{s["img"]}{UQ}" alt="{e(s["alt"])}" width="1400" height="933" fetchpriority="high">
</div></section>
<section class="block"><div class="wrap two-text">
  <div class="prose">{sections}</div>
  <aside class="box"><h3>Scope</h3><ul class="ticks">{items}</ul><h3>Areas</h3><p>Dubai, Sharjah and Abu Dhabi, close to our Business Bay office and Al Sajaa workshop.</p><h3>Related services</h3><ul>{rel}</ul></aside>
</div></section>
<section class="block alt"><div class="wrap two-text"><div>
  <h2>How we run a {e(s["name"].lower())} job</h2>
  <ol class="steps"><li><strong>Site survey.</strong> We inspect, measure and test on site before pricing anything.</li>
  <li><strong>Quotation.</strong> Itemised scope, named system, method and programme. VAT shown separately.</li>
  <li><strong>Execution.</strong> Our own crews, Monday to Saturday, phased around your operations.</li>
  <li><strong>Handover.</strong> Joint inspection, snag closure and handover documents, with the warranty terms set out in the quotation.</li></ol></div>
  <div><h2>Safe sites, every shift</h2><p>Full PPE on every site, a daily toolbox talk before work starts, a risk assessment and method statement for every scope, and barricades, signage and permits around your operations.</p></div>
</div></section>
{project_cards(s["projects"])}
{faq_html(s["faq"] + COMMON_FAQ)}'''
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "@id": SITE + path + "#service", "name": s["name"], "serviceType": s["name"],
         "description": s["desc"], "url": SITE + path, "provider": {"@id": ORG_ID},
         "areaServed": [{"@type": "City", "name": "Dubai"}, {"@type": "City", "name": "Sharjah"}, {"@type": "City", "name": "Abu Dhabi"}]},
        breadcrumb_schema(crumbs)]}
    return path, page(path, s["title"], s["desc"], s["h1"], crumbs, body, schema)


def build_area(a):
    path = f'/areas/{a["slug"]}/'
    crumbs = [("Home", "/"), ("Areas", "/#areas"), (a["name"], None)]
    cards = ''.join(f'<a class="svc-card" href="/services/{s["slug"]}/"><h3>{e(s["name"])}</h3><p>{e(s["lead"])}</p></a>' for s in SERVICES)
    body = f'''<section class="hero"><div class="wrap narrow">
  <span class="kicker">Areas we cover</span><h1>{e(a["h1"])}</h1><p class="lead">{e(a["lead"])}</p>
  <p class="places">{e(a["places"])}</p></div></section>
<section class="block"><div class="wrap"><h2>Our services in {e(a["name"])}</h2><div class="svc-grid">{cards}</div></div></section>
{project_cards(a["projects"])}
{faq_html(COMMON_FAQ)}'''
    schema = {"@context": "https://schema.org", "@graph": [breadcrumb_schema(crumbs)]}
    return path, page(path, a["title"], a["desc"], a["h1"], crumbs, body, schema)


def build_hub():
    path = '/services/'
    crumbs = [("Home", "/"), ("Services", None)]
    cards = ''.join(f'<a class="svc-card" href="/services/{s["slug"]}/"><h3>{e(s["name"])}</h3><p>{e(s["lead"])}</p></a>' for s in SERVICES)
    body = f'''<section class="hero"><div class="wrap narrow"><span class="kicker">What we do</span>
<h1>Eight technical trades. One contract.</h1>
<p class="lead">Many contractors subcontract the technical packages. We keep them in-house, so you deal with one programme, one standard and one warranty contact.</p></div></section>
<section class="block"><div class="wrap"><div class="svc-grid">{cards}</div></div></section>'''
    schema = {"@context": "https://schema.org", "@graph": [breadcrumb_schema(crumbs),
        {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f'{SITE}/services/{s["slug"]}/', "name": s["name"]} for i, s in enumerate(SERVICES)]}]}
    return path, page(path, "Our Services: Eight Technical Trades in the UAE | Z-Link",
                      "Waterproofing, epoxy flooring, industrial coatings, civil works, painting, fire systems, landscaping and turnkey fit-out in Dubai and Sharjah, by our own crews.",
                      "Eight technical trades. One contract.", crumbs, body, schema)


def main():
    out = [build_hub()] + [build_service(s) for s in SERVICES] + [build_area(a) for a in AREAS]
    for path, doc in out:
        d = '.' + path
        os.makedirs(d, exist_ok=True)
        with open(d + 'index.html', 'w', encoding='utf-8') as f:
            f.write(doc)
    urls = ['/'] + [p for p, _ in out]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f'  <url><loc>{SITE}{u}</loc><lastmod>2026-11-07</lastmod></url>')
    sm.append('</urlset>')
    open('sitemap.xml', 'w').write('\n'.join(sm) + '\n')
    print('built', len(out), 'pages;', 'sitemap', len(urls), 'urls')


if __name__ == '__main__':
    main()
