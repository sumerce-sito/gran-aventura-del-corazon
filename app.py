import streamlit as st
import streamlit.components.v1 as components
import random, requests
from datetime import date, datetime

try:
    from streamlit_lottie import st_lottie
    LOTTIE_OK = True
except ImportError:
    LOTTIE_OK = False

try:
    import plotly.graph_objects as go
    import plotly.express as px
    PLOTLY_OK = True
except ImportError:
    PLOTLY_OK = False

# ── PAGE CONFIG ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="La Gran Aventura del Corazón",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── LOTTIE LOADER ──────────────────────────────────────────────────────────────
@st.cache_data(show_spinner=False)
def load_lottie(url: str):
    try:
        r = requests.get(url, timeout=6)
        return r.json() if r.status_code == 200 else None
    except Exception:
        return None

LOTTIE_URLS = {
    "hero":     "https://assets6.lottiefiles.com/packages/lf20_qp1q7mct.json",
    "trophy":   "https://assets1.lottiefiles.com/packages/lf20_jbrw3hcz.json",
    "prayer":   "https://assets9.lottiefiles.com/packages/lf20_jcikwtux.json",
    "compass":  "https://assets4.lottiefiles.com/packages/lf20_wd1udlcz.json",
    "stars":    "https://assets2.lottiefiles.com/packages/lf20_qp1q7mct.json",
}

