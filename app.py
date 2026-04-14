import streamlit as st
import random
from datetime import date, datetime

# ── PAGE CONFIG ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="La Gran Aventura del Corazón",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── PALETA GAMING ──────────────────────────────────────────────────────────────
# bg: #080614  surface: #120d26  card: #1c1535
# cyan #06b6d4  purple #a855f7  amber #fbbf24
# green #22c55e  pink #ec4899  blue #3b82f6  orange #f97316

# ── DATA ───────────────────────────────────────────────────────────────────────
NIVELES = [
    {
        "id": 1, "supertitulo": "NIVEL 1",
        "titulo": "Estación de Descubrimiento", "icono": "⚡",
        "color": "#06b6d4", "color_dark": "#0891b2", "glow": "rgba(6,182,212,0.35)",
        "sabias_que": "¡No necesitas palabras elegantes ni perfectas para hablar con Dios! Él prefiere que le hables como a tu mejor amigo.",
        "idea_titulo": "El Superpoder de 1 Minuto",
        "idea_texto": 'A veces pensamos que rezar es muy difícil, pero no saber qué decir es el mejor comienzo. Un solo minuto donde le dices la verdad ("Aquí estoy, acompáñame") vale muchísimo más que horas de hablar como un robot.',
        "mision": '¡Levanta la mano si alguna vez te has quedado sin palabras! Hoy, siéntate en silencio un minuto y solo di en tu mente: "Hola Dios, soy yo, quiero estar contigo!"',
        "resumen": "Para orar, solo necesitas estar presente, no ser perfecto.",
        "widget": "timer",
    },
    {
        "id": 2, "supertitulo": "NIVEL 2",
        "titulo": "El Entrenamiento Diario", "icono": "🔋",
        "color": "#22c55e", "color_dark": "#16a34a", "glow": "rgba(34,197,94,0.35)",
        "sabias_que": "Tu corazón es como la batería de una tablet o consola; ¡necesita recargarse todos los días para funcionar al máximo!",
        "idea_titulo": "Las 3 Recargas Mágicas",
        "idea_texto": "No dependas de si tienes ganas o no. Conéctate tres veces al día para mantener tu energía al 100%.\n\n🌅 **Mañana** — Para encender el día.\n⚡ **Día** — Pausa rápida para no apagarte.\n🌙 **Noche** — Para cerrar y descansar en paz.",
        "mision": "¡Tócate la cabeza, el pecho y la panza! Ese es tu indicador de energía. Mañana, antes de mirar cualquier pantalla, haz la señal de la cruz lentamente para iniciar tu carga.",
        "resumen": "Tres pausas cortas al día mantienen tu corazón conectado y fuerte.",
        "widget": "recargas",
    },
    {
        "id": 3, "supertitulo": "NIVEL 3",
        "titulo": "La Base Secreta", "icono": "🛡️",
        "color": "#a855f7", "color_dark": "#7c3aed", "glow": "rgba(168,85,247,0.35)",
        "sabias_que": "¡Dios también te habla cuando tú te quedas callado! El silencio es su idioma favorito.",
        "idea_titulo": "La Postura del Héroe",
        "idea_texto": "Tu cuerpo también reza y te ayuda a concentrarte. Si te acuestas, tu cerebro pensará en dormir. Pero si te sientas derecho con las manos abiertas, te conviertes en una antena gigante lista para escuchar.\n\n📏 **Espalda** super recta\n🤲 **Manos** listas\n🦶 **Pies** firmes",
        "mision": '¡Ponte en "Postura de Héroe" ahora mismo! Cierra los ojos y cuenta hasta 10. ¡Siente la paz!',
        "resumen": "El silencio y tu postura preparan tu cuerpo para escuchar.",
        "widget": "postura",
    },
    {
        "id": 4, "supertitulo": "NIVEL 4",
        "titulo": "El Mapa del Tesoro", "icono": "🗺️",
        "color": "#fbbf24", "color_dark": "#d97706", "glow": "rgba(251,191,36,0.35)",
        "sabias_que": "¡La Biblia no es una herramienta escolar aburrida, es una carta secreta escrita especialmente para ti!",
        "idea_titulo": "Decodificando el Mensaje",
        "idea_texto": 'Se llama "Lectio Divina". Consiste en leer un pedacito de la Biblia muy despacio. No tienes que entender todo. Solo busca una sola frase o palabra que "brille" en tu corazón y guárdala.',
        "mision": "¡Finge que tienes una lupa de súper detective! Busca cualquier herramienta de lectura en tu casa, ábrela al azar y lee solo la primera línea en cámara súper lenta. Así es como buscamos las pistas de Dios.",
        "resumen": "No leas para estudiar todo, lee para encontrar tu pista secreta de hoy.",
        "widget": "diario",
    },
    {
        "id": 5, "supertitulo": "NIVEL 5",
        "titulo": "El Panel de Control", "icono": "🎮",
        "color": "#ec4899", "color_dark": "#db2777", "glow": "rgba(236,72,153,0.35)",
        "sabias_que": "Dios no quiere que finjas estar feliz si en realidad estás triste o muy asustado. ¡Él prefiere la verdad!",
        "idea_titulo": "El Botón de Emergencias",
        "idea_texto": 'Puedes usar tu superpoder en CUALQUIER emoción:\n\n😨 Si tienes miedo → *"Señor, ¡abrázame!"*\n😢 Si estás triste → *"Señor, acompáñame"*\n😄 Si estás muy feliz → *"¡Gracias por esto tan genial!"*',
        "mision": "¡Pon tu mejor cara de asombro! Luego cara triste, y luego una gran sonrisa. Recuerda: en todas esas caras, Dios está sentado a tu lado.",
        "resumen": "Cualquier emoción que sientas es el momento perfecto para hablar con Dios.",
        "widget": "emociones",
    },
    {
        "id": 6, "supertitulo": "NIVEL 6",
        "titulo": "La Gran Reunión", "icono": "⛪",
        "color": "#3b82f6", "color_dark": "#2563eb", "glow": "rgba(59,130,246,0.35)",
        "sabias_que": "¡La Misa no es un evento donde solo vas a sentarte y mirar, es la reunión de equipo más importante del universo!",
        "idea_titulo": "El Banquete de los Héroes",
        "idea_texto": "En la Misa, la magia se hace real. Dios se esconde en el pan para entrar en ti y darte fuerza. Tú también debes llevarle un regalo invisible: ofrécele un esfuerzo o una preocupación que tuviste en la semana.",
        "mision": "¡Choca los cinco en el aire! En tu próxima Misa, lleva una alegría o un problema en tus manos imaginarias y, cuando levanten el pan, entrégaselo a Dios como tu regalo secreto.",
        "resumen": "La Misa es un encuentro real para llenarte de la fuerza de Dios.",
        "widget": "regalo",
    },
    {
        "id": 7, "supertitulo": "NIVEL 7",
        "titulo": "El Explorador Imparable", "icono": "🧭",
        "color": "#f97316", "color_dark": "#ea580c", "glow": "rgba(249,115,22,0.35)",
        "sabias_que": "¡Los mejores exploradores del mundo también tropiezan, se pierden y olvidan su mapa a veces!",
        "idea_titulo": "Volver a Empezar",
        "idea_texto": 'Si un día te da pereza, te portas mal o se te olvida orar por varios días, ¡no pasa nada! Dios no se enoja ni te castiga. Él solo te espera. El truco secreto es regresar y decir: "Perdón, me distraje, ¡pero aquí estoy otra vez!"',
        "mision": '¡Da un salto muy alto donde estés! Cada vez que falles, usa ese "salto" invisible para levantarte y volver a empezar. ¡Nunca es tarde en esta aventura!',
        "resumen": "El verdadero éxito no es no fallar nunca, sino volver a intentarlo siempre.",
        "widget": "salto",
    },
]

