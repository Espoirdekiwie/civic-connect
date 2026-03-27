import streamlit as st
import uuid
from datetime import datetime
import time
import urllib.parse

# Configure page
st.set_page_config(page_title="CIVIC CONNECT // VIBRANT", page_icon="⚡", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Teko:wght@400;600;700&display=swap');

:root {
    --ln-neon: #D6FB41;
    --neon-cyan: #00F0FF;
    --neon-pink: #FF0066;
    --neon-orange: #FF5A00;
    --bg-dark: #070707;
    --card-bg: rgba(20, 20, 20, 0.95);
    --text-main: #FFFFFF;
    --border-color: #333333;
    --critical: #FF003C;
    --success: #00FF7F;
}

/* Base resets for pure white text */
.stApp {
    background-color: var(--bg-dark);
    color: var(--text-main);
}
h1, h2, h3, p, span, div, label {
    color: var(--text-main) !important;
}

/* Typography Overrides */
h1, h2, h3 {
    font-family: 'Teko', sans-serif !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
}

/* Animations - Pop up transitions */
@keyframes popIn {
    0% { opacity: 0; transform: scale(0.9) translateY(40px); }
    60% { opacity: 1; transform: scale(1.02) translateY(-5px); }
    100% { opacity: 1; transform: scale(1) translateY(0); }
}
@keyframes slideDown {
    from { opacity: 0; transform: translateY(-30px); }
    to { opacity: 1; transform: translateY(0); }
}

* { border-radius: 0 !important; }

/* Custom Hero Section */
.hero {
    background: linear-gradient(135deg, rgba(214, 251, 65, 0.08) 0%, rgba(0, 240, 255, 0.08) 100%);
    border-left: 8px solid var(--neon-cyan);
    border-right: 1px solid var(--border-color);
    border-top: 1px solid var(--border-color);
    border-bottom: 1px solid var(--border-color);
    padding: 3rem;
    margin-bottom: 2.5rem;
    position: relative;
    overflow: hidden;
    animation: slideDown 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.hero::after {
    content: "CIVIC // 01";
    position: absolute;
    right: -20px;
    bottom: -30px;
    font-size: 8rem;
    color: rgba(255,255,255,0.03);
    font-family: 'Teko', sans-serif;
    font-weight: 700;
}
.hero h1 {
    margin-bottom: 0;
    font-size: 5rem !important;
    line-height: 1;
    background: linear-gradient(to right, var(--neon-cyan), var(--ln-neon));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero p {
    font-size: 1.25rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #FFFFFF !important;
}

.hero-admin { border-left: 8px solid var(--neon-pink); background: linear-gradient(135deg, rgba(255, 0, 102, 0.08) 0%, rgba(255, 90, 0, 0.08) 100%); }
.hero-admin h1 {
    background: linear-gradient(to right, var(--neon-pink), var(--neon-orange));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Complaint Cards with Pop-In Transition */
.complaint-card {
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    padding: 1.5rem;
    margin-top: 1.5rem;
    margin-bottom: 0.5rem;
    
    /* Pop-up transition effect */
    animation: popIn 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275) backwards;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}
.complaint-card:hover {
    border-color: var(--neon-cyan);
    transform: translateY(-5px) scale(1.02);
    box-shadow: 0 10px 30px rgba(0, 240, 255, 0.15);
}

.emergency-card {
    border-color: var(--critical);
    background: linear-gradient(45deg, rgba(255, 0, 60, 0.1) 0%, transparent 100%);
}
.emergency-card:hover { border-color: var(--critical); box-shadow: 0 10px 30px rgba(255, 0, 60, 0.3); }

.card-header { border-bottom: 1px dashed var(--border-color); padding-bottom: 1rem; margin-bottom: 1rem; }
.card-title { font-size: 2.2rem; margin: 0; color: #FFFFFF !important; }
.card-meta {
    font-size: 0.9rem;
    font-weight: 700;
    text-transform: uppercase;
    display: flex;
    gap: 1.5rem;
    margin-top: 0.5rem;
}
.card-meta span { border: 1px solid var(--border-color); padding: 2px 8px; color: #FFFFFF; background: rgba(0,0,0,0.5); }
.severity-Emergency { color: #FFF !important; border-color: var(--critical) !important; background: var(--critical) !important;}
.severity-MED { color: #FFF !important; border-color: var(--neon-orange) !important; background: var(--neon-orange) !important;}
.severity-LOW { color: #000 !important; border-color: var(--ln-neon) !important; background: var(--ln-neon) !important;}

.card-desc {
    color: #FFFFFF !important;
    line-height: 1.6;
    font-size: 1.15rem;
    background: #000000;
    padding: 1.25rem;
    border-left: 4px solid var(--neon-cyan);
}
.emergency-card .card-desc { border-left-color: var(--critical); }

.card-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 1rem;
    border-top: 1px solid var(--border-color);
    padding-top: 1rem;
}

.badge { padding: 4px 12px; font-size: 0.9rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em; }
.status-Pending { background: #222; color: #FFFFFF; border: 1px solid #555; }
.status-In-Progress { background: rgba(0, 240, 255, 0.2); color: var(--neon-cyan); border: 1px solid var(--neon-cyan); }
.status-Resolved { background: var(--success); color: #000; }

/* Inputs and Buttons */
[data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea {
    background-color: #000000 !important;
    border: 1px solid var(--border-color) !important;
    color: #FFFFFF !important;
    font-family: 'Inter', sans-serif;
}
[data-testid="stTextInput"] input:focus, [data-testid="stTextArea"] textarea:focus {
    border-color: var(--neon-cyan) !important;
    box-shadow: 0 0 10px rgba(0, 240, 255, 0.2) !important;
}

/* Fix Dropdown Text Color */
[data-baseweb="popover"] * {
    color: #000000 !important;
}

[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(to right, var(--ln-neon), var(--neon-cyan)) !important;
    color: #000 !important;
    font-family: 'Teko', sans-serif !important;
    font-size: 2.2rem !important;
    text-transform: uppercase;
    border: none !important;
    width: 100%;
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
}
[data-testid="stFormSubmitButton"] button:hover {
    transform: scale(1.03) !important;
    box-shadow: 0 10px 25px rgba(214, 251, 65, 0.4) !important;
    color: #000 !important;
}

div.stButton > button {
    background: rgba(255,255,255,0.05) !important;
    color: #FFFFFF !important;
    border: 1px solid var(--border-color) !important;
    font-family: 'Teko', sans-serif !important;
    font-size: 1.4rem !important;
    text-transform: uppercase;
    transition: all 0.2s ease !important;
}
div.stButton > button:hover {
    border-color: var(--neon-pink) !important;
    color: var(--neon-pink) !important;
    background: rgba(255, 0, 102, 0.1) !important;
    transform: translateY(-2px);
}

[data-testid="stSidebar"] {
    background: #040404 !important;
    border-right: 1px solid var(--border-color);
}
</style>
""", unsafe_allow_html=True)

# --- STATE INITIALIZATION ---
if 'complaints' not in st.session_state:
    st.session_state.complaints = []
if 'civic_points' not in st.session_state:
    st.session_state.civic_points = 0
if 'badge' not in st.session_state:
    st.session_state.badge = "ROOKIE"
if 'ratings' not in st.session_state:
    st.session_state.ratings = {}

def update_gamification():
    points = st.session_state.civic_points
    if points >= 100: st.session_state.badge = "CHAMPION"
    elif points >= 50: st.session_state.badge = "PRO"
    elif points >= 30: st.session_state.badge = "VETERAN"
    elif points >= 10: st.session_state.badge = "CONTENDER"

def simulate_ai_analysis(description):
    desc_lower = description.lower()
    if any(w in desc_lower for w in ['trash', 'garbage', 'bin', 'dump']):
        return "WASTE MANAGEMENT", "LOW", "3-5 DAYS"
    elif any(w in desc_lower for w in ['pothole', 'crack', 'road']):
        return "INFRASTRUCTURE", "MED", "1-2 WKS"
    elif any(w in desc_lower for w in ['light', 'dark', 'bulb']):
        return "ELECTRICAL", "LOW", "5-7 DAYS"
    else:
        return "GENERAL", "MED", "TBD"

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h1 style='color:#D6FB41;font-size:3.5rem;line-height:1;margin-bottom:0;'>CIVIC<br>CONNECT</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    view_mode = st.radio("NAVIGATION", ["PUBLIC REPORTER", "ADMIN DASHBOARD"], label_visibility="collapsed")
    
    st.markdown("<br><hr style='border-color:#333'>", unsafe_allow_html=True)
    
    if view_mode == "PUBLIC REPORTER":
        st.markdown("<h2 style='color:#FFF;'>USER PROFILE</h2>", unsafe_allow_html=True)
        colA, colB = st.columns(2)
        colA.metric("SCORE", st.session_state.civic_points)
        colB.metric("REPORTS", len([c for c in st.session_state.complaints if 'id' in c]))
        st.markdown(f"**CLASS:** <span style='color:#00F0FF'>{st.session_state.badge}</span>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<h2 style='color:#FFF;'>SYNCED LOCATION</h2>", unsafe_allow_html=True)
        
        if st.session_state.complaints:
            latest_loc = st.session_state.complaints[0].get('location', "City Hall")
            map_query = urllib.parse.quote(latest_loc)
            st.markdown(f"""
            <iframe width="100%" height="250" style="border:1px solid #00F0FF; filter: invert(90%) hue-rotate(180deg) opacity(0.8);"
            src="https://maps.google.com/maps?q={map_query}&t=&z=14&ie=UTF8&iwloc=&output=embed"></iframe>
            """, unsafe_allow_html=True)
            st.caption(f"📍 TRACED: {latest_loc.upper()}")
        else:
            st.info("NO DATA SYNCED.")

# ==========================================
# RESIDENT VIEW
# ==========================================
if view_mode == "PUBLIC REPORTER":
    st.markdown("""
    <div class="hero">
        <h1>REPORT SYSTEM V.02</h1>
        <p>PROVIDE LOCATION AND DESCRIBE THE ISSUE TO SUBMIT A REPORT</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.3], gap="large")

    with col1:
        st.markdown("<h2>SUBMIT REPORT</h2>", unsafe_allow_html=True)
        
        with st.form("ai_complaint_form", clear_on_submit=True):
            issue_location = st.text_input("LOCATION VECTOR (Address/Landmark)", placeholder="e.g. 1st Ave & Main St")
            description = st.text_area("ANOMALY DESCRIPTION", placeholder="Identify the hazard...", height=120)
            
            st.markdown("<br>", unsafe_allow_html=True)
            is_emergency = st.checkbox("CRITICAL OVERRIDE (Life-Threatening Hazard)")
            
            submitted = st.form_submit_button("SYSTEM SUBMIT")
            
            if submitted:
                if not description.strip() or not issue_location.strip():
                    st.error("MISSING VECTOR OR DESCRIPTION.")
                else:
                    with st.spinner("SYNCING..."):
                        time.sleep(0.75)
                        
                        if is_emergency:
                            cat, sev, eta = "CRITICAL", "Emergency", "IMMEDIATE"
                        else:
                            cat, sev, eta = simulate_ai_analysis(description)
                        
                        new_complaint = {
                            "id": str(uuid.uuid4())[:6].upper(),
                            "category": cat,
                            "title": f"INC:{cat}",
                            "description": description.strip(),
                            "location": issue_location.strip(),
                            "severity": sev,
                            "eta": eta,
                            "status": "Pending",
                            "date": datetime.now().strftime("%I:%M %p"),
                            "boosts": 1,
                            "worker": "UNASSIGNED"
                        }
                        st.session_state.complaints.insert(0, new_complaint)
                        st.session_state.civic_points += 15 if is_emergency else 10
                        update_gamification()
                        
                    st.rerun()

    with col2:
        st.markdown("<h2>LIVE FEED</h2>", unsafe_allow_html=True)
        
        if not st.session_state.complaints:
            st.info("FEED OFFLINE. TRANSMIT A REPORT TO BEGIN.")
        else:
            sorted_complaints = sorted(st.session_state.complaints, key=lambda x: (x['severity'] == 'Emergency', x['boosts']), reverse=True)
            
            for idx, complaint in enumerate(sorted_complaints):
                # Dynamically set animation delay so they stagger pop-in
                delay = idx * 0.1
                
                status_formatted = complaint['status'].upper()
                status_class = f"status-{complaint['status'].replace(' ', '-')}"
                sev_class = f"severity-{complaint['severity']}"
                card_type = "emergency-card" if complaint['severity'] == "Emergency" else ""
                
                card_html = f"""
                <div class="complaint-card {card_type}" style="animation-delay: {delay}s;">
                    <div class="card-header">
                        <h3 class="card-title">{complaint['title']}</h3>
                        <div class="card-meta">
                            <span>LOC: {complaint['location']}</span>
                            <span class="{sev_class}">PRIORITY: {complaint['severity']}</span>
                            <span>ETA: {complaint['eta']}</span>
                        </div>
                    </div>
                    <div class="card-desc">"{complaint['description']}"</div>
                    <div class="card-footer">
                        <span class="badge {status_class}">STS: {status_formatted}</span>
                        <span style="color:#FFF; font-size:0.8rem">T-{complaint['date']} | ID:{complaint['id']}</span>
                    </div>
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)
                
                col_btn, col_rate, _ = st.columns([1.5, 2.5, 3])
                with col_btn:
                    if st.button(f"BOOST [ {complaint['boosts']} ]", key=f"boost_{complaint['id']}"):
                        complaint['boosts'] += 1
                        st.session_state.civic_points += 2
                        update_gamification()
                        st.rerun()
                
                with col_rate:
                    if complaint['status'] == 'Resolved':
                        if complaint['id'] not in st.session_state.ratings:
                            rating = st.feedback("stars", key=f"rate_{complaint['id']}")
                            if rating is not None:
                                st.session_state.ratings[complaint['id']] = rating + 1
                                st.session_state.civic_points += 5
                                update_gamification()
                                st.rerun()
                        else:
                            st.markdown(f"<span style='color:#D6FB41'>SYS RATING: {st.session_state.ratings[complaint['id']]}/5</span>", unsafe_allow_html=True)

# ==========================================
# ADMIN DASHBOARD
# ==========================================
elif view_mode == "ADMIN DASHBOARD":
    st.markdown("""
    <div class="hero hero-admin">
        <h1>COMMAND TERMINAL</h1>
        <p>RESTRICTED ACCESS // DEPLOY UNITS AND OVERRIDE STATUS</p>
    </div>
    """, unsafe_allow_html=True)

    total = len(st.session_state.complaints)
    emergencies = sum(1 for c in st.session_state.complaints if c['severity'] == "Emergency")
    pending = sum(1 for c in st.session_state.complaints if c['status'] == "Pending")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("TOTAL INCIDENTS", total)
    m2.metric("CRITICAL", emergencies, delta=f"+{emergencies}" if emergencies>0 else None, delta_color="inverse")
    m3.metric("PENDING", pending)
    
    st.divider()
    
    if not st.session_state.complaints:
        st.success("SYSTEM GREEN.")
    else:
        st.markdown("<h2>ACTIVE INCIDENTS</h2>", unsafe_allow_html=True)
        
        admin_complaints = sorted(st.session_state.complaints, key=lambda x: (
            0 if x['severity']=='Emergency' and x['status']!='Resolved' else 1,
            0 if x['status']=='Pending' else 1
        ))

        for c in admin_complaints:
            with st.container():
                st.markdown(f"<div style='border:1px solid #333; padding:1.5rem; margin-bottom:1rem; background:#0A0A0A;'>", unsafe_allow_html=True)
                colA, colB, colC = st.columns([2, 1, 1], gap="medium")
                
                with colA:
                    st.markdown(f"<span style='color:#FF0066; font-family:Teko; font-size:1.5rem;'>{c['id']} // {c['title']}</span>", unsafe_allow_html=True)
                    st.markdown(f"<div style='color:#FFF;font-size:0.9rem'>**LOC:** {c['location']} &nbsp;|&nbsp; **PRI:** {c['severity']}</div>", unsafe_allow_html=True)
                
                with colB:
                    workers = ["UNASSIGNED", "UNIT: ALPHA", "UNIT: BETA", "SWAT/CRITICAL"]
                    curr_worker_idx = workers.index(c.get('worker', "UNASSIGNED"))
                    new_worker = st.selectbox("DEPLOY UNIT", workers, index=curr_worker_idx, key=f"w_{c['id']}", label_visibility="collapsed")
                    if new_worker != c.get('worker'):
                        c['worker'] = new_worker
                
                with colC:
                    statuses = ["Pending", "In Progress", "Resolved"]
                    curr_status_idx = statuses.index(c['status'])
                    new_status = st.selectbox("STATUS", statuses, index=curr_status_idx, key=f"s_{c['id']}", label_visibility="collapsed")
                    if new_status != c['status']:
                        c['status'] = new_status
                
                st.markdown("</div>", unsafe_allow_html=True)