# ── DATA ───────────────────────────────────────────────────────────────────────
NIVELES = [
    {
        "id":1,"supertitulo":"NIVEL 1","titulo":"Estación de Descubrimiento","icono":"⚡",
        "color":"#06b6d4","color_dark":"#0891b2","glow":"rgba(6,182,212,0.4)",
        "sabias_que":"¡No necesitas palabras elegantes ni perfectas para hablar con Dios! Él prefiere que le hables como a tu mejor amigo.",
        "idea_titulo":"El Superpoder de 1 Minuto",
        "idea_texto":'A veces pensamos que rezar es muy difícil, pero no saber qué decir es el mejor comienzo. Un solo minuto donde le dices la verdad ("Aquí estoy, acompáñame") vale muchísimo más que horas de hablar como un robot.',
        "mision":'¡Levanta la mano si alguna vez te has quedado sin palabras! Hoy, siéntate en silencio un minuto y solo di en tu mente: "Hola Dios, soy yo, quiero estar contigo!"',
        "resumen":"Para orar, solo necesitas estar presente, no ser perfecto.","widget":"timer",
        "svg_anim": """<svg viewBox="0 0 80 80" width="70" height="70">
          <defs><filter id="glow1"><feGaussianBlur stdDeviation="3" result="blur"/>
          <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
          <polygon points="44,5 28,38 40,38 36,75 56,35 42,35" fill="#06b6d4" filter="url(#glow1)" opacity="0.9">
            <animate attributeName="opacity" values="0.6;1;0.6" dur="1.2s" repeatCount="indefinite"/>
            <animateTransform attributeName="transform" type="scale" values="1;1.08;1" dur="1.2s" additive="sum" repeatCount="indefinite"/>
          </polygon></svg>""",
    },
    {
        "id":2,"supertitulo":"NIVEL 2","titulo":"El Entrenamiento Diario","icono":"🔋",
        "color":"#22c55e","color_dark":"#16a34a","glow":"rgba(34,197,94,0.4)",
        "sabias_que":"Tu corazón es como la batería de una tablet o consola; ¡necesita recargarse todos los días para funcionar al máximo!",
        "idea_titulo":"Las 3 Recargas Mágicas",
        "idea_texto":"No dependas de si tienes ganas o no. Conéctate tres veces al día:\n\n🌅 **Mañana** — Para encender el día.\n⚡ **Día** — Pausa rápida para no apagarte.\n🌙 **Noche** — Para cerrar y descansar en paz.",
        "mision":"¡Tócate la cabeza, el pecho y la panza! Ese es tu indicador de energía. Mañana, antes de mirar cualquier pantalla, haz la señal de la cruz lentamente para iniciar tu carga.",
        "resumen":"Tres pausas cortas al día mantienen tu corazón conectado y fuerte.","widget":"recargas",
        "svg_anim": """<svg viewBox="0 0 80 80" width="70" height="70">
          <rect x="14" y="20" width="44" height="50" rx="6" fill="none" stroke="#22c55e" stroke-width="3"/>
          <rect x="28" y="14" width="16" height="8" rx="3" fill="#22c55e"/>
          <rect x="18" y="54" width="36" height="10" rx="3" fill="#22c55e">
            <animate attributeName="height" values="0;10;16;10" dur="2s" repeatCount="indefinite"/>
            <animate attributeName="y" values="64;54;48;54" dur="2s" repeatCount="indefinite"/>
          </rect>
          <rect x="18" y="42" width="36" height="10" rx="3" fill="#22c55e" opacity="0.6">
            <animate attributeName="opacity" values="0;0.6;0.6;0" dur="2s" begin="0.5s" repeatCount="indefinite"/>
          </rect>
          <rect x="18" y="30" width="36" height="10" rx="3" fill="#22c55e" opacity="0.3">
            <animate attributeName="opacity" values="0;0.3;0.3;0" dur="2s" begin="1s" repeatCount="indefinite"/>
          </rect></svg>""",
    },
    {
        "id":3,"supertitulo":"NIVEL 3","titulo":"La Base Secreta","icono":"🛡️",
        "color":"#a855f7","color_dark":"#7c3aed","glow":"rgba(168,85,247,0.4)",
        "sabias_que":"¡Dios también te habla cuando tú te quedas callado! El silencio es su idioma favorito.",
        "idea_titulo":"La Postura del Héroe",
        "idea_texto":"Tu cuerpo también reza. Si te acuestas, tu cerebro pensará en dormir. Sentarte derecho con manos abiertas te convierte en una antena gigante.\n\n📏 **Espalda** super recta\n🤲 **Manos** listas\n🦶 **Pies** firmes",
        "mision":'¡Ponte en "Postura de Héroe" ahora mismo! Cierra los ojos y cuenta hasta 10. ¡Siente la paz!',
        "resumen":"El silencio y tu postura preparan tu cuerpo para escuchar.","widget":"postura",
        "svg_anim": """<svg viewBox="0 0 80 80" width="70" height="70">
          <defs><filter id="glow3"><feGaussianBlur stdDeviation="4" result="b"/>
          <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
          <circle cx="40" cy="40" r="26" fill="none" stroke="#a855f7" stroke-width="2" opacity="0.3">
            <animate attributeName="r" values="26;34;26" dur="2.5s" repeatCount="indefinite"/>
            <animate attributeName="opacity" values="0.3;0;0.3" dur="2.5s" repeatCount="indefinite"/>
          </circle>
          <path d="M40 14 L52 35 L66 38 L55 52 L57 68 L40 60 L23 68 L25 52 L14 38 L28 35 Z"
            fill="#a855f7" filter="url(#glow3)" opacity="0.9">
            <animate attributeName="opacity" values="0.7;1;0.7" dur="2s" repeatCount="indefinite"/>
          </path></svg>""",
    },
    {
        "id":4,"supertitulo":"NIVEL 4","titulo":"El Mapa del Tesoro","icono":"🗺️",
        "color":"#fbbf24","color_dark":"#d97706","glow":"rgba(251,191,36,0.4)",
        "sabias_que":"¡La Biblia no es una herramienta escolar aburrida, es una carta secreta escrita especialmente para ti!",
        "idea_titulo":"Decodificando el Mensaje",
        "idea_texto":'Se llama "Lectio Divina". Lee un pedacito de la Biblia muy despacio. No tienes que entender todo. Solo busca una frase o palabra que "brille" en tu corazón.',
        "mision":"¡Finge que tienes una lupa de súper detective! Busca cualquier herramienta de lectura en tu casa, ábrela al azar y lee solo la primera línea en cámara súper lenta.",
        "resumen":"No leas para estudiar todo, lee para encontrar tu pista secreta de hoy.","widget":"diario",
        "svg_anim": """<svg viewBox="0 0 80 80" width="70" height="70">
          <circle cx="40" cy="40" r="22" fill="none" stroke="#fbbf24" stroke-width="3" opacity="0.5"/>
          <line x1="40" y1="18" x2="40" y2="62" stroke="#fbbf24" stroke-width="2">
            <animateTransform attributeName="transform" type="rotate" from="0 40 40" to="360 40 40" dur="4s" repeatCount="indefinite"/>
          </line>
          <line x1="40" y1="22" x2="40" y2="52" stroke="#d97706" stroke-width="3">
            <animateTransform attributeName="transform" type="rotate" from="0 40 40" to="360 40 40" dur="1.5s" repeatCount="indefinite"/>
          </line>
          <circle cx="40" cy="40" r="5" fill="#fbbf24">
            <animate attributeName="opacity" values="0.5;1;0.5" dur="1s" repeatCount="indefinite"/>
          </circle></svg>""",
    },
    {
        "id":5,"supertitulo":"NIVEL 5","titulo":"El Panel de Control","icono":"🎮",
        "color":"#ec4899","color_dark":"#db2777","glow":"rgba(236,72,153,0.4)",
        "sabias_que":"Dios no quiere que finjas estar feliz si en realidad estás triste o muy asustado. ¡Él prefiere la verdad!",
        "idea_titulo":"El Botón de Emergencias",
        "idea_texto":'Puedes usar tu superpoder en CUALQUIER emoción:\n\n😨 Si tienes miedo → *"Señor, ¡abrázame!"*\n😢 Si estás triste → *"Señor, acompáñame"*\n😄 Si estás muy feliz → *"¡Gracias por esto tan genial!"*',
        "mision":"¡Pon tu mejor cara de asombro! Luego cara triste, y luego una gran sonrisa. En todas esas caras, Dios está sentado a tu lado.",
        "resumen":"Cualquier emoción que sientas es el momento perfecto para hablar con Dios.","widget":"emociones",
        "svg_anim": """<svg viewBox="0 0 80 80" width="70" height="70">
          <rect x="12" y="25" width="56" height="35" rx="12" fill="none" stroke="#ec4899" stroke-width="3"/>
          <circle cx="26" cy="42" r="7" fill="none" stroke="#ec4899" stroke-width="2"/>
          <circle cx="23" cy="42" r="3" fill="#ec4899"><animate attributeName="cx" values="23;26;29;26;23" dur="1.5s" repeatCount="indefinite"/></circle>
          <circle cx="58" cy="36" r="4" fill="#ec4899"><animate attributeName="opacity" values="1;0.2;1" dur="0.8s" repeatCount="indefinite"/></circle>
          <circle cx="66" cy="42" r="4" fill="#ec4899"><animate attributeName="opacity" values="0.2;1;0.2" dur="0.8s" repeatCount="indefinite"/></circle>
          <circle cx="58" cy="48" r="4" fill="#ec4899"><animate attributeName="opacity" values="1;0.2;1" dur="0.8s" begin="0.4s" repeatCount="indefinite"/></circle>
          <circle cx="50" cy="42" r="4" fill="#ec4899"><animate attributeName="opacity" values="0.2;1;0.2" dur="0.8s" begin="0.4s" repeatCount="indefinite"/></circle>
          <rect x="34" y="56" width="12" height="6" rx="3" fill="#ec4899"/></svg>""",
    },
    {
        "id":6,"supertitulo":"NIVEL 6","titulo":"La Gran Reunión","icono":"⛪",
        "color":"#3b82f6","color_dark":"#2563eb","glow":"rgba(59,130,246,0.4)",
        "sabias_que":"¡La Misa no es un evento donde solo vas a sentarte y mirar, es la reunión de equipo más importante del universo!",
        "idea_titulo":"El Banquete de los Héroes",
        "idea_texto":"En la Misa, la magia se hace real. Dios se esconde en el pan para entrar en ti y darte fuerza. Llévale un regalo invisible: ofrécele un esfuerzo o una preocupación de la semana.",
        "mision":"¡Choca los cinco en el aire! En tu próxima Misa, lleva una alegría o un problema en tus manos imaginarias y, cuando levanten el pan, entrégaselo a Dios como tu regalo secreto.",
        "resumen":"La Misa es un encuentro real para llenarte de la fuerza de Dios.","widget":"regalo",
        "svg_anim": """<svg viewBox="0 0 80 80" width="70" height="70">
          <defs><filter id="glow6"><feGaussianBlur stdDeviation="3" result="b"/>
          <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
          <circle cx="40" cy="40" r="28" fill="none" stroke="#3b82f6" stroke-width="1" opacity="0.2">
            <animate attributeName="r" values="28;38;28" dur="3s" repeatCount="indefinite"/>
            <animate attributeName="opacity" values="0.2;0;0.2" dur="3s" repeatCount="indefinite"/>
          </circle>
          <circle cx="40" cy="40" r="18" fill="none" stroke="#3b82f6" stroke-width="1.5" opacity="0.4">
            <animate attributeName="r" values="18;26;18" dur="3s" begin="0.5s" repeatCount="indefinite"/>
            <animate attributeName="opacity" values="0.4;0;0.4" dur="3s" begin="0.5s" repeatCount="indefinite"/>
          </circle>
          <path d="M40 15 L40 26 M34 20 L46 20 M28 30 L28 65 L52 65 L52 30 L44 30 L44 20 L36 20 L36 30 Z"
            fill="#3b82f6" filter="url(#glow6)" opacity="0.9"/>
          <path d="M33 65 L33 50 Q40 44 47 50 L47 65" fill="#1e40af"/></svg>""",
    },
    {
        "id":7,"supertitulo":"NIVEL 7","titulo":"El Explorador Imparable","icono":"🧭",
        "color":"#f97316","color_dark":"#ea580c","glow":"rgba(249,115,22,0.4)",
        "sabias_que":"¡Los mejores exploradores del mundo también tropiezan, se pierden y olvidan su mapa a veces!",
        "idea_titulo":"Volver a Empezar",
        "idea_texto":'Si un día te da pereza o se te olvida orar, ¡no pasa nada! Dios no se enoja. Él solo te espera. El truco secreto es regresar y decir: "Perdón, me distraje, ¡pero aquí estoy otra vez!"',
        "mision":'¡Da un salto muy alto donde estés! Cada vez que falles, usa ese "salto" invisible para volver a empezar. ¡Nunca es tarde!',
        "resumen":"El verdadero éxito no es no fallar nunca, sino volver a intentarlo siempre.","widget":"salto",
        "svg_anim": """<svg viewBox="0 0 80 80" width="70" height="70">
          <circle cx="40" cy="40" r="28" fill="none" stroke="#f97316" stroke-width="2.5" opacity="0.5"/>
          <circle cx="40" cy="40" r="5" fill="#f97316"/>
          <line x1="40" y1="12" x2="40" y2="40" stroke="#f97316" stroke-width="3" stroke-linecap="round">
            <animateTransform attributeName="transform" type="rotate" from="0 40 40" to="360 40 40" dur="3s" repeatCount="indefinite"/>
          </line>
          <line x1="40" y1="20" x2="40" y2="40" stroke="#ea580c" stroke-width="2" stroke-linecap="round">
            <animateTransform attributeName="transform" type="rotate" from="0 40 40" to="-360 40 40" dur="8s" repeatCount="indefinite"/>
          </line>
          <circle cx="40" cy="12" r="3" fill="#fbbf24">
            <animateTransform attributeName="transform" type="rotate" from="0 40 40" to="360 40 40" dur="3s" repeatCount="indefinite"/>
          </circle></svg>""",
    },
]

EMOCIONES = {
    "😨 Miedo":    {"oracion":'"Señor, tengo miedo. Dame tu paz. ¡Abrázame!"',"color":"#06b6d4","tip":"Respira profundo 3 veces. Dios está más cerca cuando tienes miedo."},
    "😢 Tristeza": {"oracion":'"Señor, me siento triste. No te vayas. Acompáñame."',"color":"#3b82f6","tip":"No tienes que fingir que estás bien. Dios recibe tu tristeza."},
    "😤 Enojo":    {"oracion":'"Señor, estoy enojado. Calma mi corazón."',"color":"#f97316","tip":"El enojo no te separa de Dios. Cuéntaselo antes de actuar."},
    "😰 Ansiedad": {"oracion":'"Señor, mi mente no para. Recibe mis preocupaciones."',"color":"#a855f7","tip":"Suelta una preocupación a la vez. Imagínala en manos de Dios."},
    "😄 Alegría":  {"oracion":'"¡Gracias, Señor! Quiero que estés en este momento."',"color":"#22c55e","tip":"¡La alegría también es oración! ¡Celebra con Dios!"},
    "😴 Cansancio":{"oracion":'"Señor, estoy agotado. Sostén lo que yo no puedo."',"color":"#fbbf24","tip":"A veces la mejor oración es dormirse confiando en Dios."},
    "😕 Confusión":{"oracion":'"Señor, no entiendo nada. Ilumíname."',"color":"#ec4899","tip":"No necesitas entender todo. Solo confiar en quien sí entiende."},
}