EMOCIONES = {
    "😨 Miedo":     {"oracion": '"Señor, tengo miedo. Pero sé que estás aquí. Dame tu paz. ¡Abrázame!"',                "color": "#06b6d4", "tip": "Respira profundo 3 veces. Dios está más cerca cuando tienes miedo."},
    "😢 Tristeza":  {"oracion": '"Señor, hoy me siento triste. No te vayas. Acompáñame en silencio."',                 "color": "#3b82f6", "tip": "No tienes que fingir que estás bien. Dios recibe tu tristeza con amor."},
    "😤 Enojo":     {"oracion": '"Señor, estoy enojado. Ayúdame a no hacer daño. Calma mi corazón."',                 "color": "#f97316", "tip": "El enojo no te separa de Dios. Cuéntaselo antes de actuar."},
    "😰 Ansiedad":  {"oracion": '"Señor, mi mente no para. Recibe mis preocupaciones. Tú puedes con ellas."',          "color": "#a855f7", "tip": "Suelta una preocupación a la vez. Imagina que la pones en manos de Dios."},
    "😄 Alegría":   {"oracion": '"¡Gracias, Señor! Esto es increíble. Quiero que estés en este momento conmigo."',    "color": "#22c55e", "tip": "¡La alegría también es oración! ¡Celebra con Dios!"},
    "😴 Cansancio": {"oracion": '"Señor, estoy agotado. Sostén lo que yo no puedo. Dame descanso en Ti."',             "color": "#fbbf24", "tip": "A veces la mejor oración es dormirse confiando en Dios."},
    "😕 Confusión": {"oracion": '"Señor, no entiendo nada. Ilumíname. Guía mis pasos aunque no vea el camino."',       "color": "#ec4899", "tip": "No necesitas entender todo. Solo necesitas confiar en quien sí entiende."},
}

LOGROS = [
    {"id": "primer_nivel",  "icono": "🥇", "nombre": "Primer Paso",        "desc": "Completaste el Nivel 1",          "req": lambda p, s: 1 in p},
    {"id": "mitad",         "icono": "⚡", "nombre": "A Mitad de Camino",  "desc": "Completaste 4 niveles",           "req": lambda p, s: len(p) >= 4},
    {"id": "todos",         "icono": "🏆", "nombre": "Explorador Total",   "desc": "Completaste los 7 niveles",       "req": lambda p, s: len(p) == 7},
    {"id": "diario",        "icono": "📓", "nombre": "Guardián de Pistas", "desc": "Escribiste en el Diario Secreto", "req": lambda p, s: len(s.get("diario", [])) > 0},
    {"id": "regalo",        "icono": "🎁", "nombre": "Portador de Regalos","desc": "Enviaste un regalo invisible",    "req": lambda p, s: s.get("regalo_enviado", False)},
    {"id": "saltos",        "icono": "🦘", "nombre": "Saltador Imparable", "desc": "Diste 5 saltos de vuelta",        "req": lambda p, s: s.get("saltos", 0) >= 5},
    {"id": "emociones",     "icono": "🎭", "nombre": "Maestro Emocional",  "desc": "Usaste el panel de emociones",   "req": lambda p, s: s.get("emocion_usada", False)},
    {"id": "recargas",      "icono": "🔋", "nombre": "Energía Máxima",     "desc": "Activaste las 3 recargas",        "req": lambda p, s: s.get("recargas_completas", False)},
]

FRASES = [
    "¡Cada día que oras eres más fuerte! 💪",
    "¡Un explorador nunca se rinde! 🧭",
    "Dios te está esperando. ¡Allá vamos! ⚡",
    "¡Tu corazón tiene superpoderes! ❤️",
    "¡Lo que empezaste hoy, Dios lo termina! 🙏",
    "¡Eres un héroe del corazón! 🛡️",
]

# ── CSS GAMING ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Nunito:ital,wght@0,400;0,600;0,700;0,800;1,400&display=swap');

