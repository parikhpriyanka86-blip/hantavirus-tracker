"""
Hantavirus Outbreak Tracker — Public Information Dashboard
MV Hondius / Andes Virus — Updated June 12, 2026
"""

import streamlit as st
import plotly.graph_objects as go
from datetime import date

OUTBREAK_START = date(2026, 5, 2)
MONITORING_END = date(2026, 6, 21)
PAGE_UPDATED   = "June 12, 2026"

days_left = max(0, (MONITORING_END - date.today()).days)
days_active = (date.today() - OUTBREAK_START).days

st.set_page_config(page_title="Hantavirus Outbreak Tracker", page_icon="🦠",
                    layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"] { font-family:'Inter',sans-serif !important; background:#F7F8FA !important; font-size:16px !important; }
.main .block-container { padding:0 0 4rem !important; max-width:100% !important; }
section[data-testid="stSidebar"] { display:none; }
.stTabs [data-baseweb="tab-list"] { gap:0; background:#fff; border-bottom:2px solid #EEF0F2 !important; padding:0 32px; }
.stTabs [data-baseweb="tab"] { font-size:16px !important; font-weight:500 !important; color:#6B7280 !important; padding:14px 20px !important; border-bottom:3px solid transparent !important; background:transparent !important; }
.stTabs [aria-selected="true"] { color:#374151 !important; border-bottom:3px solid #374151 !important; }
</style>
""", unsafe_allow_html=True)

def card(content, title=None, padding="24px"):
    hdr = ""
    if title:
        hdr = ('<div style="padding:14px 22px;border-bottom:1px solid #EEF0F2;'
               'font-size:13px;font-weight:600;color:#9CA3AF;text-transform:uppercase;'
               'letter-spacing:0.08em;">' + title + '</div>')
    return ('<div style="background:#fff;border:1px solid #E5E7EB;border-radius:14px;'
            'overflow:hidden;margin-bottom:16px;">' + hdr +
            '<div style="padding:' + padding + ';">' + content + '</div></div>')

def bullet(text, color="#6B7280", size="16px"):
    return ('<div style="display:flex;gap:10px;margin-bottom:10px;align-items:flex-start;">'
            '<div style="width:7px;height:7px;border-radius:50%;background:' + color +
            ';flex-shrink:0;margin-top:6px;"></div>'
            '<div style="font-size:' + size + ';color:#374151;line-height:1.6;">' + text + '</div></div>')

def infobox(text, style="blue"):
    styles = {
        "blue":  "background:#F1F5F9;border-left:4px solid #475569;color:#334155;",
        "green": "background:#F0FDF4;border-left:4px solid #16A34A;color:#14532D;",
        "red":   "background:#FEF2F2;border-left:4px solid #B91C1C;color:#7F1D1D;",
        "amber": "background:#FFFBEB;border-left:4px solid #D97706;color:#78350F;",
    }
    s = styles.get(style, styles["blue"])
    return ('<div style="' + s + 'border-radius:0 8px 8px 0;padding:14px 18px;'
            'font-size:16px;line-height:1.7;margin:12px 0;">' + text + '</div>')

def pbg(fig, h=300):
    fig.update_layout(
        height=h, margin=dict(l=0,r=0,t=10,b=0),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", size=13, color="#6B7280"),
        legend=dict(font=dict(size=12), bgcolor="rgba(0,0,0,0)", orientation="h", y=1.12),
        xaxis=dict(gridcolor="#F3F4F6", linecolor="#E5E7EB", tickfont=dict(size=12, color="#6B7280")),
        yaxis=dict(gridcolor="#F3F4F6", tickfont=dict(size=12, color="#6B7280")),
    )

# ═══════════════════════════ HERO ═══════════════════════════
st.markdown(f"""
<div style="background:#1F2937;padding:48px 40px 40px;color:#fff;">
  <div style="max-width:1100px;margin:0 auto;">
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:16px;flex-wrap:wrap;">
      <span style="background:rgba(255,255,255,0.12);border:1px solid rgba(255,255,255,0.2);
                   font-size:11px;font-weight:600;padding:4px 12px;border-radius:20px;
                   letter-spacing:0.08em;">ACTIVE OUTBREAK · DAY {days_active}</span>
      <span style="background:rgba(255,255,255,0.12);border:1px solid rgba(255,255,255,0.2);
                   font-size:11px;font-weight:600;padding:4px 12px;border-radius:20px;
                   letter-spacing:0.08em;">ANDES HANTAVIRUS</span>
      <span style="background:rgba(255,255,255,0.12);border:1px solid rgba(255,255,255,0.2);
                   font-size:11px;font-weight:600;padding:4px 12px;border-radius:20px;
                   letter-spacing:0.08em;">CDC LEVEL 3 ALERT</span>
    </div>
    <div style="font-size:2.4rem;font-weight:700;line-height:1.2;margin-bottom:14px;
                letter-spacing:-0.01em;">Hantavirus Outbreak — MV Hondius Cruise Ship</div>
    <div style="font-size:16px;opacity:0.8;max-width:680px;line-height:1.7;margin-bottom:24px;">
      A rare outbreak of Andes hantavirus — the only strain known to spread between people —
      began on a cruise ship in the South Atlantic in April 2026.
      All passengers have disembarked and are under monitoring in their home countries.
    </div>
    <div style="display:flex;gap:36px;flex-wrap:wrap;">
      <div><div style="font-size:2.6rem;font-weight:700;line-height:1;">13</div>
        <div style="font-size:12px;opacity:0.65;margin-top:3px;font-weight:500;
                    letter-spacing:0.05em;text-transform:uppercase;">Total Cases</div></div>
      <div><div style="font-size:2.6rem;font-weight:700;line-height:1;">3</div>
        <div style="font-size:12px;opacity:0.65;margin-top:3px;font-weight:500;
                    letter-spacing:0.05em;text-transform:uppercase;">Deaths</div></div>
      <div><div style="font-size:2.6rem;font-weight:700;line-height:1;">8</div>
        <div style="font-size:12px;opacity:0.65;margin-top:3px;font-weight:500;
                    letter-spacing:0.05em;text-transform:uppercase;">Countries</div></div>
      <div><div style="font-size:2.6rem;font-weight:700;line-height:1;">600+</div>
        <div style="font-size:12px;opacity:0.65;margin-top:3px;font-weight:500;
                    letter-spacing:0.05em;text-transform:uppercase;">Contacts Traced</div></div>
      <div><div style="font-size:2.6rem;font-weight:700;line-height:1;color:#86EFAC;">{days_left}</div>
        <div style="font-size:12px;opacity:0.65;margin-top:3px;font-weight:500;
                    letter-spacing:0.05em;text-transform:uppercase;">Days to End Monitoring</div></div>
    </div>
    <div style="margin-top:20px;font-size:12px;opacity:0.45;letter-spacing:0.06em;">
      WHO · CDC · ECDC · CDPH · Global.health · Updated {PAGE_UPDATED}
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="background:#FFFBEB;border-bottom:1px solid #FDE68A;padding:14px 40px;
            display:flex;align-items:center;gap:12px;">
  <span style="font-size:20px;">ℹ️</span>
  <div style="font-size:15px;color:#78350F;line-height:1.5;">
    <strong>Think you may have been exposed?</strong> Contact your local public health
    department immediately ·
    Monitoring period for exposed travelers ends ~June 21, 2026
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "How It Started", "Global Spread", "Outbreak Data", "Clinical Guide", "Updates"
])

# ═══════════════════════ TAB 1 ═══════════════════════
with tab1:
    st.markdown("<div style='max-width:1100px;margin:0 auto;padding:24px 24px 0;'>", unsafe_allow_html=True)

    col_a, col_b = st.columns([1.1, 1])

    with col_a:
        st.markdown(card("""
        <div style="font-size:16px;color:#111827;line-height:1.8;margin-bottom:18px;">
          On <strong>April 1, 2026</strong>, the expedition vessel <strong>MV Hondius</strong>
          departed Ushuaia, Argentina — carrying <strong>86 passengers and 61 crew from 23
          countries</strong> — on a voyage through the South Atlantic, including Antarctica
          and remote islands.
        </div>
        <div style="font-size:16px;color:#111827;line-height:1.8;margin-bottom:18px;">
          In early April, several passengers developed flu-like illness, initially thought
          to be a common shipboard virus. By late April, multiple passengers were critically
          ill with severe pneumonia and respiratory failure.
        </div>
        <div style="font-size:16px;color:#111827;line-height:1.8;margin-bottom:18px;">
          WHO was notified on <strong>May 2</strong>. On <strong>May 6</strong>, the cause was
          confirmed: <strong>Andes virus</strong> — the only hantavirus known to spread from
          person to person.
        </div>
        <div style="font-size:16px;color:#111827;line-height:1.8;">
          All 147 passengers disembarked in Tenerife, Spain on May 10 and were repatriated
          to their home countries for monitoring and care.
        </div>
        """, title="The Story"), unsafe_allow_html=True)

    with col_b:
        voyage = [
            ("Apr 1",  "#64748B", "Departs Ushuaia, Argentina"),
            ("Early Apr","#D97706","Passengers develop flu-like illness"),
            ("Apr 24", "#B91C1C", "First cases evacuated for care"),
            ("May 2",  "#B91C1C", "WHO notified · 3 deaths reported"),
            ("May 6",  "#7C3AED", "Andes virus confirmed · CDC Level 3"),
            ("May 10", "#D97706", "All passengers disembark Tenerife"),
            ("May 25", "#475569", "13th case confirmed (Spain)"),
            ("Jun 21", "#16A34A", "42-day monitoring period ends"),
        ]
        tl_html = ""
        for d, col, txt in voyage:
            tl_html += ('<div style="display:flex;gap:12px;margin-bottom:14px;align-items:flex-start;">'
                        '<div style="width:9px;height:9px;border-radius:50%;background:' + col +
                        ';flex-shrink:0;margin-top:5px;"></div><div>'
                        '<div style="font-size:12px;font-weight:600;color:#9CA3AF;margin-bottom:2px;">' + d + '</div>'
                        '<div style="font-size:15px;color:#374151;line-height:1.5;">' + txt + '</div></div></div>')
        st.markdown(card(tl_html, title="Voyage Timeline"), unsafe_allow_html=True)

        st.markdown(infobox(
            "<strong>Why Andes virus is different:</strong> It is the only hantavirus known "
            "to spread person-to-person, through close, sustained contact with a symptomatic "
            "person. All other hantaviruses spread only through rodent contact.", "amber"),
            unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ═══════════════════════ TAB 2 — GLOBAL SPREAD (with world map) ═══════════════════════
with tab2:
    st.markdown("<div style='max-width:1100px;margin:0 auto;padding:24px 24px 0;'>", unsafe_allow_html=True)

    # Case distribution map with ESRI imagery basemap
    country_centers = [
        ("Netherlands", "NLD", 5.3, 52.1, 4, "#1E40AF"),
        ("United Kingdom", "GBR", -2.0, 54.0, 3, "#1E40AF"),
        ("Spain", "ESP", -3.7, 40.0, 2, "#0D9488"),
        ("Germany", "DEU", 10.5, 51.2, 1, "#B91C1C"),
        ("Switzerland", "CHE", 8.2, 46.8, 1, "#7C3AED"),
        ("France", "FRA", 2.5, 46.6, 1, "#EA580C"),
        ("Canada", "CAN", -106.3, 56.1, 1, "#0D9488"),
    ]
    fig_map = go.Figure(go.Scattermap(
        lon=[c[2] for c in country_centers],
        lat=[c[3] for c in country_centers],
        mode="markers+text",
        marker=dict(size=[18+c[4]*7 for c in country_centers],
                    color=[c[5] for c in country_centers], opacity=0.65),
        text=[c[0] for c in country_centers],
        textposition="top center",
        textfont=dict(size=12, color="#1F2937", family="Inter"),
        hovertext=[c[0] + ": " + str(c[4]) + (" cases" if c[4]>1 else " case") for c in country_centers],
        hoverinfo="text",
    ))
    fig_map.update_layout(
        height=400, margin=dict(l=0,r=0,t=0,b=0),
        map=dict(
            style="white-bg",
            layers=[dict(
                sourcetype="raster", below="traces",
                source=["https://server.arcgisonline.com/ArcGIS/rest/services/"
                        "World_Street_Map/MapServer/tile/{z}/{y}/{x}"]
            )],
            center=dict(lon=-10, lat=45), zoom=2.2,
            bounds=dict(west=-130, east=40, south=10, north=70)
        ),
    )
    st.markdown(card("", title="Confirmed Cases by Country"), unsafe_allow_html=True)
    st.plotly_chart(fig_map, use_container_width=True)
    st.caption("Circle size = number of confirmed cases · ESRI World Street Map · "
               "Source: WHO DON, Global.health, national health agencies")

    country_data = [
        ("Netherlands", "NLD", 4, 2),
        ("United Kingdom", "GBR", 3, 1),
        ("Spain", "ESP", 2, 0),
        ("Germany", "DEU", 1, 1),
        ("Switzerland", "CHE", 1, 0),
        ("France", "FRA", 1, 0),
        ("Canada", "CAN", 1, 0),
    ]

    col_a, col_b = st.columns(2)

    with col_a:
        bars_html = ""
        for country, iso, cases_n, deaths in sorted(country_data, key=lambda x: x[2], reverse=True):
            if cases_n == 0:
                continue
            pct = int((cases_n / 4) * 100)
            col_bar = "#B91C1C" if deaths > 0 else "#64748B"
            deaths_txt = (' · <span style="color:#B91C1C;">' + str(deaths) +
                          (' deaths' if deaths > 1 else ' death') + '</span>') if deaths else ""
            bars_html += ('<div style="margin-bottom:14px;">'
                          '<div style="display:flex;justify-content:space-between;margin-bottom:5px;font-size:15px;">'
                          '<span style="font-weight:500;color:#1F2937;">' + country + '</span>'
                          '<span style="color:#6B7280;">' + str(cases_n) +
                          (' cases' if cases_n > 1 else ' case') + deaths_txt + '</span></div>'
                          '<div style="background:#F3F4F6;border-radius:4px;height:10px;overflow:hidden;">'
                          '<div style="width:' + str(pct) + '%;height:100%;background:' + col_bar +
                          ';border-radius:4px;"></div></div></div>')
        st.markdown(card(bars_html, title="Cases by Country"), unsafe_allow_html=True)

    with col_b:
        st.markdown(card(f"""
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
          <div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;
                      padding:16px;text-align:center;">
            <div style="font-size:2.2rem;font-weight:700;color:#1F2937;line-height:1;">12</div>
            <div style="font-size:13px;color:#6B7280;margin-top:4px;">Confirmed</div>
          </div>
          <div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;
                      padding:16px;text-align:center;">
            <div style="font-size:2.2rem;font-weight:700;color:#1F2937;line-height:1;">1</div>
            <div style="font-size:13px;color:#6B7280;margin-top:4px;">Probable</div>
          </div>
          <div style="background:#FEF2F2;border-radius:10px;padding:16px;text-align:center;">
            <div style="font-size:2.2rem;font-weight:700;color:#B91C1C;line-height:1;">3</div>
            <div style="font-size:13px;color:#B91C1C;margin-top:4px;">Deaths · CFR 23%</div>
          </div>
          <div style="background:#F0FDF4;border-radius:10px;padding:16px;text-align:center;">
            <div style="font-size:2.2rem;font-weight:700;color:#16A34A;line-height:1;">0</div>
            <div style="font-size:13px;color:#16A34A;margin-top:4px;">Secondary cases</div>
          </div>
        </div>
        {infobox("<strong>No secondary transmission identified.</strong> All 13 cases are individuals who were aboard MV Hondius — none acquired the infection after disembarking.", "green")}
        """, title="Outbreak Summary"), unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ═══════════════════════ TAB 3 — OUTBREAK DATA ═══════════════════════
with tab3:
    st.markdown("<div style='max-width:1100px;margin:0 auto;padding:24px 24px 0;'>", unsafe_allow_html=True)

    EPI_DATES     = ["Apr 6","Apr 24","Apr 27","Apr 28","Apr 30","May 1","May 10","May 12","May 25"]
    EPI_CONFIRMED = [0, 2, 1, 1, 1, 1, 1, 1, 1]
    EPI_PROBABLE  = [1, 0, 0, 1, 0, 0, 0, 0, 0]
    EPI_CUM       = [1, 3, 4, 6, 7, 8, 9, 10, 11]

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(card("", title="Epidemic Curve — Cases by Onset Date"), unsafe_allow_html=True)
        fig_e = go.Figure()
        fig_e.add_trace(go.Bar(x=EPI_DATES, y=EPI_CONFIRMED, name="Confirmed",
                               marker_color="#475569", opacity=0.9))
        fig_e.add_trace(go.Bar(x=EPI_DATES, y=EPI_PROBABLE, name="Probable",
                               marker_color="#CBD5E1", opacity=0.9))
        pbg(fig_e, 280)
        fig_e.update_layout(barmode="stack", xaxis=dict(tickangle=45, tickfont=dict(size=11)))
        st.plotly_chart(fig_e, use_container_width=True)
        st.caption("Deaths recorded among earliest cases · Source: WHO DON")

    with col_b:
        st.markdown(card("", title="Cumulative Confirmed Cases"), unsafe_allow_html=True)
        fig_cum = go.Figure(go.Scatter(
            x=EPI_DATES, y=EPI_CUM, mode="lines+markers",
            line=dict(color="#475569", width=3),
            fill="tozeroy", fillcolor="rgba(71,85,105,0.07)",
            marker=dict(size=9, color="#475569", line=dict(width=2, color="#fff"))))
        pbg(fig_cum, 280)
        st.plotly_chart(fig_cum, use_container_width=True)
        st.caption("Cumulative confirmed cases · Source: Global.health / WHO")

    # Linelist
    st.markdown(card("", title="Case Linelist — 13 Cases (12 Confirmed, 1 Probable)"), unsafe_allow_html=True)

    linelist = [
        ["1",  "Dutch",    "Probable",  "Deceased",               "Index case. Suspected land exposure before boarding."],
        ["2",  "Dutch",    "Confirmed", "Deceased",               "Close contact of Case 1."],
        ["3",  "British",  "Confirmed", "Hospitalized · ICU",     "Evacuated for intensive care."],
        ["4",  "German",   "Confirmed", "Deceased",               "Pneumonia developed rapidly."],
        ["5",  "Dutch",    "Confirmed", "Hospitalized",           "Transferred for care in Netherlands."],
        ["6",  "British",  "Confirmed", "Hospitalized",           "Transferred for care in Netherlands."],
        ["7",  "Swiss",    "Confirmed", "Hospitalized · Isolated","Treated at university hospital."],
        ["8",  "British",  "Confirmed", "Hospitalized · Isolated","Coordinated repatriation and isolation."],
        ["9",  "French",   "Confirmed", "Hospitalized · ICU",     "Confirmed positive on repatriation flight."],
        ["10", "Spanish",  "Confirmed", "Recovered",              "Asymptomatic positive among repatriated passengers."],
        ["11", "Canadian", "Confirmed", "Recovered",              "Identified after returning home."],
        ["12", "Dutch",    "Confirmed", "Hospitalized · Isolated","Reported via national health authority."],
        ["13", "Spanish",  "Confirmed", "Hospitalized · Isolated","Confirmed positive May 25, 2026."],
    ]
    status_pill = {"Confirmed": "background:#F1F5F9;color:#334155;",
                    "Probable":  "background:#FEF3C7;color:#92400E;"}
    outcome_pill = {
        "Deceased": "background:#1F2937;color:#fff;",
        "Hospitalized · ICU": "background:#FEE2E2;color:#B91C1C;",
        "Hospitalized": "background:#FEF3C7;color:#92400E;",
        "Hospitalized · Isolated": "background:#FEF3C7;color:#92400E;",
        "Recovered": "background:#D1FAE5;color:#065F46;",
    }
    rows = ""
    for num, nat, status, outcome, notes in linelist:
        ss = status_pill.get(status, "background:#F3F4F6;color:#374151;")
        os_ = outcome_pill.get(outcome, "background:#F3F4F6;color:#374151;")
        rows += ('<tr style="border-bottom:1px solid #F9FAFB;">'
                '<td style="padding:10px 12px;font-size:14px;font-weight:600;color:#6B7280;white-space:nowrap;">Case ' + num + '</td>'
                '<td style="padding:10px 12px;font-size:14px;color:#374151;white-space:nowrap;">' + nat + '</td>'
                '<td style="padding:10px 12px;"><span style="font-size:13px;padding:3px 10px;border-radius:12px;font-weight:500;' + ss + '">' + status + '</span></td>'
                '<td style="padding:10px 12px;"><span style="font-size:13px;padding:3px 10px;border-radius:12px;font-weight:500;white-space:nowrap;' + os_ + '">' + outcome + '</span></td>'
                '<td style="padding:10px 12px;font-size:14px;color:#6B7280;max-width:280px;">' + notes + '</td></tr>')

    table_html = ('<table style="width:100%;border-collapse:collapse;"><thead>'
                  '<tr style="background:#F9FAFB;border-bottom:2px solid #E5E7EB;">'
                  '<th style="padding:10px 12px;text-align:left;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.07em;color:#6B7280;">Case</th>'
                  '<th style="padding:10px 12px;text-align:left;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.07em;color:#6B7280;">Nationality</th>'
                  '<th style="padding:10px 12px;text-align:left;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.07em;color:#6B7280;">Status</th>'
                  '<th style="padding:10px 12px;text-align:left;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.07em;color:#6B7280;">Outcome</th>'
                  '<th style="padding:10px 12px;text-align:left;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.07em;color:#6B7280;">Notes</th></tr></thead>'
                  '<tbody>' + rows + '</tbody></table>')
    st.markdown(table_html, unsafe_allow_html=True)
    st.caption("Source: WHO DON-600/601, Global.health Hondius hantavirus dataset, national health agencies")

    # Case definitions
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        st.markdown(card(
            bullet("<strong>Confirmed:</strong> Meets clinical criteria and tested positive for Andes hantavirus.", "#B91C1C") +
            bullet("<strong>Probable:</strong> Has matching symptoms and close contact with a known/likely case.", "#D97706"),
            title="Case Definitions"), unsafe_allow_html=True)
    with col_d2:
        st.markdown(card(
            bullet("<strong>Inconclusive:</strong> Conflicting or incomplete lab evidence, repeat testing pending.", "#6B7280") +
            bullet("<strong>Suspected:</strong> Shared transport with a case, plus fever and one of: muscle aches, chills, headache, GI symptoms, or breathing problems.", "#475569"),
            title="Case Definitions — continued"), unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ═══════════════════════ TAB 4 — CLINICAL GUIDE ═══════════════════════
with tab4:
    st.markdown("<div style='max-width:1100px;margin:0 auto;padding:24px 24px 0;'>", unsafe_allow_html=True)

    st.markdown(infobox(
        "<strong>This information is for general public awareness.</strong> "
        "If you think you have been exposed or are experiencing symptoms, contact your "
        "local public health department immediately.", "red"),
        unsafe_allow_html=True)

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown(card(
            '<div style="font-size:16px;color:#374151;line-height:1.8;margin-bottom:16px;">'
            'Hantavirus Pulmonary Syndrome (HPS) is a severe lung disease. The Andes virus '
            'strain in this outbreak is unique because it is the only hantavirus that can '
            'spread between people.</div>'
            '<div style="font-size:16px;color:#374151;line-height:1.8;margin-bottom:16px;">'
            '<strong>Case fatality rate in this outbreak: 23%</strong> (3 of 13 cases). '
            'There is no approved antiviral treatment — '
            '<strong>early hospital care is the most important factor in survival.</strong></div>' +
            infobox("Andes virus does not naturally occur in North America. The rodent that carries it lives only in southern South America.", "blue"),
            title="What is Hantavirus?"), unsafe_allow_html=True)

        # Symptoms — single source of truth
        phase1 = "".join(['<div style="background:#F8FAFC;border-radius:8px;padding:10px 14px;font-size:14px;color:#374151;">' + s + '</div>'
                          for s in ["🌡️ Fever 38–40°C","💪 Severe muscle aches","😴 Extreme fatigue","🤕 Severe headache","🤢 Nausea & vomiting","💫 Dizziness"]])
        phase2 = "".join(['<div style="background:#FEF2F2;border-radius:8px;padding:10px 14px;font-size:14px;color:#7F1D1D;">' + s + '</div>'
                          for s in ["🫁 Sudden shortness of breath","💧 Fluid in lungs","📉 Low oxygen levels","⬇️ Low blood pressure","💓 Rapid heart rate","🩸 Low platelet count"]])
        st.markdown(card(
            '<div style="background:#F8FAFC;border-radius:10px;padding:14px 16px;margin-bottom:12px;font-size:15px;color:#334155;">'
            '<strong>Phase 1 — Prodromal (Days 1–5)</strong><br>Begins 4–42 days after exposure. Looks like the flu.</div>'
            '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:16px;">' + phase1 + '</div>'
            '<div style="background:#FEF2F2;border-radius:10px;padding:14px 16px;margin-bottom:12px;font-size:15px;color:#7F1D1D;">'
            '<strong>Phase 2 — Emergency (Days 5–10)</strong><br>Can deteriorate within hours. Call 911 immediately.</div>'
            '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:16px;">' + phase2 + '</div>'
            '<div style="background:#F0FDF4;border-radius:10px;padding:14px 16px;font-size:15px;color:#14532D;">'
            '<strong>Phase 3 — Recovery (Weeks to months)</strong><br>Survivors who receive ICU care begin gradual recovery.</div>',
            title="Symptoms — Know the Signs"), unsafe_allow_html=True)

    with col_b:
        st.markdown(card(
            '<div style="background:#FEF2F2;border-radius:10px;padding:16px;margin-bottom:16px;">'
            '<div style="font-size:16px;font-weight:600;color:#B91C1C;margin-bottom:8px;">Call 911 immediately if you have:</div>' +
            bullet("Difficulty breathing or shortness of breath", "#B91C1C") +
            bullet("Chest pain or tightness", "#B91C1C") +
            bullet("Low blood pressure or fainting", "#B91C1C") +
            bullet("Confusion or extreme weakness", "#B91C1C") + '</div>'
            '<div style="background:#FFFBEB;border-radius:10px;padding:16px;">'
            '<div style="font-size:17px;font-weight:600;color:#92400E;margin-bottom:8px;">Contact your local public health department if you:</div>' +
            bullet("Were aboard MV Hondius or had close contact with a confirmed case", "#D97706") +
            bullet("Have fever plus muscle aches within 42 days of possible exposure", "#D97706") +
            bullet("Are unsure whether you need to be monitored", "#D97706") + '</div>' +
            infobox("<strong>Tell your doctor or the ER about your possible hantavirus exposure BEFORE you arrive</strong> — this helps them prepare proper precautions.", "blue"),
            title="What To Do"), unsafe_allow_html=True)

        # Clinicians
        diag = (bullet("High clinical suspicion required — early symptoms mimic influenza") +
                bullet("<strong>PCR for Andes virus RNA</strong> — specialized public health labs only") +
                bullet("Serology (IgM/IgG) positive from symptom onset") +
                bullet("CBC: thrombocytopenia + immunoblasts = highly suggestive") +
                bullet("Chest imaging: bilateral interstitial infiltrates") +
                bullet("Echo: reduced ejection fraction if cardiogenic component present"))
        treat = (bullet("<strong>No approved antiviral</strong> for Andes hantavirus HPS", "#B91C1C") +
                bullet("Early ICU admission before respiratory failure develops", "#B91C1C") +
                bullet("Oxygen → mechanical ventilation, lung-protective strategy", "#B91C1C") +
                bullet("Cautious fluid management — avoid volume overload", "#B91C1C") +
                bullet("Vasopressors for cardiogenic shock", "#B91C1C") +
                bullet("ECMO considered early for severe shock — case series show benefit", "#B91C1C") +
                bullet("Ribavirin: no proven benefit for HPS", "#B91C1C"))
        st.markdown(card(
            '<div style="font-size:13px;font-weight:600;color:#9CA3AF;text-transform:uppercase;letter-spacing:0.07em;margin-bottom:10px;">Diagnosis</div>' + diag +
            '<div style="font-size:13px;font-weight:600;color:#9CA3AF;text-transform:uppercase;letter-spacing:0.07em;margin:18px 0 10px;">Treatment</div>' + treat +
            infobox("<strong>For clinicians:</strong> Contact your state public health laboratory before sending specimens. Early infectious disease consultation is recommended.", "blue"),
            title="For Clinicians — Diagnosis & Treatment"), unsafe_allow_html=True)

        # Prevention
        st.markdown('<div style="font-size:13px;font-weight:700;color:#9CA3AF;'
                    'text-transform:uppercase;letter-spacing:0.08em;margin:8px 0 12px;">'
                    'Prevention — Avoiding Rodent Exposure</div>', unsafe_allow_html=True)
        prev_steps = [
            ("Ventilate first", "Open windows and doors for at least 30 minutes before entering any space with signs of rodent activity."),
            ("Never dry sweep", "Spray droppings with a 10% bleach solution, let it soak for 5 minutes, then wet-mop. Never sweep or vacuum dry droppings."),
            ("Wear protection", "Wear an N95 respirator mask and gloves when cleaning any rodent-contaminated area."),
            ("Seal entry points", "Block holes as small as a pencil width using steel wool, caulk, or hardware cloth."),
            ("Store food sealed", "Keep food, pet food, and birdseed in rodent-proof sealed containers."),
            ("Camping safely", "Use tents with floors, sleep off the ground, air out cabins before use, and never feed wild rodents."),
        ]
        for i, (title, desc) in enumerate(prev_steps, 1):
            with st.expander(str(i) + ". " + title):
                st.markdown('<div style="font-size:16px;color:#374151;line-height:1.7;padding:4px 0;">' + desc + '</div>',
                           unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ═══════════════════════ TAB 5 — UPDATES ═══════════════════════
with tab5:
    st.markdown("<div style='max-width:1100px;margin:0 auto;padding:24px 24px 0;'>", unsafe_allow_html=True)
    col_a, col_b = st.columns([1.6, 1])

    updates = [
        ("Jun 12", "#475569", "Tracker reflects updated Global.health case dataset: 13 total cases (12 confirmed, 1 probable). No secondary cases identified."),
        ("May 25", "#475569", "13th case confirmed in Spain."),
        ("May 18", "#D97706", "Quarantine period continues for repatriated travelers under public health monitoring."),
        ("May 15", "#16A34A", "Earlier inconclusive case in repatriated traveler determined NEGATIVE on further testing."),
        ("May 13", "#475569", "WHO update (DON-601) following repatriation of passengers — 11 cases reported at this point."),
        ("May 10", "#D97706", "All 147 passengers disembark in Tenerife, Spain and begin repatriation to home countries."),
        ("May 6",  "#B91C1C", "Andes virus confirmed by laboratory testing. CDC issues Level 3 Health Alert (HAN-528)."),
        ("May 2",  "#B91C1C", "WHO notified of cluster aboard MV Hondius — 3 deaths, multiple critically ill. International response begins."),
        ("Apr 24", "#D97706", "First cases evacuated from ship for urgent medical care."),
        ("Apr 6",  "#94A3B8", "Index case — probable symptom onset, suspected land exposure before boarding."),
        ("Apr 1",  "#64748B", "MV Hondius departs Ushuaia, Argentina with 86 passengers and 61 crew from 23 countries."),
    ]

    with col_a:
        st.markdown(card("", title="Full Situation Update Log"), unsafe_allow_html=True)
        upd_html = ""
        for d, col, txt in updates:
            upd_html += ('<div style="display:flex;gap:12px;padding:10px 0;border-bottom:1px solid #F9FAFB;align-items:flex-start;">'
                         '<div style="width:7px;height:7px;border-radius:50%;background:' + col + ';flex-shrink:0;margin-top:6px;"></div>'
                         '<div style="font-size:13px;font-weight:600;color:' + col + ';min-width:48px;flex-shrink:0;padding-top:1px;">' + d + '</div>'
                         '<div style="font-size:15px;color:#374151;line-height:1.6;">' + txt + '</div></div>')
        st.markdown(card(upd_html), unsafe_allow_html=True)
        st.markdown(
            '<div style="padding:12px 16px;background:#F9FAFB;border-radius:8px;'
            'font-size:12px;color:#9CA3AF;line-height:1.7;">'
            'Sources: WHO DON-600/601 · ECDC · CDC HAN-528 · Global.health Hondius hantavirus dataset · '
            'Updated ' + PAGE_UPDATED + '</div>', unsafe_allow_html=True)

    with col_b:
        st.markdown(card(
            infobox("<strong>Report possible exposure</strong><br><br>Were you aboard MV Hondius or in close contact with a confirmed case? Contact your local public health department immediately.", "red"),
            title="Report Exposure"), unsafe_allow_html=True)

        st.markdown(card("", title="Official Sources"), unsafe_allow_html=True)
        for name, url in [
            ("CDC — Hantavirus Situation Summary", "https://www.cdc.gov/hantavirus/situation-summary/index.html"),
            ("CDC — HAN-528 Health Alert", "https://www.cdc.gov/han/php/notices/han00528.html"),
            ("WHO — Disease Outbreak Notice", "https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON604"),
            ("ECDC — Outbreak Update", "https://www.ecdc.europa.eu/en/infectious-disease-topics/hantavirus-infection/surveillance-and-updates/andes-hantavirus-outbreak"),
        ]:
            st.link_button(name, url, use_container_width=True)

        st.markdown(
            '<div style="background:#fff;border:1px solid #E5E7EB;border-radius:14px;'
            'padding:16px 20px;font-size:12px;color:#9CA3AF;line-height:1.7;text-align:center;">'
            'Hantavirus Outbreak Tracker<br>Updated ' + PAGE_UPDATED + '<br>'
            'Not a substitute for clinical guidance.</div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)