LOGROS = [
    {"id":"primer",  "icono":"🥇","nombre":"Primer Paso",        "desc":"Completaste el Nivel 1",          "req":lambda p,s:1 in p},
    {"id":"mitad",   "icono":"⚡","nombre":"A Mitad de Camino",  "desc":"Completaste 4 niveles",           "req":lambda p,s:len(p)>=4},
    {"id":"todos",   "icono":"🏆","nombre":"Explorador Total",   "desc":"Completaste los 7 niveles",       "req":lambda p,s:len(p)==7},
    {"id":"diario",  "icono":"📓","nombre":"Guardián de Pistas", "desc":"Escribiste en el Diario Secreto", "req":lambda p,s:len(s.get("diario",[]))>0},
    {"id":"regalo",  "icono":"🎁","nombre":"Portador de Regalos","desc":"Enviaste un regalo invisible",    "req":lambda p,s:s.get("regalo_enviado",False)},
    {"id":"saltos",  "icono":"🦘","nombre":"Saltador Imparable", "desc":"Diste 5 saltos de vuelta",        "req":lambda p,s:s.get("saltos",0)>=5},
    {"id":"emociones","icono":"🎭","nombre":"Maestro Emocional", "desc":"Usaste el panel de emociones",   "req":lambda p,s:s.get("emocion_usada",False)},
    {"id":"recargas","icono":"🔋","nombre":"Energía Máxima",     "desc":"Activaste las 3 recargas",        "req":lambda p,s:s.get("recargas_completas",False)},
]

FRASES = ["¡Cada día que oras eres más fuerte! 💪","¡Un explorador nunca se rinde! 🧭",
          "Dios te está esperando. ¡Allá vamos! ⚡","¡Tu corazón tiene superpoderes! ❤️",
          "¡Lo que empezaste hoy, Dios lo termina! 🙏","¡Eres un héroe del corazón! 🛡️"]

# ── CSS ────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Nunito:ital,wght@0,400;0,600;0,700;0,800;1,400&display=swap');

