import streamlit as st

st.set_page_config(layout="wide", page_title="Cotation Temps réel")

# ── Paramètres d'espacement ──────────────────
SPACE_TITRE_INPUTS = 10   # px entre la ligne fine et la ligne 1 des inputs
SPACE_ENTRE_LIGNES = 4    # px entre les lignes de boutons

st.markdown("""
<style>

/* Labels désactivés (type primary + disabled) → bleu foncé */
button[kind="primary"][disabled] {
    background-color: #1a5276 !important;
    opacity: 1 !important;
    color: white !important;
    cursor: default !important;
    border: none !important;
    font-weight: 600 !important;
    text-align: left !important;
    justify-content: flex-start !important;
    padding-left: 12px !important;
}
/* Le <p> intérieur du bouton Streamlit */
button[kind="primary"][disabled] p {
    text-align: left !important;
    width: 100% !important;
}

/* Boutons actifs (type secondary) → rose saumon, SAUF le popover */
button[kind="secondary"]:not([disabled]):not([data-testid="stPopoverButton"]) {
    background-color: #e8938a !important;
    color: #1a1a1a !important;
    border: none !important;
    font-weight: 700 !important;
}
button[kind="secondary"]:not([disabled]):not([data-testid="stPopoverButton"]):hover {
    background-color: #e74c3c !important;
    color: white !important;
}

/* Bouton Prompt → rouge via son wrapper id */
#btn-prompt-wrap button {
    background-color: #c0392b !important;
    color: white !important;
    font-weight: 700 !important;
    border: none !important;
}
#btn-prompt-wrap button:hover {
    background-color: #a93226 !important;
}
    background-color: #c0392b !important;
    color: white !important;
    font-weight: 700 !important;
    border: none !important;
}
#btn-expl-wrap button:hover {
    background-color: #a93226 !important;
}

/* Flux arrêté = bouton désactivé secondary → gris */
button[kind="secondary"][disabled] {
    background-color: #7f8c8d !important;
    opacity: 1 !important;
    color: white !important;
    font-weight: 600 !important;
    border: none !important;
    cursor: default !important;
}

/* Popover petit bouton "?" → gris foncé, rond, petit */
div[data-testid="stPopover"] {
    display: flex !important;
    align-items: flex-end !important;
    height: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
}
div[data-testid="stPopover"] > button {
    height: 22px !important;
    width: 22px !important;
    min-height: 22px !important;
    padding: 0 !important;
    font-size: 11px !important;
    font-weight: bold !important;
    border-radius: 50% !important;
    line-height: 22px !important;
    background-color: #b8bcc2 !important;
    color: #2c3e50 !important;
    border: none !important;
}

/* Supprime marges résiduelles */
div[data-testid="stVerticalBlock"] > div {
    margin-bottom: 0 !important;
    padding-bottom: 0 !important;
}

/* Fond de page gris */
div[data-testid="stAppViewContainer"] {
    background-color: #e8eaed !important;
}
div[data-testid="stMain"] {
    background-color: #e8eaed !important;
}

/* Champs de saisie → fond blanc + coins arrondis partout */

/* text_input */
div[data-testid="stTextInput"] input {
    background-color: #ffffff !important;
    border-radius: 6px !important;
}

/* selectbox */
div[data-testid="stSelectbox"] > div > div {
    background-color: #ffffff !important;
    border-radius: 6px !important;
}

/* number_input : le champ texte central */
div[data-testid="stNumberInput"] input {
    background-color: #ffffff !important;
}
/* number_input : le conteneur global avec les boutons +/- */
div[data-testid="stNumberInput"] > div {
    background-color: #ffffff !important;
    border-radius: 6px !important;
    overflow: hidden !important;
}

/* Dropdown selectbox ouvert → fond blanc */
ul[data-testid="stSelectboxVirtualDropdown"] {
    background-color: #ffffff !important;
}

/* Métriques : conteneur transparent comme un champ de saisie */
div[data-testid="stMetric"] {
    background-color: transparent !important;
    padding: 0 !important;
}

/* Valeur métrique : même hauteur que les inputs, police sobre */
div[data-testid="stMetricValue"] {
    background-color: #ffffff !important;
    border-radius: 6px !important;
    padding: 0 10px !important;
    margin-top: 2px !important;
    font-size: 0.9rem !important;
    line-height: 2.1 !important;     /* aligne la hauteur sur celle des inputs */
    min-height: 38px !important;
    display: flex !important;
    align-items: center !important;
}

/* Label de la métrique : même style que les labels des inputs */
div[data-testid="stMetricLabel"] p {
    font-size: 0.8rem !important;
    color: #555 !important;
}

</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
#  LIGNE TITRE — base 10
#  [Pop:0.3][Titre:4.7][vide:5]
# ═══════════════════════════════════════════════════════════════
t1, t2, t3 = st.columns([0.3, 4.7, 5], vertical_alignment="center")
with t1:
    with st.popover("?"):
        st.markdown("**À propos de cette page**")
        st.markdown("- Interface de cotation en temps réel via Interactive Brokers")
        st.markdown("- Connexion via API TWS ou IB Gateway")
        st.markdown("- Les données sont mises à jour tick par tick")
        st.markdown("- Le flux peut être arrêté/relancé sans redémarrer l'application")
with t2:
    st.markdown(
        "<h2 style='color:#1a5276; font-weight:800; margin:0; padding:0;'>"
        "Cotation Temps réel (V4 – callback)</h2>",
        unsafe_allow_html=True
    )
# t3 : vide

# Ligne fine collée sous le titre
st.markdown(
    "<hr style='margin:0; padding:0; border:none; border-top:1px solid #b8bcc2;'>",
    unsafe_allow_html=True
)
# Espace entre la ligne fine et les inputs
st.markdown(f"<div style='height:{SPACE_TITRE_INPUTS}px;'></div>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
#  LIGNE 1 — base 10
#  [Env:1][Sym:1][Exch:1][Niv:1][Mode:1][Interv:1][Lim:1][Ticks:1][HeureIB:1][vide:1]
# ═══════════════════════════════════════════════════════════════
c1,c2,c3,c4,c5,c6,c7,c8,c9,c10 = st.columns(
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    vertical_alignment="bottom"
)
with c1:
    st.selectbox("Environnement", ["live","paper","simulation"], key="env")
with c2:
    st.text_input("Symbole", value="SPY", key="sym")
with c3:
    st.selectbox("Exchange", ["SMART","NYSE","NASDAQ"], key="exch")
with c4:
    st.selectbox("Niveau d'abonnement", [1,2,3,4], index=3, key="niv")
with c5:
    st.selectbox("Mode", ["Real-Time","Delayed","Frozen"], key="mode")
with c6:
    st.number_input("Intervalle / S", min_value=1, max_value=60,
                    value=5, step=1, key="interv")
with c7:
    st.number_input("Limite / tick", min_value=1000, max_value=500000,
                    value=50000, step=1000, key="lim")
with c8:
    st.button("Ticks : 0 / 50,000", key="ticks_display",
              disabled=True, type="primary",
              use_container_width=True)
with c9:
    st.button("✅  Heure IB : OK", key="heure_ib",
              disabled=True, type="primary",
              use_container_width=True)
# c10 : vide

# ═══════════════════════════════════════════════════════════════
#  LIGNE 2 — base 10
#  [Ctrl acq:2][GO:1][STOP:1][REINIT:1][Flux:1][vide:4]
# ═══════════════════════════════════════════════════════════════
r2c1,r2c2,r2c3,r2c4,r2c5,r2c6 = st.columns(
    [2, 1, 1, 1, 1, 4],
    vertical_alignment="bottom"
)
with r2c1:
    st.button("Contrôle acquisition", key="lbl_ctrl",
              disabled=True, type="primary",
              use_container_width=True)
with r2c2:
    st.button("►►►  GO",      key="btn_go",     use_container_width=True)
with r2c3:
    st.button("►►►  STOP",    key="btn_stop",   use_container_width=True)
with r2c4:
    st.button("►►►  REINIT",  key="btn_reinit", use_container_width=True)
with r2c5:
    st.button("⏸  Flux arrêté", key="btn_flux",
              disabled=True,
              use_container_width=True)
# r2c6 : vide (4)

# ═══════════════════════════════════════════════════════════════
#  LIGNE 3 — base 10
#  [Last:1][Bid:1][Ask:1][Volume:1][GRAPH:1][LOG:1][Heure:1][vide:3]
# ═══════════════════════════════════════════════════════════════
r3c1,r3c2,r3c3,r3c4,r3c5,r3c6,r3c7,r3c8 = st.columns(
    [1, 1, 1, 1, 1, 1, 1, 3],
    vertical_alignment="bottom"
)
with r3c1:
    st.metric("Last",   "—")
with r3c2:
    st.metric("Bid",    "—")
with r3c3:
    st.metric("Ask",    "—")
with r3c4:
    st.metric("Volume", "—")
with r3c5:
    st.button("►►►  GRAPH ON-OFF", key="btn_graph", use_container_width=True)
with r3c6:
    st.button("►►►  LOG ON-OFF",   key="btn_log",   use_container_width=True)
with r3c7:
    st.button("Heure : —", key="lbl_heure",
              disabled=True, type="primary",
              use_container_width=True)
# r3c8 : vide (3)

# ═══════════════════════════════════════════════════════════════
#  LIGNE TEST — base 10
#  [Pop:0.3][Ctrl acq:1.7][vide:8]
# ═══════════════════════════════════════════════════════════════
tst1, tst2, tst3 = st.columns([0.3, 1.7, 8], vertical_alignment="bottom")
with tst1:
    with st.popover("?"):
        st.markdown("**Aide — Contrôle acquisition**")
        st.markdown("- Démarre ou arrête l'acquisition des données")
        st.markdown("- Le flux peut être relancé sans redémarrer l'application")
with tst2:
    st.button("Contrôle acquisition", key="lbl_ctrl_test",
              disabled=True, type="primary",
              use_container_width=True)
# tst3 : vide

# ═══════════════════════════════════════════════════════════════
#  LIGNE 4 — base 10
#  [Explication:2][vide:8]  → bouton rouge déclenchant un expander
# ═══════════════════════════════════════════════════════════════
r4c1, r4c2, r4c3 = st.columns([1, 1, 8], vertical_alignment="bottom")
with r4c1:
    st.markdown("<div id='btn-expl-wrap'>", unsafe_allow_html=True)
    expl = st.button("►►►  Explication", key="btn_expl", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
with r4c2:
    st.markdown("<div id='btn-prompt-wrap'>", unsafe_allow_html=True)
    prompt = st.button("►►►  Prompt", key="btn_prompt", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

if expl:
    st.session_state["show_expl"] = not st.session_state.get("show_expl", False)

if prompt:
    st.session_state["show_prompt"] = not st.session_state.get("show_prompt", False)

if st.session_state.get("show_expl", False):
    with st.expander("", expanded=True):
        st.markdown("""
## Architecture générale

Cette page est construite sur une **grille de 10 colonnes** utilisée comme référence commune pour toutes les lignes. Chaque ligne est déclarée avec `st.columns([...])` dont la somme des proportions fait toujours **10**. Les colonnes inutilisées en fin de ligne restent vides et servent à maintenir la cohérence visuelle horizontale.

---

## Proportions par ligne

| Ligne | Contenu | Proportions |
|-------|---------|-------------|
| **Titre** | Popover + Titre + vide | 0.3 + 4.7 + 5 = 10 |
| **1** | 7 champs de saisie + Ticks + Heure IB + vide | 1×9 + 1 = 10 |
| **2** | Label Contrôle (2) + GO + STOP + REINIT + Flux + vide | 2+1+1+1+1+4 = 10 |
| **3** | Last + Bid + Ask + Volume + GRAPH + LOG + Heure + vide | 1×7 + 3 = 10 |
| **4** | Bouton Explication + vide | 2 + 8 = 10 |

---

## Stratégie d'alignement horizontal

Le paramètre `vertical_alignment="bottom"` de `st.columns()` aligne les bases de tous les widgets sur une ligne basse commune. Mais il ne fonctionne correctement que si **tous les éléments sont des vrais widgets natifs Streamlit** de hauteur comparable.

### Widgets qui ne posent AUCUN problème
Ces widgets ont une hauteur fixe et sont pleinement gérés par `vertical_alignment` :

| Widget | Remarque |
|--------|----------|
| `st.button()` | Référence absolue de hauteur |
| `st.metric()` | Natif, bien géré |
| `st.popover()` | Natif, bien géré |
| `st.checkbox()`, `st.toggle()`, `st.radio()` | Natifs, boîte physique fixe |
| `st.selectbox()`, `st.text_input()`, `st.number_input()` | Natifs, mais leur **label** consomme de la hauteur → utiliser `label_visibility="collapsed"` si besoin |

### Widgets qui posent le MÊME problème que `st.markdown()`
Ces éléments génèrent du contenu HTML libre sans hauteur définie — `vertical_alignment` ne sait pas les gérer :

| Widget | Problème |
|--------|----------|
| `st.markdown()` | Principal coupable — génère une `<div>` de hauteur variable |
| `st.write()` | Alias de `st.markdown()` dans la plupart des cas |
| `st.caption()` | Texte grisé, même comportement |
| `st.text()` | Texte brut, hauteur non standardisée |
| `st.latex()` | Formules mathématiques, hauteur imprévisible |
| `st.code()` | Blocs de code, hauteur variable selon le contenu |
| `st.html()` | HTML brut injecté, encore plus imprévisible |

### Solution adoptée
Les **labels bleus** ("Contrôle acquisition", "Ticks", "Heure") sont des `st.button(disabled=True, type="primary")` stylisés en CSS. Streamlit les traite exactement comme les boutons actifs pour le calcul d'alignement.

Les **métriques** (Last, Bid, Ask, Volume) utilisent `st.metric()` dont seule la valeur reçoit un fond blanc via CSS sur `div[data-testid="stMetricValue"]`, le label restant transparent comme pour les champs de saisie.

---

## Stratégie CSS

Streamlit génère des classes aléatoires (`st-emotion-cache-...`) qui changent à chaque rechargement. La règle absolue : **ne jamais cibler ces classes**, utiliser uniquement les `data-testid` stables :

```css
div[data-testid="stButton"]        /* boutons */
div[data-testid="stSelectbox"]     /* listes déroulantes */
div[data-testid="stNumberInput"]   /* champs numériques */
div[data-testid="stMetricValue"]   /* valeur des métriques */
div[data-testid="stPopover"]       /* popover */
button[kind="primary"][disabled]   /* labels-boutons */
button[kind="secondary"]           /* boutons d'action */
```

Le fond de page gris (`#e8eaed`) met en valeur tous les éléments blancs par contraste, sans bordures complexes sur chaque widget.
        """)

if st.session_state.get("show_prompt", False):
    with st.expander("", expanded=True):
        st.markdown("""
## Format de prompt pour créer une interface

Utilise ce format pour décrire une nouvelle interface. Chaque ligne fait toujours **10** en proportion.

---

### Paramètres globaux (à déclarer en tête)
```
Fond de page : #e8eaed | Hauteur boutons : 38px
Espace titre/ligne1 : 10px | Espace entre lignes : 4px
```

---

### Format d'une ligne
```
L[n] [élément:proportion "texte" couleur | élément:proportion | vide:proportion]
```

---

### Mots-clés disponibles

| Mot-clé | Widget Streamlit | Remarque |
|---------|-----------------|----------|
| `pop` | `st.popover("?")` | Toujours 0.3, rond, gris |
| `label` | `st.button(disabled=True, type="primary")` | Texte aligné à gauche, bleu foncé |
| `btn` | `st.button()` | Rose saumon par défaut |
| `metric` | `st.metric()` | Fond blanc sur valeur uniquement |
| `input` | `st.text_input()` | Fond blanc, coins arrondis |
| `select` | `st.selectbox()` | Fond blanc, coins arrondis |
| `num` | `st.number_input()` | Fond blanc, coins arrondis |
| `vide` | colonne vide | Complète jusqu'à 10 |
| `DIVIDER` | ligne fine + espace | Séparateur entre titre et contenu |

---

### Couleurs disponibles pour les boutons
`rose` (défaut) | `rouge` | `bleu` | `vert` | `gris`

---

### Exemple complet
```
Nouvelle interface "Gestion des ordres"
Fond : #e8eaed | Espace titre/L1 : 8px

TITRE  [pop:0.3 | titre:4.7 "Gestion des ordres" | vide:5]
DIVIDER
L1     [select:1 "Compte" | input:1 "Symbole" | num:1 "Qté" |
        select:1 "Type" | num:1 "Prix limite" | vide:5]
L2     [label:2 "Passage d'ordre" | btn:1 "ACHAT" vert |
        btn:1 "VENTE" rouge | btn:1 "ANNULER" | btn:1 "En attente" gris | vide:4]
L3     [metric:1 "PnL" | metric:1 "Position" | metric:1 "Prix moy" | vide:7]
L4     [btn:1 "►►►  Explication" rouge | btn:1 "►►►  Prompt" rouge | vide:8]
```

---

### Règles importantes
- La somme des proportions de chaque ligne doit toujours faire **10**
- Ne jamais utiliser `st.markdown()` pour afficher du texte sur une ligne de colonnes → utiliser `label` à la place
- Le `pop` fait toujours **0.3** et si suivi d'un `label`, ensemble ils font **2** (0.3 + 1.7)
- Le titre est **intouchable** sauf mention explicite dans le prompt
        """)