from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, HRFlowable

RED = colors.HexColor("#B0211E")
DARK = colors.HexColor("#1a1a1a")
GREY = colors.HexColor("#444444")

doc = SimpleDocTemplate("FIREBREAK-5-Minute-Fit-Check.pdf", pagesize=letter,
    leftMargin=0.6*inch, rightMargin=0.6*inch, topMargin=0.5*inch, bottomMargin=0.45*inch,
    title="FIREBREAK - 5-Minute Fit Check")

title = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=16, textColor=RED, spaceAfter=2, leading=18)
sub   = ParagraphStyle("sub", fontName="Helvetica-Oblique", fontSize=9.5, textColor=GREY, spaceAfter=8, leading=12)
hdr   = ParagraphStyle("hdr", fontName="Helvetica-Bold", fontSize=10.5, textColor=RED, spaceBefore=7, spaceAfter=2, leading=12)
body  = ParagraphStyle("body", fontName="Helvetica", fontSize=9.3, textColor=DARK, leading=12.3)
quote = ParagraphStyle("quote", fontName="Helvetica-Oblique", fontSize=9.3, textColor=DARK, leading=12.3, leftIndent=6)

def bullets(items, st=body):
    return ListFlowable([ListItem(Paragraph(x, st), leftIndent=12, value="•") for x in items],
        bulletType="bullet", start="•", leftIndent=10, bulletFontSize=8, spaceBefore=0, spaceAfter=0)

S = []
S += [Paragraph("FIREBREAK — 5-Minute Fit Check", title)]
S += [Paragraph("Listen 80%, talk 20%. Goal: qualify the fit and book the demo — or bow out honestly.", sub)]
S += [HRFlowable(width="100%", thickness=0.8, color=RED, spaceAfter=4)]

S += [Paragraph("1 · FRAME (30 sec)", hdr)]
S += [Paragraph("&ldquo;Appreciate the 5 minutes. My goal is just to see together if FIREBREAK&rsquo;s worth a closer look — a few quick questions, 60 seconds on what it does, and if it&rsquo;s not a fit I&rsquo;ll say so. Fair?&rdquo;", quote)]

S += [Paragraph("2 · SITUATION (pick 2)", hdr)]
S += [bullets([
  "&ldquo;What are you protecting — and what&rsquo;s your first line when a fire starts?&rdquo;",
  "&ldquo;What do you use today — water, foam, dozers, crews — and where does it fall short?&rdquo;",
  "&ldquo;What keeps you up at night on fire risk?&rdquo;"])]

S += [Paragraph("3 · PROBLEM (pick 1–2, by category)", hdr)]
S += [bullets([
  "<b>Private industry:</b> first 5–10 min before mutual aid? where is water/foam a liability? AFFF transition?",
  "<b>Airports:</b> where in the AFFF phase-out? grass/brush along the field?",
  "<b>Wildfire:</b> holding line with no water? embers ahead of the front?",
  "<b>Rx burns:</b> acres missed to the window? containment close calls?",
  "<b>HOA / WUI:</b> insurance / defensible-space pressure? who clears the greenbelts?"])]

S += [Paragraph("4 · STAKES (pick 1)", hdr)]
S += [bullets([
  "&ldquo;If that went wrong — [spread / escape / non-renewal / loss] — what does it cost you?&rdquo;",
  "&ldquo;What&rsquo;s the cost of living with it another season?&rdquo;"])]

S += [Paragraph("5 · DECISION (pick 1–2)", hdr)]
S += [bullets([
  "&ldquo;Who else is in the conversation if it&rsquo;s a fit?&rdquo;",
  "&ldquo;Any budget / timing window — fiscal year, fire season, renewal/audit?&rdquo;"])]

S += [Paragraph("6 · WHAT IT IS (60 sec)", hdr)]
S += [Paragraph("&ldquo;FIREBREAK fights fire with air — no water, no chemicals. [Category benefit.] Patented, Made in the USA. Field test: ~6x faster than the control burn at 55% output.&rdquo;", quote)]

S += [Paragraph("7 · CLOSE", hdr)]
S += [bullets([
  "<b>FIT →</b> &ldquo;Sounds like a fit. It clicks when you see it move fire — let&rsquo;s grab 15–20 min for a walkthrough on [site]. [day] or [day]?&rdquo;",
  "<b>NOT YET →</b> &ldquo;Don&rsquo;t want to waste your time — [honest read]. If [trigger] changes, I&rsquo;ll reach back out.&rdquo;"])]

S += [HRFlowable(width="100%", thickness=0.8, color=RED, spaceBefore=8, spaceAfter=4)]
S += [Paragraph("<b>QUALIFY —</b> <font color='#1a7a2e'><b>GREEN (go for the demo):</b></font> owns it · feels the pain · has budget/access · has a timing trigger (season, renewal, audit).&nbsp;&nbsp; <font color='#B0211E'><b>RED (slow down):</b></font> no authority · no pain · no timeline · &ldquo;just send info.&rdquo;", body)]

doc.build(S)
print("built FIREBREAK-5-Minute-Fit-Check.pdf")