/* ── BASE ── */
html,body,[data-testid="stAppViewContainer"],[data-testid="stMain"],.main,.block-container {
    background:#080614 !important; font-family:'Nunito',sans-serif !important; color:#e2e8ff !important;
}
[data-testid="stSidebar"] {
    background:linear-gradient(180deg,#0f0a1e 0%,#080614 100%) !important;
    border-right:1px solid rgba(168,85,247,0.2) !important;
}
[data-testid="stSidebar"] * { color:#c4b5fd !important; font-family:'Nunito',sans-serif !important; }
[data-testid="stSidebar"] input { background:rgba(168,85,247,0.08) !important; border:1px solid rgba(168,85,247,0.3) !important; border-radius:10px !important; color:#e2e8ff !important; }
[data-testid="stSidebar"] hr  { border-color:rgba(168,85,247,0.2) !important; }
[data-testid="stSidebar"] .stRadio > label { color:#7c3aed !important; font-size:10px !important; letter-spacing:2px !important; text-transform:uppercase !important; }
[data-testid="stSidebar"] .stRadio label span { font-size:13px !important; color:#c4b5fd !important; }

/* ── PROGRESS BAR ── */
.stProgress>div>div { background:linear-gradient(90deg,#7c3aed,#06b6d4) !important; border-radius:99px !important; box-shadow:0 0 10px rgba(6,182,212,0.5) !important; }
.stProgress>div { background:rgba(255,255,255,0.06) !important; border-radius:99px !important; }

/* ── BUTTONS ── */
.stButton>button { border-radius:12px !important; font-family:'Nunito',sans-serif !important; font-weight:700 !important; font-size:14px !important; transition:all 0.25s !important; border:1px solid rgba(168,85,247,0.3) !important; background:rgba(168,85,247,0.1) !important; color:#c4b5fd !important; }
.stButton>button:hover { transform:translateY(-2px) !important; box-shadow:0 0 20px rgba(168,85,247,0.4) !important; border-color:rgba(168,85,247,0.7) !important; }
.stButton>button[kind="primary"] { background:linear-gradient(135deg,#7c3aed,#06b6d4) !important; border:none !important; color:white !important; box-shadow:0 0 16px rgba(124,58,237,0.4) !important; }
.stButton>button[kind="primary"]:hover { box-shadow:0 0 30px rgba(6,182,212,0.5) !important; }

/* ── INPUTS ── */
.stTextInput>div>div>input,.stTextArea>div>div>textarea {
    background:rgba(168,85,247,0.07) !important; border:1px solid rgba(168,85,247,0.25) !important;
    border-radius:12px !important; color:#e2e8ff !important; font-family:'Nunito',sans-serif !important;
}
.stTextInput>div>div>input:focus,.stTextArea>div>div>textarea:focus { border-color:rgba(6,182,212,0.6) !important; box-shadow:0 0 12px rgba(6,182,212,0.2) !important; }
.stTextInput label,.stTextArea label { color:#c4b5fd !important; font-weight:700 !important; }
.stCheckbox label { color:#c4b5fd !important; font-size:14px !important; }
.stFormSubmitButton>button { background:linear-gradient(135deg,#7c3aed,#06b6d4) !important; border:none !important; color:white !important; font-weight:700 !important; border-radius:12px !important; box-shadow:0 0 14px rgba(124,58,237,0.4) !important; }

/* ── EXPANDER ── */
.streamlit-expanderHeader { background:rgba(168,85,247,0.08) !important; border-radius:12px !important; color:#c4b5fd !important; font-weight:700 !important; font-size:14px !important; border:1px solid rgba(168,85,247,0.2) !important; }
.streamlit-expanderContent { background:rgba(168,85,247,0.04) !important; border:1px solid rgba(168,85,247,0.15) !important; border-top:none !important; border-radius:0 0 12px 12px !important; color:#cbd5e1 !important; }

/* ── METRICS ── */
[data-testid="metric-container"] { background:rgba(168,85,247,0.08) !important; border:1px solid rgba(168,85,247,0.2) !important; border-radius:14px !important; padding:16px !important; }
[data-testid="metric-container"] label { color:#7c3aed !important; font-size:11px !important; letter-spacing:1px !important; text-transform:uppercase !important; }
[data-testid="metric-container"] [data-testid="stMetricValue"] { color:#e2e8ff !important; font-family:'Orbitron',monospace !important; }

/* ── ALERTS ── */
[data-testid="stAlert"] { background:rgba(6,182,212,0.1) !important; border:1px solid rgba(6,182,212,0.3) !important; color:#a5f3fc !important; border-radius:12px !important; }

/* ── HIDE DEFAULTS ── */
#MainMenu { visibility:hidden; } footer { visibility:hidden; }

/* ════ KEYFRAME ANIMATIONS ════ */
@keyframes float {
    0%,100% { transform:translateY(0px) rotate(0deg); }
    33%      { transform:translateY(-8px) rotate(2deg); }
    66%      { transform:translateY(-4px) rotate(-1deg); }
}
@keyframes fadeInUp {
    from { opacity:0; transform:translateY(24px); }
    to   { opacity:1; transform:translateY(0); }
}
@keyframes pulseGlow {
    0%,100% { box-shadow:0 0 12px var(--glow,rgba(124,58,237,0.3)); }
    50%     { box-shadow:0 0 32px var(--glow,rgba(124,58,237,0.7)); }
}
@keyframes gradientShift {
    0%   { background-position:0% 50%; }
    50%  { background-position:100% 50%; }
    100% { background-position:0% 50%; }
}
@keyframes shimmer {
    from { background-position:-200% 0; }
    to   { background-position:200% 0; }
}
@keyframes spinSlow { from { transform:rotate(0deg); } to { transform:rotate(360deg); } }
@keyframes blink  { 0%,100%{opacity:1} 50%{opacity:0.4} }
@keyframes scaleIn { from{transform:scale(0.8);opacity:0} to{transform:scale(1);opacity:1} }
@keyframes heartbeat { 0%,100%{transform:scale(1)} 15%{transform:scale(1.15)} 30%{transform:scale(1)} 45%{transform:scale(1.08)} }

/* ════ CUSTOM COMPONENTS ════ */

/* HERO */
.hero {
    background:linear-gradient(135deg,#0f0a1e 0%,#1a0f3c 50%,#0a1628 100%);
    border-radius:24px; padding:0 0 40px; margin-bottom:24px;
    border:1px solid rgba(168,85,247,0.25); overflow:hidden; position:relative;
    animation:fadeInUp 0.6s ease;
}
.hero-canvas-wrap { width:100%; height:220px; position:relative; overflow:hidden; border-radius:24px 24px 0 0; }
.hero-body { padding:0 36px 8px; text-align:center; position:relative; z-index:2; }
.hero-eyebrow {
    display:inline-flex; align-items:center; gap:8px;
    background:rgba(124,58,237,0.15); border:1px solid rgba(124,58,237,0.4);
    color:#a78bfa; font-size:11px; letter-spacing:3px; text-transform:uppercase;
    padding:6px 20px; border-radius:99px; margin-bottom:16px;
    font-family:'Orbitron',monospace; font-weight:400;
    animation:fadeInUp 0.5s ease 0.2s both;
}
.hero-title {
    font-family:'Orbitron',monospace; font-size:clamp(24px,4vw,46px); font-weight:900;
    background:linear-gradient(135deg,#e2e8ff,#a78bfa,#06b6d4,#fbbf24,#e2e8ff);
    background-size:300% 300%;
    -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
    line-height:1.15; margin-bottom:8px;
    animation:gradientShift 4s ease infinite, fadeInUp 0.6s ease 0.3s both;
}
.hero-name   { font-size:22px; color:#e2e8ff; font-weight:800; margin-bottom:4px; animation:fadeInUp 0.6s ease 0.4s both; }
.hero-tagline{ font-size:14px; color:#6b7280; font-style:italic; margin-bottom:28px; animation:fadeInUp 0.6s ease 0.5s both; }
.hero-icons  { display:flex; justify-content:center; gap:22px; flex-wrap:wrap; animation:fadeInUp 0.6s ease 0.6s both; }
.hero-icon-wrap { text-align:center; }
.hero-bubble {
    width:58px; height:58px; border-radius:16px; display:flex; align-items:center; justify-content:center;
    font-size:25px; margin:0 auto 6px; border:1px solid; animation:float 3s ease-in-out infinite;
}
.hero-bubble:nth-child(1){animation-delay:0s} .hero-bubble:nth-child(2){animation-delay:0.5s}
.hero-bubble:nth-child(3){animation-delay:1s}  .hero-bubble:nth-child(4){animation-delay:1.5s}
.hero-icon-lbl { font-size:9px; letter-spacing:1.5px; text-transform:uppercase; font-weight:700; }

/* INTRO CARD */
.intro-card {
    background:rgba(124,58,237,0.07); border:1px solid rgba(124,58,237,0.2);
    border-radius:16px; padding:20px 26px; text-align:center; margin-bottom:20px;
    animation:fadeInUp 0.6s ease 0.4s both;
}
.intro-tag { font-size:10px; letter-spacing:2px; color:#7c3aed; text-transform:uppercase; font-weight:800; margin-bottom:8px; font-family:'Orbitron',monospace; }
.intro-txt  { font-size:14px; color:#94a3b8; line-height:1.75; font-style:italic; }

/* NIVEL HEADER */
.nivel-hdr {
    border-radius:18px 18px 0 0; padding:20px 24px 18px; color:#fff;
    position:relative; overflow:hidden; animation:fadeInUp 0.5s ease;
}
.nivel-hdr::after { content:''; position:absolute; inset:0; background:rgba(0,0,0,0.2); pointer-events:none; }
.nivel-hdr-content { position:relative; z-index:2; display:flex; align-items:center; gap:20px; }
.nivel-tag { font-size:9px; letter-spacing:3px; opacity:0.75; font-weight:800; text-transform:uppercase; margin-bottom:4px; font-family:'Orbitron',monospace; }
.nivel-ttl { font-family:'Orbitron',monospace; font-size:20px; font-weight:700; }

/* RESUMEN */
.resumen { padding:15px 22px; color:#fff; font-style:italic; font-size:14px; font-weight:700; display:flex; align-items:center; gap:10px; border-radius:12px; margin-top:8px; }

/* WIDGET BOX */
.wbox {
    background:linear-gradient(135deg,#0f0a1e,#12122a);
    border-radius:18px; padding:24px; border:1px solid;
    text-align:center; color:#e2e8ff; margin:8px 0 16px;
}
.wbox-title { font-family:'Orbitron',monospace; font-size:16px; font-weight:700; margin-bottom:4px; }
.wbox-sub   { font-size:13px; color:#6b7280; font-style:italic; margin-bottom:16px; }

/* LOGRO */
.logro { border-radius:14px; padding:13px 16px; display:flex; align-items:center; gap:14px; margin-bottom:10px; border:1px solid; transition:all 0.2s; }
.logro-on  { background:rgba(124,58,237,0.12); border-color:rgba(124,58,237,0.4); animation:scaleIn 0.4s ease; }
.logro-off { background:rgba(255,255,255,0.02); border-color:rgba(255,255,255,0.05); filter:grayscale(1) opacity(0.35); }

/* POWER ROW */
.prow { background:rgba(124,58,237,0.08); border-radius:12px; padding:12px 16px; display:flex; align-items:center; gap:12px; margin-bottom:8px; border:1px solid rgba(124,58,237,0.2); color:#c4b5fd; font-size:14px; transition:all .2s; }
.prow:hover { background:rgba(124,58,237,0.16); transform:translateX(4px); }

/* MISION DIA */
.mdia { background:rgba(124,58,237,0.1); border-radius:14px; padding:16px 18px; border:1px solid rgba(124,58,237,0.3); }
.mdia-tag { font-size:9px; letter-spacing:2px; color:#7c3aed; text-transform:uppercase; margin-bottom:4px; font-weight:800; font-family:'Orbitron',monospace; }
.mdia-txt  { font-size:13px; color:#94a3b8; font-style:italic; line-height:1.65; }

/* CHIP */
.chip { background:rgba(124,58,237,0.15); border:1px solid rgba(124,58,237,0.35); border-radius:99px; padding:5px 14px; font-size:12px; color:#a78bfa; display:inline-block; margin:3px; white-space:nowrap; font-weight:700; }

/* FINAL */
.fcard {
    background:linear-gradient(135deg,#0f0a1e,#1a0f3c,#0a1628);
    border-radius:24px; padding:52px 36px; text-align:center;
    border:1px solid rgba(124,58,237,0.3);
    box-shadow:0 0 60px rgba(124,58,237,0.15),0 0 120px rgba(6,182,212,0.08);
    animation:pulseGlow 3s ease-in-out infinite;
    --glow: rgba(124,58,237,0.3);
}
.fcard-title {
    font-family:'Orbitron',monospace; font-size:28px; font-weight:900;
    background:linear-gradient(135deg,#e2e8ff,#a78bfa,#06b6d4);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
    margin-bottom:14px; animation:gradientShift 4s ease infinite;
    background-size:300% 300%;
}
.fcard-msg { font-size:15px; color:#94a3b8; font-style:italic; line-height:1.85; max-width:500px; margin:0 auto 24px; }

/* TROPHY ICON ANIMATION */
.trophy-anim { animation:heartbeat 1.5s ease-in-out infinite; display:inline-block; font-size:80px; }

/* NIVEL GRID */
.nivel-grid-btn { animation:fadeInUp 0.4s ease; }
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE ──────────────────────────────────────────────────────────────
defaults = {
    "progress":set(),"page":"Inicio","nombre":"",
    "diario":[],"regalo_enviado":False,"regalo_texto":"",
    "saltos":0,"emocion_usada":False,
    "recargas":set(),"recargas_completas":False,
    "notas":{},"mision_dia_idx":None,"mision_dia_fecha":None,
}
for k,v in defaults.items():
    if k not in st.session_state: st.session_state[k]=v

hoy=str(date.today())
if st.session_state.mision_dia_fecha!=hoy:
    st.session_state.mision_dia_idx=random.randint(0,6); st.session_state.mision_dia_fecha=hoy
mision_dia=NIVELES[st.session_state.mision_dia_idx]

def logros_ok():
    p,s=st.session_state.progress,st.session_state
    return [lg for lg in LOGROS if lg["req"](p,s)]

# ── CANVAS DE PARTÍCULAS ───────────────────────────────────────────────────────
PARTICLE_CANVAS = """
<canvas id="c" style="width:100%;height:220px;display:block;background:transparent"></canvas>
<script>
const c=document.getElementById('c');
const ctx=c.getContext('2d');
c.width=c.offsetWidth||900; c.height=220;
const COLORS=['#7c3aed','#06b6d4','#fbbf24','#a855f7','#22c55e','#ec4899','#f97316'];
const N=60;
const pts=Array.from({length:N},()=>({
  x:Math.random()*c.width, y:Math.random()*c.height,
  r:Math.random()*2.5+0.5,
  vx:(Math.random()-.5)*0.6, vy:(Math.random()-.5)*0.4,
  c:COLORS[Math.floor(Math.random()*COLORS.length)],
  a:Math.random(),
  da:(Math.random()-.5)*0.015,
  glow:Math.random()*6+2
}));
function draw(){
  ctx.clearRect(0,0,c.width,c.height);
  // connections
  for(let i=0;i<N;i++){
    for(let j=i+1;j<N;j++){
      const d=Math.hypot(pts[i].x-pts[j].x,pts[i].y-pts[j].y);
      if(d<120){
        ctx.beginPath();
        ctx.moveTo(pts[i].x,pts[i].y);
        ctx.lineTo(pts[j].x,pts[j].y);
        ctx.strokeStyle=pts[i].c+'22';
        ctx.lineWidth=0.5*(1-d/120);
        ctx.stroke();
      }
    }
  }
  pts.forEach(p=>{
    p.x+=p.vx; p.y+=p.vy;
    p.a+=p.da; if(p.a<0.1||p.a>1){p.da*=-1;}
    if(p.x<0)p.x=c.width; if(p.x>c.width)p.x=0;
    if(p.y<0)p.y=c.height; if(p.y>c.height)p.y=0;
    ctx.save();
    ctx.shadowColor=p.c; ctx.shadowBlur=p.glow;
    ctx.globalAlpha=p.a;
    ctx.beginPath(); ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
    ctx.fillStyle=p.c; ctx.fill();
    ctx.restore();
  });
  requestAnimationFrame(draw);
}
draw();
window.addEventListener('resize',()=>{c.width=c.offsetWidth||900;});
</script>
"""

# ── SIDEBAR ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<p style="font-family:Orbitron,monospace;font-size:13px;font-weight:900;color:#a78bfa;letter-spacing:2px;">⚔️ LA GRAN AVENTURA</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:11px;color:#4b3a72;font-style:italic;margin-top:-12px;">del Corazón · 7 Niveles</p>', unsafe_allow_html=True)
    st.divider()

    nombre_in=st.text_input("👤 Tu nombre de explorador",value=st.session_state.nombre,placeholder="Escribe tu nombre...")
    if nombre_in!=st.session_state.nombre: st.session_state.nombre=nombre_in

    st.divider()

    done=len(st.session_state.progress); total=len(NIVELES)
    st.markdown(f'<p style="font-size:11px;font-weight:700;color:#a78bfa;font-family:Orbitron,monospace;letter-spacing:1px;">PROGRESO · {done}/{total}</p>', unsafe_allow_html=True)
    st.progress(done/total)

    # Anillo SVG de progreso
    pct=done/total; angle=pct*360; r=30; circ=2*3.14159*r
    dash=pct*circ; gap=circ-dash
    st.markdown(f"""
    <div style="display:flex;justify-content:center;margin:8px 0">
    <svg width="80" height="80" viewBox="0 0 80 80">
      <circle cx="40" cy="40" r="{r}" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="7"/>
      <circle cx="40" cy="40" r="{r}" fill="none" stroke="url(#pg)" stroke-width="7"
        stroke-dasharray="{dash:.1f} {gap:.1f}" stroke-linecap="round"
        transform="rotate(-90 40 40)">
        <animate attributeName="stroke-dasharray" from="0 {circ:.1f}" to="{dash:.1f} {gap:.1f}" dur="1.2s" fill="freeze"/>
      </circle>
      <defs><linearGradient id="pg" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0%" stop-color="#7c3aed"/><stop offset="100%" stop-color="#06b6d4"/>
      </linearGradient></defs>
      <text x="40" y="45" text-anchor="middle" fill="#e2e8ff"
        font-family="Orbitron,monospace" font-size="14" font-weight="700">{int(pct*100)}%</text>
    </svg></div>""", unsafe_allow_html=True)

    n_logros=len(logros_ok())
    st.markdown(f'<span class="chip">🏅 {n_logros}/{len(LOGROS)} logros</span><span class="chip">📓 {len(st.session_state.diario)} entradas</span>', unsafe_allow_html=True)
    st.divider()

    opciones=["🏠 Inicio"]+[f"{n['icono']} {n['supertitulo']}: {n['titulo']}" for n in NIVELES]+["🏆 ¡Completado!"]
    choice=st.radio("nav",opciones,label_visibility="collapsed")
    if   choice=="🏠 Inicio":        st.session_state.page="Inicio"
    elif choice=="🏆 ¡Completado!":  st.session_state.page="Final"
    else:
        nid=int(choice.split("NIVEL ")[1].split(":")[0]); st.session_state.page=f"nivel_{nid}"

    st.divider()
    st.markdown(f"""<div class="mdia">
        <div class="mdia-tag">🎯 misión del día</div>
        <div style="font-size:15px;font-weight:800;color:#c4b5fd;margin-bottom:4px;">{mision_dia['icono']} {mision_dia['titulo']}</div>
        <div class="mdia-txt">"{mision_dia['mision'][:80]}…"</div></div>""", unsafe_allow_html=True)

    st.divider()
    frase=FRASES[date.today().toordinal()%len(FRASES)]
    st.markdown(f'<p style="font-size:11px;color:#4b3a72;font-style:italic;text-align:center;">{frase}</p>', unsafe_allow_html=True)


# ── PLOTLY HELPERS ─────────────────────────────────────────────────────────────
def radar_superpoderes():
    if not PLOTLY_OK: return
    nombres=[n["titulo"] for n in NIVELES]
    valores=[1 if n["id"] in st.session_state.progress else 0 for n in NIVELES]
    colores=["#22c55e" if v else "#1c1535" for v in valores]

    fig=go.Figure()
    # fondo gris
    fig.add_trace(go.Scatterpolar(
        r=[1]*7, theta=nombres, fill='toself',
        fillcolor='rgba(168,85,247,0.05)', line=dict(color='rgba(168,85,247,0.2)',width=1),
        name='Total', hoverinfo='skip'
    ))
    # completados
    fig.add_trace(go.Scatterpolar(
        r=valores+[valores[0]], theta=nombres+[nombres[0]], fill='toself',
        fillcolor='rgba(6,182,212,0.18)',
        line=dict(color='#06b6d4',width=2.5),
        name='Completados',
        marker=dict(color=['#06b6d4' if v else 'rgba(0,0,0,0)' for v in valores+[valores[0]]],size=10)
    ))
    fig.update_layout(
        polar=dict(
            bgcolor='rgba(15,10,30,0.0)',
            radialaxis=dict(visible=False,range=[0,1]),
            angularaxis=dict(
                tickfont=dict(size=11,color='#c4b5fd',family='Nunito'),
                linecolor='rgba(168,85,247,0.2)',
                gridcolor='rgba(168,85,247,0.1)',
            )
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        margin=dict(l=50,r=50,t=30,b=30),
        height=340,
    )
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})

def donut_progreso():
    if not PLOTLY_OK: return
    done=len(st.session_state.progress); remaining=7-done
    fig=go.Figure(go.Pie(
        values=[done,remaining],
        labels=["Completados","Pendientes"],
        hole=0.72,
        marker=dict(colors=["#7c3aed","rgba(168,85,247,0.08)"],
                    line=dict(color=['#a855f7','rgba(0,0,0,0)'],width=[2,0])),
        textinfo='none', hoverinfo='label+value',
    ))
    fig.add_annotation(
        text=f"<b>{done}/7</b>", x=0.5, y=0.5, showarrow=False,
        font=dict(size=24,color='#e2e8ff',family='Orbitron'),
        xanchor='center', yanchor='middle'
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False, margin=dict(l=10,r=10,t=10,b=10), height=200,
    )
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})

def bar_logros():
    if not PLOTLY_OK: return
    ok=logros_ok(); nombres_ok=[lg["nombre"] for lg in ok]
    todos=[lg["nombre"] for lg in LOGROS]
    vals=[1 if n in nombres_ok else 0 for n in todos]
    colores=["#7c3aed" if v else "rgba(168,85,247,0.1)" for v in vals]

    fig=go.Figure(go.Bar(
        x=todos, y=vals,
        marker_color=colores,
        marker_line=dict(color=['rgba(168,85,247,0.5)' if v else 'rgba(168,85,247,0.1)' for v in vals],width=1),
        text=[lg["icono"] for lg in LOGROS],
        textposition='outside',
        hovertemplate='<b>%{x}</b><extra></extra>',
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(visible=False,range=[0,1.5]),
        xaxis=dict(tickfont=dict(size=10,color='#c4b5fd',family='Nunito'),
                   tickangle=-20, gridcolor='rgba(0,0,0,0)'),
        margin=dict(l=0,r=0,t=30,b=60), height=200,
    )
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})


# ── WIDGETS ────────────────────────────────────────────────────────────────────
def widget_timer():
    components.html("""
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Nunito:wght@700&display=swap" rel="stylesheet">
<style>
body{margin:0;background:transparent}
.w{background:linear-gradient(135deg,#0f0a1e,#12122a);border:1px solid rgba(6,182,212,0.4);border-radius:18px;padding:28px 24px;text-align:center;color:#e2e8ff;box-shadow:0 0 30px rgba(6,182,212,0.12);}
#title{font-family:Orbitron,monospace;font-size:15px;color:#06b6d4;margin-bottom:4px;font-weight:700}
#sub{font-size:12px;color:#4b5563;font-style:italic;margin-bottom:18px}
#display{font-family:Orbitron,monospace;font-size:72px;font-weight:900;background:linear-gradient(135deg,#06b6d4,#a78bfa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin:4px 0;letter-spacing:4px;line-height:1}
#msg{font-size:13px;color:#94a3b8;min-height:20px;margin-bottom:16px;font-style:italic}
.bar-w{width:100%;background:rgba(255,255,255,0.06);border-radius:99px;height:5px;margin:8px 0 16px;overflow:hidden}
#bar{height:5px;border-radius:99px;background:linear-gradient(90deg,#7c3aed,#06b6d4);width:100%;transition:width 1s linear;box-shadow:0 0 10px rgba(6,182,212,0.6)}
.btns{display:flex;gap:10px;justify-content:center}
button{padding:10px 24px;border-radius:12px;font-size:14px;font-weight:700;cursor:pointer;transition:all .2s;font-family:Nunito,sans-serif;border:none}
#bs{background:linear-gradient(135deg,#7c3aed,#06b6d4);color:#fff;box-shadow:0 0 16px rgba(124,58,237,0.4)}
#bs:hover{box-shadow:0 0 28px rgba(6,182,212,0.6);transform:translateY(-2px)}
#br{background:rgba(168,85,247,0.12);border:1px solid rgba(168,85,247,0.3);color:#a78bfa}
</style>
<div class="w">
  <div id="title">⏱️ Temporizador de Oración</div>
  <div id="sub">Permanece 1 minuto en silencio con Dios.</div>
  <div id="display">01:00</div>
  <div class="bar-w"><div id="bar"></div></div>
  <div id="msg"></div>
  <div class="btns">
    <button id="bs" onclick="toggle()">▶ Iniciar</button>
    <button id="br" onclick="reset()">⏹ Reiniciar</button>
  </div>
</div>
<script>
const MSGS=["Silencio... Dios te escucha 🙏","Quédate presente... ❤️","Ya casi... ¡lo estás logrando! ⚡","¡Último tramo! 🌟"];
let t=60,iv=null,run=false;
const D=()=>document.getElementById('display');
const M=()=>document.getElementById('msg');
const BS=()=>document.getElementById('bs');
const BAR=()=>document.getElementById('bar');
function fmt(s){return String(Math.floor(s/60)).padStart(2,'0')+':'+String(s%60).padStart(2,'0')}
function toggle(){
  if(run){clearInterval(iv);run=false;BS().textContent='▶ Continuar';return}
  run=true;BS().textContent='⏸ Pausar';
  iv=setInterval(()=>{t--;D().textContent=fmt(t);BAR().style.width=(t/60*100)+'%';
    M().textContent=t>0?MSGS[Math.min(Math.floor((1-t/60)*4),3)]:'';
    if(t<=0){clearInterval(iv);run=false;
      D().style.backgroundImage='linear-gradient(135deg,#22c55e,#06b6d4)';
      D().textContent='🙏 Amén!';M().textContent='¡Lo lograste! Dios estuvo contigo. ✨';BS().textContent='▶ Iniciar';}
  },1000);
}
function reset(){clearInterval(iv);run=false;t=60;D().textContent='01:00';D().style.backgroundImage='linear-gradient(135deg,#06b6d4,#a78bfa)';M().textContent='';BAR().style.width='100%';BS().textContent='▶ Iniciar';}
</script>""", height=310, scrolling=False)

def widget_recargas():
    st.markdown('<div class="wbox" style="border-color:rgba(34,197,94,0.4);text-align:left"><div class="wbox-title" style="color:#22c55e">🔋 Recargas de Hoy</div><div class="wbox-sub">Marca las que ya activaste.</div></div>', unsafe_allow_html=True)
    cols=st.columns(3)
    for i,(ico,lab,desc) in enumerate([("🌅","Mañana","Encendiste el día"),("⚡","Día","Pausa rápida"),("🌙","Noche","Cierre en paz")]):
        with cols[i]:
            st.markdown(f'<div style="text-align:center;font-size:36px;margin-bottom:4px">{ico}</div>', unsafe_allow_html=True)
            if st.checkbox(f"**{lab}** — *{desc}*",value=i in st.session_state.recargas,key=f"rec_{i}"):
                st.session_state.recargas.add(i)
            else: st.session_state.recargas.discard(i)
    if len(st.session_state.recargas)==3:
        st.session_state.recargas_completas=True; st.success("🔋 ¡Batería al 100%! Logro: **Energía Máxima** ⚡")
    else: st.info(f"Te faltan **{3-len(st.session_state.recargas)}** recarga(s).")

def widget_postura():
    st.markdown('<div class="wbox" style="border-color:rgba(168,85,247,0.4);text-align:left"><div class="wbox-title" style="color:#a855f7">🛡️ Verificador de Postura del Héroe</div><div class="wbox-sub">Actívalos uno por uno.</div></div>', unsafe_allow_html=True)
    items=["📏 Espalda recta y firme","🤲 Manos abiertas o juntas","🦶 Pies apoyados en el suelo","👁️ Ojos cerrados o mirada al suelo","🌬️ Respiré profundo 3 veces"]
    pts=sum(1 for j,item in enumerate(items) if st.checkbox(item,key=f"pos_{j}"))
    if pts==5: st.success("🛡️ **¡Postura de Héroe activada!** 🙏"); st.balloons()
    elif pts: st.info(f"{pts}/5 puntos — ¡casi lista!")

def widget_diario():
    st.markdown('<div class="wbox" style="border-color:rgba(251,191,36,0.4);text-align:left"><div class="wbox-title" style="color:#fbbf24">📓 Diario de Pistas Secretas</div><div class="wbox-sub">¿Qué frase brilló en tu corazón hoy?</div></div>', unsafe_allow_html=True)
    with st.form("f_diario",clear_on_submit=True):
        pista=st.text_area("✍️ Mi pista secreta de hoy...",placeholder='Ej: "Sean fuertes y valientes" y lo que me dijo a mí...',height=80)
        if st.form_submit_button("💾 Guardar pista",use_container_width=True):
            if pista.strip():
                st.session_state.diario.append({"fecha":datetime.now().strftime("%d/%m/%Y %H:%M"),"texto":pista.strip()})
                st.success("✅ ¡Pista guardada! Logro: **Guardián de Pistas** 📓"); st.balloons()
    if st.session_state.diario:
        st.markdown(f"**📚 Tus pistas ({len(st.session_state.diario)})**")
        for e in reversed(st.session_state.diario[-5:]):
            with st.expander(f"🕐 {e['fecha']}"):
                st.markdown(f'*"{e["texto"]}"*')

def widget_emociones():
    st.markdown('<div class="wbox" style="border-color:rgba(236,72,153,0.4);text-align:left"><div class="wbox-title" style="color:#ec4899">🎭 Panel de Emociones</div><div class="wbox-sub">¿Cómo te sientes? Elige tu emoción.</div></div>', unsafe_allow_html=True)
    cols=st.columns(4)
    for i,(label,_) in enumerate(EMOCIONES.items()):
        with cols[i%4]:
            if st.button(label,use_container_width=True,key=f"em_{i}"):
                st.session_state["emocion_sel"]=label; st.session_state.emocion_usada=True; st.rerun()
    sel=st.session_state.get("emocion_sel")
    if sel and sel in EMOCIONES:
        d=EMOCIONES[sel]
        st.markdown(f"""<div style="background:{d['color']}18;border:2px solid {d['color']}55;border-radius:16px;padding:20px 22px;margin-top:12px;">
            <div style="font-size:22px;font-weight:800;color:{d['color']};margin-bottom:10px;animation:fadeInUp 0.4s ease">{sel}</div>
            <div style="font-size:16px;font-style:italic;color:#e2e8ff;margin-bottom:12px;line-height:1.65">{d['oracion']}</div>
            <div style="font-size:13px;background:rgba(255,255,255,0.04);border-radius:10px;padding:10px 14px;color:#94a3b8">
                💡 <strong style="color:{d['color']}">Recuerda:</strong> {d['tip']}</div></div>""", unsafe_allow_html=True)

def widget_regalo():
    st.markdown('<div class="wbox" style="border-color:rgba(59,130,246,0.4);text-align:left"><div class="wbox-title" style="color:#3b82f6">🎁 Prepara tu Regalo Invisible</div><div class="wbox-sub">¿Qué le llevas a Dios en la próxima Misa?</div></div>', unsafe_allow_html=True)
    if st.session_state.regalo_enviado:
        st.success(f"🎁 **Regalo preparado:** *\"{st.session_state.regalo_texto}\"*")
        if st.button("🔄 Preparar nuevo regalo",use_container_width=True):
            st.session_state.regalo_enviado=False; st.session_state.regalo_texto=""; st.rerun()
    else:
        with st.form("f_regalo"):
            r=st.text_area("¿Qué esfuerzo, preocupación o alegría le llevas?",placeholder="Ej: Mi miedo a los exámenes...",height=80)
            if st.form_submit_button("🎁 Preparar regalo",use_container_width=True):
                if r.strip():
                    st.session_state.regalo_texto=r.strip(); st.session_state.regalo_enviado=True
                    st.success("✅ ¡Logro: Portador de Regalos! 🎁"); st.balloons(); st.rerun()

def widget_salto():
    s=st.session_state.saltos
    st.markdown(f"""<div class="wbox" style="border-color:rgba(249,115,22,0.4)">
        <div class="wbox-title" style="color:#f97316">🦘 Contador de Saltos de Vuelta</div>
        <div class="wbox-sub">Cada regreso después de fallar es un salto.</div>
        <div style="font-family:Orbitron,monospace;font-size:80px;font-weight:900;
             background:linear-gradient(135deg,#f97316,#fbbf24);-webkit-background-clip:text;
             -webkit-text-fill-color:transparent;background-clip:text;line-height:1;margin:6px 0;
             animation:heartbeat 1.5s ease-in-out infinite;">{s}</div>
        <div style="font-size:13px;color:#6b7280">saltos dados</div></div>""", unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        if st.button("🦘 ¡Dar un salto!",use_container_width=True,type="primary"):
            st.session_state.saltos+=1; st.rerun()
    with c2:
        if st.button("🔄 Reiniciar",use_container_width=True):
            st.session_state.saltos=0; st.rerun()
    msgs=["¡Bien! Dios te recibe siempre. 🙏","¡Dos veces! Cada regreso cuenta. ⚡","¡Tres! Los héroes no se rinden. 🛡️","¡Cuatro! Ya casi llegas al logro. 🎯","¡CINCO! ¡Explorador Imparable! 🏆"]
    if 0<s<=5: st.markdown(f'*{msgs[s-1]}*')
    if s>=5: st.success("🦘 **¡Logro: Saltador Imparable!** ¡5+ saltos!")


# ── PAGE: INICIO ──────────────────────────────────────────────────────────────
def page_inicio():
    n=st.session_state.nombre; saludo=f"¡Hola, {n}!" if n else "¡Hola, Explorador!"

    # Hero con canvas de partículas
    st.markdown('<div class="hero">', unsafe_allow_html=True)
    st.markdown('<div class="hero-canvas-wrap">', unsafe_allow_html=True)
    components.html(PARTICLE_CANVAS, height=220, scrolling=False)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="hero-body">
        <div class="hero-eyebrow">⚔️ &nbsp;Tu Superpoder Secreto&nbsp; ⚔️</div>
        <div class="hero-title">LA GRAN AVENTURA<br>DEL CORAZÓN</div>
        <div class="hero-name">{saludo}</div>
        <div class="hero-tagline">Descubre tu superpoder secreto para hablar con Dios.</div>
        <div class="hero-icons">
            <div class="hero-icon-wrap">
                <div class="hero-bubble" style="background:rgba(6,182,212,0.12);border-color:rgba(6,182,212,0.4);box-shadow:0 0 18px rgba(6,182,212,0.25)">🧭</div>
                <div class="hero-icon-lbl" style="color:#06b6d4">Explora</div>
            </div>
            <div class="hero-icon-wrap">
                <div class="hero-bubble" style="background:rgba(168,85,247,0.12);border-color:rgba(168,85,247,0.4);box-shadow:0 0 18px rgba(168,85,247,0.25)">📖</div>
                <div class="hero-icon-lbl" style="color:#a855f7">Aprende</div>
            </div>
            <div class="hero-icon-wrap">
                <div class="hero-bubble" style="background:rgba(251,191,36,0.12);border-color:rgba(251,191,36,0.4);box-shadow:0 0 18px rgba(251,191,36,0.25)">⚡</div>
                <div class="hero-icon-lbl" style="color:#fbbf24">Activa</div>
            </div>
            <div class="hero-icon-wrap">
                <div class="hero-bubble" style="background:rgba(34,197,94,0.12);border-color:rgba(34,197,94,0.4);box-shadow:0 0 18px rgba(34,197,94,0.25)">🏆</div>
                <div class="hero-icon-lbl" style="color:#22c55e">Completa</div>
            </div>
        </div>
    </div></div>
    """, unsafe_allow_html=True)

    st.markdown("""<div class="intro-card">
        <div class="intro-tag">✦ Esta no es una herramienta ordinaria ✦</div>
        <div class="intro-txt">Es una herramienta que te lleva al tesoro más grande del universo: aprender a hablar con Dios. Cada nivel desbloquea un superpoder nuevo. ¿Listo para la aventura?</div>
    </div>""", unsafe_allow_html=True)

    # Misión del día
    with st.expander(f"🎯  MISIÓN DEL DÍA — {mision_dia['icono']} {mision_dia['titulo']}",expanded=True):
        st.markdown(f"> *{mision_dia['mision']}*")
        st.caption(f"📌 {mision_dia['resumen']}")
        if st.button(f"→ Ir al {mision_dia['supertitulo']}",key="btn_mdia"):
            st.session_state.page=f"nivel_{mision_dia['id']}"; st.rerun()

    st.markdown("---")
    st.markdown('<p style="font-family:Orbitron,monospace;font-size:11px;font-weight:700;color:#7c3aed;letter-spacing:2px;">🗺️ LOS 7 NIVELES</p>', unsafe_allow_html=True)

    cols=st.columns(2)
    for i,nv in enumerate(NIVELES):
        done=nv["id"] in st.session_state.progress; chk="✅" if done else "○"
        with cols[i%2]:
            if st.button(f"{chk}  {nv['icono']}  **{nv['supertitulo']}**\n\n{nv['titulo']}",key=f"hn{nv['id']}",use_container_width=True):
                st.session_state.page=f"nivel_{nv['id']}"; st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🏆  Ver Pantalla Final",use_container_width=True,type="primary"):
        st.session_state.page="Final"; st.rerun()


# ── PAGE: NIVEL ───────────────────────────────────────────────────────────────
def page_nivel(nv):
    # Header con SVG animado
    st.markdown(f"""
    <div class="nivel-hdr" style="background:linear-gradient(135deg,{nv['color']},{nv['color_dark']});
         box-shadow:0 0 40px {nv['glow']};">
        <div class="nivel-hdr-content">
            <div>{nv['svg_anim']}</div>
            <div>
                <div class="nivel-tag">{nv['supertitulo']}</div>
                <div class="nivel-ttl">{nv['titulo']}</div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)

    with st.expander("💡  ¿Sabías que...?",expanded=True):
        st.markdown(f'<div style="color:#a5f3fc;font-size:15px;line-height:1.7;">{nv["sabias_que"]}</div>', unsafe_allow_html=True)

    with st.expander("🏺  La Idea de Oro",expanded=True):
        st.markdown(f'<div style="font-family:Orbitron,monospace;font-size:14px;font-weight:700;color:{nv["color"]};margin-bottom:10px;">{nv["idea_titulo"]}</div>', unsafe_allow_html=True)
        st.markdown(nv["idea_texto"])

    with st.expander("🎯  Misión para ti",expanded=True):
        st.markdown(f'<div style="font-size:15px;color:#fde68a;line-height:1.7;"><strong>¡Tu misión!</strong> {nv["mision"]}</div>', unsafe_allow_html=True)

    # Widget especial
    wmap={"timer":widget_timer,"recargas":widget_recargas,"postura":widget_postura,
          "diario":widget_diario,"emociones":widget_emociones,"regalo":widget_regalo,"salto":widget_salto}
    if nv.get("widget") in wmap:
        st.markdown("---")
        st.markdown('<p style="font-family:Orbitron,monospace;font-size:11px;font-weight:700;color:#7c3aed;letter-spacing:2px;">🛠️ HERRAMIENTA DE PRÁCTICA</p>', unsafe_allow_html=True)
        wmap[nv["widget"]]()

    # Notas
    st.markdown("---")
    with st.expander("📝  Mis notas personales",expanded=False):
        nota=st.text_area("¿Qué aprendiste?",value=st.session_state.notas.get(nv["id"],""),height=80,key=f"nota_{nv['id']}")
        st.session_state.notas[nv["id"]]=nota

    # Resumen con glow
    st.markdown(f"""<div class="resumen" style="background:linear-gradient(90deg,{nv['color']},{nv['color_dark']});
         box-shadow:0 0 20px {nv['glow']};">
        📌 &nbsp;<strong>Resumen:</strong>&nbsp;{nv['resumen']}</div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        if st.button("← Inicio",use_container_width=True): st.session_state.page="Inicio"; st.rerun()
    with c2:
        if nv["id"] in st.session_state.progress: st.success("✅ ¡Nivel completado!")
        elif st.button("☐  Marcar como completado",use_container_width=True,type="primary"):
            st.session_state.progress.add(nv["id"]); st.balloons(); st.rerun()

    if nv["id"]<len(NIVELES):
        nx=NIVELES[nv["id"]]
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button(f"→ Siguiente: {nx['icono']} {nx['titulo']}",use_container_width=True):
            st.session_state.page=f"nivel_{nx['id']}"; st.rerun()


# ── PAGE: FINAL ───────────────────────────────────────────────────────────────
def page_final():
    done=len(st.session_state.progress); nb=st.session_state.nombre or "Explorador"
    ok=logros_ok()

    st.markdown(f"""<div class="fcard">
        <div class="trophy-anim">🏆</div>
        <div style="font-size:18px;letter-spacing:2px;color:#fbbf24;margin:12px 0;">{'⭐ '*7}</div>
        <div class="fcard-title">¡Lo lograste, {nb}!</div>
        <div class="fcard-msg">Ya tienes el superpoder más grande del universo: saber que Dios te escucha siempre,
        en cualquier lugar, con cualquier emoción.<br><br>
        Esta herramienta no termina aquí. Apenas empieza.<br>
        <strong style="color:#06b6d4">¡Sigue explorando cada día!</strong></div></div>""", unsafe_allow_html=True)

    # Lottie trophy (con fallback)
    if LOTTIE_OK:
        lottie_data=load_lottie(LOTTIE_URLS["trophy"])
        if lottie_data:
            c1,c2,c3=st.columns([1,2,1])
            with c2: st_lottie(lottie_data,height=180,key="trophy_anim")

    st.markdown("<br>", unsafe_allow_html=True)

    # GRÁFICOS ──────────────────────────────────────────────────────────────
    st.markdown('<p style="font-family:Orbitron,monospace;font-size:11px;font-weight:700;color:#7c3aed;letter-spacing:2px;">📊 TUS ESTADÍSTICAS VISUALES</p>', unsafe_allow_html=True)

    gc1,gc2=st.columns([1,1])
    with gc1:
        st.markdown('<p style="font-size:12px;color:#6b7280;text-align:center;">Superpoderes desbloqueados</p>', unsafe_allow_html=True)
        radar_superpoderes()
    with gc2:
        st.markdown('<p style="font-size:12px;color:#6b7280;text-align:center;">Progreso general</p>', unsafe_allow_html=True)
        donut_progreso()
        st.markdown('<p style="font-size:12px;color:#6b7280;text-align:center;margin-top:-8px">Logros</p>', unsafe_allow_html=True)
        bar_logros()

    # Métricas
    st.markdown("---")
    c1,c2,c3,c4=st.columns(4)
    c1.metric("Niveles",f"{done}/7")
    c2.metric("Logros",f"{len(ok)}/{len(LOGROS)}")
    c3.metric("Diario",len(st.session_state.diario))
    c4.metric("Saltos",st.session_state.saltos)

    if done==7: st.success("🎉 **¡AVENTURA COMPLETA!** ¡Eres un Explorador Imparable!")
    else: st.info(f"Has completado **{done} de 7** niveles. ¡La aventura te espera!")

    st.markdown("---")
    st.markdown('<p style="font-family:Orbitron,monospace;font-size:11px;font-weight:700;color:#7c3aed;letter-spacing:2px;">🏅 LOGROS</p>', unsafe_allow_html=True)
    ca,cb=st.columns(2)
    for i,lg in enumerate(LOGROS):
        desbloqueado=lg["req"](st.session_state.progress,st.session_state)
        cls="logro-on" if desbloqueado else "logro-off"
        ct="#e2e8ff" if desbloqueado else "#444"; ec="#22c55e" if desbloqueado else "#374151"
        with (ca if i%2==0 else cb):
            st.markdown(f"""<div class="logro {cls}">
                <span style="font-size:28px">{lg['icono']}</span>
                <div><div style="font-weight:800;font-size:14px;color:{ct}">{lg['nombre']}</div>
                <div style="font-size:12px;color:#4b5563">{lg['desc']}</div>
                <div style="font-size:11px;font-weight:700;color:{ec}">{'✅ Desbloqueado' if desbloqueado else '🔒 Bloqueado'}</div></div>
            </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<p style="font-family:Orbitron,monospace;font-size:11px;font-weight:700;color:#7c3aed;letter-spacing:2px;">⚡ SUPERPODERES</p>', unsafe_allow_html=True)
    for ico,txt,nid in [("⚡","Orar en 1 minuto, en cualquier lugar",1),("🔋","Las 3 Recargas Mágicas diarias",2),
                         ("🛡️","La Postura del Héroe para escuchar",3),("🗺️","Leer la Biblia como detective secreto",4),
                         ("🎮","El Botón de Emergencias en toda emoción",5),("⛪","La Misa como la gran reunión de equipo",6),
                         ("🧭","Volver a empezar siempre",7)]:
        chk="✅" if nid in st.session_state.progress else "○"
        st.markdown(f'<div class="prow"><span style="font-size:22px">{ico}</span><span style="flex:1">{txt}</span><span style="font-size:18px">{chk}</span></div>', unsafe_allow_html=True)

    if st.session_state.diario:
        st.markdown("---")
        st.markdown(f'<p style="font-family:Orbitron,monospace;font-size:11px;font-weight:700;color:#7c3aed;letter-spacing:2px;">📓 DIARIO ({len(st.session_state.diario)} entradas)</p>', unsafe_allow_html=True)
        for e in reversed(st.session_state.diario):
            with st.expander(f"🕐 {e['fecha']}"): st.markdown(f'*"{e["texto"]}"*')

    st.markdown("<br>", unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        if st.button("🔄 Reiniciar progreso",use_container_width=True):
            for k,v in defaults.items():
                st.session_state[k]=set() if isinstance(v,set) else ([] if isinstance(v,list) else ({} if isinstance(v,dict) else v))
            st.session_state.page="Inicio"; st.rerun()
    with c2:
        if st.button("🧭 Volver al inicio",use_container_width=True,type="primary"):
            st.session_state.page="Inicio"; st.rerun()


# ── ROUTER ────────────────────────────────────────────────────────────────────
pg=st.session_state.page
if   pg=="Inicio":          page_inicio()
elif pg=="Final":           page_final()
elif pg.startswith("nivel_"):
    nid=int(pg.split("_")[1])
    page_nivel(next(n for n in NIVELES if n["id"]==nid))