/* ── RESET & BASE ── */
html, body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
.main, .block-container {
    background: #080614 !important;
    font-family: 'Nunito', sans-serif !important;
    color: #e2e8ff !important;
}

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f0a1e 0%, #080614 100%) !important;
    border-right: 1px solid rgba(168,85,247,0.2) !important;
}
[data-testid="stSidebar"] * { color: #c4b5fd !important; font-family: 'Nunito', sans-serif !important; }
[data-testid="stSidebar"] input {
    background: rgba(168,85,247,0.08) !important;
    border: 1px solid rgba(168,85,247,0.3) !important;
    border-radius: 10px !important;
    color: #e2e8ff !important;
}
[data-testid="stSidebar"] hr { border-color: rgba(168,85,247,0.2) !important; }
[data-testid="stSidebar"] .stRadio > label { color: #7c3aed !important; font-size:10px !important; letter-spacing:2px !important; text-transform:uppercase !important; }
[data-testid="stSidebar"] .stRadio label span { font-size:13px !important; color:#c4b5fd !important; }
[data-testid="stSidebar"] small,
[data-testid="stSidebar"] .stCaption { color: #6b7280 !important; }

/* ── PROGRESS BAR ── */
.stProgress > div > div {
    background: linear-gradient(90deg, #7c3aed, #06b6d4) !important;
    border-radius: 99px !important;
    box-shadow: 0 0 8px rgba(6,182,212,0.5) !important;
}
.stProgress > div {
    background: rgba(255,255,255,0.06) !important;
    border-radius: 99px !important;
}

/* ── BUTTONS ── */
.stButton > button {
    border-radius: 12px !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    transition: all 0.2s !important;
    border: 1px solid rgba(168,85,247,0.3) !important;
    background: rgba(168,85,247,0.12) !important;
    color: #c4b5fd !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 0 18px rgba(168,85,247,0.4) !important;
    border-color: rgba(168,85,247,0.7) !important;
    background: rgba(168,85,247,0.22) !important;
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #7c3aed, #06b6d4) !important;
    border: none !important;
    color: white !important;
    box-shadow: 0 0 14px rgba(124,58,237,0.4) !important;
}
.stButton > button[kind="primary"]:hover {
    box-shadow: 0 0 28px rgba(6,182,212,0.5) !important;
    transform: translateY(-2px) !important;
}

/* ── INPUTS & TEXTAREAS ── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: rgba(168,85,247,0.07) !important;
    border: 1px solid rgba(168,85,247,0.25) !important;
    border-radius: 12px !important;
    color: #e2e8ff !important;
    font-family: 'Nunito', sans-serif !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: rgba(6,182,212,0.6) !important;
    box-shadow: 0 0 10px rgba(6,182,212,0.2) !important;
}
.stTextInput label, .stTextArea label { color: #c4b5fd !important; font-weight:600 !important; }

/* ── CHECKBOXES ── */
.stCheckbox label { color: #c4b5fd !important; font-size: 14px !important; }
.stCheckbox > label > div { border-color: rgba(168,85,247,0.4) !important; background: rgba(168,85,247,0.1) !important; }

/* ── FORM SUBMIT ── */
.stFormSubmitButton > button {
    background: linear-gradient(135deg, #7c3aed, #06b6d4) !important;
    border: none !important;
    color: white !important;
    font-weight: 700 !important;
    border-radius: 12px !important;
    box-shadow: 0 0 14px rgba(124,58,237,0.4) !important;
}

/* ── EXPANDER ── */
.streamlit-expanderHeader {
    background: rgba(168,85,247,0.08) !important;
    border-radius: 12px !important;
    color: #c4b5fd !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    border: 1px solid rgba(168,85,247,0.2) !important;
}
.streamlit-expanderContent {
    background: rgba(168,85,247,0.04) !important;
    border: 1px solid rgba(168,85,247,0.15) !important;
    border-top: none !important;
    border-radius: 0 0 12px 12px !important;
    color: #cbd5e1 !important;
}

/* ── INFO / SUCCESS / WARNING ── */
.stAlert { border-radius: 12px !important; font-family: 'Nunito', sans-serif !important; }
[data-testid="stAlert"] { background: rgba(6,182,212,0.1) !important; border: 1px solid rgba(6,182,212,0.3) !important; color: #a5f3fc !important; border-radius: 12px !important; }

/* ── METRICS ── */
[data-testid="metric-container"] {
    background: rgba(168,85,247,0.08) !important;
    border: 1px solid rgba(168,85,247,0.2) !important;
    border-radius: 14px !important;
    padding: 16px !important;
}
[data-testid="metric-container"] label { color: #7c3aed !important; font-size:11px !important; letter-spacing:1px !important; text-transform:uppercase !important; }
[data-testid="metric-container"] [data-testid="stMetricValue"] { color: #e2e8ff !important; font-family: 'Orbitron', monospace !important; }

/* ── HIDE DEFAULTS ── */
#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }

/* ════════════════════════════════════════════════
   COMPONENTES CUSTOM
   ════════════════════════════════════════════════ */

/* HERO */
.hero {
    background: linear-gradient(135deg, #0f0a1e 0%, #1a0f3c 50%, #0a1628 100%);
    border-radius: 24px;
    padding: 56px 36px 48px;
    text-align: center;
    margin-bottom: 24px;
    border: 1px solid rgba(168,85,247,0.25);
    box-shadow: 0 0 60px rgba(124,58,237,0.15), 0 0 120px rgba(6,182,212,0.08);
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute; inset: 0;
    background: radial-gradient(ellipse at 30% 20%, rgba(124,58,237,0.18) 0%, transparent 55%),
                radial-gradient(ellipse at 70% 80%, rgba(6,182,212,0.12) 0%, transparent 55%);
    pointer-events: none;
}
.hero-eyebrow {
    display: inline-flex; align-items: center; gap: 8px;
    background: rgba(124,58,237,0.15);
    border: 1px solid rgba(124,58,237,0.4);
    color: #a78bfa;
    font-size: 11px; letter-spacing: 3px; text-transform: uppercase;
    padding: 6px 20px; border-radius: 99px; margin-bottom: 20px;
    font-family: 'Orbitron', monospace; font-weight: 400;
}
.hero-title {
    font-family: 'Orbitron', monospace;
    font-size: clamp(28px, 4vw, 48px); font-weight: 900;
    background: linear-gradient(135deg, #e2e8ff 20%, #a78bfa 60%, #06b6d4 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.2; margin-bottom: 6px;
}
.hero-subtitle { font-size: 15px; color: #7c3aed; font-weight: 700; margin-bottom: 4px; }
.hero-name {
    font-size: 20px; color: #e2e8ff; font-weight: 800; margin-bottom: 6px;
}
.hero-tagline { font-size: 14px; color: #6b7280; font-style: italic; margin-bottom: 28px; }
.hero-icons { display:flex; justify-content:center; gap:20px; flex-wrap:wrap; }
.hero-icon-wrap { text-align:center; }
.hero-bubble {
    width: 56px; height: 56px; border-radius: 16px;
    display: flex; align-items: center; justify-content: center;
    font-size: 24px; margin: 0 auto 6px;
    border: 1px solid;
}
.hero-icon-lbl { font-size: 9px; letter-spacing: 1.5px; text-transform: uppercase; font-weight: 700; }

/* INTRO CARD */
.intro-card {
    background: rgba(124,58,237,0.07);
    border: 1px solid rgba(124,58,237,0.2);
    border-radius: 16px; padding: 20px 26px;
    text-align: center; margin-bottom: 20px;
}
.intro-tag { font-size: 10px; letter-spacing: 2px; color: #7c3aed; text-transform: uppercase; font-weight: 800; margin-bottom: 8px; font-family:'Orbitron',monospace; }
.intro-txt { font-size: 14px; color: #94a3b8; line-height: 1.75; font-style: italic; }

/* NIVEL HEADER */
.nivel-hdr {
    border-radius: 18px 18px 0 0;
    padding: 24px 28px 20px;
    color: #fff;
    position: relative; overflow: hidden;
}
.nivel-hdr::before {
    content:'';
    position:absolute; inset:0;
    background: rgba(0,0,0,0.25);
    pointer-events:none;
}
.nivel-hdr-content { position:relative; z-index:1; }
.nivel-tag { font-size: 10px; letter-spacing: 3px; opacity: 0.75; font-weight:800; text-transform:uppercase; margin-bottom:6px; font-family:'Orbitron',monospace; }
.nivel-ttl { font-family: 'Orbitron', monospace; font-size: 22px; font-weight: 700; }

/* NIVEL BODY */
.nivel-body {
    background: #10091f;
    border: 1px solid rgba(168,85,247,0.18);
    border-top: none;
    border-radius: 0 0 18px 18px;
    margin-bottom: 24px;
    overflow: hidden;
}

/* BLOQUE ROWS */
.bloque-sabias { background: rgba(6,182,212,0.07); border-bottom: 1px solid rgba(6,182,212,0.15); padding:18px 22px; }
.bloque-oro    { background: rgba(251,191,36,0.06); border-bottom: 1px solid rgba(251,191,36,0.15); padding:18px 22px; }
.bloque-mision { background: rgba(236,72,153,0.07); border-bottom: 1px solid rgba(236,72,153,0.15); padding:18px 22px; }
.bloque-tag { font-size:9px; letter-spacing:2px; text-transform:uppercase; font-weight:800; margin-bottom:6px; font-family:'Orbitron',monospace; }
.bloque-txt { font-size:14px; line-height:1.7; }
.bloque-oro-ttl { font-size:16px; font-weight:800; margin-bottom:10px; color:#fbbf24; }

/* RESUMEN */
.resumen { padding:16px 22px; color:#fff; font-style:italic; font-size:14px; font-weight:700; display:flex; align-items:center; gap:10px; }

/* WIDGET BOX */
.wbox {
    background: linear-gradient(135deg, #0f0a1e, #12122a);
    border-radius: 18px; padding: 28px 24px;
    border: 1px solid; margin: 8px 0 16px;
    text-align: center; color: #e2e8ff;
}
.wbox-title { font-family:'Orbitron',monospace; font-size:17px; font-weight:700; margin-bottom:6px; }
.wbox-sub { font-size:13px; color:#6b7280; font-style:italic; margin-bottom:18px; }

/* LOGRO CARD */
.logro { border-radius:14px; padding:14px 16px; display:flex; align-items:center; gap:14px; margin-bottom:10px; border:1px solid; }
.logro-on  { background: rgba(124,58,237,0.12); border-color: rgba(124,58,237,0.4); }
.logro-off { background: rgba(255,255,255,0.02); border-color: rgba(255,255,255,0.06); filter: grayscale(1) opacity(0.4); }

/* POWER ROW */
.prow { background: rgba(124,58,237,0.08); border-radius:12px; padding:13px 16px; display:flex; align-items:center; gap:12px; margin-bottom:8px; border:1px solid rgba(124,58,237,0.2); color:#c4b5fd; font-size:14px; }

/* MISION DIA */
.mdia { background: rgba(124,58,237,0.1); border-radius:14px; padding:18px 20px; border:1px solid rgba(124,58,237,0.3); }
.mdia-tag { font-size:9px; letter-spacing:2px; color:#7c3aed; text-transform:uppercase; margin-bottom:6px; font-weight:800; font-family:'Orbitron',monospace; }
.mdia-txt { font-size:13px; color:#94a3b8; font-style:italic; line-height:1.65; }

/* CHIP */
.chip { background: rgba(124,58,237,0.15); border:1px solid rgba(124,58,237,0.35); border-radius:99px; padding:5px 14px; font-size:12px; color:#a78bfa; display:inline-block; margin:3px; white-space:nowrap; font-weight:700; }

/* FINAL CARD */
.fcard {
    background: linear-gradient(135deg, #0f0a1e 0%, #1a0f3c 50%, #0a1628 100%);
    border-radius: 24px; padding: 52px 36px; text-align: center;
    border: 1px solid rgba(124,58,237,0.3);
    box-shadow: 0 0 60px rgba(124,58,237,0.15), 0 0 120px rgba(6,182,212,0.08);
}
.fcard-title {
    font-family:'Orbitron',monospace; font-size:30px; font-weight:900;
    background: linear-gradient(135deg, #e2e8ff, #a78bfa, #06b6d4);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
    margin-bottom:14px;
}
.fcard-msg { font-size:15px; color:#94a3b8; font-style:italic; line-height:1.85; max-width:500px; margin:0 auto 24px; }

/* NIVEL GRID CARD */
.nivel-grid-card {
    background: rgba(168,85,247,0.07);
    border: 1px solid rgba(168,85,247,0.2);
    border-radius: 16px; padding: 18px 16px;
    cursor: pointer; transition: all 0.2s;
    text-align: center;
}
.nivel-grid-card:hover {
    background: rgba(168,85,247,0.15);
    border-color: rgba(168,85,247,0.5);
    transform: translateY(-2px);
    box-shadow: 0 0 20px rgba(168,85,247,0.2);
}
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE ──────────────────────────────────────────────────────────────
defaults = {
    "progress": set(), "page": "Inicio", "nombre": "",
    "diario": [], "regalo_enviado": False, "regalo_texto": "",
    "saltos": 0, "emocion_usada": False,
    "recargas": set(), "recargas_completas": False,
    "notas": {}, "mision_dia_idx": None, "mision_dia_fecha": None,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

hoy = str(date.today())
if st.session_state.mision_dia_fecha != hoy:
    st.session_state.mision_dia_idx   = random.randint(0, len(NIVELES) - 1)
    st.session_state.mision_dia_fecha = hoy

mision_dia = NIVELES[st.session_state.mision_dia_idx]

def logros_ok():
    p, s = st.session_state.progress, st.session_state
    return [lg for lg in LOGROS if lg["req"](p, s)]

# ── SIDEBAR ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<p style="font-family:Orbitron,monospace;font-size:13px;font-weight:900;color:#a78bfa;letter-spacing:2px;">⚔️ LA GRAN AVENTURA</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:11px;color:#4b3a72;font-style:italic;margin-top:-12px;">del Corazón · 7 Niveles</p>', unsafe_allow_html=True)
    st.divider()

    nombre_in = st.text_input("👤 Tu nombre de explorador", value=st.session_state.nombre, placeholder="Escribe tu nombre...")
    if nombre_in != st.session_state.nombre:
        st.session_state.nombre = nombre_in

    st.divider()

    done  = len(st.session_state.progress)
    total = len(NIVELES)
    st.markdown(f'<p style="font-size:12px;font-weight:700;color:#a78bfa;font-family:Orbitron,monospace;">PROGRESO · {done}/{total}</p>', unsafe_allow_html=True)
    st.progress(done / total)

    n_logros = len(logros_ok())
    st.markdown(
        f'<span class="chip">🏅 {n_logros}/{len(LOGROS)} logros</span>'
        f'<span class="chip">📓 {len(st.session_state.diario)} entradas</span>',
        unsafe_allow_html=True,
    )
    st.divider()

    opciones = ["🏠 Inicio"] + [f"{n['icono']} {n['supertitulo']}: {n['titulo']}" for n in NIVELES] + ["🏆 ¡Completado!"]
    choice = st.radio("nav", opciones, label_visibility="collapsed")
    if choice == "🏠 Inicio":                           st.session_state.page = "Inicio"
    elif choice == "🏆 ¡Completado!":                   st.session_state.page = "Final"
    else:
        nid = int(choice.split("NIVEL ")[1].split(":")[0])
        st.session_state.page = f"nivel_{nid}"

    st.divider()
    st.markdown(f"""
    <div class="mdia">
        <div class="mdia-tag">🎯 misión del día</div>
        <div style="font-size:16px;font-weight:800;color:#c4b5fd;margin-bottom:4px;">{mision_dia['icono']} {mision_dia['titulo']}</div>
        <div class="mdia-txt">"{mision_dia['mision'][:80]}…"</div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    frase = FRASES[date.today().toordinal() % len(FRASES)]
    st.markdown(f'<p style="font-size:11px;color:#4b3a72;font-style:italic;text-align:center;">{frase}</p>', unsafe_allow_html=True)


# ── WIDGETS ────────────────────────────────────────────────────────────────────
def widget_timer():
    st.components.v1.html("""
    <style>
    body { margin:0; background:transparent; font-family:'Nunito',sans-serif; }
    .wbox {
        background: linear-gradient(135deg,#0f0a1e,#12122a);
        border:1px solid rgba(6,182,212,0.35);
        border-radius:18px; padding:28px 24px; text-align:center;
        color:#e2e8ff; box-shadow:0 0 30px rgba(6,182,212,0.1);
    }
    #title { font-family:'Orbitron',monospace; font-size:16px; color:#06b6d4; margin-bottom:4px; font-weight:700; }
    #sub   { font-size:13px; color:#4b5563; font-style:italic; margin-bottom:20px; }
    #display {
        font-family:'Orbitron',monospace; font-size:72px; font-weight:900;
        background: linear-gradient(135deg,#06b6d4,#a78bfa);
        -webkit-background-clip:text; -webkit-text-fill-color:transparent;
        background-clip:text; margin:4px 0; letter-spacing:4px; line-height:1;
    }
    #msg { font-size:14px; color:#94a3b8; min-height:22px; margin-bottom:18px; font-style:italic; }
    .btns { display:flex; gap:12px; justify-content:center; flex-wrap:wrap; }
    button {
        padding:11px 28px; border-radius:12px; font-size:14px; font-weight:700;
        cursor:pointer; transition:all .2s; font-family:'Nunito',sans-serif; border:none;
    }
    #btn-start { background:linear-gradient(135deg,#7c3aed,#06b6d4); color:#fff; box-shadow:0 0 16px rgba(124,58,237,0.4); }
    #btn-start:hover { box-shadow:0 0 28px rgba(6,182,212,0.5); transform:translateY(-2px); }
    #btn-reset { background:rgba(168,85,247,0.12); border:1px solid rgba(168,85,247,0.3); color:#a78bfa; }
    #btn-reset:hover { background:rgba(168,85,247,0.22); transform:translateY(-1px); }
    .bar-wrap { width:100%; background:rgba(255,255,255,0.06); border-radius:99px; height:6px; margin:10px 0 16px; overflow:hidden; }
    #bar { height:6px; border-radius:99px; background:linear-gradient(90deg,#7c3aed,#06b6d4); width:100%; transition:width 1s linear; box-shadow:0 0 8px rgba(6,182,212,0.5); }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Nunito:wght@700&display=swap" rel="stylesheet">
    <div class="wbox">
        <div id="title">⏱️ Temporizador de Oración</div>
        <div id="sub">Permanece 1 minuto en silencio con Dios.</div>
        <div id="display">01:00</div>
        <div class="bar-wrap"><div id="bar"></div></div>
        <div id="msg"></div>
        <div class="btns">
            <button id="btn-start" onclick="toggle()">▶ Iniciar</button>
            <button id="btn-reset" onclick="reset()">⏹ Reiniciar</button>
        </div>
    </div>
    <script>
    const MSGS=["Silencio... Dios te escucha 🙏","Quédate presente... ❤️","Ya casi... ¡lo estás logrando! ⚡","¡Último tramo! 🌟"];
    let t=60,iv=null,running=false;
    const D=()=>document.getElementById('display');
    const M=()=>document.getElementById('msg');
    const B=()=>document.getElementById('btn-start');
    const BAR=()=>document.getElementById('bar');
    function fmt(s){return String(Math.floor(s/60)).padStart(2,'0')+':'+String(s%60).padStart(2,'0');}
    function toggle(){
        if(running){clearInterval(iv);running=false;B().textContent='▶ Continuar';return;}
        running=true;B().textContent='⏸ Pausar';
        iv=setInterval(()=>{
            t--;
            D().textContent=fmt(t);
            BAR().style.width=(t/60*100)+'%';
            let idx=Math.min(Math.floor((1-t/60)*4),3);
            M().textContent=t>0?MSGS[idx]:'';
            if(t<=0){clearInterval(iv);running=false;
                D().style.backgroundImage='linear-gradient(135deg,#22c55e,#06b6d4)';
                D().textContent='🙏 Amén!';
                M().textContent='¡Lo lograste! Dios estuvo contigo. ✨';
                B().textContent='▶ Iniciar';}
        },1000);
    }
    function reset(){
        clearInterval(iv);running=false;t=60;
        D().textContent='01:00';
        D().style.backgroundImage='linear-gradient(135deg,#06b6d4,#a78bfa)';
        M().textContent='';BAR().style.width='100%';B().textContent='▶ Iniciar';
    }
    </script>
    """, height=310, scrolling=False)

def widget_recargas():
    st.markdown('<div class="wbox" style="border-color:rgba(34,197,94,0.35);text-align:left;padding:22px"><div class="wbox-title" style="color:#22c55e">🔋 Recargas de Hoy</div><div class="wbox-sub">Marca las que ya activaste.</div></div>', unsafe_allow_html=True)
    labels = [("🌅","Mañana","Encendiste el día"),("⚡","Día","Pausa rápida activa"),("🌙","Noche","Cierre en paz")]
    cols = st.columns(3)
    for i,(ico,lab,desc) in enumerate(labels):
        with cols[i]:
            st.markdown(f'<div style="text-align:center;font-size:34px;margin-bottom:4px">{ico}</div>', unsafe_allow_html=True)
            if st.checkbox(f"**{lab}** — *{desc}*", value=i in st.session_state.recargas, key=f"rec_{i}"):
                st.session_state.recargas.add(i)
            else:
                st.session_state.recargas.discard(i)
    if len(st.session_state.recargas) == 3:
        st.session_state.recargas_completas = True
        st.success("🔋 ¡Batería al 100%! Logro desbloqueado: **Energía Máxima** ⚡")
    else:
        st.info(f"Te faltan **{3 - len(st.session_state.recargas)}** recarga(s) para llegar al 100%.")

def widget_postura():
    st.markdown('<div class="wbox" style="border-color:rgba(168,85,247,0.4);text-align:left;padding:22px"><div class="wbox-title" style="color:#a855f7">🛡️ Verificador de Postura del Héroe</div><div class="wbox-sub">Actívalos uno por uno antes de orar.</div></div>', unsafe_allow_html=True)
    items = ["📏 Espalda recta y firme","🤲 Manos abiertas o juntas","🦶 Pies apoyados en el suelo","👁️ Ojos cerrados o mirada al suelo","🌬️ Respiré profundo 3 veces"]
    pts = sum(1 for j,item in enumerate(items) if st.checkbox(item, key=f"pos_{j}"))
    if pts == 5:
        st.success("🛡️ **¡Postura de Héroe activada!** Estás listo para escuchar a Dios. 🙏")
        st.balloons()
    elif pts:
        st.info(f"{pts}/5 puntos — ¡casi lista!")

def widget_diario():
    st.markdown('<div class="wbox" style="border-color:rgba(251,191,36,0.4);text-align:left;padding:22px"><div class="wbox-title" style="color:#fbbf24">📓 Diario de Pistas Secretas</div><div class="wbox-sub">¿Qué frase brilló en tu corazón hoy? Guárdala aquí.</div></div>', unsafe_allow_html=True)
    with st.form("f_diario", clear_on_submit=True):
        pista = st.text_area("✍️ Mi pista secreta de hoy...", placeholder='Ej: "Sean fuertes y valientes" y lo que me dijo a mí...', height=90)
        if st.form_submit_button("💾 Guardar pista", use_container_width=True):
            if pista.strip():
                st.session_state.diario.append({"fecha": datetime.now().strftime("%d/%m/%Y %H:%M"), "texto": pista.strip()})
                st.success("✅ ¡Pista guardada! Logro: **Guardián de Pistas** 📓")
                st.balloons()
    if st.session_state.diario:
        st.markdown(f"**📚 Tus pistas ({len(st.session_state.diario)})**")
        for e in reversed(st.session_state.diario[-5:]):
            with st.expander(f"🕐 {e['fecha']}"):
                st.markdown(f'*"{e["texto"]}"*')

def widget_emociones():
    st.markdown('<div class="wbox" style="border-color:rgba(236,72,153,0.4);text-align:left;padding:22px"><div class="wbox-title" style="color:#ec4899">🎭 Panel de Emociones</div><div class="wbox-sub">¿Cómo te sientes ahora? Elige tu emoción y recibe tu oración.</div></div>', unsafe_allow_html=True)
    cols = st.columns(4)
    for i,(label,_) in enumerate(EMOCIONES.items()):
        with cols[i%4]:
            if st.button(label, use_container_width=True, key=f"em_{i}"):
                st.session_state["emocion_sel"] = label
                st.session_state.emocion_usada = True
                st.rerun()
    sel = st.session_state.get("emocion_sel")
    if sel and sel in EMOCIONES:
        d = EMOCIONES[sel]
        st.markdown(f"""
        <div style="background:{d['color']}18;border:2px solid {d['color']}55;border-radius:16px;padding:20px 22px;margin-top:12px;">
            <div style="font-size:22px;font-weight:800;color:{d['color']};margin-bottom:10px;">{sel}</div>
            <div style="font-size:16px;font-style:italic;color:#e2e8ff;margin-bottom:12px;line-height:1.65;">{d['oracion']}</div>
            <div style="font-size:13px;background:rgba(255,255,255,0.04);border-radius:10px;padding:10px 14px;color:#94a3b8;">
                💡 <strong style="color:{d['color']}">Recuerda:</strong> {d['tip']}
            </div>
        </div>""", unsafe_allow_html=True)

def widget_regalo():
    st.markdown('<div class="wbox" style="border-color:rgba(59,130,246,0.4);text-align:left;padding:22px"><div class="wbox-title" style="color:#3b82f6">🎁 Prepara tu Regalo Invisible</div><div class="wbox-sub">Escribe qué le vas a entregar a Dios en la próxima Misa.</div></div>', unsafe_allow_html=True)
    if st.session_state.regalo_enviado:
        st.success(f"🎁 **Regalo preparado:** *\"{st.session_state.regalo_texto}\"*")
        st.markdown("*Llévalo en tu corazón a la Misa. Cuando levanten el pan, entrégaselo.*")
        if st.button("🔄 Preparar un nuevo regalo", use_container_width=True):
            st.session_state.regalo_enviado = False; st.session_state.regalo_texto = ""; st.rerun()
    else:
        with st.form("f_regalo"):
            r = st.text_area("¿Qué esfuerzo, preocupación o alegría le llevas?", placeholder="Ej: Mi miedo a los exámenes, la alegría de mi cumpleaños...", height=80)
            if st.form_submit_button("🎁 Preparar regalo", use_container_width=True):
                if r.strip():
                    st.session_state.regalo_texto = r.strip(); st.session_state.regalo_enviado = True
                    st.success("✅ ¡Logro desbloqueado: Portador de Regalos! 🎁")
                    st.balloons(); st.rerun()

def widget_salto():
    s = st.session_state.saltos
    st.markdown(f"""
    <div class="wbox" style="border-color:rgba(249,115,22,0.4)">
        <div class="wbox-title" style="color:#f97316">🦘 Contador de Saltos de Vuelta</div>
        <div class="wbox-sub">Cada vez que vuelves después de fallar, das un salto.</div>
        <div style="font-family:'Orbitron',monospace;font-size:80px;font-weight:900;
                    background:linear-gradient(135deg,#f97316,#fbbf24);
                    -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                    background-clip:text;line-height:1;margin:8px 0;">{s}</div>
        <div style="font-size:13px;color:#6b7280;">saltos dados</div>
    </div>""", unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    with c1:
        if st.button("🦘 ¡Dar un salto!", use_container_width=True, type="primary"):
            st.session_state.saltos += 1; st.rerun()
    with c2:
        if st.button("🔄 Reiniciar", use_container_width=True):
            st.session_state.saltos = 0; st.rerun()
    msgs = ["¡Bien! Dios te recibe siempre. 🙏","¡Dos veces! Cada regreso cuenta. ⚡","¡Tres! Los héroes no se rinden. 🛡️","¡Cuatro! Ya casi llegas al logro. 🎯","¡CINCO! ¡Explorador Imparable! 🏆"]
    if 0 < s <= 5: st.markdown(f'*{msgs[s-1]}*')
    if s >= 5: st.success("🦘 **¡Logro: Saltador Imparable!** ¡5+ saltos de vuelta!")

# ── PAGE: INICIO ──────────────────────────────────────────────────────────────
def page_inicio():
    n = st.session_state.nombre
    saludo = f"¡Hola, {n}!" if n else "¡Hola, Explorador!"

    st.markdown(f"""
    <div class="hero">
        <div class="hero-eyebrow">⚔️ &nbsp; Tu Superpoder Secreto &nbsp; ⚔️</div>
        <div class="hero-title">LA GRAN AVENTURA<br>DEL CORAZÓN</div>
        <div class="hero-name">{saludo}</div>
        <div class="hero-tagline">Descubre tu superpoder secreto para hablar con Dios.</div>
        <div class="hero-icons">
            <div class="hero-icon-wrap">
                <div class="hero-bubble" style="background:rgba(6,182,212,0.12);border-color:rgba(6,182,212,0.35);box-shadow:0 0 16px rgba(6,182,212,0.2)">🧭</div>
                <div class="hero-icon-lbl" style="color:#06b6d4">Explora</div>
            </div>
            <div class="hero-icon-wrap">
                <div class="hero-bubble" style="background:rgba(168,85,247,0.12);border-color:rgba(168,85,247,0.35);box-shadow:0 0 16px rgba(168,85,247,0.2)">📖</div>
                <div class="hero-icon-lbl" style="color:#a855f7">Aprende</div>
            </div>
            <div class="hero-icon-wrap">
                <div class="hero-bubble" style="background:rgba(251,191,36,0.12);border-color:rgba(251,191,36,0.35);box-shadow:0 0 16px rgba(251,191,36,0.2)">⚡</div>
                <div class="hero-icon-lbl" style="color:#fbbf24">Activa</div>
            </div>
            <div class="hero-icon-wrap">
                <div class="hero-bubble" style="background:rgba(34,197,94,0.12);border-color:rgba(34,197,94,0.35);box-shadow:0 0 16px rgba(34,197,94,0.2)">🏆</div>
                <div class="hero-icon-lbl" style="color:#22c55e">Completa</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="intro-card">
        <div class="intro-tag">✦ Esta no es una herramienta ordinaria ✦</div>
        <div class="intro-txt">
            Es una herramienta que te lleva al tesoro más grande del universo: aprender a hablar con Dios.
            Cada nivel desbloquea un superpoder nuevo. ¿Listo para la aventura?
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Misión del día
    with st.expander(f"🎯  MISIÓN DEL DÍA — {mision_dia['icono']} {mision_dia['titulo']}", expanded=True):
        st.markdown(f"> *{mision_dia['mision']}*")
        st.caption(f"📌 {mision_dia['resumen']}")
        if st.button(f"→ Ir al {mision_dia['supertitulo']}", key="btn_mdia"):
            st.session_state.page = f"nivel_{mision_dia['id']}"; st.rerun()

    st.markdown("---")
    st.markdown('<p style="font-family:Orbitron,monospace;font-size:12px;font-weight:700;color:#7c3aed;letter-spacing:2px;">🗺️ LOS 7 NIVELES</p>', unsafe_allow_html=True)

    cols = st.columns(2)
    for i, nv in enumerate(NIVELES):
        done = nv["id"] in st.session_state.progress
        chk  = "✅" if done else "○"
        with cols[i % 2]:
            if st.button(f"{chk}  {nv['icono']}  **{nv['supertitulo']}**\n\n{nv['titulo']}", key=f"hn{nv['id']}", use_container_width=True):
                st.session_state.page = f"nivel_{nv['id']}"; st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🏆  Ver Pantalla Final", use_container_width=True, type="primary"):
        st.session_state.page = "Final"; st.rerun()


# ── PAGE: NIVEL ───────────────────────────────────────────────────────────────
def page_nivel(nv):
    st.markdown(f"""
    <div class="nivel-hdr" style="background:linear-gradient(135deg,{nv['color']},{nv['color_dark']});
         box-shadow:0 0 30px {nv['glow']};">
        <div class="nivel-hdr-content">
            <div class="nivel-tag">{nv['supertitulo']}</div>
            <div class="nivel-ttl">{nv['icono']}  {nv['titulo']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("💡  ¿Sabías que...?", expanded=True):
        st.markdown(f'<div style="color:#a5f3fc;font-size:15px;line-height:1.7;">{nv["sabias_que"]}</div>', unsafe_allow_html=True)

    with st.expander("🏺  La Idea de Oro", expanded=True):
        st.markdown(f'<div style="font-family:Orbitron,monospace;font-size:15px;font-weight:700;color:{nv["color"]};margin-bottom:10px;">{nv["idea_titulo"]}</div>', unsafe_allow_html=True)
        st.markdown(nv["idea_texto"])

    with st.expander("🎯  Misión para ti", expanded=True):
        st.markdown(f'<div style="font-size:15px;color:#fde68a;line-height:1.7;"><strong>¡Tu misión!</strong> {nv["mision"]}</div>', unsafe_allow_html=True)

    # Widget especial
    wmap = {"timer":widget_timer,"recargas":widget_recargas,"postura":widget_postura,
            "diario":widget_diario,"emociones":widget_emociones,"regalo":widget_regalo,"salto":widget_salto}
    if nv.get("widget") in wmap:
        st.markdown("---")
        st.markdown('<p style="font-family:Orbitron,monospace;font-size:11px;font-weight:700;color:#7c3aed;letter-spacing:2px;">🛠️ HERRAMIENTA DE PRÁCTICA</p>', unsafe_allow_html=True)
        wmap[nv["widget"]]()

    # Notas
    st.markdown("---")
    with st.expander("📝  Mis notas personales", expanded=False):
        nota = st.text_area("¿Qué aprendiste? ¿Qué quieres recordar?", value=st.session_state.notas.get(nv["id"],""), height=90, key=f"nota_{nv['id']}")
        st.session_state.notas[nv["id"]] = nota

    # Resumen
    st.markdown(f"""
    <div class="resumen" style="background:linear-gradient(90deg,{nv['color']},{nv['color_dark']});
         border-radius:12px;margin-top:8px;box-shadow:0 0 20px {nv['glow']};">
        📌 &nbsp;<strong>Resumen:</strong>&nbsp;{nv['resumen']}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    with c1:
        if st.button("← Inicio", use_container_width=True):
            st.session_state.page = "Inicio"; st.rerun()
    with c2:
        if nv["id"] in st.session_state.progress:
            st.success("✅ ¡Nivel completado!")
        else:
            if st.button("☐  Marcar como completado", use_container_width=True, type="primary"):
                st.session_state.progress.add(nv["id"]); st.balloons(); st.rerun()

    if nv["id"] < len(NIVELES):
        nx = NIVELES[nv["id"]]
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button(f"→ Siguiente: {nx['icono']} {nx['titulo']}", use_container_width=True):
            st.session_state.page = f"nivel_{nx['id']}"; st.rerun()


# ── PAGE: FINAL ───────────────────────────────────────────────────────────────
def page_final():
    done  = len(st.session_state.progress)
    total = len(NIVELES)
    nb    = st.session_state.nombre or "Explorador"
    ok    = logros_ok()

    st.markdown(f"""
    <div class="fcard">
        <div style="font-size:72px;margin-bottom:12px;">🏆</div>
        <div style="font-size:18px;letter-spacing:2px;color:#fbbf24;margin-bottom:14px;">{'⭐ '*7}</div>
        <div class="fcard-title">¡Lo lograste, {nb}!</div>
        <div class="fcard-msg">
            Ya tienes el superpoder más grande del universo: saber que Dios te escucha siempre,
            en cualquier lugar, con cualquier palabra, con cualquier emoción.<br><br>
            Esta herramienta no termina aquí. Apenas empieza.<br>
            <strong style="color:#06b6d4;">¡Sigue explorando cada día!</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Niveles",        f"{done}/{total}")
    c2.metric("Logros",         f"{len(ok)}/{len(LOGROS)}")
    c3.metric("Diario",         len(st.session_state.diario))
    c4.metric("Saltos",         st.session_state.saltos)

    if done == total:
        st.success("🎉 **¡AVENTURA COMPLETA!** ¡Eres un Explorador Imparable!")
    else:
        st.info(f"Has completado **{done} de {total}** niveles. ¡La aventura te espera!")

    st.markdown("---")
    st.markdown('<p style="font-family:Orbitron,monospace;font-size:11px;font-weight:700;color:#7c3aed;letter-spacing:2px;">🏅 LOGROS</p>', unsafe_allow_html=True)
    ca,cb = st.columns(2)
    for i,lg in enumerate(LOGROS):
        desbloqueado = lg["req"](st.session_state.progress, st.session_state)
        cls = "logro-on" if desbloqueado else "logro-off"
        col_txt = "#e2e8ff" if desbloqueado else "#444"
        estado = ("✅ Desbloqueado" if desbloqueado else "🔒 Bloqueado")
        ec = "#22c55e" if desbloqueado else "#374151"
        with (ca if i%2==0 else cb):
            st.markdown(f"""
            <div class="logro {cls}">
                <span style="font-size:28px">{lg['icono']}</span>
                <div>
                    <div style="font-weight:800;font-size:14px;color:{col_txt}">{lg['nombre']}</div>
                    <div style="font-size:12px;color:#4b5563">{lg['desc']}</div>
                    <div style="font-size:11px;font-weight:700;color:{ec}">{estado}</div>
                </div>
            </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<p style="font-family:Orbitron,monospace;font-size:11px;font-weight:700;color:#7c3aed;letter-spacing:2px;">⚡ SUPERPODERES</p>', unsafe_allow_html=True)
    for ico,txt,nid in [("⚡","Orar en 1 minuto, en cualquier lugar",1),("🔋","Las 3 Recargas Mágicas diarias",2),
                         ("🛡️","La Postura del Héroe para escuchar",3),("🗺️","Leer la Biblia como detective secreto",4),
                         ("🎮","El Botón de Emergencias en toda emoción",5),("⛪","La Misa como la gran reunión de equipo",6),
                         ("🧭","Volver a empezar siempre",7)]:
        chk = "✅" if nid in st.session_state.progress else "○"
        st.markdown(f'<div class="prow"><span style="font-size:22px">{ico}</span><span style="flex:1">{txt}</span><span style="font-size:18px">{chk}</span></div>', unsafe_allow_html=True)

    if st.session_state.diario:
        st.markdown("---")
        st.markdown(f'<p style="font-family:Orbitron,monospace;font-size:11px;font-weight:700;color:#7c3aed;letter-spacing:2px;">📓 DIARIO SECRETO ({len(st.session_state.diario)} entradas)</p>', unsafe_allow_html=True)
        for e in reversed(st.session_state.diario):
            with st.expander(f"🕐 {e['fecha']}"):
                st.markdown(f'*"{e["texto"]}"*')

    st.markdown("<br>", unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    with c1:
        if st.button("🔄 Reiniciar progreso", use_container_width=True):
            for k,v in defaults.items():
                st.session_state[k] = set() if isinstance(v,set) else ([] if isinstance(v,list) else ({} if isinstance(v,dict) else v))
            st.session_state.page = "Inicio"; st.rerun()
    with c2:
        if st.button("🧭 Volver al inicio", use_container_width=True, type="primary"):
            st.session_state.page = "Inicio"; st.rerun()


# ── ROUTER ────────────────────────────────────────────────────────────────────
pg = st.session_state.page
if   pg == "Inicio":            page_inicio()
elif pg == "Final":             page_final()
elif pg.startswith("nivel_"):
    nid = int(pg.split("_")[1])
    page_nivel(next(n for n in NIVELES if n["id"] == nid))
