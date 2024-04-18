import streamlit as st
from streamlit.logger import get_logger
from streamlit.hello.utils import show_code
import altair as alt
import numpy as np
import pandas as pd

LOGGER = get_logger(__name__)

st.set_page_config(page_title="Pāḷi Text Juncture Splitterrrrr", page_icon="🌴")

# Sidebar

#st.sidebar.header("Language")
#st.sidebar.write("""<div style="width:100%;"><img src="https://cdn.britannica.com/33/4833-004-828A9A84/Flag-United-States-of-America.jpg" width="22px"> English</img></div>
#                 <div style="width:100%;"><a href="https://translate.google.co.id/?hl=id&sl=en&tl=id&op=translate"><img src="https://i.pinimg.com/736x/91/3d/f8/913df8098c7237aae279c4628302f49c.jpg" width="22px"> Bahasa Indonesia</img></a></div>""", unsafe_allow_html=True)
 
#st.sidebar.divider()

st.sidebar.header("Customize your conversion:")

st.markdown("<h1 style='text-align: center;'>Pāḷi Text Juncture Splitter 🌴</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'><em>For easy Pāḷi reading.</em></h3>", unsafe_allow_html=True)
st.divider()

st.markdown("<h4 style='text-align: center;'>What is it and who is it for?</h6>", unsafe_allow_html=True)

"""
The _Pāḷi Text Juncture Splitter_ is a fragmentizing tool that break up Pāḷi texts based on the class of each syllable (heavy or light) so that you may read them _effortlessly_ with just the right tempo.\n
It is perfect for beginners and intermediates in Pāḷi reading, Pāḷi instructors who are looking for a teaching aid, as well as those who would like to proficiently chant Parittā verses.\n
"""

st.markdown("<h6 style='text-align: center;'>For an example, here is a split stanza from <em>Ratana Sutta</em>:</h6>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Yā — nī — dha bhū — tā — ni samā — gatā — ni —</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Bhum — mā — ni vā — yā — ni va an — talik — khe —</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Sab — be — va bhū — tā — sumanā — bhavan — tu —</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Atho — pi sak — kac — ca suṇan — tu bhā — sitaṃ —</p>", unsafe_allow_html=True)

st.divider()
"""
**Start splitting by inserting Pāḷi text here:**
"""
def animation_demo() -> None:
    # Insert Text
    insert_text = st.text_area('', height=200, placeholder="e.g. 'Namo tassa bhagavato arahato sammāsambuddhassa.'")

    # Medial anusvāra/niggahīta to nasal (gaṃgā → gaṅgā)
    nasal_check = st.sidebar.checkbox(label='Medial anusvāra/niggahīta to nasal (gaṃgā → gaṅgā)')

    # Nasal ññ → nñ)
    nñ_check = st.sidebar.checkbox(label='ññ → nñ')

    # Nasal ṅ, ṃ, ṁ → ng)
    ng_check = st.sidebar.checkbox(label='ṅ, ṃ, ṁ → ng')

    # Split text in UPPERCASE
    uppercase_check = st.sidebar.checkbox(label='Split text in UPPERCASE')

    # Saṃyoga - Pauses
    samyoga_pauses_check = st.sidebar.checkbox(label='Saṃyoga chanting style - Pauses')
    st.sidebar.caption('↳ no pauses at commas, periods, and the end of lines')

    # Saṃyoga - Consonants
    samyoga_consonants_check = st.sidebar.checkbox(label='Saṃyoga chanting style - Consonants')
    st.sidebar.caption('↳ no retroflex consonants; b, bh → ph; d, dh → th; g, gh → kh; j, jh →ch; ñ → y')

    # Anusvāra/niggahīta standard conversion (ṃ ⇄ ṁ)
    anusvara_select = st.sidebar.selectbox(
    "Anusvāra/niggahīta standard conversion  \n(ṃ ⇄ ṁ)",
    ("None", "Change to ṃ - IAST (International Alphabet of Sanskrit Transliteration)", "Change to ṁ - ISO 15919: Pāḷi"),
    index=None,
    placeholder="None",
    )

    # Default & Custom Juncture Sign
    def_sepa= " — "
    juncture_placeholder = "Optional"
    custom_sepa = st.sidebar.text_input(label='Customize your own juncture sign:', placeholder=juncture_placeholder)
    st.sidebar.caption('↳ try • , _ , - , ^ , / , \ , = , ~ , | , )( , }{ , or ][ ')
    if custom_sepa == '':
        sepa=def_sepa
    else:
        sepa=(" "+custom_sepa+" ")

    # Show Unsplit Text of Each Split Line
    show_unsplit = st.sidebar.checkbox(label='Show unsplit text')
    st.sidebar.caption('↳ Unsplit text followed by split text line by line')

    #Fix line breaks to double whitespaces and line breaks
    fixed_text= insert_text.replace('\n','  \n')

    # Insert juncture sign after long vowels (ā, ī, ū, e, o)
    # lowercase
    added_V_ā_sepa = fixed_text.replace('ā','ā'+sepa)
    added_V_ī_sepa = added_V_ā_sepa.replace('ī','ī'+sepa)
    added_V_ū_sepa = added_V_ī_sepa.replace('ū','ū'+sepa)
    added_V_e_sepa = added_V_ū_sepa.replace('e','e'+sepa)
    added_V_o_sepa = added_V_e_sepa.replace('o','o'+sepa)

    # TitleCase
    # a
    Ā_ka = added_V_o_sepa.replace('Āka', 'Ā'+sepa+'ka')
    Ā_kha = Ā_ka.replace('Ākha', 'Ā'+sepa+'kha')
    Ā_ga = Ā_kha.replace('Āga', 'Ā'+sepa+'ga')
    Ā_gha = Ā_ga.replace('Āgha', 'Ā'+sepa+'gha')
    Ā_ṅa = Ā_gha.replace('Āṅa', 'Ā'+sepa+'ṅa')
    Ā_ca = Ā_ṅa.replace('Āca', 'Ā'+sepa+'ca')
    Ā_cha = Ā_ca.replace('Ācha', 'Ā'+sepa+'cha')
    Ā_ja = Ā_cha.replace('Āja', 'Ā'+sepa+'ja')
    Ā_jha = Ā_ja.replace('Ājha', 'Ā'+sepa+'jha')
    Ā_ña = Ā_jha.replace('Āña', 'Ā'+sepa+'ña')
    Ā_ṭa = Ā_ña.replace('Āṭa', 'Ā'+sepa+'ṭa')
    Ā_ṭha = Ā_ṭa.replace('Āṭha', 'Ā'+sepa+'ṭha')
    Ā_ḍa = Ā_ṭha.replace('Āḍa', 'Ā'+sepa+'ḍa')
    Ā_ḍha = Ā_ḍa.replace('Āḍha', 'Ā'+sepa+'ḍha')
    Ā_ṇa = Ā_ḍha.replace('Āṇa', 'Ā'+sepa+'ṇa')
    Ā_ta = Ā_ṇa.replace('Āta', 'Ā'+sepa+'ta')
    Ā_tha = Ā_ta.replace('Ātha', 'Ā'+sepa+'tha')
    Ā_da = Ā_tha.replace('Āda', 'Ā'+sepa+'da')
    Ā_dha = Ā_da.replace('Ādha', 'Ā'+sepa+'dha')
    Ā_na = Ā_dha.replace('Āna', 'Ā'+sepa+'na')
    Ā_pa = Ā_na.replace('Āpa', 'Ā'+sepa+'pa')
    Ā_pha = Ā_pa.replace('Āpha', 'Ā'+sepa+'pha')
    Ā_ba = Ā_pha.replace('Āba', 'Ā'+sepa+'ba')
    Ā_bha = Ā_ba.replace('Ābha', 'Ā'+sepa+'bha')
    Ā_ma = Ā_bha.replace('Āma', 'Ā'+sepa+'ma')
    Ā_ra = Ā_ma.replace('Āra', 'Ā'+sepa+'ra')
    Ā_la = Ā_ra.replace('Āla', 'Ā'+sepa+'la')
    Ā_ḷa = Ā_la.replace('Āḷa', 'Ā'+sepa+'ḷa')
    Ā_ya = Ā_ḷa.replace('Āya', 'Ā'+sepa+'ya')
    Ā_va = Ā_ya.replace('Āva', 'Ā'+sepa+'va')
    Ā_sa = Ā_va.replace('Āsa', 'Ā'+sepa+'sa')
    Ā_ha = Ā_sa.replace('Āha', 'Ā'+sepa+'ha')

    Ī_ka = Ā_ha.replace('Īka', 'Ī'+sepa+'ka')
    Ī_kha = Ī_ka.replace('Īkha', 'Ī'+sepa+'kha')
    Ī_ga = Ī_kha.replace('Īga', 'Ī'+sepa+'ga')
    Ī_gha = Ī_ga.replace('Īgha', 'Ī'+sepa+'gha')
    Ī_ṅa = Ī_gha.replace('Īṅa', 'Ī'+sepa+'ṅa')
    Ī_ca = Ī_ṅa.replace('Īca', 'Ī'+sepa+'ca')
    Ī_cha = Ī_ca.replace('Īcha', 'Ī'+sepa+'cha')
    Ī_ja = Ī_cha.replace('Īja', 'Ī'+sepa+'ja')
    Ī_jha = Ī_ja.replace('Ījha', 'Ī'+sepa+'jha')
    Ī_ña = Ī_jha.replace('Īña', 'Ī'+sepa+'ña')
    Ī_ṭa = Ī_ña.replace('Īṭa', 'Ī'+sepa+'ṭa')
    Ī_ṭha = Ī_ṭa.replace('Īṭha', 'Ī'+sepa+'ṭha')
    Ī_ḍa = Ī_ṭha.replace('Īḍa', 'Ī'+sepa+'ḍa')
    Ī_ḍha = Ī_ḍa.replace('Īḍha', 'Ī'+sepa+'ḍha')
    Ī_ṇa = Ī_ḍha.replace('Īṇa', 'Ī'+sepa+'ṇa')
    Ī_ta = Ī_ṇa.replace('Īta', 'Ī'+sepa+'ta')
    Ī_tha = Ī_ta.replace('Ītha', 'Ī'+sepa+'tha')
    Ī_da = Ī_tha.replace('Īda', 'Ī'+sepa+'da')
    Ī_dha = Ī_da.replace('Īdha', 'Ī'+sepa+'dha')
    Ī_na = Ī_dha.replace('Īna', 'Ī'+sepa+'na')
    Ī_pa = Ī_na.replace('Īpa', 'Ī'+sepa+'pa')
    Ī_pha = Ī_pa.replace('Īpha', 'Ī'+sepa+'pha')
    Ī_ba = Ī_pha.replace('Ība', 'Ī'+sepa+'ba')
    Ī_bha = Ī_ba.replace('Ībha', 'Ī'+sepa+'bha')
    Ī_ma = Ī_bha.replace('Īma', 'Ī'+sepa+'ma')
    Ī_ra = Ī_ma.replace('Īra', 'Ī'+sepa+'ra')
    Ī_la = Ī_ra.replace('Īla', 'Ī'+sepa+'la')
    Ī_ḷa = Ī_la.replace('Īḷa', 'Ī'+sepa+'ḷa')
    Ī_ya = Ī_ḷa.replace('Īya', 'Ī'+sepa+'ya')
    Ī_va = Ī_ya.replace('Īva', 'Ī'+sepa+'va')
    Ī_sa = Ī_va.replace('Īsa', 'Ī'+sepa+'sa')
    Ī_ha = Ī_sa.replace('Īha', 'Ī'+sepa+'ha')

    Ū_ka = Ī_ha.replace('Ūka', 'Ū'+sepa+'ka')
    Ū_kha = Ū_ka.replace('Ūkha', 'Ū'+sepa+'kha')
    Ū_ga = Ū_kha.replace('Ūga', 'Ū'+sepa+'ga')
    Ū_gha = Ū_ga.replace('Ūgha', 'Ū'+sepa+'gha')
    Ū_ṅa = Ū_gha.replace('Ūṅa', 'Ū'+sepa+'ṅa')
    Ū_ca = Ū_ṅa.replace('Ūca', 'Ū'+sepa+'ca')
    Ū_cha = Ū_ca.replace('Ūcha', 'Ū'+sepa+'cha')
    Ū_ja = Ū_cha.replace('Ūja', 'Ū'+sepa+'ja')
    Ū_jha = Ū_ja.replace('Ūjha', 'Ū'+sepa+'jha')
    Ū_ña = Ū_jha.replace('Ūña', 'Ū'+sepa+'ña')
    Ū_ṭa = Ū_ña.replace('Ūṭa', 'Ū'+sepa+'ṭa')
    Ū_ṭha = Ū_ṭa.replace('Ūṭha', 'Ū'+sepa+'ṭha')
    Ū_ḍa = Ū_ṭha.replace('Ūḍa', 'Ū'+sepa+'ḍa')
    Ū_ḍha = Ū_ḍa.replace('Ūḍha', 'Ū'+sepa+'ḍha')
    Ū_ṇa = Ū_ḍha.replace('Ūṇa', 'Ū'+sepa+'ṇa')
    Ū_ta = Ū_ṇa.replace('Ūta', 'Ū'+sepa+'ta')
    Ū_tha = Ū_ta.replace('Ūtha', 'Ū'+sepa+'tha')
    Ū_da = Ū_tha.replace('Ūda', 'Ū'+sepa+'da')
    Ū_dha = Ū_da.replace('Ūdha', 'Ū'+sepa+'dha')
    Ū_na = Ū_dha.replace('Ūna', 'Ū'+sepa+'na')
    Ū_pa = Ū_na.replace('Ūpa', 'Ū'+sepa+'pa')
    Ū_pha = Ū_pa.replace('Ūpha', 'Ū'+sepa+'pha')
    Ū_ba = Ū_pha.replace('Ūba', 'Ū'+sepa+'ba')
    Ū_bha = Ū_ba.replace('Ūbha', 'Ū'+sepa+'bha')
    Ū_ma = Ū_bha.replace('Ūma', 'Ū'+sepa+'ma')
    Ū_ra = Ū_ma.replace('Ūra', 'Ū'+sepa+'ra')
    Ū_la = Ū_ra.replace('Ūla', 'Ū'+sepa+'la')
    Ū_ḷa = Ū_la.replace('Ūḷa', 'Ū'+sepa+'ḷa')
    Ū_ya = Ū_ḷa.replace('Ūya', 'Ū'+sepa+'ya')
    Ū_va = Ū_ya.replace('Ūva', 'Ū'+sepa+'va')
    Ū_sa = Ū_va.replace('Ūsa', 'Ū'+sepa+'sa')
    Ū_ha = Ū_sa.replace('Ūha', 'Ū'+sepa+'ha')

    E_ka = Ū_ha.replace('Eka', 'E'+sepa+'ka')
    E_kha = E_ka.replace('Ekha', 'E'+sepa+'kha')
    E_ga = E_kha.replace('Ega', 'E'+sepa+'ga')
    E_gha = E_ga.replace('Egha', 'E'+sepa+'gha')
    E_ṅa = E_gha.replace('Eṅa', 'E'+sepa+'ṅa')
    E_ca = E_ṅa.replace('Eca', 'E'+sepa+'ca')
    E_cha = E_ca.replace('Echa', 'E'+sepa+'cha')
    E_ja = E_cha.replace('Eja', 'E'+sepa+'ja')
    E_jha = E_ja.replace('Ejha', 'E'+sepa+'jha')
    E_ña = E_jha.replace('Eña', 'E'+sepa+'ña')
    E_ṭa = E_ña.replace('Eṭa', 'E'+sepa+'ṭa')
    E_ṭha = E_ṭa.replace('Eṭha', 'E'+sepa+'ṭha')
    E_ḍa = E_ṭha.replace('Eḍa', 'E'+sepa+'ḍa')
    E_ḍha = E_ḍa.replace('Eḍha', 'E'+sepa+'ḍha')
    E_ṇa = E_ḍha.replace('Eṇa', 'E'+sepa+'ṇa')
    E_ta = E_ṇa.replace('Eta', 'E'+sepa+'ta')
    E_tha = E_ta.replace('Etha', 'E'+sepa+'tha')
    E_da = E_tha.replace('Eda', 'E'+sepa+'da')
    E_dha = E_da.replace('Edha', 'E'+sepa+'dha')
    E_na = E_dha.replace('Ena', 'E'+sepa+'na')
    E_pa = E_na.replace('Epa', 'E'+sepa+'pa')
    E_pha = E_pa.replace('Epha', 'E'+sepa+'pha')
    E_ba = E_pha.replace('Eba', 'E'+sepa+'ba')
    E_bha = E_ba.replace('Ebha', 'E'+sepa+'bha')
    E_ma = E_bha.replace('Ema', 'E'+sepa+'ma')
    E_ra = E_ma.replace('Era', 'E'+sepa+'ra')
    E_la = E_ra.replace('Ela', 'E'+sepa+'la')
    E_ḷa = E_la.replace('Eḷa', 'E'+sepa+'ḷa')
    E_ya = E_ḷa.replace('Eya', 'E'+sepa+'ya')
    E_va = E_ya.replace('Eva', 'E'+sepa+'va')
    E_sa = E_va.replace('Esa', 'E'+sepa+'sa')
    E_ha = E_sa.replace('Eha', 'E'+sepa+'ha')

    O_ka = E_ha.replace('Oka', 'O'+sepa+'ka')
    O_kha = O_ka.replace('Okha', 'O'+sepa+'kha')
    O_ga = O_kha.replace('Oga', 'O'+sepa+'ga')
    O_gha = O_ga.replace('Ogha', 'O'+sepa+'gha')
    O_ṅa = O_gha.replace('Oṅa', 'O'+sepa+'ṅa')
    O_ca = O_ṅa.replace('Oca', 'O'+sepa+'ca')
    O_cha = O_ca.replace('Ocha', 'O'+sepa+'cha')
    O_ja = O_cha.replace('Oja', 'O'+sepa+'ja')
    O_jha = O_ja.replace('Ojha', 'O'+sepa+'jha')
    O_ña = O_jha.replace('Oña', 'O'+sepa+'ña')
    O_ṭa = O_ña.replace('Oṭa', 'O'+sepa+'ṭa')
    O_ṭha = O_ṭa.replace('Oṭha', 'O'+sepa+'ṭha')
    O_ḍa = O_ṭha.replace('Oḍa', 'O'+sepa+'ḍa')
    O_ḍha = O_ḍa.replace('Oḍha', 'O'+sepa+'ḍha')
    O_ṇa = O_ḍha.replace('Oṇa', 'O'+sepa+'ṇa')
    O_ta = O_ṇa.replace('Ota', 'O'+sepa+'ta')
    O_tha = O_ta.replace('Otha', 'O'+sepa+'tha')
    O_da = O_tha.replace('Oda', 'O'+sepa+'da')
    O_dha = O_da.replace('Odha', 'O'+sepa+'dha')
    O_na = O_dha.replace('Ona', 'O'+sepa+'na')
    O_pa = O_na.replace('Opa', 'O'+sepa+'pa')
    O_pha = O_pa.replace('Opha', 'O'+sepa+'pha')
    O_ba = O_pha.replace('Oba', 'O'+sepa+'ba')
    O_bha = O_ba.replace('Obha', 'O'+sepa+'bha')
    O_ma = O_bha.replace('Oma', 'O'+sepa+'ma')
    O_ra = O_ma.replace('Ora', 'O'+sepa+'ra')
    O_la = O_ra.replace('Ola', 'O'+sepa+'la')
    O_ḷa = O_la.replace('Oḷa', 'O'+sepa+'ḷa')
    O_ya = O_ḷa.replace('Oya', 'O'+sepa+'ya')
    O_va = O_ya.replace('Ova', 'O'+sepa+'va')
    O_sa = O_va.replace('Osa', 'O'+sepa+'sa')
    O_ha = O_sa.replace('Oha', 'O'+sepa+'ha')

    # ā
    Ā_kā = O_ha.replace('Ākā', 'Ā'+sepa+'kā')
    Ā_khā = Ā_kā.replace('Ākhā', 'Ā'+sepa+'khā')
    Ā_gā = Ā_khā.replace('Āgā', 'Ā'+sepa+'gā')
    Ā_ghā = Ā_gā.replace('Āghā', 'Ā'+sepa+'ghā')
    Ā_ṅā = Ā_ghā.replace('Āṅā', 'Ā'+sepa+'ṅā')
    Ā_cā = Ā_ṅā.replace('Ācā', 'Ā'+sepa+'cā')
    Ā_chā = Ā_cā.replace('Āchā', 'Ā'+sepa+'chā')
    Ā_jā = Ā_chā.replace('Ājā', 'Ā'+sepa+'jā')
    Ā_jhā = Ā_jā.replace('Ājhā', 'Ā'+sepa+'jhā')
    Ā_ñā = Ā_jhā.replace('Āñā', 'Ā'+sepa+'ñā')
    Ā_ṭā = Ā_ñā.replace('Āṭā', 'Ā'+sepa+'ṭā')
    Ā_ṭhā = Ā_ṭā.replace('Āṭhā', 'Ā'+sepa+'ṭhā')
    Ā_ḍā = Ā_ṭhā.replace('Āḍā', 'Ā'+sepa+'ḍā')
    Ā_ḍhā = Ā_ḍā.replace('Āḍhā', 'Ā'+sepa+'ḍhā')
    Ā_ṇā = Ā_ḍhā.replace('Āṇā', 'Ā'+sepa+'ṇā')
    Ā_tā = Ā_ṇā.replace('Ātā', 'Ā'+sepa+'tā')
    Ā_thā = Ā_tā.replace('Āthā', 'Ā'+sepa+'thā')
    Ā_dā = Ā_thā.replace('Ādā', 'Ā'+sepa+'dā')
    Ā_dhā = Ā_dā.replace('Ādhā', 'Ā'+sepa+'dhā')
    Ā_nā = Ā_dhā.replace('Ānā', 'Ā'+sepa+'nā')
    Ā_pā = Ā_nā.replace('Āpā', 'Ā'+sepa+'pā')
    Ā_phā = Ā_pā.replace('Āphā', 'Ā'+sepa+'phā')
    Ā_bā = Ā_phā.replace('Ābā', 'Ā'+sepa+'bā')
    Ā_bhā = Ā_bā.replace('Ābhā', 'Ā'+sepa+'bhā')
    Ā_mā = Ā_bhā.replace('Āmā', 'Ā'+sepa+'mā')
    Ā_rā = Ā_mā.replace('Ārā', 'Ā'+sepa+'rā')
    Ā_lā = Ā_rā.replace('Ālā', 'Ā'+sepa+'lā')
    Ā_ḷā = Ā_lā.replace('Āḷā', 'Ā'+sepa+'ḷā')
    Ā_yā = Ā_ḷā.replace('Āyā', 'Ā'+sepa+'yā')
    Ā_vā = Ā_yā.replace('Āvā', 'Ā'+sepa+'vā')
    Ā_sā = Ā_vā.replace('Āsā', 'Ā'+sepa+'sā')
    Ā_hā = Ā_sā.replace('Āhā', 'Ā'+sepa+'hā')

    Ī_kā = Ā_hā.replace('Īkā', 'Ī'+sepa+'kā')
    Ī_khā = Ī_kā.replace('Īkhā', 'Ī'+sepa+'khā')
    Ī_gā = Ī_khā.replace('Īgā', 'Ī'+sepa+'gā')
    Ī_ghā = Ī_gā.replace('Īghā', 'Ī'+sepa+'ghā')
    Ī_ṅā = Ī_ghā.replace('Īṅā', 'Ī'+sepa+'ṅā')
    Ī_cā = Ī_ṅā.replace('Īcā', 'Ī'+sepa+'cā')
    Ī_chā = Ī_cā.replace('Īchā', 'Ī'+sepa+'chā')
    Ī_jā = Ī_chā.replace('Ījā', 'Ī'+sepa+'jā')
    Ī_jhā = Ī_jā.replace('Ījhā', 'Ī'+sepa+'jhā')
    Ī_ñā = Ī_jhā.replace('Īñā', 'Ī'+sepa+'ñā')
    Ī_ṭā = Ī_ñā.replace('Īṭā', 'Ī'+sepa+'ṭā')
    Ī_ṭhā = Ī_ṭā.replace('Īṭhā', 'Ī'+sepa+'ṭhā')
    Ī_ḍā = Ī_ṭhā.replace('Īḍā', 'Ī'+sepa+'ḍā')
    Ī_ḍhā = Ī_ḍā.replace('Īḍhā', 'Ī'+sepa+'ḍhā')
    Ī_ṇā = Ī_ḍhā.replace('Īṇā', 'Ī'+sepa+'ṇā')
    Ī_tā = Ī_ṇā.replace('Ītā', 'Ī'+sepa+'tā')
    Ī_thā = Ī_tā.replace('Īthā', 'Ī'+sepa+'thā')
    Ī_dā = Ī_thā.replace('Īdā', 'Ī'+sepa+'dā')
    Ī_dhā = Ī_dā.replace('Īdhā', 'Ī'+sepa+'dhā')
    Ī_nā = Ī_dhā.replace('Īnā', 'Ī'+sepa+'nā')
    Ī_pā = Ī_nā.replace('Īpā', 'Ī'+sepa+'pā')
    Ī_phā = Ī_pā.replace('Īphā', 'Ī'+sepa+'phā')
    Ī_bā = Ī_phā.replace('Ībā', 'Ī'+sepa+'bā')
    Ī_bhā = Ī_bā.replace('Ībhā', 'Ī'+sepa+'bhā')
    Ī_mā = Ī_bhā.replace('Īmā', 'Ī'+sepa+'mā')
    Ī_rā = Ī_mā.replace('Īrā', 'Ī'+sepa+'rā')
    Ī_lā = Ī_rā.replace('Īlā', 'Ī'+sepa+'lā')
    Ī_ḷā = Ī_lā.replace('Īḷā', 'Ī'+sepa+'ḷā')
    Ī_yā = Ī_ḷā.replace('Īyā', 'Ī'+sepa+'yā')
    Ī_vā = Ī_yā.replace('Īvā', 'Ī'+sepa+'vā')
    Ī_sā = Ī_vā.replace('Īsā', 'Ī'+sepa+'sā')
    Ī_hā = Ī_sā.replace('Īhā', 'Ī'+sepa+'hā')

    Ū_kā = Ī_hā.replace('Ūkā', 'Ū'+sepa+'kā')
    Ū_khā = Ū_kā.replace('Ūkhā', 'Ū'+sepa+'khā')
    Ū_gā = Ū_khā.replace('Ūgā', 'Ū'+sepa+'gā')
    Ū_ghā = Ū_gā.replace('Ūghā', 'Ū'+sepa+'ghā')
    Ū_ṅā = Ū_ghā.replace('Ūṅā', 'Ū'+sepa+'ṅā')
    Ū_cā = Ū_ṅā.replace('Ūcā', 'Ū'+sepa+'cā')
    Ū_chā = Ū_cā.replace('Ūchā', 'Ū'+sepa+'chā')
    Ū_jā = Ū_chā.replace('Ūjā', 'Ū'+sepa+'jā')
    Ū_jhā = Ū_jā.replace('Ūjhā', 'Ū'+sepa+'jhā')
    Ū_ñā = Ū_jhā.replace('Ūñā', 'Ū'+sepa+'ñā')
    Ū_ṭā = Ū_ñā.replace('Ūṭā', 'Ū'+sepa+'ṭā')
    Ū_ṭhā = Ū_ṭā.replace('Ūṭhā', 'Ū'+sepa+'ṭhā')
    Ū_ḍā = Ū_ṭhā.replace('Ūḍā', 'Ū'+sepa+'ḍā')
    Ū_ḍhā = Ū_ḍā.replace('Ūḍhā', 'Ū'+sepa+'ḍhā')
    Ū_ṇā = Ū_ḍhā.replace('Ūṇā', 'Ū'+sepa+'ṇā')
    Ū_tā = Ū_ṇā.replace('Ūtā', 'Ū'+sepa+'tā')
    Ū_thā = Ū_tā.replace('Ūthā', 'Ū'+sepa+'thā')
    Ū_dā = Ū_thā.replace('Ūdā', 'Ū'+sepa+'dā')
    Ū_dhā = Ū_dā.replace('Ūdhā', 'Ū'+sepa+'dhā')
    Ū_nā = Ū_dhā.replace('Ūnā', 'Ū'+sepa+'nā')
    Ū_pā = Ū_nā.replace('Ūpā', 'Ū'+sepa+'pā')
    Ū_phā = Ū_pā.replace('Ūphā', 'Ū'+sepa+'phā')
    Ū_bā = Ū_phā.replace('Ūbā', 'Ū'+sepa+'bā')
    Ū_bhā = Ū_bā.replace('Ūbhā', 'Ū'+sepa+'bhā')
    Ū_mā = Ū_bhā.replace('Ūmā', 'Ū'+sepa+'mā')
    Ū_rā = Ū_mā.replace('Ūrā', 'Ū'+sepa+'rā')
    Ū_lā = Ū_rā.replace('Ūlā', 'Ū'+sepa+'lā')
    Ū_ḷā = Ū_lā.replace('Ūḷā', 'Ū'+sepa+'ḷā')
    Ū_yā = Ū_ḷā.replace('Ūyā', 'Ū'+sepa+'yā')
    Ū_vā = Ū_yā.replace('Ūvā', 'Ū'+sepa+'vā')
    Ū_sā = Ū_vā.replace('Ūsā', 'Ū'+sepa+'sā')
    Ū_hā = Ū_sā.replace('Ūhā', 'Ū'+sepa+'hā')

    E_kā = Ū_hā.replace('Ekā', 'E'+sepa+'kā')
    E_khā = E_kā.replace('Ekhā', 'E'+sepa+'khā')
    E_gā = E_khā.replace('Egā', 'E'+sepa+'gā')
    E_ghā = E_gā.replace('Eghā', 'E'+sepa+'ghā')
    E_ṅā = E_ghā.replace('Eṅā', 'E'+sepa+'ṅā')
    E_cā = E_ṅā.replace('Ecā', 'E'+sepa+'cā')
    E_chā = E_cā.replace('Echā', 'E'+sepa+'chā')
    E_jā = E_chā.replace('Ejā', 'E'+sepa+'jā')
    E_jhā = E_jā.replace('Ejhā', 'E'+sepa+'jhā')
    E_ñā = E_jhā.replace('Eñā', 'E'+sepa+'ñā')
    E_ṭā = E_ñā.replace('Eṭā', 'E'+sepa+'ṭā')
    E_ṭhā = E_ṭā.replace('Eṭhā', 'E'+sepa+'ṭhā')
    E_ḍā = E_ṭhā.replace('Eḍā', 'E'+sepa+'ḍā')
    E_ḍhā = E_ḍā.replace('Eḍhā', 'E'+sepa+'ḍhā')
    E_ṇā = E_ḍhā.replace('Eṇā', 'E'+sepa+'ṇā')
    E_tā = E_ṇā.replace('Etā', 'E'+sepa+'tā')
    E_thā = E_tā.replace('Ethā', 'E'+sepa+'thā')
    E_dā = E_thā.replace('Edā', 'E'+sepa+'dā')
    E_dhā = E_dā.replace('Edhā', 'E'+sepa+'dhā')
    E_nā = E_dhā.replace('Enā', 'E'+sepa+'nā')
    E_pā = E_nā.replace('Epā', 'E'+sepa+'pā')
    E_phā = E_pā.replace('Ephā', 'E'+sepa+'phā')
    E_bā = E_phā.replace('Ebā', 'E'+sepa+'bā')
    E_bhā = E_bā.replace('Ebhā', 'E'+sepa+'bhā')
    E_mā = E_bhā.replace('Emā', 'E'+sepa+'mā')
    E_rā = E_mā.replace('Erā', 'E'+sepa+'rā')
    E_lā = E_rā.replace('Elā', 'E'+sepa+'lā')
    E_ḷā = E_lā.replace('Eḷā', 'E'+sepa+'ḷā')
    E_yā = E_ḷā.replace('Eyā', 'E'+sepa+'yā')
    E_vā = E_yā.replace('Evā', 'E'+sepa+'vā')
    E_sā = E_vā.replace('Esā', 'E'+sepa+'sā')
    E_hā = E_sā.replace('Ehā', 'E'+sepa+'hā')

    O_kā = E_hā.replace('Okā', 'O'+sepa+'kā')
    O_khā = O_kā.replace('Okhā', 'O'+sepa+'khā')
    O_gā = O_khā.replace('Ogā', 'O'+sepa+'gā')
    O_ghā = O_gā.replace('Oghā', 'O'+sepa+'ghā')
    O_ṅā = O_ghā.replace('Oṅā', 'O'+sepa+'ṅā')
    O_cā = O_ṅā.replace('Ocā', 'O'+sepa+'cā')
    O_chā = O_cā.replace('Ochā', 'O'+sepa+'chā')
    O_jā = O_chā.replace('Ojā', 'O'+sepa+'jā')
    O_jhā = O_jā.replace('Ojhā', 'O'+sepa+'jhā')
    O_ñā = O_jhā.replace('Oñā', 'O'+sepa+'ñā')
    O_ṭā = O_ñā.replace('Oṭā', 'O'+sepa+'ṭā')
    O_ṭhā = O_ṭā.replace('Oṭhā', 'O'+sepa+'ṭhā')
    O_ḍā = O_ṭhā.replace('Oḍā', 'O'+sepa+'ḍā')
    O_ḍhā = O_ḍā.replace('Oḍhā', 'O'+sepa+'ḍhā')
    O_ṇā = O_ḍhā.replace('Oṇā', 'O'+sepa+'ṇā')
    O_tā = O_ṇā.replace('Otā', 'O'+sepa+'tā')
    O_thā = O_tā.replace('Othā', 'O'+sepa+'thā')
    O_dā = O_thā.replace('Odā', 'O'+sepa+'dā')
    O_dhā = O_dā.replace('Odhā', 'O'+sepa+'dhā')
    O_nā = O_dhā.replace('Onā', 'O'+sepa+'nā')
    O_pā = O_nā.replace('Opā', 'O'+sepa+'pā')
    O_phā = O_pā.replace('Ophā', 'O'+sepa+'phā')
    O_bā = O_phā.replace('Obā', 'O'+sepa+'bā')
    O_bhā = O_bā.replace('Obhā', 'O'+sepa+'bhā')
    O_mā = O_bhā.replace('Omā', 'O'+sepa+'mā')
    O_rā = O_mā.replace('Orā', 'O'+sepa+'rā')
    O_lā = O_rā.replace('Olā', 'O'+sepa+'lā')
    O_ḷā = O_lā.replace('Oḷā', 'O'+sepa+'ḷā')
    O_yā = O_ḷā.replace('Oyā', 'O'+sepa+'yā')
    O_vā = O_yā.replace('Ovā', 'O'+sepa+'vā')
    O_sā = O_vā.replace('Osā', 'O'+sepa+'sā')
    O_hā = O_sā.replace('Ohā', 'O'+sepa+'hā')

    # i
    Ā_ki = O_hā.replace('Āki', 'Ā'+sepa+'ki')
    Ā_khi = Ā_ki.replace('Ākhi', 'Ā'+sepa+'khi')
    Ā_gi = Ā_khi.replace('Āgi', 'Ā'+sepa+'gi')
    Ā_ghi = Ā_gi.replace('Āghi', 'Ā'+sepa+'ghi')
    Ā_ṅi = Ā_ghi.replace('Āṅi', 'Ā'+sepa+'ṅi')
    Ā_ci = Ā_ṅi.replace('Āci', 'Ā'+sepa+'ci')
    Ā_chi = Ā_ci.replace('Āchi', 'Ā'+sepa+'chi')
    Ā_ji = Ā_chi.replace('Āji', 'Ā'+sepa+'ji')
    Ā_jhi = Ā_ji.replace('Ājhi', 'Ā'+sepa+'jhi')
    Ā_ñi = Ā_jhi.replace('Āñi', 'Ā'+sepa+'ñi')
    Ā_ṭi = Ā_ñi.replace('Āṭi', 'Ā'+sepa+'ṭi')
    Ā_ṭhi = Ā_ṭi.replace('Āṭhi', 'Ā'+sepa+'ṭhi')
    Ā_ḍi = Ā_ṭhi.replace('Āḍi', 'Ā'+sepa+'ḍi')
    Ā_ḍhi = Ā_ḍi.replace('Āḍhi', 'Ā'+sepa+'ḍhi')
    Ā_ṇi = Ā_ḍhi.replace('Āṇi', 'Ā'+sepa+'ṇi')
    Ā_ti = Ā_ṇi.replace('Āti', 'Ā'+sepa+'ti')
    Ā_thi = Ā_ti.replace('Āthi', 'Ā'+sepa+'thi')
    Ā_di = Ā_thi.replace('Ādi', 'Ā'+sepa+'di')
    Ā_dhi = Ā_di.replace('Ādhi', 'Ā'+sepa+'dhi')
    Ā_ni = Ā_dhi.replace('Āni', 'Ā'+sepa+'ni')
    Ā_pi = Ā_ni.replace('Āpi', 'Ā'+sepa+'pi')
    Ā_phi = Ā_pi.replace('Āphi', 'Ā'+sepa+'phi')
    Ā_bi = Ā_phi.replace('Ābi', 'Ā'+sepa+'bi')
    Ā_bhi = Ā_bi.replace('Ābhi', 'Ā'+sepa+'bhi')
    Ā_mi = Ā_bhi.replace('Āmi', 'Ā'+sepa+'mi')
    Ā_ri = Ā_mi.replace('Āri', 'Ā'+sepa+'ri')
    Ā_li = Ā_ri.replace('Āli', 'Ā'+sepa+'li')
    Ā_ḷi = Ā_li.replace('Āḷi', 'Ā'+sepa+'ḷi')
    Ā_yi = Ā_ḷi.replace('Āyi', 'Ā'+sepa+'yi')
    Ā_vi = Ā_yi.replace('Āvi', 'Ā'+sepa+'vi')
    Ā_si = Ā_vi.replace('Āsi', 'Ā'+sepa+'si')
    Ā_hi = Ā_si.replace('Āhi', 'Ā'+sepa+'hi')

    Ī_ki = Ā_hi.replace('Īki', 'Ī'+sepa+'ki')
    Ī_khi = Ī_ki.replace('Īkhi', 'Ī'+sepa+'khi')
    Ī_gi = Ī_khi.replace('Īgi', 'Ī'+sepa+'gi')
    Ī_ghi = Ī_gi.replace('Īghi', 'Ī'+sepa+'ghi')
    Ī_ṅi = Ī_ghi.replace('Īṅi', 'Ī'+sepa+'ṅi')
    Ī_ci = Ī_ṅi.replace('Īci', 'Ī'+sepa+'ci')
    Ī_chi = Ī_ci.replace('Īchi', 'Ī'+sepa+'chi')
    Ī_ji = Ī_chi.replace('Īji', 'Ī'+sepa+'ji')
    Ī_jhi = Ī_ji.replace('Ījhi', 'Ī'+sepa+'jhi')
    Ī_ñi = Ī_jhi.replace('Īñi', 'Ī'+sepa+'ñi')
    Ī_ṭi = Ī_ñi.replace('Īṭi', 'Ī'+sepa+'ṭi')
    Ī_ṭhi = Ī_ṭi.replace('Īṭhi', 'Ī'+sepa+'ṭhi')
    Ī_ḍi = Ī_ṭhi.replace('Īḍi', 'Ī'+sepa+'ḍi')
    Ī_ḍhi = Ī_ḍi.replace('Īḍhi', 'Ī'+sepa+'ḍhi')
    Ī_ṇi = Ī_ḍhi.replace('Īṇi', 'Ī'+sepa+'ṇi')
    Ī_ti = Ī_ṇi.replace('Īti', 'Ī'+sepa+'ti')
    Ī_thi = Ī_ti.replace('Īthi', 'Ī'+sepa+'thi')
    Ī_di = Ī_thi.replace('Īdi', 'Ī'+sepa+'di')
    Ī_dhi = Ī_di.replace('Īdhi', 'Ī'+sepa+'dhi')
    Ī_ni = Ī_dhi.replace('Īni', 'Ī'+sepa+'ni')
    Ī_pi = Ī_ni.replace('Īpi', 'Ī'+sepa+'pi')
    Ī_phi = Ī_pi.replace('Īphi', 'Ī'+sepa+'phi')
    Ī_bi = Ī_phi.replace('Ībi', 'Ī'+sepa+'bi')
    Ī_bhi = Ī_bi.replace('Ībhi', 'Ī'+sepa+'bhi')
    Ī_mi = Ī_bhi.replace('Īmi', 'Ī'+sepa+'mi')
    Ī_ri = Ī_mi.replace('Īri', 'Ī'+sepa+'ri')
    Ī_li = Ī_ri.replace('Īli', 'Ī'+sepa+'li')
    Ī_ḷi = Ī_li.replace('Īḷi', 'Ī'+sepa+'ḷi')
    Ī_yi = Ī_ḷi.replace('Īyi', 'Ī'+sepa+'yi')
    Ī_vi = Ī_yi.replace('Īvi', 'Ī'+sepa+'vi')
    Ī_si = Ī_vi.replace('Īsi', 'Ī'+sepa+'si')
    Ī_hi = Ī_si.replace('Īhi', 'Ī'+sepa+'hi')

    Ū_ki = Ī_hi.replace('Ūki', 'Ū'+sepa+'ki')
    Ū_khi = Ū_ki.replace('Ūkhi', 'Ū'+sepa+'khi')
    Ū_gi = Ū_khi.replace('Ūgi', 'Ū'+sepa+'gi')
    Ū_ghi = Ū_gi.replace('Ūghi', 'Ū'+sepa+'ghi')
    Ū_ṅi = Ū_ghi.replace('Ūṅi', 'Ū'+sepa+'ṅi')
    Ū_ci = Ū_ṅi.replace('Ūci', 'Ū'+sepa+'ci')
    Ū_chi = Ū_ci.replace('Ūchi', 'Ū'+sepa+'chi')
    Ū_ji = Ū_chi.replace('Ūji', 'Ū'+sepa+'ji')
    Ū_jhi = Ū_ji.replace('Ūjhi', 'Ū'+sepa+'jhi')
    Ū_ñi = Ū_jhi.replace('Ūñi', 'Ū'+sepa+'ñi')
    Ū_ṭi = Ū_ñi.replace('Ūṭi', 'Ū'+sepa+'ṭi')
    Ū_ṭhi = Ū_ṭi.replace('Ūṭhi', 'Ū'+sepa+'ṭhi')
    Ū_ḍi = Ū_ṭhi.replace('Ūḍi', 'Ū'+sepa+'ḍi')
    Ū_ḍhi = Ū_ḍi.replace('Ūḍhi', 'Ū'+sepa+'ḍhi')
    Ū_ṇi = Ū_ḍhi.replace('Ūṇi', 'Ū'+sepa+'ṇi')
    Ū_ti = Ū_ṇi.replace('Ūti', 'Ū'+sepa+'ti')
    Ū_thi = Ū_ti.replace('Ūthi', 'Ū'+sepa+'thi')
    Ū_di = Ū_thi.replace('Ūdi', 'Ū'+sepa+'di')
    Ū_dhi = Ū_di.replace('Ūdhi', 'Ū'+sepa+'dhi')
    Ū_ni = Ū_dhi.replace('Ūni', 'Ū'+sepa+'ni')
    Ū_pi = Ū_ni.replace('Ūpi', 'Ū'+sepa+'pi')
    Ū_phi = Ū_pi.replace('Ūphi', 'Ū'+sepa+'phi')
    Ū_bi = Ū_phi.replace('Ūbi', 'Ū'+sepa+'bi')
    Ū_bhi = Ū_bi.replace('Ūbhi', 'Ū'+sepa+'bhi')
    Ū_mi = Ū_bhi.replace('Ūmi', 'Ū'+sepa+'mi')
    Ū_ri = Ū_mi.replace('Ūri', 'Ū'+sepa+'ri')
    Ū_li = Ū_ri.replace('Ūli', 'Ū'+sepa+'li')
    Ū_ḷi = Ū_li.replace('Ūḷi', 'Ū'+sepa+'ḷi')
    Ū_yi = Ū_ḷi.replace('Ūyi', 'Ū'+sepa+'yi')
    Ū_vi = Ū_yi.replace('Ūvi', 'Ū'+sepa+'vi')
    Ū_si = Ū_vi.replace('Ūsi', 'Ū'+sepa+'si')
    Ū_hi = Ū_si.replace('Ūhi', 'Ū'+sepa+'hi')

    E_ki = Ū_hi.replace('Eki', 'E'+sepa+'ki')
    E_khi = E_ki.replace('Ekhi', 'E'+sepa+'khi')
    E_gi = E_khi.replace('Egi', 'E'+sepa+'gi')
    E_ghi = E_gi.replace('Eghi', 'E'+sepa+'ghi')
    E_ṅi = E_ghi.replace('Eṅi', 'E'+sepa+'ṅi')
    E_ci = E_ṅi.replace('Eci', 'E'+sepa+'ci')
    E_chi = E_ci.replace('Echi', 'E'+sepa+'chi')
    E_ji = E_chi.replace('Eji', 'E'+sepa+'ji')
    E_jhi = E_ji.replace('Ejhi', 'E'+sepa+'jhi')
    E_ñi = E_jhi.replace('Eñi', 'E'+sepa+'ñi')
    E_ṭi = E_ñi.replace('Eṭi', 'E'+sepa+'ṭi')
    E_ṭhi = E_ṭi.replace('Eṭhi', 'E'+sepa+'ṭhi')
    E_ḍi = E_ṭhi.replace('Eḍi', 'E'+sepa+'ḍi')
    E_ḍhi = E_ḍi.replace('Eḍhi', 'E'+sepa+'ḍhi')
    E_ṇi = E_ḍhi.replace('Eṇi', 'E'+sepa+'ṇi')
    E_ti = E_ṇi.replace('Eti', 'E'+sepa+'ti')
    E_thi = E_ti.replace('Ethi', 'E'+sepa+'thi')
    E_di = E_thi.replace('Edi', 'E'+sepa+'di')
    E_dhi = E_di.replace('Edhi', 'E'+sepa+'dhi')
    E_ni = E_dhi.replace('Eni', 'E'+sepa+'ni')
    E_pi = E_ni.replace('Epi', 'E'+sepa+'pi')
    E_phi = E_pi.replace('Ephi', 'E'+sepa+'phi')
    E_bi = E_phi.replace('Ebi', 'E'+sepa+'bi')
    E_bhi = E_bi.replace('Ebhi', 'E'+sepa+'bhi')
    E_mi = E_bhi.replace('Emi', 'E'+sepa+'mi')
    E_ri = E_mi.replace('Eri', 'E'+sepa+'ri')
    E_li = E_ri.replace('Eli', 'E'+sepa+'li')
    E_ḷi = E_li.replace('Eḷi', 'E'+sepa+'ḷi')
    E_yi = E_ḷi.replace('Eyi', 'E'+sepa+'yi')
    E_vi = E_yi.replace('Evi', 'E'+sepa+'vi')
    E_si = E_vi.replace('Esi', 'E'+sepa+'si')
    E_hi = E_si.replace('Ehi', 'E'+sepa+'hi')

    O_ki = E_hi.replace('Oki', 'O'+sepa+'ki')
    O_khi = O_ki.replace('Okhi', 'O'+sepa+'khi')
    O_gi = O_khi.replace('Ogi', 'O'+sepa+'gi')
    O_ghi = O_gi.replace('Oghi', 'O'+sepa+'ghi')
    O_ṅi = O_ghi.replace('Oṅi', 'O'+sepa+'ṅi')
    O_ci = O_ṅi.replace('Oci', 'O'+sepa+'ci')
    O_chi = O_ci.replace('Ochi', 'O'+sepa+'chi')
    O_ji = O_chi.replace('Oji', 'O'+sepa+'ji')
    O_jhi = O_ji.replace('Ojhi', 'O'+sepa+'jhi')
    O_ñi = O_jhi.replace('Oñi', 'O'+sepa+'ñi')
    O_ṭi = O_ñi.replace('Oṭi', 'O'+sepa+'ṭi')
    O_ṭhi = O_ṭi.replace('Oṭhi', 'O'+sepa+'ṭhi')
    O_ḍi = O_ṭhi.replace('Oḍi', 'O'+sepa+'ḍi')
    O_ḍhi = O_ḍi.replace('Oḍhi', 'O'+sepa+'ḍhi')
    O_ṇi = O_ḍhi.replace('Oṇi', 'O'+sepa+'ṇi')
    O_ti = O_ṇi.replace('Oti', 'O'+sepa+'ti')
    O_thi = O_ti.replace('Othi', 'O'+sepa+'thi')
    O_di = O_thi.replace('Odi', 'O'+sepa+'di')
    O_dhi = O_di.replace('Odhi', 'O'+sepa+'dhi')
    O_ni = O_dhi.replace('Oni', 'O'+sepa+'ni')
    O_pi = O_ni.replace('Opi', 'O'+sepa+'pi')
    O_phi = O_pi.replace('Ophi', 'O'+sepa+'phi')
    O_bi = O_phi.replace('Obi', 'O'+sepa+'bi')
    O_bhi = O_bi.replace('Obhi', 'O'+sepa+'bhi')
    O_mi = O_bhi.replace('Omi', 'O'+sepa+'mi')
    O_ri = O_mi.replace('Ori', 'O'+sepa+'ri')
    O_li = O_ri.replace('Oli', 'O'+sepa+'li')
    O_ḷi = O_li.replace('Oḷi', 'O'+sepa+'ḷi')
    O_yi = O_ḷi.replace('Oyi', 'O'+sepa+'yi')
    O_vi = O_yi.replace('Ovi', 'O'+sepa+'vi')
    O_si = O_vi.replace('Osi', 'O'+sepa+'si')
    O_hi = O_si.replace('Ohi', 'O'+sepa+'hi')

    # ī
    Ā_kī = O_hi.replace('Ākī', 'Ā'+sepa+'kī')
    Ā_khī = Ā_kī.replace('Ākhī', 'Ā'+sepa+'khī')
    Ā_gī = Ā_khī.replace('Āgī', 'Ā'+sepa+'gī')
    Ā_ghī = Ā_gī.replace('Āghī', 'Ā'+sepa+'ghī')
    Ā_ṅī = Ā_ghī.replace('Āṅī', 'Ā'+sepa+'ṅī')
    Ā_cī = Ā_ṅī.replace('Ācī', 'Ā'+sepa+'cī')
    Ā_chī = Ā_cī.replace('Āchī', 'Ā'+sepa+'chī')
    Ā_jī = Ā_chī.replace('Ājī', 'Ā'+sepa+'jī')
    Ā_jhī = Ā_jī.replace('Ājhī', 'Ā'+sepa+'jhī')
    Ā_ñī = Ā_jhī.replace('Āñī', 'Ā'+sepa+'ñī')
    Ā_ṭī = Ā_ñī.replace('Āṭī', 'Ā'+sepa+'ṭī')
    Ā_ṭhī = Ā_ṭī.replace('Āṭhī', 'Ā'+sepa+'ṭhī')
    Ā_ḍī = Ā_ṭhī.replace('Āḍī', 'Ā'+sepa+'ḍī')
    Ā_ḍhī = Ā_ḍī.replace('Āḍhī', 'Ā'+sepa+'ḍhī')
    Ā_ṇī = Ā_ḍhī.replace('Āṇī', 'Ā'+sepa+'ṇī')
    Ā_tī = Ā_ṇī.replace('Ātī', 'Ā'+sepa+'tī')
    Ā_thī = Ā_tī.replace('Āthī', 'Ā'+sepa+'thī')
    Ā_dī = Ā_thī.replace('Ādī', 'Ā'+sepa+'dī')
    Ā_dhī = Ā_dī.replace('Ādhī', 'Ā'+sepa+'dhī')
    Ā_nī = Ā_dhī.replace('Ānī', 'Ā'+sepa+'nī')
    Ā_pī = Ā_nī.replace('Āpī', 'Ā'+sepa+'pī')
    Ā_phī = Ā_pī.replace('Āphī', 'Ā'+sepa+'phī')
    Ā_bī = Ā_phī.replace('Ābī', 'Ā'+sepa+'bī')
    Ā_bhī = Ā_bī.replace('Ābhī', 'Ā'+sepa+'bhī')
    Ā_mī = Ā_bhī.replace('Āmī', 'Ā'+sepa+'mī')
    Ā_rī = Ā_mī.replace('Ārī', 'Ā'+sepa+'rī')
    Ā_lī = Ā_rī.replace('Ālī', 'Ā'+sepa+'lī')
    Ā_ḷī = Ā_lī.replace('Āḷī', 'Ā'+sepa+'ḷī')
    Ā_yī = Ā_ḷī.replace('Āyī', 'Ā'+sepa+'yī')
    Ā_vī = Ā_yī.replace('Āvī', 'Ā'+sepa+'vī')
    Ā_sī = Ā_vī.replace('Āsī', 'Ā'+sepa+'sī')
    Ā_hī = Ā_sī.replace('Āhī', 'Ā'+sepa+'hī')

    Ī_kī = Ā_hī.replace('Īkī', 'Ī'+sepa+'kī')
    Ī_khī = Ī_kī.replace('Īkhī', 'Ī'+sepa+'khī')
    Ī_gī = Ī_khī.replace('Īgī', 'Ī'+sepa+'gī')
    Ī_ghī = Ī_gī.replace('Īghī', 'Ī'+sepa+'ghī')
    Ī_ṅī = Ī_ghī.replace('Īṅī', 'Ī'+sepa+'ṅī')
    Ī_cī = Ī_ṅī.replace('Īcī', 'Ī'+sepa+'cī')
    Ī_chī = Ī_cī.replace('Īchī', 'Ī'+sepa+'chī')
    Ī_jī = Ī_chī.replace('Ījī', 'Ī'+sepa+'jī')
    Ī_jhī = Ī_jī.replace('Ījhī', 'Ī'+sepa+'jhī')
    Ī_ñī = Ī_jhī.replace('Īñī', 'Ī'+sepa+'ñī')
    Ī_ṭī = Ī_ñī.replace('Īṭī', 'Ī'+sepa+'ṭī')
    Ī_ṭhī = Ī_ṭī.replace('Īṭhī', 'Ī'+sepa+'ṭhī')
    Ī_ḍī = Ī_ṭhī.replace('Īḍī', 'Ī'+sepa+'ḍī')
    Ī_ḍhī = Ī_ḍī.replace('Īḍhī', 'Ī'+sepa+'ḍhī')
    Ī_ṇī = Ī_ḍhī.replace('Īṇī', 'Ī'+sepa+'ṇī')
    Ī_tī = Ī_ṇī.replace('Ītī', 'Ī'+sepa+'tī')
    Ī_thī = Ī_tī.replace('Īthī', 'Ī'+sepa+'thī')
    Ī_dī = Ī_thī.replace('Īdī', 'Ī'+sepa+'dī')
    Ī_dhī = Ī_dī.replace('Īdhī', 'Ī'+sepa+'dhī')
    Ī_nī = Ī_dhī.replace('Īnī', 'Ī'+sepa+'nī')
    Ī_pī = Ī_nī.replace('Īpī', 'Ī'+sepa+'pī')
    Ī_phī = Ī_pī.replace('Īphī', 'Ī'+sepa+'phī')
    Ī_bī = Ī_phī.replace('Ībī', 'Ī'+sepa+'bī')
    Ī_bhī = Ī_bī.replace('Ībhī', 'Ī'+sepa+'bhī')
    Ī_mī = Ī_bhī.replace('Īmī', 'Ī'+sepa+'mī')
    Ī_rī = Ī_mī.replace('Īrī', 'Ī'+sepa+'rī')
    Ī_lī = Ī_rī.replace('Īlī', 'Ī'+sepa+'lī')
    Ī_ḷī = Ī_lī.replace('Īḷī', 'Ī'+sepa+'ḷī')
    Ī_yī = Ī_ḷī.replace('Īyī', 'Ī'+sepa+'yī')
    Ī_vī = Ī_yī.replace('Īvī', 'Ī'+sepa+'vī')
    Ī_sī = Ī_vī.replace('Īsī', 'Ī'+sepa+'sī')
    Ī_hī = Ī_sī.replace('Īhī', 'Ī'+sepa+'hī')

    Ū_kī = Ī_hī.replace('Ūkī', 'Ū'+sepa+'kī')
    Ū_khī = Ū_kī.replace('Ūkhī', 'Ū'+sepa+'khī')
    Ū_gī = Ū_khī.replace('Ūgī', 'Ū'+sepa+'gī')
    Ū_ghī = Ū_gī.replace('Ūghī', 'Ū'+sepa+'ghī')
    Ū_ṅī = Ū_ghī.replace('Ūṅī', 'Ū'+sepa+'ṅī')
    Ū_cī = Ū_ṅī.replace('Ūcī', 'Ū'+sepa+'cī')
    Ū_chī = Ū_cī.replace('Ūchī', 'Ū'+sepa+'chī')
    Ū_jī = Ū_chī.replace('Ūjī', 'Ū'+sepa+'jī')
    Ū_jhī = Ū_jī.replace('Ūjhī', 'Ū'+sepa+'jhī')
    Ū_ñī = Ū_jhī.replace('Ūñī', 'Ū'+sepa+'ñī')
    Ū_ṭī = Ū_ñī.replace('Ūṭī', 'Ū'+sepa+'ṭī')
    Ū_ṭhī = Ū_ṭī.replace('Ūṭhī', 'Ū'+sepa+'ṭhī')
    Ū_ḍī = Ū_ṭhī.replace('Ūḍī', 'Ū'+sepa+'ḍī')
    Ū_ḍhī = Ū_ḍī.replace('Ūḍhī', 'Ū'+sepa+'ḍhī')
    Ū_ṇī = Ū_ḍhī.replace('Ūṇī', 'Ū'+sepa+'ṇī')
    Ū_tī = Ū_ṇī.replace('Ūtī', 'Ū'+sepa+'tī')
    Ū_thī = Ū_tī.replace('Ūthī', 'Ū'+sepa+'thī')
    Ū_dī = Ū_thī.replace('Ūdī', 'Ū'+sepa+'dī')
    Ū_dhī = Ū_dī.replace('Ūdhī', 'Ū'+sepa+'dhī')
    Ū_nī = Ū_dhī.replace('Ūnī', 'Ū'+sepa+'nī')
    Ū_pī = Ū_nī.replace('Ūpī', 'Ū'+sepa+'pī')
    Ū_phī = Ū_pī.replace('Ūphī', 'Ū'+sepa+'phī')
    Ū_bī = Ū_phī.replace('Ūbī', 'Ū'+sepa+'bī')
    Ū_bhī = Ū_bī.replace('Ūbhī', 'Ū'+sepa+'bhī')
    Ū_mī = Ū_bhī.replace('Ūmī', 'Ū'+sepa+'mī')
    Ū_rī = Ū_mī.replace('Ūrī', 'Ū'+sepa+'rī')
    Ū_lī = Ū_rī.replace('Ūlī', 'Ū'+sepa+'lī')
    Ū_ḷī = Ū_lī.replace('Ūḷī', 'Ū'+sepa+'ḷī')
    Ū_yī = Ū_ḷī.replace('Ūyī', 'Ū'+sepa+'yī')
    Ū_vī = Ū_yī.replace('Ūvī', 'Ū'+sepa+'vī')
    Ū_sī = Ū_vī.replace('Ūsī', 'Ū'+sepa+'sī')
    Ū_hī = Ū_sī.replace('Ūhī', 'Ū'+sepa+'hī')

    E_kī = Ū_hī.replace('Ekī', 'E'+sepa+'kī')
    E_khī = E_kī.replace('Ekhī', 'E'+sepa+'khī')
    E_gī = E_khī.replace('Egī', 'E'+sepa+'gī')
    E_ghī = E_gī.replace('Eghī', 'E'+sepa+'ghī')
    E_ṅī = E_ghī.replace('Eṅī', 'E'+sepa+'ṅī')
    E_cī = E_ṅī.replace('Ecī', 'E'+sepa+'cī')
    E_chī = E_cī.replace('Echī', 'E'+sepa+'chī')
    E_jī = E_chī.replace('Ejī', 'E'+sepa+'jī')
    E_jhī = E_jī.replace('Ejhī', 'E'+sepa+'jhī')
    E_ñī = E_jhī.replace('Eñī', 'E'+sepa+'ñī')
    E_ṭī = E_ñī.replace('Eṭī', 'E'+sepa+'ṭī')
    E_ṭhī = E_ṭī.replace('Eṭhī', 'E'+sepa+'ṭhī')
    E_ḍī = E_ṭhī.replace('Eḍī', 'E'+sepa+'ḍī')
    E_ḍhī = E_ḍī.replace('Eḍhī', 'E'+sepa+'ḍhī')
    E_ṇī = E_ḍhī.replace('Eṇī', 'E'+sepa+'ṇī')
    E_tī = E_ṇī.replace('Etī', 'E'+sepa+'tī')
    E_thī = E_tī.replace('Ethī', 'E'+sepa+'thī')
    E_dī = E_thī.replace('Edī', 'E'+sepa+'dī')
    E_dhī = E_dī.replace('Edhī', 'E'+sepa+'dhī')
    E_nī = E_dhī.replace('Enī', 'E'+sepa+'nī')
    E_pī = E_nī.replace('Epī', 'E'+sepa+'pī')
    E_phī = E_pī.replace('Ephī', 'E'+sepa+'phī')
    E_bī = E_phī.replace('Ebī', 'E'+sepa+'bī')
    E_bhī = E_bī.replace('Ebhī', 'E'+sepa+'bhī')
    E_mī = E_bhī.replace('Emī', 'E'+sepa+'mī')
    E_rī = E_mī.replace('Erī', 'E'+sepa+'rī')
    E_lī = E_rī.replace('Elī', 'E'+sepa+'lī')
    E_ḷī = E_lī.replace('Eḷī', 'E'+sepa+'ḷī')
    E_yī = E_ḷī.replace('Eyī', 'E'+sepa+'yī')
    E_vī = E_yī.replace('Evī', 'E'+sepa+'vī')
    E_sī = E_vī.replace('Esī', 'E'+sepa+'sī')
    E_hī = E_sī.replace('Ehī', 'E'+sepa+'hī')

    O_kī = E_hī.replace('Okī', 'O'+sepa+'kī')
    O_khī = O_kī.replace('Okhī', 'O'+sepa+'khī')
    O_gī = O_khī.replace('Ogī', 'O'+sepa+'gī')
    O_ghī = O_gī.replace('Oghī', 'O'+sepa+'ghī')
    O_ṅī = O_ghī.replace('Oṅī', 'O'+sepa+'ṅī')
    O_cī = O_ṅī.replace('Ocī', 'O'+sepa+'cī')
    O_chī = O_cī.replace('Ochī', 'O'+sepa+'chī')
    O_jī = O_chī.replace('Ojī', 'O'+sepa+'jī')
    O_jhī = O_jī.replace('Ojhī', 'O'+sepa+'jhī')
    O_ñī = O_jhī.replace('Oñī', 'O'+sepa+'ñī')
    O_ṭī = O_ñī.replace('Oṭī', 'O'+sepa+'ṭī')
    O_ṭhī = O_ṭī.replace('Oṭhī', 'O'+sepa+'ṭhī')
    O_ḍī = O_ṭhī.replace('Oḍī', 'O'+sepa+'ḍī')
    O_ḍhī = O_ḍī.replace('Oḍhī', 'O'+sepa+'ḍhī')
    O_ṇī = O_ḍhī.replace('Oṇī', 'O'+sepa+'ṇī')
    O_tī = O_ṇī.replace('Otī', 'O'+sepa+'tī')
    O_thī = O_tī.replace('Othī', 'O'+sepa+'thī')
    O_dī = O_thī.replace('Odī', 'O'+sepa+'dī')
    O_dhī = O_dī.replace('Odhī', 'O'+sepa+'dhī')
    O_nī = O_dhī.replace('Onī', 'O'+sepa+'nī')
    O_pī = O_nī.replace('Opī', 'O'+sepa+'pī')
    O_phī = O_pī.replace('Ophī', 'O'+sepa+'phī')
    O_bī = O_phī.replace('Obī', 'O'+sepa+'bī')
    O_bhī = O_bī.replace('Obhī', 'O'+sepa+'bhī')
    O_mī = O_bhī.replace('Omī', 'O'+sepa+'mī')
    O_rī = O_mī.replace('Orī', 'O'+sepa+'rī')
    O_lī = O_rī.replace('Olī', 'O'+sepa+'lī')
    O_ḷī = O_lī.replace('Oḷī', 'O'+sepa+'ḷī')
    O_yī = O_ḷī.replace('Oyī', 'O'+sepa+'yī')
    O_vī = O_yī.replace('Ovī', 'O'+sepa+'vī')
    O_sī = O_vī.replace('Osī', 'O'+sepa+'sī')
    O_hī = O_sī.replace('Ohī', 'O'+sepa+'hī')

    # u
    Ā_ku = O_hī.replace('Āku', 'Ā'+sepa+'ku')
    Ā_khu = Ā_ku.replace('Ākhu', 'Ā'+sepa+'khu')
    Ā_gu = Ā_khu.replace('Āgu', 'Ā'+sepa+'gu')
    Ā_ghu = Ā_gu.replace('Āghu', 'Ā'+sepa+'ghu')
    Ā_ṅu = Ā_ghu.replace('Āṅu', 'Ā'+sepa+'ṅu')
    Ā_cu = Ā_ṅu.replace('Ācu', 'Ā'+sepa+'cu')
    Ā_chu = Ā_cu.replace('Āchu', 'Ā'+sepa+'chu')
    Ā_ju = Ā_chu.replace('Āju', 'Ā'+sepa+'ju')
    Ā_jhu = Ā_ju.replace('Ājhu', 'Ā'+sepa+'jhu')
    Ā_ñu = Ā_jhu.replace('Āñu', 'Ā'+sepa+'ñu')
    Ā_ṭu = Ā_ñu.replace('Āṭu', 'Ā'+sepa+'ṭu')
    Ā_ṭhu = Ā_ṭu.replace('Āṭhu', 'Ā'+sepa+'ṭhu')
    Ā_ḍu = Ā_ṭhu.replace('Āḍu', 'Ā'+sepa+'ḍu')
    Ā_ḍhu = Ā_ḍu.replace('Āḍhu', 'Ā'+sepa+'ḍhu')
    Ā_ṇu = Ā_ḍhu.replace('Āṇu', 'Ā'+sepa+'ṇu')
    Ā_tu = Ā_ṇu.replace('Ātu', 'Ā'+sepa+'tu')
    Ā_thu = Ā_tu.replace('Āthu', 'Ā'+sepa+'thu')
    Ā_du = Ā_thu.replace('Ādu', 'Ā'+sepa+'du')
    Ā_dhu = Ā_du.replace('Ādhu', 'Ā'+sepa+'dhu')
    Ā_nu = Ā_dhu.replace('Ānu', 'Ā'+sepa+'nu')
    Ā_pu = Ā_nu.replace('Āpu', 'Ā'+sepa+'pu')
    Ā_phu = Ā_pu.replace('Āphu', 'Ā'+sepa+'phu')
    Ā_bu = Ā_phu.replace('Ābu', 'Ā'+sepa+'bu')
    Ā_bhu = Ā_bu.replace('Ābhu', 'Ā'+sepa+'bhu')
    Ā_mu = Ā_bhu.replace('Āmu', 'Ā'+sepa+'mu')
    Ā_ru = Ā_mu.replace('Āru', 'Ā'+sepa+'ru')
    Ā_lu = Ā_ru.replace('Ālu', 'Ā'+sepa+'lu')
    Ā_ḷu = Ā_lu.replace('Āḷu', 'Ā'+sepa+'ḷu')
    Ā_yu = Ā_ḷu.replace('Āyu', 'Ā'+sepa+'yu')
    Ā_vu = Ā_yu.replace('Āvu', 'Ā'+sepa+'vu')
    Ā_su = Ā_vu.replace('Āsu', 'Ā'+sepa+'su')
    Ā_hu = Ā_su.replace('Āhu', 'Ā'+sepa+'hu')

    Ī_ku = Ā_hu.replace('Īku', 'Ī'+sepa+'ku')
    Ī_khu = Ī_ku.replace('Īkhu', 'Ī'+sepa+'khu')
    Ī_gu = Ī_khu.replace('Īgu', 'Ī'+sepa+'gu')
    Ī_ghu = Ī_gu.replace('Īghu', 'Ī'+sepa+'ghu')
    Ī_ṅu = Ī_ghu.replace('Īṅu', 'Ī'+sepa+'ṅu')
    Ī_cu = Ī_ṅu.replace('Īcu', 'Ī'+sepa+'cu')
    Ī_chu = Ī_cu.replace('Īchu', 'Ī'+sepa+'chu')
    Ī_ju = Ī_chu.replace('Īju', 'Ī'+sepa+'ju')
    Ī_jhu = Ī_ju.replace('Ījhu', 'Ī'+sepa+'jhu')
    Ī_ñu = Ī_jhu.replace('Īñu', 'Ī'+sepa+'ñu')
    Ī_ṭu = Ī_ñu.replace('Īṭu', 'Ī'+sepa+'ṭu')
    Ī_ṭhu = Ī_ṭu.replace('Īṭhu', 'Ī'+sepa+'ṭhu')
    Ī_ḍu = Ī_ṭhu.replace('Īḍu', 'Ī'+sepa+'ḍu')
    Ī_ḍhu = Ī_ḍu.replace('Īḍhu', 'Ī'+sepa+'ḍhu')
    Ī_ṇu = Ī_ḍhu.replace('Īṇu', 'Ī'+sepa+'ṇu')
    Ī_tu = Ī_ṇu.replace('Ītu', 'Ī'+sepa+'tu')
    Ī_thu = Ī_tu.replace('Īthu', 'Ī'+sepa+'thu')
    Ī_du = Ī_thu.replace('Īdu', 'Ī'+sepa+'du')
    Ī_dhu = Ī_du.replace('Īdhu', 'Ī'+sepa+'dhu')
    Ī_nu = Ī_dhu.replace('Īnu', 'Ī'+sepa+'nu')
    Ī_pu = Ī_nu.replace('Īpu', 'Ī'+sepa+'pu')
    Ī_phu = Ī_pu.replace('Īphu', 'Ī'+sepa+'phu')
    Ī_bu = Ī_phu.replace('Ību', 'Ī'+sepa+'bu')
    Ī_bhu = Ī_bu.replace('Ībhu', 'Ī'+sepa+'bhu')
    Ī_mu = Ī_bhu.replace('Īmu', 'Ī'+sepa+'mu')
    Ī_ru = Ī_mu.replace('Īru', 'Ī'+sepa+'ru')
    Ī_lu = Ī_ru.replace('Īlu', 'Ī'+sepa+'lu')
    Ī_ḷu = Ī_lu.replace('Īḷu', 'Ī'+sepa+'ḷu')
    Ī_yu = Ī_ḷu.replace('Īyu', 'Ī'+sepa+'yu')
    Ī_vu = Ī_yu.replace('Īvu', 'Ī'+sepa+'vu')
    Ī_su = Ī_vu.replace('Īsu', 'Ī'+sepa+'su')
    Ī_hu = Ī_su.replace('Īhu', 'Ī'+sepa+'hu')

    Ū_ku = Ī_hu.replace('Ūku', 'Ū'+sepa+'ku')
    Ū_khu = Ū_ku.replace('Ūkhu', 'Ū'+sepa+'khu')
    Ū_gu = Ū_khu.replace('Ūgu', 'Ū'+sepa+'gu')
    Ū_ghu = Ū_gu.replace('Ūghu', 'Ū'+sepa+'ghu')
    Ū_ṅu = Ū_ghu.replace('Ūṅu', 'Ū'+sepa+'ṅu')
    Ū_cu = Ū_ṅu.replace('Ūcu', 'Ū'+sepa+'cu')
    Ū_chu = Ū_cu.replace('Ūchu', 'Ū'+sepa+'chu')
    Ū_ju = Ū_chu.replace('Ūju', 'Ū'+sepa+'ju')
    Ū_jhu = Ū_ju.replace('Ūjhu', 'Ū'+sepa+'jhu')
    Ū_ñu = Ū_jhu.replace('Ūñu', 'Ū'+sepa+'ñu')
    Ū_ṭu = Ū_ñu.replace('Ūṭu', 'Ū'+sepa+'ṭu')
    Ū_ṭhu = Ū_ṭu.replace('Ūṭhu', 'Ū'+sepa+'ṭhu')
    Ū_ḍu = Ū_ṭhu.replace('Ūḍu', 'Ū'+sepa+'ḍu')
    Ū_ḍhu = Ū_ḍu.replace('Ūḍhu', 'Ū'+sepa+'ḍhu')
    Ū_ṇu = Ū_ḍhu.replace('Ūṇu', 'Ū'+sepa+'ṇu')
    Ū_tu = Ū_ṇu.replace('Ūtu', 'Ū'+sepa+'tu')
    Ū_thu = Ū_tu.replace('Ūthu', 'Ū'+sepa+'thu')
    Ū_du = Ū_thu.replace('Ūdu', 'Ū'+sepa+'du')
    Ū_dhu = Ū_du.replace('Ūdhu', 'Ū'+sepa+'dhu')
    Ū_nu = Ū_dhu.replace('Ūnu', 'Ū'+sepa+'nu')
    Ū_pu = Ū_nu.replace('Ūpu', 'Ū'+sepa+'pu')
    Ū_phu = Ū_pu.replace('Ūphu', 'Ū'+sepa+'phu')
    Ū_bu = Ū_phu.replace('Ūbu', 'Ū'+sepa+'bu')
    Ū_bhu = Ū_bu.replace('Ūbhu', 'Ū'+sepa+'bhu')
    Ū_mu = Ū_bhu.replace('Ūmu', 'Ū'+sepa+'mu')
    Ū_ru = Ū_mu.replace('Ūru', 'Ū'+sepa+'ru')
    Ū_lu = Ū_ru.replace('Ūlu', 'Ū'+sepa+'lu')
    Ū_ḷu = Ū_lu.replace('Ūḷu', 'Ū'+sepa+'ḷu')
    Ū_yu = Ū_ḷu.replace('Ūyu', 'Ū'+sepa+'yu')
    Ū_vu = Ū_yu.replace('Ūvu', 'Ū'+sepa+'vu')
    Ū_su = Ū_vu.replace('Ūsu', 'Ū'+sepa+'su')
    Ū_hu = Ū_su.replace('Ūhu', 'Ū'+sepa+'hu')

    E_ku = Ū_hu.replace('Eku', 'E'+sepa+'ku')
    E_khu = E_ku.replace('Ekhu', 'E'+sepa+'khu')
    E_gu = E_khu.replace('Egu', 'E'+sepa+'gu')
    E_ghu = E_gu.replace('Eghu', 'E'+sepa+'ghu')
    E_ṅu = E_ghu.replace('Eṅu', 'E'+sepa+'ṅu')
    E_cu = E_ṅu.replace('Ecu', 'E'+sepa+'cu')
    E_chu = E_cu.replace('Echu', 'E'+sepa+'chu')
    E_ju = E_chu.replace('Eju', 'E'+sepa+'ju')
    E_jhu = E_ju.replace('Ejhu', 'E'+sepa+'jhu')
    E_ñu = E_jhu.replace('Eñu', 'E'+sepa+'ñu')
    E_ṭu = E_ñu.replace('Eṭu', 'E'+sepa+'ṭu')
    E_ṭhu = E_ṭu.replace('Eṭhu', 'E'+sepa+'ṭhu')
    E_ḍu = E_ṭhu.replace('Eḍu', 'E'+sepa+'ḍu')
    E_ḍhu = E_ḍu.replace('Eḍhu', 'E'+sepa+'ḍhu')
    E_ṇu = E_ḍhu.replace('Eṇu', 'E'+sepa+'ṇu')
    E_tu = E_ṇu.replace('Etu', 'E'+sepa+'tu')
    E_thu = E_tu.replace('Ethu', 'E'+sepa+'thu')
    E_du = E_thu.replace('Edu', 'E'+sepa+'du')
    E_dhu = E_du.replace('Edhu', 'E'+sepa+'dhu')
    E_nu = E_dhu.replace('Enu', 'E'+sepa+'nu')
    E_pu = E_nu.replace('Epu', 'E'+sepa+'pu')
    E_phu = E_pu.replace('Ephu', 'E'+sepa+'phu')
    E_bu = E_phu.replace('Ebu', 'E'+sepa+'bu')
    E_bhu = E_bu.replace('Ebhu', 'E'+sepa+'bhu')
    E_mu = E_bhu.replace('Emu', 'E'+sepa+'mu')
    E_ru = E_mu.replace('Eru', 'E'+sepa+'ru')
    E_lu = E_ru.replace('Elu', 'E'+sepa+'lu')
    E_ḷu = E_lu.replace('Eḷu', 'E'+sepa+'ḷu')
    E_yu = E_ḷu.replace('Eyu', 'E'+sepa+'yu')
    E_vu = E_yu.replace('Evu', 'E'+sepa+'vu')
    E_su = E_vu.replace('Esu', 'E'+sepa+'su')
    E_hu = E_su.replace('Ehu', 'E'+sepa+'hu')

    O_ku = E_hu.replace('Oku', 'O'+sepa+'ku')
    O_khu = O_ku.replace('Okhu', 'O'+sepa+'khu')
    O_gu = O_khu.replace('Ogu', 'O'+sepa+'gu')
    O_ghu = O_gu.replace('Oghu', 'O'+sepa+'ghu')
    O_ṅu = O_ghu.replace('Oṅu', 'O'+sepa+'ṅu')
    O_cu = O_ṅu.replace('Ocu', 'O'+sepa+'cu')
    O_chu = O_cu.replace('Ochu', 'O'+sepa+'chu')
    O_ju = O_chu.replace('Oju', 'O'+sepa+'ju')
    O_jhu = O_ju.replace('Ojhu', 'O'+sepa+'jhu')
    O_ñu = O_jhu.replace('Oñu', 'O'+sepa+'ñu')
    O_ṭu = O_ñu.replace('Oṭu', 'O'+sepa+'ṭu')
    O_ṭhu = O_ṭu.replace('Oṭhu', 'O'+sepa+'ṭhu')
    O_ḍu = O_ṭhu.replace('Oḍu', 'O'+sepa+'ḍu')
    O_ḍhu = O_ḍu.replace('Oḍhu', 'O'+sepa+'ḍhu')
    O_ṇu = O_ḍhu.replace('Oṇu', 'O'+sepa+'ṇu')
    O_tu = O_ṇu.replace('Otu', 'O'+sepa+'tu')
    O_thu = O_tu.replace('Othu', 'O'+sepa+'thu')
    O_du = O_thu.replace('Odu', 'O'+sepa+'du')
    O_dhu = O_du.replace('Odhu', 'O'+sepa+'dhu')
    O_nu = O_dhu.replace('Onu', 'O'+sepa+'nu')
    O_pu = O_nu.replace('Opu', 'O'+sepa+'pu')
    O_phu = O_pu.replace('Ophu', 'O'+sepa+'phu')
    O_bu = O_phu.replace('Obu', 'O'+sepa+'bu')
    O_bhu = O_bu.replace('Obhu', 'O'+sepa+'bhu')
    O_mu = O_bhu.replace('Omu', 'O'+sepa+'mu')
    O_ru = O_mu.replace('Oru', 'O'+sepa+'ru')
    O_lu = O_ru.replace('Olu', 'O'+sepa+'lu')
    O_ḷu = O_lu.replace('Oḷu', 'O'+sepa+'ḷu')
    O_yu = O_ḷu.replace('Oyu', 'O'+sepa+'yu')
    O_vu = O_yu.replace('Ovu', 'O'+sepa+'vu')
    O_su = O_vu.replace('Osu', 'O'+sepa+'su')
    O_hu = O_su.replace('Ohu', 'O'+sepa+'hu')

    # ū
    Ā_kū = O_hu.replace('Ākū', 'Ā'+sepa+'kū')
    Ā_khū = Ā_kū.replace('Ākhū', 'Ā'+sepa+'khū')
    Ā_gū = Ā_khū.replace('Āgū', 'Ā'+sepa+'gū')
    Ā_ghū = Ā_gū.replace('Āghū', 'Ā'+sepa+'ghū')
    Ā_ṅū = Ā_ghū.replace('Āṅū', 'Ā'+sepa+'ṅū')
    Ā_cū = Ā_ṅū.replace('Ācū', 'Ā'+sepa+'cū')
    Ā_chū = Ā_cū.replace('Āchū', 'Ā'+sepa+'chū')
    Ā_jū = Ā_chū.replace('Ājū', 'Ā'+sepa+'jū')
    Ā_jhū = Ā_jū.replace('Ājhū', 'Ā'+sepa+'jhū')
    Ā_ñū = Ā_jhū.replace('Āñū', 'Ā'+sepa+'ñū')
    Ā_ṭū = Ā_ñū.replace('Āṭū', 'Ā'+sepa+'ṭū')
    Ā_ṭhū = Ā_ṭū.replace('Āṭhū', 'Ā'+sepa+'ṭhū')
    Ā_ḍū = Ā_ṭhū.replace('Āḍū', 'Ā'+sepa+'ḍū')
    Ā_ḍhū = Ā_ḍū.replace('Āḍhū', 'Ā'+sepa+'ḍhū')
    Ā_ṇū = Ā_ḍhū.replace('Āṇū', 'Ā'+sepa+'ṇū')
    Ā_tū = Ā_ṇū.replace('Ātū', 'Ā'+sepa+'tū')
    Ā_thū = Ā_tū.replace('Āthū', 'Ā'+sepa+'thū')
    Ā_dū = Ā_thū.replace('Ādū', 'Ā'+sepa+'dū')
    Ā_dhū = Ā_dū.replace('Ādhū', 'Ā'+sepa+'dhū')
    Ā_nū = Ā_dhū.replace('Ānū', 'Ā'+sepa+'nū')
    Ā_pū = Ā_nū.replace('Āpū', 'Ā'+sepa+'pū')
    Ā_phū = Ā_pū.replace('Āphū', 'Ā'+sepa+'phū')
    Ā_bū = Ā_phū.replace('Ābū', 'Ā'+sepa+'bū')
    Ā_bhū = Ā_bū.replace('Ābhū', 'Ā'+sepa+'bhū')
    Ā_mū = Ā_bhū.replace('Āmū', 'Ā'+sepa+'mū')
    Ā_rū = Ā_mū.replace('Ārū', 'Ā'+sepa+'rū')
    Ā_lū = Ā_rū.replace('Ālū', 'Ā'+sepa+'lū')
    Ā_ḷū = Ā_lū.replace('Āḷū', 'Ā'+sepa+'ḷū')
    Ā_yū = Ā_ḷū.replace('Āyū', 'Ā'+sepa+'yū')
    Ā_vū = Ā_yū.replace('Āvū', 'Ā'+sepa+'vū')
    Ā_sū = Ā_vū.replace('Āsū', 'Ā'+sepa+'sū')
    Ā_hū = Ā_sū.replace('Āhū', 'Ā'+sepa+'hū')

    Ī_kū = Ā_hū.replace('Īkū', 'Ī'+sepa+'kū')
    Ī_khū = Ī_kū.replace('Īkhū', 'Ī'+sepa+'khū')
    Ī_gū = Ī_khū.replace('Īgū', 'Ī'+sepa+'gū')
    Ī_ghū = Ī_gū.replace('Īghū', 'Ī'+sepa+'ghū')
    Ī_ṅū = Ī_ghū.replace('Īṅū', 'Ī'+sepa+'ṅū')
    Ī_cū = Ī_ṅū.replace('Īcū', 'Ī'+sepa+'cū')
    Ī_chū = Ī_cū.replace('Īchū', 'Ī'+sepa+'chū')
    Ī_jū = Ī_chū.replace('Ījū', 'Ī'+sepa+'jū')
    Ī_jhū = Ī_jū.replace('Ījhū', 'Ī'+sepa+'jhū')
    Ī_ñū = Ī_jhū.replace('Īñū', 'Ī'+sepa+'ñū')
    Ī_ṭū = Ī_ñū.replace('Īṭū', 'Ī'+sepa+'ṭū')
    Ī_ṭhū = Ī_ṭū.replace('Īṭhū', 'Ī'+sepa+'ṭhū')
    Ī_ḍū = Ī_ṭhū.replace('Īḍū', 'Ī'+sepa+'ḍū')
    Ī_ḍhū = Ī_ḍū.replace('Īḍhū', 'Ī'+sepa+'ḍhū')
    Ī_ṇū = Ī_ḍhū.replace('Īṇū', 'Ī'+sepa+'ṇū')
    Ī_tū = Ī_ṇū.replace('Ītū', 'Ī'+sepa+'tū')
    Ī_thū = Ī_tū.replace('Īthū', 'Ī'+sepa+'thū')
    Ī_dū = Ī_thū.replace('Īdū', 'Ī'+sepa+'dū')
    Ī_dhū = Ī_dū.replace('Īdhū', 'Ī'+sepa+'dhū')
    Ī_nū = Ī_dhū.replace('Īnū', 'Ī'+sepa+'nū')
    Ī_pū = Ī_nū.replace('Īpū', 'Ī'+sepa+'pū')
    Ī_phū = Ī_pū.replace('Īphū', 'Ī'+sepa+'phū')
    Ī_bū = Ī_phū.replace('Ībū', 'Ī'+sepa+'bū')
    Ī_bhū = Ī_bū.replace('Ībhū', 'Ī'+sepa+'bhū')
    Ī_mū = Ī_bhū.replace('Īmū', 'Ī'+sepa+'mū')
    Ī_rū = Ī_mū.replace('Īrū', 'Ī'+sepa+'rū')
    Ī_lū = Ī_rū.replace('Īlū', 'Ī'+sepa+'lū')
    Ī_ḷū = Ī_lū.replace('Īḷū', 'Ī'+sepa+'ḷū')
    Ī_yū = Ī_ḷū.replace('Īyū', 'Ī'+sepa+'yū')
    Ī_vū = Ī_yū.replace('Īvū', 'Ī'+sepa+'vū')
    Ī_sū = Ī_vū.replace('Īsū', 'Ī'+sepa+'sū')
    Ī_hū = Ī_sū.replace('Īhū', 'Ī'+sepa+'hū')

    Ū_kū = Ī_hū.replace('Ūkū', 'Ū'+sepa+'kū')
    Ū_khū = Ū_kū.replace('Ūkhū', 'Ū'+sepa+'khū')
    Ū_gū = Ū_khū.replace('Ūgū', 'Ū'+sepa+'gū')
    Ū_ghū = Ū_gū.replace('Ūghū', 'Ū'+sepa+'ghū')
    Ū_ṅū = Ū_ghū.replace('Ūṅū', 'Ū'+sepa+'ṅū')
    Ū_cū = Ū_ṅū.replace('Ūcū', 'Ū'+sepa+'cū')
    Ū_chū = Ū_cū.replace('Ūchū', 'Ū'+sepa+'chū')
    Ū_jū = Ū_chū.replace('Ūjū', 'Ū'+sepa+'jū')
    Ū_jhū = Ū_jū.replace('Ūjhū', 'Ū'+sepa+'jhū')
    Ū_ñū = Ū_jhū.replace('Ūñū', 'Ū'+sepa+'ñū')
    Ū_ṭū = Ū_ñū.replace('Ūṭū', 'Ū'+sepa+'ṭū')
    Ū_ṭhū = Ū_ṭū.replace('Ūṭhū', 'Ū'+sepa+'ṭhū')
    Ū_ḍū = Ū_ṭhū.replace('Ūḍū', 'Ū'+sepa+'ḍū')
    Ū_ḍhū = Ū_ḍū.replace('Ūḍhū', 'Ū'+sepa+'ḍhū')
    Ū_ṇū = Ū_ḍhū.replace('Ūṇū', 'Ū'+sepa+'ṇū')
    Ū_tū = Ū_ṇū.replace('Ūtū', 'Ū'+sepa+'tū')
    Ū_thū = Ū_tū.replace('Ūthū', 'Ū'+sepa+'thū')
    Ū_dū = Ū_thū.replace('Ūdū', 'Ū'+sepa+'dū')
    Ū_dhū = Ū_dū.replace('Ūdhū', 'Ū'+sepa+'dhū')
    Ū_nū = Ū_dhū.replace('Ūnū', 'Ū'+sepa+'nū')
    Ū_pū = Ū_nū.replace('Ūpū', 'Ū'+sepa+'pū')
    Ū_phū = Ū_pū.replace('Ūphū', 'Ū'+sepa+'phū')
    Ū_bū = Ū_phū.replace('Ūbū', 'Ū'+sepa+'bū')
    Ū_bhū = Ū_bū.replace('Ūbhū', 'Ū'+sepa+'bhū')
    Ū_mū = Ū_bhū.replace('Ūmū', 'Ū'+sepa+'mū')
    Ū_rū = Ū_mū.replace('Ūrū', 'Ū'+sepa+'rū')
    Ū_lū = Ū_rū.replace('Ūlū', 'Ū'+sepa+'lū')
    Ū_ḷū = Ū_lū.replace('Ūḷū', 'Ū'+sepa+'ḷū')
    Ū_yū = Ū_ḷū.replace('Ūyū', 'Ū'+sepa+'yū')
    Ū_vū = Ū_yū.replace('Ūvū', 'Ū'+sepa+'vū')
    Ū_sū = Ū_vū.replace('Ūsū', 'Ū'+sepa+'sū')
    Ū_hū = Ū_sū.replace('Ūhū', 'Ū'+sepa+'hū')

    E_kū = Ū_hū.replace('Ekū', 'E'+sepa+'kū')
    E_khū = E_kū.replace('Ekhū', 'E'+sepa+'khū')
    E_gū = E_khū.replace('Egū', 'E'+sepa+'gū')
    E_ghū = E_gū.replace('Eghū', 'E'+sepa+'ghū')
    E_ṅū = E_ghū.replace('Eṅū', 'E'+sepa+'ṅū')
    E_cū = E_ṅū.replace('Ecū', 'E'+sepa+'cū')
    E_chū = E_cū.replace('Echū', 'E'+sepa+'chū')
    E_jū = E_chū.replace('Ejū', 'E'+sepa+'jū')
    E_jhū = E_jū.replace('Ejhū', 'E'+sepa+'jhū')
    E_ñū = E_jhū.replace('Eñū', 'E'+sepa+'ñū')
    E_ṭū = E_ñū.replace('Eṭū', 'E'+sepa+'ṭū')
    E_ṭhū = E_ṭū.replace('Eṭhū', 'E'+sepa+'ṭhū')
    E_ḍū = E_ṭhū.replace('Eḍū', 'E'+sepa+'ḍū')
    E_ḍhū = E_ḍū.replace('Eḍhū', 'E'+sepa+'ḍhū')
    E_ṇū = E_ḍhū.replace('Eṇū', 'E'+sepa+'ṇū')
    E_tū = E_ṇū.replace('Etū', 'E'+sepa+'tū')
    E_thū = E_tū.replace('Ethū', 'E'+sepa+'thū')
    E_dū = E_thū.replace('Edū', 'E'+sepa+'dū')
    E_dhū = E_dū.replace('Edhū', 'E'+sepa+'dhū')
    E_nū = E_dhū.replace('Enū', 'E'+sepa+'nū')
    E_pū = E_nū.replace('Epū', 'E'+sepa+'pū')
    E_phū = E_pū.replace('Ephū', 'E'+sepa+'phū')
    E_bū = E_phū.replace('Ebū', 'E'+sepa+'bū')
    E_bhū = E_bū.replace('Ebhū', 'E'+sepa+'bhū')
    E_mū = E_bhū.replace('Emū', 'E'+sepa+'mū')
    E_rū = E_mū.replace('Erū', 'E'+sepa+'rū')
    E_lū = E_rū.replace('Elū', 'E'+sepa+'lū')
    E_ḷū = E_lū.replace('Eḷū', 'E'+sepa+'ḷū')
    E_yū = E_ḷū.replace('Eyū', 'E'+sepa+'yū')
    E_vū = E_yū.replace('Evū', 'E'+sepa+'vū')
    E_sū = E_vū.replace('Esū', 'E'+sepa+'sū')
    E_hū = E_sū.replace('Ehū', 'E'+sepa+'hū')

    O_kū = E_hū.replace('Okū', 'O'+sepa+'kū')
    O_khū = O_kū.replace('Okhū', 'O'+sepa+'khū')
    O_gū = O_khū.replace('Ogū', 'O'+sepa+'gū')
    O_ghū = O_gū.replace('Oghū', 'O'+sepa+'ghū')
    O_ṅū = O_ghū.replace('Oṅū', 'O'+sepa+'ṅū')
    O_cū = O_ṅū.replace('Ocū', 'O'+sepa+'cū')
    O_chū = O_cū.replace('Ochū', 'O'+sepa+'chū')
    O_jū = O_chū.replace('Ojū', 'O'+sepa+'jū')
    O_jhū = O_jū.replace('Ojhū', 'O'+sepa+'jhū')
    O_ñū = O_jhū.replace('Oñū', 'O'+sepa+'ñū')
    O_ṭū = O_ñū.replace('Oṭū', 'O'+sepa+'ṭū')
    O_ṭhū = O_ṭū.replace('Oṭhū', 'O'+sepa+'ṭhū')
    O_ḍū = O_ṭhū.replace('Oḍū', 'O'+sepa+'ḍū')
    O_ḍhū = O_ḍū.replace('Oḍhū', 'O'+sepa+'ḍhū')
    O_ṇū = O_ḍhū.replace('Oṇū', 'O'+sepa+'ṇū')
    O_tū = O_ṇū.replace('Otū', 'O'+sepa+'tū')
    O_thū = O_tū.replace('Othū', 'O'+sepa+'thū')
    O_dū = O_thū.replace('Odū', 'O'+sepa+'dū')
    O_dhū = O_dū.replace('Odhū', 'O'+sepa+'dhū')
    O_nū = O_dhū.replace('Onū', 'O'+sepa+'nū')
    O_pū = O_nū.replace('Opū', 'O'+sepa+'pū')
    O_phū = O_pū.replace('Ophū', 'O'+sepa+'phū')
    O_bū = O_phū.replace('Obū', 'O'+sepa+'bū')
    O_bhū = O_bū.replace('Obhū', 'O'+sepa+'bhū')
    O_mū = O_bhū.replace('Omū', 'O'+sepa+'mū')
    O_rū = O_mū.replace('Orū', 'O'+sepa+'rū')
    O_lū = O_rū.replace('Olū', 'O'+sepa+'lū')
    O_ḷū = O_lū.replace('Oḷū', 'O'+sepa+'ḷū')
    O_yū = O_ḷū.replace('Oyū', 'O'+sepa+'yū')
    O_vū = O_yū.replace('Ovū', 'O'+sepa+'vū')
    O_sū = O_vū.replace('Osū', 'O'+sepa+'sū')
    O_hū = O_sū.replace('Ohū', 'O'+sepa+'hū')

    # e
    Ā_ke = O_hū.replace('Āke', 'Ā'+sepa+'ke')
    Ā_khe = Ā_ke.replace('Ākhe', 'Ā'+sepa+'khe')
    Ā_ge = Ā_khe.replace('Āge', 'Ā'+sepa+'ge')
    Ā_ghe = Ā_ge.replace('Āghe', 'Ā'+sepa+'ghe')
    Ā_ṅe = Ā_ghe.replace('Āṅe', 'Ā'+sepa+'ṅe')
    Ā_ce = Ā_ṅe.replace('Āce', 'Ā'+sepa+'ce')
    Ā_che = Ā_ce.replace('Āche', 'Ā'+sepa+'che')
    Ā_je = Ā_che.replace('Āje', 'Ā'+sepa+'je')
    Ā_jhe = Ā_je.replace('Ājhe', 'Ā'+sepa+'jhe')
    Ā_ñe = Ā_jhe.replace('Āñe', 'Ā'+sepa+'ñe')
    Ā_ṭe = Ā_ñe.replace('Āṭe', 'Ā'+sepa+'ṭe')
    Ā_ṭhe = Ā_ṭe.replace('Āṭhe', 'Ā'+sepa+'ṭhe')
    Ā_ḍe = Ā_ṭhe.replace('Āḍe', 'Ā'+sepa+'ḍe')
    Ā_ḍhe = Ā_ḍe.replace('Āḍhe', 'Ā'+sepa+'ḍhe')
    Ā_ṇe = Ā_ḍhe.replace('Āṇe', 'Ā'+sepa+'ṇe')
    Ā_te = Ā_ṇe.replace('Āte', 'Ā'+sepa+'te')
    Ā_the = Ā_te.replace('Āthe', 'Ā'+sepa+'the')
    Ā_de = Ā_the.replace('Āde', 'Ā'+sepa+'de')
    Ā_dhe = Ā_de.replace('Ādhe', 'Ā'+sepa+'dhe')
    Ā_ne = Ā_dhe.replace('Āne', 'Ā'+sepa+'ne')
    Ā_pe = Ā_ne.replace('Āpe', 'Ā'+sepa+'pe')
    Ā_phe = Ā_pe.replace('Āphe', 'Ā'+sepa+'phe')
    Ā_be = Ā_phe.replace('Ābe', 'Ā'+sepa+'be')
    Ā_bhe = Ā_be.replace('Ābhe', 'Ā'+sepa+'bhe')
    Ā_me = Ā_bhe.replace('Āme', 'Ā'+sepa+'me')
    Ā_re = Ā_me.replace('Āre', 'Ā'+sepa+'re')
    Ā_le = Ā_re.replace('Āle', 'Ā'+sepa+'le')
    Ā_ḷe = Ā_le.replace('Āḷe', 'Ā'+sepa+'ḷe')
    Ā_ye = Ā_ḷe.replace('Āye', 'Ā'+sepa+'ye')
    Ā_ve = Ā_ye.replace('Āve', 'Ā'+sepa+'ve')
    Ā_se = Ā_ve.replace('Āse', 'Ā'+sepa+'se')
    Ā_he = Ā_se.replace('Āhe', 'Ā'+sepa+'he')

    Ī_ke = Ā_he.replace('Īke', 'Ī'+sepa+'ke')
    Ī_khe = Ī_ke.replace('Īkhe', 'Ī'+sepa+'khe')
    Ī_ge = Ī_khe.replace('Īge', 'Ī'+sepa+'ge')
    Ī_ghe = Ī_ge.replace('Īghe', 'Ī'+sepa+'ghe')
    Ī_ṅe = Ī_ghe.replace('Īṅe', 'Ī'+sepa+'ṅe')
    Ī_ce = Ī_ṅe.replace('Īce', 'Ī'+sepa+'ce')
    Ī_che = Ī_ce.replace('Īche', 'Ī'+sepa+'che')
    Ī_je = Ī_che.replace('Īje', 'Ī'+sepa+'je')
    Ī_jhe = Ī_je.replace('Ījhe', 'Ī'+sepa+'jhe')
    Ī_ñe = Ī_jhe.replace('Īñe', 'Ī'+sepa+'ñe')
    Ī_ṭe = Ī_ñe.replace('Īṭe', 'Ī'+sepa+'ṭe')
    Ī_ṭhe = Ī_ṭe.replace('Īṭhe', 'Ī'+sepa+'ṭhe')
    Ī_ḍe = Ī_ṭhe.replace('Īḍe', 'Ī'+sepa+'ḍe')
    Ī_ḍhe = Ī_ḍe.replace('Īḍhe', 'Ī'+sepa+'ḍhe')
    Ī_ṇe = Ī_ḍhe.replace('Īṇe', 'Ī'+sepa+'ṇe')
    Ī_te = Ī_ṇe.replace('Īte', 'Ī'+sepa+'te')
    Ī_the = Ī_te.replace('Īthe', 'Ī'+sepa+'the')
    Ī_de = Ī_the.replace('Īde', 'Ī'+sepa+'de')
    Ī_dhe = Ī_de.replace('Īdhe', 'Ī'+sepa+'dhe')
    Ī_ne = Ī_dhe.replace('Īne', 'Ī'+sepa+'ne')
    Ī_pe = Ī_ne.replace('Īpe', 'Ī'+sepa+'pe')
    Ī_phe = Ī_pe.replace('Īphe', 'Ī'+sepa+'phe')
    Ī_be = Ī_phe.replace('Ībe', 'Ī'+sepa+'be')
    Ī_bhe = Ī_be.replace('Ībhe', 'Ī'+sepa+'bhe')
    Ī_me = Ī_bhe.replace('Īme', 'Ī'+sepa+'me')
    Ī_re = Ī_me.replace('Īre', 'Ī'+sepa+'re')
    Ī_le = Ī_re.replace('Īle', 'Ī'+sepa+'le')
    Ī_ḷe = Ī_le.replace('Īḷe', 'Ī'+sepa+'ḷe')
    Ī_ye = Ī_ḷe.replace('Īye', 'Ī'+sepa+'ye')
    Ī_ve = Ī_ye.replace('Īve', 'Ī'+sepa+'ve')
    Ī_se = Ī_ve.replace('Īse', 'Ī'+sepa+'se')
    Ī_he = Ī_se.replace('Īhe', 'Ī'+sepa+'he')

    Ū_ke = Ī_he.replace('Ūke', 'Ū'+sepa+'ke')
    Ū_khe = Ū_ke.replace('Ūkhe', 'Ū'+sepa+'khe')
    Ū_ge = Ū_khe.replace('Ūge', 'Ū'+sepa+'ge')
    Ū_ghe = Ū_ge.replace('Ūghe', 'Ū'+sepa+'ghe')
    Ū_ṅe = Ū_ghe.replace('Ūṅe', 'Ū'+sepa+'ṅe')
    Ū_ce = Ū_ṅe.replace('Ūce', 'Ū'+sepa+'ce')
    Ū_che = Ū_ce.replace('Ūche', 'Ū'+sepa+'che')
    Ū_je = Ū_che.replace('Ūje', 'Ū'+sepa+'je')
    Ū_jhe = Ū_je.replace('Ūjhe', 'Ū'+sepa+'jhe')
    Ū_ñe = Ū_jhe.replace('Ūñe', 'Ū'+sepa+'ñe')
    Ū_ṭe = Ū_ñe.replace('Ūṭe', 'Ū'+sepa+'ṭe')
    Ū_ṭhe = Ū_ṭe.replace('Ūṭhe', 'Ū'+sepa+'ṭhe')
    Ū_ḍe = Ū_ṭhe.replace('Ūḍe', 'Ū'+sepa+'ḍe')
    Ū_ḍhe = Ū_ḍe.replace('Ūḍhe', 'Ū'+sepa+'ḍhe')
    Ū_ṇe = Ū_ḍhe.replace('Ūṇe', 'Ū'+sepa+'ṇe')
    Ū_te = Ū_ṇe.replace('Ūte', 'Ū'+sepa+'te')
    Ū_the = Ū_te.replace('Ūthe', 'Ū'+sepa+'the')
    Ū_de = Ū_the.replace('Ūde', 'Ū'+sepa+'de')
    Ū_dhe = Ū_de.replace('Ūdhe', 'Ū'+sepa+'dhe')
    Ū_ne = Ū_dhe.replace('Ūne', 'Ū'+sepa+'ne')
    Ū_pe = Ū_ne.replace('Ūpe', 'Ū'+sepa+'pe')
    Ū_phe = Ū_pe.replace('Ūphe', 'Ū'+sepa+'phe')
    Ū_be = Ū_phe.replace('Ūbe', 'Ū'+sepa+'be')
    Ū_bhe = Ū_be.replace('Ūbhe', 'Ū'+sepa+'bhe')
    Ū_me = Ū_bhe.replace('Ūme', 'Ū'+sepa+'me')
    Ū_re = Ū_me.replace('Ūre', 'Ū'+sepa+'re')
    Ū_le = Ū_re.replace('Ūle', 'Ū'+sepa+'le')
    Ū_ḷe = Ū_le.replace('Ūḷe', 'Ū'+sepa+'ḷe')
    Ū_ye = Ū_ḷe.replace('Ūye', 'Ū'+sepa+'ye')
    Ū_ve = Ū_ye.replace('Ūve', 'Ū'+sepa+'ve')
    Ū_se = Ū_ve.replace('Ūse', 'Ū'+sepa+'se')
    Ū_he = Ū_se.replace('Ūhe', 'Ū'+sepa+'he')

    E_ke = Ū_he.replace('Eke', 'E'+sepa+'ke')
    E_khe = E_ke.replace('Ekhe', 'E'+sepa+'khe')
    E_ge = E_khe.replace('Ege', 'E'+sepa+'ge')
    E_ghe = E_ge.replace('Eghe', 'E'+sepa+'ghe')
    E_ṅe = E_ghe.replace('Eṅe', 'E'+sepa+'ṅe')
    E_ce = E_ṅe.replace('Ece', 'E'+sepa+'ce')
    E_che = E_ce.replace('Eche', 'E'+sepa+'che')
    E_je = E_che.replace('Eje', 'E'+sepa+'je')
    E_jhe = E_je.replace('Ejhe', 'E'+sepa+'jhe')
    E_ñe = E_jhe.replace('Eñe', 'E'+sepa+'ñe')
    E_ṭe = E_ñe.replace('Eṭe', 'E'+sepa+'ṭe')
    E_ṭhe = E_ṭe.replace('Eṭhe', 'E'+sepa+'ṭhe')
    E_ḍe = E_ṭhe.replace('Eḍe', 'E'+sepa+'ḍe')
    E_ḍhe = E_ḍe.replace('Eḍhe', 'E'+sepa+'ḍhe')
    E_ṇe = E_ḍhe.replace('Eṇe', 'E'+sepa+'ṇe')
    E_te = E_ṇe.replace('Ete', 'E'+sepa+'te')
    E_the = E_te.replace('Ethe', 'E'+sepa+'the')
    E_de = E_the.replace('Ede', 'E'+sepa+'de')
    E_dhe = E_de.replace('Edhe', 'E'+sepa+'dhe')
    E_ne = E_dhe.replace('Ene', 'E'+sepa+'ne')
    E_pe = E_ne.replace('Epe', 'E'+sepa+'pe')
    E_phe = E_pe.replace('Ephe', 'E'+sepa+'phe')
    E_be = E_phe.replace('Ebe', 'E'+sepa+'be')
    E_bhe = E_be.replace('Ebhe', 'E'+sepa+'bhe')
    E_me = E_bhe.replace('Eme', 'E'+sepa+'me')
    E_re = E_me.replace('Ere', 'E'+sepa+'re')
    E_le = E_re.replace('Ele', 'E'+sepa+'le')
    E_ḷe = E_le.replace('Eḷe', 'E'+sepa+'ḷe')
    E_ye = E_ḷe.replace('Eye', 'E'+sepa+'ye')
    E_ve = E_ye.replace('Eve', 'E'+sepa+'ve')
    E_se = E_ve.replace('Ese', 'E'+sepa+'se')
    E_he = E_se.replace('Ehe', 'E'+sepa+'he')

    O_ke = E_he.replace('Oke', 'O'+sepa+'ke')
    O_khe = O_ke.replace('Okhe', 'O'+sepa+'khe')
    O_ge = O_khe.replace('Oge', 'O'+sepa+'ge')
    O_ghe = O_ge.replace('Oghe', 'O'+sepa+'ghe')
    O_ṅe = O_ghe.replace('Oṅe', 'O'+sepa+'ṅe')
    O_ce = O_ṅe.replace('Oce', 'O'+sepa+'ce')
    O_che = O_ce.replace('Oche', 'O'+sepa+'che')
    O_je = O_che.replace('Oje', 'O'+sepa+'je')
    O_jhe = O_je.replace('Ojhe', 'O'+sepa+'jhe')
    O_ñe = O_jhe.replace('Oñe', 'O'+sepa+'ñe')
    O_ṭe = O_ñe.replace('Oṭe', 'O'+sepa+'ṭe')
    O_ṭhe = O_ṭe.replace('Oṭhe', 'O'+sepa+'ṭhe')
    O_ḍe = O_ṭhe.replace('Oḍe', 'O'+sepa+'ḍe')
    O_ḍhe = O_ḍe.replace('Oḍhe', 'O'+sepa+'ḍhe')
    O_ṇe = O_ḍhe.replace('Oṇe', 'O'+sepa+'ṇe')
    O_te = O_ṇe.replace('Ote', 'O'+sepa+'te')
    O_the = O_te.replace('Othe', 'O'+sepa+'the')
    O_de = O_the.replace('Ode', 'O'+sepa+'de')
    O_dhe = O_de.replace('Odhe', 'O'+sepa+'dhe')
    O_ne = O_dhe.replace('One', 'O'+sepa+'ne')
    O_pe = O_ne.replace('Ope', 'O'+sepa+'pe')
    O_phe = O_pe.replace('Ophe', 'O'+sepa+'phe')
    O_be = O_phe.replace('Obe', 'O'+sepa+'be')
    O_bhe = O_be.replace('Obhe', 'O'+sepa+'bhe')
    O_me = O_bhe.replace('Ome', 'O'+sepa+'me')
    O_re = O_me.replace('Ore', 'O'+sepa+'re')
    O_le = O_re.replace('Ole', 'O'+sepa+'le')
    O_ḷe = O_le.replace('Oḷe', 'O'+sepa+'ḷe')
    O_ye = O_ḷe.replace('Oye', 'O'+sepa+'ye')
    O_ve = O_ye.replace('Ove', 'O'+sepa+'ve')
    O_se = O_ve.replace('Ose', 'O'+sepa+'se')
    O_he = O_se.replace('Ohe', 'O'+sepa+'he')

    # o
    Ā_ko = O_he.replace('Āko', 'Ā'+sepa+'ko')
    Ā_kho = Ā_ko.replace('Ākho', 'Ā'+sepa+'kho')
    Ā_go = Ā_kho.replace('Āgo', 'Ā'+sepa+'go')
    Ā_gho = Ā_go.replace('Āgho', 'Ā'+sepa+'gho')
    Ā_ṅo = Ā_gho.replace('Āṅo', 'Ā'+sepa+'ṅo')
    Ā_co = Ā_ṅo.replace('Āco', 'Ā'+sepa+'co')
    Ā_cho = Ā_co.replace('Ācho', 'Ā'+sepa+'cho')
    Ā_jo = Ā_cho.replace('Ājo', 'Ā'+sepa+'jo')
    Ā_jho = Ā_jo.replace('Ājho', 'Ā'+sepa+'jho')
    Ā_ño = Ā_jho.replace('Āño', 'Ā'+sepa+'ño')
    Ā_ṭo = Ā_ño.replace('Āṭo', 'Ā'+sepa+'ṭo')
    Ā_ṭho = Ā_ṭo.replace('Āṭho', 'Ā'+sepa+'ṭho')
    Ā_ḍo = Ā_ṭho.replace('Āḍo', 'Ā'+sepa+'ḍo')
    Ā_ḍho = Ā_ḍo.replace('Āḍho', 'Ā'+sepa+'ḍho')
    Ā_ṇo = Ā_ḍho.replace('Āṇo', 'Ā'+sepa+'ṇo')
    Ā_to = Ā_ṇo.replace('Āto', 'Ā'+sepa+'to')
    Ā_tho = Ā_to.replace('Ātho', 'Ā'+sepa+'tho')
    Ā_do = Ā_tho.replace('Ādo', 'Ā'+sepa+'do')
    Ā_dho = Ā_do.replace('Ādho', 'Ā'+sepa+'dho')
    Ā_no = Ā_dho.replace('Āno', 'Ā'+sepa+'no')
    Ā_po = Ā_no.replace('Āpo', 'Ā'+sepa+'po')
    Ā_pho = Ā_po.replace('Āpho', 'Ā'+sepa+'pho')
    Ā_bo = Ā_pho.replace('Ābo', 'Ā'+sepa+'bo')
    Ā_bho = Ā_bo.replace('Ābho', 'Ā'+sepa+'bho')
    Ā_mo = Ā_bho.replace('Āmo', 'Ā'+sepa+'mo')
    Ā_ro = Ā_mo.replace('Āro', 'Ā'+sepa+'ro')
    Ā_lo = Ā_ro.replace('Ālo', 'Ā'+sepa+'lo')
    Ā_ḷo = Ā_lo.replace('Āḷo', 'Ā'+sepa+'ḷo')
    Ā_yo = Ā_ḷo.replace('Āyo', 'Ā'+sepa+'yo')
    Ā_vo = Ā_yo.replace('Āvo', 'Ā'+sepa+'vo')
    Ā_so = Ā_vo.replace('Āso', 'Ā'+sepa+'so')
    Ā_ho = Ā_so.replace('Āho', 'Ā'+sepa+'ho')

    Ī_ko = Ā_ho.replace('Īko', 'Ī'+sepa+'ko')
    Ī_kho = Ī_ko.replace('Īkho', 'Ī'+sepa+'kho')
    Ī_go = Ī_kho.replace('Īgo', 'Ī'+sepa+'go')
    Ī_gho = Ī_go.replace('Īgho', 'Ī'+sepa+'gho')
    Ī_ṅo = Ī_gho.replace('Īṅo', 'Ī'+sepa+'ṅo')
    Ī_co = Ī_ṅo.replace('Īco', 'Ī'+sepa+'co')
    Ī_cho = Ī_co.replace('Īcho', 'Ī'+sepa+'cho')
    Ī_jo = Ī_cho.replace('Ījo', 'Ī'+sepa+'jo')
    Ī_jho = Ī_jo.replace('Ījho', 'Ī'+sepa+'jho')
    Ī_ño = Ī_jho.replace('Īño', 'Ī'+sepa+'ño')
    Ī_ṭo = Ī_ño.replace('Īṭo', 'Ī'+sepa+'ṭo')
    Ī_ṭho = Ī_ṭo.replace('Īṭho', 'Ī'+sepa+'ṭho')
    Ī_ḍo = Ī_ṭho.replace('Īḍo', 'Ī'+sepa+'ḍo')
    Ī_ḍho = Ī_ḍo.replace('Īḍho', 'Ī'+sepa+'ḍho')
    Ī_ṇo = Ī_ḍho.replace('Īṇo', 'Ī'+sepa+'ṇo')
    Ī_to = Ī_ṇo.replace('Īto', 'Ī'+sepa+'to')
    Ī_tho = Ī_to.replace('Ītho', 'Ī'+sepa+'tho')
    Ī_do = Ī_tho.replace('Īdo', 'Ī'+sepa+'do')
    Ī_dho = Ī_do.replace('Īdho', 'Ī'+sepa+'dho')
    Ī_no = Ī_dho.replace('Īno', 'Ī'+sepa+'no')
    Ī_po = Ī_no.replace('Īpo', 'Ī'+sepa+'po')
    Ī_pho = Ī_po.replace('Īpho', 'Ī'+sepa+'pho')
    Ī_bo = Ī_pho.replace('Ībo', 'Ī'+sepa+'bo')
    Ī_bho = Ī_bo.replace('Ībho', 'Ī'+sepa+'bho')
    Ī_mo = Ī_bho.replace('Īmo', 'Ī'+sepa+'mo')
    Ī_ro = Ī_mo.replace('Īro', 'Ī'+sepa+'ro')
    Ī_lo = Ī_ro.replace('Īlo', 'Ī'+sepa+'lo')
    Ī_ḷo = Ī_lo.replace('Īḷo', 'Ī'+sepa+'ḷo')
    Ī_yo = Ī_ḷo.replace('Īyo', 'Ī'+sepa+'yo')
    Ī_vo = Ī_yo.replace('Īvo', 'Ī'+sepa+'vo')
    Ī_so = Ī_vo.replace('Īso', 'Ī'+sepa+'so')
    Ī_ho = Ī_so.replace('Īho', 'Ī'+sepa+'ho')

    Ū_ko = Ī_ho.replace('Ūko', 'Ū'+sepa+'ko')
    Ū_kho = Ū_ko.replace('Ūkho', 'Ū'+sepa+'kho')
    Ū_go = Ū_kho.replace('Ūgo', 'Ū'+sepa+'go')
    Ū_gho = Ū_go.replace('Ūgho', 'Ū'+sepa+'gho')
    Ū_ṅo = Ū_gho.replace('Ūṅo', 'Ū'+sepa+'ṅo')
    Ū_co = Ū_ṅo.replace('Ūco', 'Ū'+sepa+'co')
    Ū_cho = Ū_co.replace('Ūcho', 'Ū'+sepa+'cho')
    Ū_jo = Ū_cho.replace('Ūjo', 'Ū'+sepa+'jo')
    Ū_jho = Ū_jo.replace('Ūjho', 'Ū'+sepa+'jho')
    Ū_ño = Ū_jho.replace('Ūño', 'Ū'+sepa+'ño')
    Ū_ṭo = Ū_ño.replace('Ūṭo', 'Ū'+sepa+'ṭo')
    Ū_ṭho = Ū_ṭo.replace('Ūṭho', 'Ū'+sepa+'ṭho')
    Ū_ḍo = Ū_ṭho.replace('Ūḍo', 'Ū'+sepa+'ḍo')
    Ū_ḍho = Ū_ḍo.replace('Ūḍho', 'Ū'+sepa+'ḍho')
    Ū_ṇo = Ū_ḍho.replace('Ūṇo', 'Ū'+sepa+'ṇo')
    Ū_to = Ū_ṇo.replace('Ūto', 'Ū'+sepa+'to')
    Ū_tho = Ū_to.replace('Ūtho', 'Ū'+sepa+'tho')
    Ū_do = Ū_tho.replace('Ūdo', 'Ū'+sepa+'do')
    Ū_dho = Ū_do.replace('Ūdho', 'Ū'+sepa+'dho')
    Ū_no = Ū_dho.replace('Ūno', 'Ū'+sepa+'no')
    Ū_po = Ū_no.replace('Ūpo', 'Ū'+sepa+'po')
    Ū_pho = Ū_po.replace('Ūpho', 'Ū'+sepa+'pho')
    Ū_bo = Ū_pho.replace('Ūbo', 'Ū'+sepa+'bo')
    Ū_bho = Ū_bo.replace('Ūbho', 'Ū'+sepa+'bho')
    Ū_mo = Ū_bho.replace('Ūmo', 'Ū'+sepa+'mo')
    Ū_ro = Ū_mo.replace('Ūro', 'Ū'+sepa+'ro')
    Ū_lo = Ū_ro.replace('Ūlo', 'Ū'+sepa+'lo')
    Ū_ḷo = Ū_lo.replace('Ūḷo', 'Ū'+sepa+'ḷo')
    Ū_yo = Ū_ḷo.replace('Ūyo', 'Ū'+sepa+'yo')
    Ū_vo = Ū_yo.replace('Ūvo', 'Ū'+sepa+'vo')
    Ū_so = Ū_vo.replace('Ūso', 'Ū'+sepa+'so')
    Ū_ho = Ū_so.replace('Ūho', 'Ū'+sepa+'ho')

    E_ko = Ū_ho.replace('Eko', 'E'+sepa+'ko')
    E_kho = E_ko.replace('Ekho', 'E'+sepa+'kho')
    E_go = E_kho.replace('Ego', 'E'+sepa+'go')
    E_gho = E_go.replace('Egho', 'E'+sepa+'gho')
    E_ṅo = E_gho.replace('Eṅo', 'E'+sepa+'ṅo')
    E_co = E_ṅo.replace('Eco', 'E'+sepa+'co')
    E_cho = E_co.replace('Echo', 'E'+sepa+'cho')
    E_jo = E_cho.replace('Ejo', 'E'+sepa+'jo')
    E_jho = E_jo.replace('Ejho', 'E'+sepa+'jho')
    E_ño = E_jho.replace('Eño', 'E'+sepa+'ño')
    E_ṭo = E_ño.replace('Eṭo', 'E'+sepa+'ṭo')
    E_ṭho = E_ṭo.replace('Eṭho', 'E'+sepa+'ṭho')
    E_ḍo = E_ṭho.replace('Eḍo', 'E'+sepa+'ḍo')
    E_ḍho = E_ḍo.replace('Eḍho', 'E'+sepa+'ḍho')
    E_ṇo = E_ḍho.replace('Eṇo', 'E'+sepa+'ṇo')
    E_to = E_ṇo.replace('Eto', 'E'+sepa+'to')
    E_tho = E_to.replace('Etho', 'E'+sepa+'tho')
    E_do = E_tho.replace('Edo', 'E'+sepa+'do')
    E_dho = E_do.replace('Edho', 'E'+sepa+'dho')
    E_no = E_dho.replace('Eno', 'E'+sepa+'no')
    E_po = E_no.replace('Epo', 'E'+sepa+'po')
    E_pho = E_po.replace('Epho', 'E'+sepa+'pho')
    E_bo = E_pho.replace('Ebo', 'E'+sepa+'bo')
    E_bho = E_bo.replace('Ebho', 'E'+sepa+'bho')
    E_mo = E_bho.replace('Emo', 'E'+sepa+'mo')
    E_ro = E_mo.replace('Ero', 'E'+sepa+'ro')
    E_lo = E_ro.replace('Elo', 'E'+sepa+'lo')
    E_ḷo = E_lo.replace('Eḷo', 'E'+sepa+'ḷo')
    E_yo = E_ḷo.replace('Eyo', 'E'+sepa+'yo')
    E_vo = E_yo.replace('Evo', 'E'+sepa+'vo')
    E_so = E_vo.replace('Eso', 'E'+sepa+'so')
    E_ho = E_so.replace('Eho', 'E'+sepa+'ho')

    O_ko = E_ho.replace('Oko', 'O'+sepa+'ko')
    O_kho = O_ko.replace('Okho', 'O'+sepa+'kho')
    O_go = O_kho.replace('Ogo', 'O'+sepa+'go')
    O_gho = O_go.replace('Ogho', 'O'+sepa+'gho')
    O_ṅo = O_gho.replace('Oṅo', 'O'+sepa+'ṅo')
    O_co = O_ṅo.replace('Oco', 'O'+sepa+'co')
    O_cho = O_co.replace('Ocho', 'O'+sepa+'cho')
    O_jo = O_cho.replace('Ojo', 'O'+sepa+'jo')
    O_jho = O_jo.replace('Ojho', 'O'+sepa+'jho')
    O_ño = O_jho.replace('Oño', 'O'+sepa+'ño')
    O_ṭo = O_ño.replace('Oṭo', 'O'+sepa+'ṭo')
    O_ṭho = O_ṭo.replace('Oṭho', 'O'+sepa+'ṭho')
    O_ḍo = O_ṭho.replace('Oḍo', 'O'+sepa+'ḍo')
    O_ḍho = O_ḍo.replace('Oḍho', 'O'+sepa+'ḍho')
    O_ṇo = O_ḍho.replace('Oṇo', 'O'+sepa+'ṇo')
    O_to = O_ṇo.replace('Oto', 'O'+sepa+'to')
    O_tho = O_to.replace('Otho', 'O'+sepa+'tho')
    O_do = O_tho.replace('Odo', 'O'+sepa+'do')
    O_dho = O_do.replace('Odho', 'O'+sepa+'dho')
    O_no = O_dho.replace('Ono', 'O'+sepa+'no')
    O_po = O_no.replace('Opo', 'O'+sepa+'po')
    O_pho = O_po.replace('Opho', 'O'+sepa+'pho')
    O_bo = O_pho.replace('Obo', 'O'+sepa+'bo')
    O_bho = O_bo.replace('Obho', 'O'+sepa+'bho')
    O_mo = O_bho.replace('Omo', 'O'+sepa+'mo')
    O_ro = O_mo.replace('Oro', 'O'+sepa+'ro')
    O_lo = O_ro.replace('Olo', 'O'+sepa+'lo')
    O_ḷo = O_lo.replace('Oḷo', 'O'+sepa+'ḷo')
    O_yo = O_ḷo.replace('Oyo', 'O'+sepa+'yo')
    O_vo = O_yo.replace('Ovo', 'O'+sepa+'vo')
    O_so = O_vo.replace('Oso', 'O'+sepa+'so')
    O_ho = O_so.replace('Oho', 'O'+sepa+'ho')

    # UPPERCASE
    added_V_Ā_sepa = O_ho.replace('Ā', 'Ā'+sepa)
    added_V_Ī_sepa = added_V_Ā_sepa.replace('Ī', 'Ī'+sepa)
    added_V_Ū_sepa = added_V_Ī_sepa.replace('Ū', 'Ū'+sepa)
    added_V_E_sepa = added_V_Ū_sepa.replace('E', 'E'+sepa)
    added_V_O_sepa = added_V_E_sepa.replace('O', 'O'+sepa)

    # Insert juncture sign after the letter m followed by a space:
    # lowercase
    if uppercase_check:
        V_o_or_V_O = added_V_O_sepa
    else:
        V_o_or_V_O = O_ho
    m_sepa = V_o_or_V_O.replace("m"+" ","m"+" "+sepa)
    # UPPERCASE
    M_sepa = m_sepa.replace("M"+" ","M"+" "+sepa)

    if uppercase_check:
        ṁ_sepa_or_Ṁ_sepa = M_sepa
    else:
        ṁ_sepa_or_Ṁ_sepa = m_sepa

    # Insert juncture sign inbetween 1st, 3rd and 5th  vaggas (unaspirated and nasals, aspirated combinations are unnecessary) double consonants
    # lowercase
    # kk, gg, ṅṅ, ṅk, ṅg,
    # cc, jj, ññ, ñc, ñj
    # ṭṭ, ḍḍ, ṇṇ, ṇṭ, ṇḍ
    # tt, dd, nn, nt, nd
    # pp, bb, mm, mp, mb

    k_sepa_k = ṁ_sepa_or_Ṁ_sepa.replace("kk","k"+sepa+"k")
    g_sepa_g = k_sepa_k.replace("gg","g"+sepa+"g")
    ṅ_sepa_ṅ = g_sepa_g.replace("ṅṅ","ṅ"+sepa+"ṅ")
    ṅ_sepa_k = ṅ_sepa_ṅ.replace("ṅk","ṅ"+sepa+"k")
    ṅ_sepa_g = ṅ_sepa_k.replace("ṅg","ṅ"+sepa+"g")

    c_sepa_c = ṅ_sepa_g.replace("cc","c"+sepa+"c")
    j_sepa_j = c_sepa_c.replace("jj","j"+sepa+"j")
    ñ_sepa_ñ = j_sepa_j.replace("ññ","ñ"+sepa+"ñ")
    ñ_sepa_c = ñ_sepa_ñ.replace("ñc","ñ"+sepa+"c")
    ñ_sepa_j = ñ_sepa_c.replace("ñj","ñ"+sepa+"j")

    ṭ_sepa_ṭ = ñ_sepa_j.replace("ṭṭ","ṭ"+sepa+"ṭ")
    ḍ_sepa_ḍ = ṭ_sepa_ṭ.replace("ḍḍ","ḍ"+sepa+"ḍ")
    ṇ_sepa_ṇ = ḍ_sepa_ḍ.replace("ṇṇ","ṇ"+sepa+"ṇ")
    ṇ_sepa_ṭ = ṇ_sepa_ṇ.replace("ṇṭ","ṇ"+sepa+"ṭ")
    ṇ_sepa_ḍ = ṇ_sepa_ṭ.replace("ṇḍ","ṇ"+sepa+"ḍ")

    t_sepa_t = ṇ_sepa_ḍ.replace("tt","t"+sepa+"t")
    d_sepa_d = t_sepa_t.replace("dd","d"+sepa+"d")
    n_sepa_n = d_sepa_d.replace("nn","n"+sepa+"n")
    n_sepa_t = n_sepa_n.replace("nt","n"+sepa+"t")
    n_sepa_d = n_sepa_t.replace("nd","n"+sepa+"d")

    p_sepa_p = n_sepa_d.replace("pp","p"+sepa+"p")
    b_sepa_b = p_sepa_p.replace("bb","b"+sepa+"b")
    m_sepa_m = b_sepa_b.replace("mm","m"+sepa+"m")
    m_sepa_p = m_sepa_m.replace("mp","m"+sepa+"p")
    m_sepa_b = m_sepa_p.replace("mb","m"+sepa+"b")
    # UPPERCASE

    K_sepa_K = m_sepa_b.replace("KK","K"+sepa+"K")
    G_sepa_G = K_sepa_K.replace("GG","G"+sepa+"G")
    Ṅ_sepa_Ṅ = G_sepa_G.replace("ṄṄ","Ṅ"+sepa+"Ṅ")
    Ṅ_sepa_K = Ṅ_sepa_Ṅ.replace("ṄK","Ṅ"+sepa+"K")
    Ṅ_sepa_G = Ṅ_sepa_K.replace("ṄG","Ṅ"+sepa+"G")

    C_sepa_C = Ṅ_sepa_G.replace("CC","C"+sepa+"C")
    J_sepa_J = C_sepa_C.replace("JJ","J"+sepa+"J")
    Ñ_sepa_Ñ = J_sepa_J.replace("ÑÑ","Ñ"+sepa+"Ñ")
    Ñ_sepa_C = Ñ_sepa_Ñ.replace("ÑC","Ñ"+sepa+"C")
    Ñ_sepa_J = Ñ_sepa_C.replace("ÑJ","Ñ"+sepa+"J")

    Ṭ_sepa_Ṭ = Ñ_sepa_J.replace("ṬṬ","Ṭ"+sepa+"Ṭ")
    Ḍ_sepa_Ḍ = Ṭ_sepa_Ṭ.replace("ḌḌ","Ḍ"+sepa+"Ḍ")
    Ṇ_sepa_Ṇ = Ḍ_sepa_Ḍ.replace("ṆṆ","Ṇ"+sepa+"Ṇ")
    Ṇ_sepa_Ṭ = Ṇ_sepa_Ṇ.replace("ṆṬ","Ṇ"+sepa+"Ṭ")
    Ṇ_sepa_Ḍ = Ṇ_sepa_Ṭ.replace("ṆḌ","Ṇ"+sepa+"Ḍ")

    T_sepa_T = Ṇ_sepa_Ḍ.replace("TT","T"+sepa+"T")
    D_sepa_D = T_sepa_T.replace("DD","D"+sepa+"D")
    N_sepa_N = D_sepa_D.replace("NN","N"+sepa+"N")
    N_sepa_T = N_sepa_N.replace("NT","N"+sepa+"T")
    N_sepa_D = N_sepa_T.replace("ND","N"+sepa+"D")

    P_sepa_P = N_sepa_D.replace("PP","P"+sepa+"P")
    B_sepa_B = P_sepa_P.replace("BB","B"+sepa+"B")
    M_sepa_M = B_sepa_B.replace("MM","M"+sepa+"M")
    M_sepa_P = M_sepa_M.replace("MP","M"+sepa+"P")
    M_sepa_B = M_sepa_P.replace("MB","M"+sepa+"B")

    # Insert juncture sign after the letter ṃ:
    # lowercase
    if uppercase_check:
        m_sepa_b_or_M_sepa_B = M_sepa_B
    else:
        m_sepa_b_or_M_sepa_B = m_sepa_b
    ṃ_sepa = m_sepa_b_or_M_sepa_B.replace("ṃ","ṃ"+sepa)
    # UPPERCASE
    Ṃ_sepa = ṃ_sepa.replace("Ṃ","Ṃ"+sepa)

    # Insert juncture sign after the letter ṁ:
    # lowercase
    if uppercase_check:
        ṃ_sepa_or_Ṃ_sepa = Ṃ_sepa
    else:
        ṃ_sepa_or_Ṃ_sepa = ṃ_sepa
    ṁ_sepa = ṃ_sepa_or_Ṃ_sepa.replace("ṁ","ṁ"+sepa)
    # UPPERCASE
    Ṁ_sepa = ṁ_sepa.replace("Ṁ","Ṁ"+sepa)

    # Insert juncture sign after the letter h and s if they preceed the letter m:
    # lowercase
    if uppercase_check:
        ṁ_sepa_or_Ṁ_sepa = Ṁ_sepa
    else:
        ṁ_sepa_or_Ṁ_sepa = ṁ_sepa
    h_sepa_m = ṁ_sepa_or_Ṁ_sepa.replace("hm","h"+sepa+"m")
    s_sepa_m = h_sepa_m.replace("sm","s"+sepa+"m")
    # UPPERCASE
    H_sepa_M = s_sepa_m.replace("HM","H"+sepa+"M")
    S_sepa_M = H_sepa_M.replace("SM","S"+sepa+"M")
    
    # Insert juncture sign after the letters ñ, ṇ, n, m, y, ḷ, l, and v if they preceed the letter h:
    # lowercase
    if uppercase_check:
        s_sepa_m_or_S_sepa_M = S_sepa_M
    else:
        s_sepa_m_or_S_sepa_M = s_sepa_m
    ñ_sepa_h = s_sepa_m_or_S_sepa_M.replace("ñh","ñ"+sepa+"h")
    ṇ_sepa_h = ñ_sepa_h.replace("ṇh","ṇ"+sepa+"h")
    n_sepa_h = ṇ_sepa_h.replace("nh","n"+sepa+"h")
    m_sepa_h = n_sepa_h.replace("mh","m"+sepa+"h")
    y_sepa_h = m_sepa_h.replace("yh","y"+sepa+"h")
    ḷ_sepa_h = y_sepa_h.replace("ḷh","ḷ"+sepa+"h")
    l_sepa_h = ḷ_sepa_h.replace("lh","l"+sepa+"h")
    v_sepa_h = l_sepa_h.replace("vh","v"+sepa+"h")
    # UPPERCASE
    Ñ_sepa_H = v_sepa_h.replace("ÑH","Ñ"+sepa+"H")
    Ṇ_sepa_H = Ñ_sepa_H.replace("ṆH","Ṇ"+sepa+"H")
    N_sepa_H = Ṇ_sepa_H.replace("NH","N"+sepa+"H")
    M_sepa_H = N_sepa_H.replace("MH","M"+sepa+"H")
    Y_sepa_H = M_sepa_H.replace("YH","Y"+sepa+"H")
    Ḷ_sepa_H = Y_sepa_H.replace("ḶH","Ḷ"+sepa+"H")
    L_sepa_H = Ḷ_sepa_H.replace("LH","L"+sepa+"H")
    V_sepa_H = L_sepa_H.replace("VH","V"+sepa+"H")
    
    # Insert juncture sign after the letters k, m, y, l, and v if they preceed the letter y:
    # lowercase
    if uppercase_check:
        v_sepa_h_or_V_sepa_H = V_sepa_H
    else:
        v_sepa_h_or_V_sepa_H = v_sepa_h
    k_sepa_y = v_sepa_h_or_V_sepa_H.replace("ky","k"+sepa+"y")
    m_sepa_y = k_sepa_y.replace("my","m"+sepa+"y")
    y_sepa_y = m_sepa_y.replace("yy","y"+sepa+"y")
    l_sepa_y = y_sepa_y.replace("ly","l"+sepa+"y")
    v_sepa_y = l_sepa_y.replace("vy","v"+sepa+"y")
    # UPPERCASE
    K_sepa_Y = v_sepa_y.replace("KY","K"+sepa+"Y")
    M_sepa_Y = K_sepa_Y.replace("MY","M"+sepa+"Y")
    Y_sepa_Y = M_sepa_Y.replace("YY","Y"+sepa+"Y")
    L_sepa_Y = Y_sepa_Y.replace("LY","L"+sepa+"Y")
    V_sepa_Y = L_sepa_Y.replace("VY","V"+sepa+"Y")
        
    # Insert juncture sign after the letter l if they preceed the letter l:
    # lowercase
    if uppercase_check:
        v_sepa_y_or_V_sepa_Y = V_sepa_Y
    else:
        v_sepa_y_or_V_sepa_Y = v_sepa_y
    l_sepa_l = v_sepa_y_or_V_sepa_Y.replace("ll","l"+sepa+"l")
    # UPPERCASE
    L_sepa_L = l_sepa_l.replace("LL","L"+sepa+"L")
        
    # Insert juncture sign after the letters m and s if they preceed the letter s:
    # lowercase
    if uppercase_check:
        l_sepa_l_or_L_sepa_L = L_sepa_L
    else:
        l_sepa_l_or_L_sepa_L = l_sepa_l
    m_sepa_s = l_sepa_l_or_L_sepa_L.replace("ms","m"+sepa+"s")
    s_sepa_s = m_sepa_s.replace("ss","s"+sepa+"s")
    # UPPERCASE
    M_sepa_S = s_sepa_s.replace("MS","M"+sepa+"S")
    S_sepa_S = M_sepa_S.replace("SS","S"+sepa+"S")
        
    # Insert juncture sign after the letters t, d, y and s if they preceed the letter v:
    # lowercase
    if uppercase_check:
        s_sepa_s_or_S_sepa_S = S_sepa_S
    else:
        s_sepa_s_or_S_sepa_S = s_sepa_s
    t_sepa_v = s_sepa_s_or_S_sepa_S.replace("tv","t"+sepa+"v")
    d_sepa_v = t_sepa_v.replace("dv","d"+sepa+"v")
    y_sepa_v = d_sepa_v.replace("vv","y"+sepa+"v")
    s_sepa_v = y_sepa_v.replace("sv","s"+sepa+"v")
    # UPPERCASE
    T_sepa_V = s_sepa_v.replace("TV","T"+sepa+"V")
    D_sepa_V = T_sepa_V.replace("DV","D"+sepa+"V")
    Y_sepa_V = D_sepa_V.replace("VV","Y"+sepa+"V")
    S_sepa_V = Y_sepa_V.replace("SV","S"+sepa+"V")
        
    # Remove juncture sign; long vowels (ā, ī, ū, e, o) followed by 1st, 3rd and 5th vaggas (unaspirated and nasals, aspirated combinations are unnecessary) double consonants    
    # lowercase
    if uppercase_check:
        s_sepa_v_or_S_sepa_V = S_sepa_V
    else:
        s_sepa_v_or_S_sepa_V = s_sepa_v
    āk_sepa = s_sepa_v_or_S_sepa_V.replace("ā"+sepa+"k"+sepa, "ā"+"k"+sepa)
    āg_sepa = āk_sepa.replace("ā"+sepa+"g"+sepa, "ā"+"g"+sepa)
    āṅ_sepa = āg_sepa.replace("ā"+sepa+"ṅ"+sepa, "ā"+"ṅ"+sepa)
    āc_sepa = āṅ_sepa.replace("ā"+sepa+"c"+sepa, "ā"+"c"+sepa)
    āj_sepa = āc_sepa.replace("ā"+sepa+"j"+sepa, "ā"+"j"+sepa)
    āñ_sepa = āj_sepa.replace("ā"+sepa+"ñ"+sepa, "ā"+"ñ"+sepa)
    āṭ_sepa = āñ_sepa.replace("ā"+sepa+"ṭ"+sepa, "ā"+"ṭ"+sepa)
    āḍ_sepa = āṭ_sepa.replace("ā"+sepa+"ḍ"+sepa, "ā"+"ḍ"+sepa)
    āṇ_sepa = āḍ_sepa.replace("ā"+sepa+"ṇ"+sepa, "ā"+"ṅ"+sepa)
    āt_sepa = āṇ_sepa.replace("ā"+sepa+"t"+sepa, "ā"+"t"+sepa)
    ād_sepa = āt_sepa.replace("ā"+sepa+"d"+sepa, "ā"+"d"+sepa)
    ān_sepa = ād_sepa.replace("ā"+sepa+"n"+sepa, "ā"+"n"+sepa)
    āp_sepa = ān_sepa.replace("ā"+sepa+"p"+sepa, "ā"+"p"+sepa)
    āb_sepa = āp_sepa.replace("ā"+sepa+"b"+sepa, "ā"+"b"+sepa)
    ām_sepa = āb_sepa.replace("ā"+sepa+"m"+sepa, "ā"+"m"+sepa)
        
    īk_sepa = ām_sepa.replace("ī"+sepa+"k"+sepa, "ī"+"k"+sepa)
    īg_sepa = īk_sepa.replace("ī"+sepa+"g"+sepa, "ī"+"g"+sepa)
    īṅ_sepa = īg_sepa.replace("ī"+sepa+"ṅ"+sepa, "ī"+"ṅ"+sepa)
    īc_sepa = īṅ_sepa.replace("ī"+sepa+"c"+sepa, "ī"+"c"+sepa)
    īj_sepa = īc_sepa.replace("ī"+sepa+"j"+sepa, "ī"+"j"+sepa)
    īñ_sepa = īj_sepa.replace("ī"+sepa+"ñ"+sepa, "ī"+"ñ"+sepa)
    īṭ_sepa = īñ_sepa.replace("ī"+sepa+"ṭ"+sepa, "ī"+"ṭ"+sepa)
    īḍ_sepa = īṭ_sepa.replace("ī"+sepa+"ḍ"+sepa, "ī"+"ḍ"+sepa)
    īṇ_sepa = īḍ_sepa.replace("ī"+sepa+"ṇ"+sepa, "ī"+"ṅ"+sepa)
    īt_sepa = īṇ_sepa.replace("ī"+sepa+"t"+sepa, "ī"+"t"+sepa)
    īd_sepa = īt_sepa.replace("ī"+sepa+"d"+sepa, "ī"+"d"+sepa)
    īn_sepa = īd_sepa.replace("ī"+sepa+"n"+sepa, "ī"+"n"+sepa)
    īp_sepa = īn_sepa.replace("ī"+sepa+"p"+sepa, "ī"+"p"+sepa)
    īb_sepa = īp_sepa.replace("ī"+sepa+"b"+sepa, "ī"+"b"+sepa)
    īm_sepa = īb_sepa.replace("ī"+sepa+"m"+sepa, "ī"+"m"+sepa)

    ūk_sepa = īm_sepa.replace("ū"+sepa+"k"+sepa, "ū"+"k"+sepa)
    ūg_sepa = ūk_sepa.replace("ū"+sepa+"g"+sepa, "ū"+"g"+sepa)
    ūṅ_sepa = ūg_sepa.replace("ū"+sepa+"ṅ"+sepa, "ū"+"ṅ"+sepa)
    ūc_sepa = ūṅ_sepa.replace("ū"+sepa+"c"+sepa, "ū"+"c"+sepa)
    ūj_sepa = ūc_sepa.replace("ū"+sepa+"j"+sepa, "ū"+"j"+sepa)
    ūñ_sepa = ūj_sepa.replace("ū"+sepa+"ñ"+sepa, "ū"+"ñ"+sepa)
    ūṭ_sepa = ūñ_sepa.replace("ū"+sepa+"ṭ"+sepa, "ū"+"ṭ"+sepa)
    ūḍ_sepa = ūṭ_sepa.replace("ū"+sepa+"ḍ"+sepa, "ū"+"ḍ"+sepa)
    ūṇ_sepa = ūḍ_sepa.replace("ū"+sepa+"ṇ"+sepa, "ū"+"ṅ"+sepa)
    ūt_sepa = ūṇ_sepa.replace("ū"+sepa+"t"+sepa, "ū"+"t"+sepa)
    ūd_sepa = ūt_sepa.replace("ū"+sepa+"d"+sepa, "ū"+"d"+sepa)
    ūn_sepa = ūd_sepa.replace("ū"+sepa+"n"+sepa, "ū"+"n"+sepa)
    ūp_sepa = ūn_sepa.replace("ū"+sepa+"p"+sepa, "ū"+"p"+sepa)
    ūb_sepa = ūp_sepa.replace("ū"+sepa+"b"+sepa, "ū"+"b"+sepa)
    ūm_sepa = ūb_sepa.replace("ū"+sepa+"m"+sepa, "ū"+"m"+sepa)

    ek_sepa = ūm_sepa.replace("e"+sepa+"k"+sepa, "e"+"k"+sepa)
    eg_sepa = ek_sepa.replace("e"+sepa+"g"+sepa, "e"+"g"+sepa)
    eṅ_sepa = eg_sepa.replace("e"+sepa+"ṅ"+sepa, "e"+"ṅ"+sepa)
    ec_sepa = eṅ_sepa.replace("e"+sepa+"c"+sepa, "e"+"c"+sepa)
    ej_sepa = ec_sepa.replace("e"+sepa+"j"+sepa, "e"+"j"+sepa)
    eñ_sepa = ej_sepa.replace("e"+sepa+"ñ"+sepa, "e"+"ñ"+sepa)
    eṭ_sepa = eñ_sepa.replace("e"+sepa+"ṭ"+sepa, "e"+"ṭ"+sepa)
    eḍ_sepa = eṭ_sepa.replace("e"+sepa+"ḍ"+sepa, "e"+"ḍ"+sepa)
    eṇ_sepa = eḍ_sepa.replace("e"+sepa+"ṇ"+sepa, "e"+"ṅ"+sepa)
    et_sepa = eṇ_sepa.replace("e"+sepa+"t"+sepa, "e"+"t"+sepa)
    ed_sepa = et_sepa.replace("e"+sepa+"d"+sepa, "e"+"d"+sepa)
    en_sepa = ed_sepa.replace("e"+sepa+"n"+sepa, "e"+"n"+sepa)
    ep_sepa = en_sepa.replace("e"+sepa+"p"+sepa, "e"+"p"+sepa)
    eb_sepa = ep_sepa.replace("e"+sepa+"b"+sepa, "e"+"b"+sepa)
    em_sepa = eb_sepa.replace("e"+sepa+"m"+sepa, "e"+"m"+sepa)

    ok_sepa = em_sepa.replace("o"+sepa+"k"+sepa, "o"+"k"+sepa)
    og_sepa = ok_sepa.replace("o"+sepa+"g"+sepa, "o"+"g"+sepa)
    oṅ_sepa = og_sepa.replace("o"+sepa+"ṅ"+sepa, "o"+"ṅ"+sepa)
    oc_sepa = oṅ_sepa.replace("o"+sepa+"c"+sepa, "o"+"c"+sepa)
    oj_sepa = oc_sepa.replace("o"+sepa+"j"+sepa, "o"+"j"+sepa)
    oñ_sepa = oj_sepa.replace("o"+sepa+"ñ"+sepa, "o"+"ñ"+sepa)
    oṭ_sepa = oñ_sepa.replace("o"+sepa+"ṭ"+sepa, "o"+"ṭ"+sepa)
    oḍ_sepa = oṭ_sepa.replace("o"+sepa+"ḍ"+sepa, "o"+"ḍ"+sepa)
    oṇ_sepa = oḍ_sepa.replace("o"+sepa+"ṇ"+sepa, "o"+"ṅ"+sepa)
    ot_sepa = oṇ_sepa.replace("o"+sepa+"t"+sepa, "o"+"t"+sepa)
    od_sepa = ot_sepa.replace("o"+sepa+"d"+sepa, "o"+"d"+sepa)
    on_sepa = od_sepa.replace("o"+sepa+"n"+sepa, "o"+"n"+sepa)
    op_sepa = on_sepa.replace("o"+sepa+"p"+sepa, "o"+"p"+sepa)
    ob_sepa = op_sepa.replace("o"+sepa+"b"+sepa, "o"+"b"+sepa)
    om_sepa = ob_sepa.replace("o"+sepa+"m"+sepa, "o"+"m"+sepa)
    #UPPERCASE
    ĀK_sepa = om_sepa.replace("Ā"+sepa+"K"+sepa, "Ā"+"K"+sepa)
    ĀG_sepa = ĀK_sepa.replace("Ā"+sepa+"G"+sepa, "Ā"+"G"+sepa)
    ĀṄ_sepa = ĀG_sepa.replace("Ā"+sepa+"Ṅ"+sepa, "Ā"+"Ṅ"+sepa)
    ĀC_sepa = ĀṄ_sepa.replace("Ā"+sepa+"C"+sepa, "Ā"+"C"+sepa)
    ĀJ_sepa = ĀC_sepa.replace("Ā"+sepa+"J"+sepa, "Ā"+"J"+sepa)
    ĀÑ_sepa = ĀJ_sepa.replace("Ā"+sepa+"Ñ"+sepa, "Ā"+"Ñ"+sepa)
    ĀṬ_sepa = ĀÑ_sepa.replace("Ā"+sepa+"Ṭ"+sepa, "Ā"+"Ṭ"+sepa)
    ĀḌ_sepa = ĀṬ_sepa.replace("Ā"+sepa+"Ḍ"+sepa, "Ā"+"Ḍ"+sepa)
    ĀṆ_sepa = ĀḌ_sepa.replace("Ā"+sepa+"Ṇ"+sepa, "Ā"+"Ṅ"+sepa)
    ĀT_sepa = ĀṆ_sepa.replace("Ā"+sepa+"T"+sepa, "Ā"+"T"+sepa)
    ĀD_sepa = ĀT_sepa.replace("Ā"+sepa+"D"+sepa, "Ā"+"D"+sepa)
    ĀN_sepa = ĀD_sepa.replace("Ā"+sepa+"N"+sepa, "Ā"+"N"+sepa)
    ĀP_sepa = ĀN_sepa.replace("Ā"+sepa+"P"+sepa, "Ā"+"P"+sepa)
    ĀB_sepa = ĀP_sepa.replace("Ā"+sepa+"B"+sepa, "Ā"+"B"+sepa)
    ĀM_sepa = ĀB_sepa.replace("Ā"+sepa+"M"+sepa, "Ā"+"M"+sepa)

    ĪK_sepa = ĀM_sepa.replace("Ī"+sepa+"K"+sepa, "Ī"+"K"+sepa)
    ĪG_sepa = ĪK_sepa.replace("Ī"+sepa+"G"+sepa, "Ī"+"G"+sepa)
    ĪṄ_sepa = ĪG_sepa.replace("Ī"+sepa+"Ṅ"+sepa, "Ī"+"Ṅ"+sepa)
    ĪC_sepa = ĪṄ_sepa.replace("Ī"+sepa+"C"+sepa, "Ī"+"C"+sepa)
    ĪJ_sepa = ĪC_sepa.replace("Ī"+sepa+"J"+sepa, "Ī"+"J"+sepa)
    ĪÑ_sepa = ĪJ_sepa.replace("Ī"+sepa+"Ñ"+sepa, "Ī"+"Ñ"+sepa)
    ĪṬ_sepa = ĪÑ_sepa.replace("Ī"+sepa+"Ṭ"+sepa, "Ī"+"Ṭ"+sepa)
    ĪḌ_sepa = ĪṬ_sepa.replace("Ī"+sepa+"Ḍ"+sepa, "Ī"+"Ḍ"+sepa)
    ĪṆ_sepa = ĪḌ_sepa.replace("Ī"+sepa+"Ṇ"+sepa, "Ī"+"Ṅ"+sepa)
    ĪT_sepa = ĪṆ_sepa.replace("Ī"+sepa+"T"+sepa, "Ī"+"T"+sepa)
    ĪD_sepa = ĪT_sepa.replace("Ī"+sepa+"D"+sepa, "Ī"+"D"+sepa)
    ĪN_sepa = ĪD_sepa.replace("Ī"+sepa+"N"+sepa, "Ī"+"N"+sepa)
    ĪP_sepa = ĪN_sepa.replace("Ī"+sepa+"P"+sepa, "Ī"+"P"+sepa)
    ĪB_sepa = ĪP_sepa.replace("Ī"+sepa+"B"+sepa, "Ī"+"B"+sepa)
    ĪM_sepa = ĪB_sepa.replace("Ī"+sepa+"M"+sepa, "Ī"+"M"+sepa)

    ŪK_sepa = ĪM_sepa.replace("Ū"+sepa+"K"+sepa, "Ū"+"K"+sepa)
    ŪG_sepa = ŪK_sepa.replace("Ū"+sepa+"G"+sepa, "Ū"+"G"+sepa)
    ŪṄ_sepa = ŪG_sepa.replace("Ū"+sepa+"Ṅ"+sepa, "Ū"+"Ṅ"+sepa)
    ŪC_sepa = ŪṄ_sepa.replace("Ū"+sepa+"C"+sepa, "Ū"+"C"+sepa)
    ŪJ_sepa = ŪC_sepa.replace("Ū"+sepa+"J"+sepa, "Ū"+"J"+sepa)
    ŪÑ_sepa = ŪJ_sepa.replace("Ū"+sepa+"Ñ"+sepa, "Ū"+"Ñ"+sepa)
    ŪṬ_sepa = ŪÑ_sepa.replace("Ū"+sepa+"Ṭ"+sepa, "Ū"+"Ṭ"+sepa)
    ŪḌ_sepa = ŪṬ_sepa.replace("Ū"+sepa+"Ḍ"+sepa, "Ū"+"Ḍ"+sepa)
    ŪṆ_sepa = ŪḌ_sepa.replace("Ū"+sepa+"Ṇ"+sepa, "Ū"+"Ṅ"+sepa)
    ŪT_sepa = ŪṆ_sepa.replace("Ū"+sepa+"T"+sepa, "Ū"+"T"+sepa)
    ŪD_sepa = ŪT_sepa.replace("Ū"+sepa+"D"+sepa, "Ū"+"D"+sepa)
    ŪN_sepa = ŪD_sepa.replace("Ū"+sepa+"N"+sepa, "Ū"+"N"+sepa)
    ŪP_sepa = ŪN_sepa.replace("Ū"+sepa+"P"+sepa, "Ū"+"P"+sepa)
    ŪB_sepa = ŪP_sepa.replace("Ū"+sepa+"B"+sepa, "Ū"+"B"+sepa)
    ŪM_sepa = ŪB_sepa.replace("Ū"+sepa+"M"+sepa, "Ū"+"M"+sepa)

    EK_sepa = ŪM_sepa.replace("E"+sepa+"K"+sepa, "E"+"K"+sepa)
    EG_sepa = EK_sepa.replace("E"+sepa+"G"+sepa, "E"+"G"+sepa)
    EṄ_sepa = EG_sepa.replace("E"+sepa+"Ṅ"+sepa, "E"+"Ṅ"+sepa)
    EC_sepa = EṄ_sepa.replace("E"+sepa+"C"+sepa, "E"+"C"+sepa)
    EJ_sepa = EC_sepa.replace("E"+sepa+"J"+sepa, "E"+"J"+sepa)
    EÑ_sepa = EJ_sepa.replace("E"+sepa+"Ñ"+sepa, "E"+"Ñ"+sepa)
    EṬ_sepa = EÑ_sepa.replace("E"+sepa+"Ṭ"+sepa, "E"+"Ṭ"+sepa)
    EḌ_sepa = EṬ_sepa.replace("E"+sepa+"Ḍ"+sepa, "E"+"Ḍ"+sepa)
    EṆ_sepa = EḌ_sepa.replace("E"+sepa+"Ṇ"+sepa, "E"+"Ṅ"+sepa)
    ET_sepa = EṆ_sepa.replace("E"+sepa+"T"+sepa, "E"+"T"+sepa)
    ED_sepa = ET_sepa.replace("E"+sepa+"D"+sepa, "E"+"D"+sepa)
    EN_sepa = ED_sepa.replace("E"+sepa+"N"+sepa, "E"+"N"+sepa)
    EP_sepa = EN_sepa.replace("E"+sepa+"P"+sepa, "E"+"P"+sepa)
    EB_sepa = EP_sepa.replace("E"+sepa+"B"+sepa, "E"+"B"+sepa)
    EM_sepa = EB_sepa.replace("E"+sepa+"M"+sepa, "E"+"M"+sepa)

    OK_sepa = EM_sepa.replace("O"+sepa+"K"+sepa, "O"+"K"+sepa)
    OG_sepa = OK_sepa.replace("O"+sepa+"G"+sepa, "O"+"G"+sepa)
    OṄ_sepa = OG_sepa.replace("O"+sepa+"Ṅ"+sepa, "O"+"Ṅ"+sepa)
    OC_sepa = OṄ_sepa.replace("O"+sepa+"C"+sepa, "O"+"C"+sepa)
    OJ_sepa = OC_sepa.replace("O"+sepa+"J"+sepa, "O"+"J"+sepa)
    OÑ_sepa = OJ_sepa.replace("O"+sepa+"Ñ"+sepa, "O"+"Ñ"+sepa)
    OṬ_sepa = OÑ_sepa.replace("O"+sepa+"Ṭ"+sepa, "O"+"Ṭ"+sepa)
    OḌ_sepa = OṬ_sepa.replace("O"+sepa+"Ḍ"+sepa, "O"+"Ḍ"+sepa)
    OṆ_sepa = OḌ_sepa.replace("O"+sepa+"Ṇ"+sepa, "O"+"Ṅ"+sepa)
    OT_sepa = OṆ_sepa.replace("O"+sepa+"T"+sepa, "O"+"T"+sepa)
    OD_sepa = OT_sepa.replace("O"+sepa+"D"+sepa, "O"+"D"+sepa)
    ON_sepa = OD_sepa.replace("O"+sepa+"N"+sepa, "O"+"N"+sepa)
    OP_sepa = ON_sepa.replace("O"+sepa+"P"+sepa, "O"+"P"+sepa)
    OB_sepa = OP_sepa.replace("O"+sepa+"B"+sepa, "O"+"B"+sepa)
    OM_sepa = OB_sepa.replace("O"+sepa+"M"+sepa, "O"+"M"+sepa)

    # Remove juncture sign after long vowels (ā, ī, ū, e, o) followed by the letter ṃ or ṁ:
    # lowercase
    if uppercase_check:
        om_sepa_or_OM_sepa = OM_sepa
    else:
        om_sepa_or_OM_sepa = om_sepa
    āṃ = om_sepa_or_OM_sepa.replace("ā"+sepa+"ṃ", "ā"+"ṃ")
    īṃ = āṃ.replace("ī"+sepa+"ṃ", "ī"+"ṃ")
    ūṃ = īṃ.replace("ū"+sepa+"ṃ", "ū"+"ṃ")
    eṃ = ūṃ.replace("e"+sepa+"ṃ", "e"+"ṃ")
    oṃ = eṃ.replace("o"+sepa+"ṃ", "o"+"ṃ")

    āṁ = oṃ.replace("ā"+sepa+"ṁ", "ā"+"ṁ")
    īṁ = āṁ.replace("ī"+sepa+"ṁ", "ī"+"ṁ")
    ūṁ = īṁ.replace("ū"+sepa+"ṁ", "ū"+"ṁ")
    eṁ = ūṁ.replace("e"+sepa+"ṁ", "e"+"ṁ")
    oṁ = eṁ.replace("o"+sepa+"ṁ", "o"+"ṁ")
    # UPPERCASE
    ĀṂ = oṁ.replace("Ā"+sepa+"Ṃ", "Ā"+"Ṃ")
    ĪṂ = ĀṂ.replace("Ī"+sepa+"Ṃ", "Ī"+"Ṃ")
    ŪṂ = ĪṂ.replace("Ū"+sepa+"Ṃ", "Ū"+"Ṃ")
    EṂ = ŪṂ.replace("E"+sepa+"Ṃ", "E"+"Ṃ")
    OṂ = EṂ.replace("O"+sepa+"Ṃ", "O"+"Ṃ")

    ĀṀ = OṂ.replace("Ā"+sepa+"Ṁ", "Ā"+"Ṁ")
    ĪṀ = ĀṀ.replace("Ī"+sepa+"Ṁ", "Ī"+"Ṁ")
    ŪṀ = ĪṀ.replace("Ū"+sepa+"Ṁ", "Ū"+"Ṁ")
    EṀ = ŪṀ.replace("E"+sepa+"Ṁ", "E"+"Ṁ")
    OṀ = EṀ.replace("O"+sepa+"Ṁ", "O"+"Ṁ")

    # Remove juncture sign after long vowels (ā, ī, ū, e, o) followed by h_m, and s_m
    # lowercase
    if uppercase_check:
        oṁ_or_OṀ = OṀ
    else:
        oṁ_or_OṀ = oṁ
    āh_sepa_m = oṁ_or_OṀ.replace("ā"+sepa+"h"+sepa+"m", "ā"+"h"+sepa+"m")
    īh_sepa_m = āh_sepa_m.replace("ī"+sepa+"h"+sepa+"m", "ī"+"h"+sepa+"m")
    ūh_sepa_m = īh_sepa_m.replace("ū"+sepa+"h"+sepa+"m", "ū"+"h"+sepa+"m")
    eh_sepa_m = ūh_sepa_m.replace("e"+sepa+"h"+sepa+"m", "e"+"h"+sepa+"m")
    oh_sepa_m = eh_sepa_m.replace("o"+sepa+"h"+sepa+"m", "o"+"h"+sepa+"m")
    ās_sepa_m = oh_sepa_m.replace("ā"+sepa+"s"+sepa+"m", "ā"+"s"+sepa+"m")
    īs_sepa_m = ās_sepa_m.replace("ī"+sepa+"s"+sepa+"m", "ī"+"s"+sepa+"m")
    ūs_sepa_m = īs_sepa_m.replace("ū"+sepa+"s"+sepa+"m", "ū"+"s"+sepa+"m")
    es_sepa_m = ūs_sepa_m.replace("e"+sepa+"s"+sepa+"m", "e"+"s"+sepa+"m")
    os_sepa_m = es_sepa_m.replace("o"+sepa+"s"+sepa+"m", "o"+"s"+sepa+"m")
    #UPPERCASE
    ĀH_sepa_M = os_sepa_m.replace("Ā"+sepa+"H"+sepa+"M", "Ā"+"H"+sepa+"M")
    ĪH_sepa_M = ĀH_sepa_M.replace("Ī"+sepa+"H"+sepa+"M", "Ī"+"H"+sepa+"M")
    ŪH_sepa_M = ĪH_sepa_M.replace("Ū"+sepa+"H"+sepa+"M", "Ū"+"H"+sepa+"M")
    EH_sepa_M = ŪH_sepa_M.replace("E"+sepa+"H"+sepa+"M", "E"+"H"+sepa+"M")
    OH_sepa_M = EH_sepa_M.replace("O"+sepa+"H"+sepa+"M", "O"+"H"+sepa+"M")
    ĀS_sepa_M = OH_sepa_M.replace("Ā"+sepa+"S"+sepa+"M", "Ā"+"S"+sepa+"M")
    ĪS_sepa_M = ĀS_sepa_M.replace("Ī"+sepa+"S"+sepa+"M", "Ī"+"S"+sepa+"M")
    ŪS_sepa_M = ĪS_sepa_M.replace("Ū"+sepa+"S"+sepa+"M", "Ū"+"S"+sepa+"M")
    ES_sepa_M = ŪS_sepa_M.replace("E"+sepa+"S"+sepa+"M", "E"+"S"+sepa+"M")
    OS_sepa_M = ES_sepa_M.replace("O"+sepa+"S"+sepa+"M", "O"+"S"+sepa+"M")

    # Remove juncture sign after long vowels (ā, ī, ū, e, o) followed by ñ_h, ṇ_h, n_h, m_h, y_h, ḷ_h, l_h, v_h
    # lowercase
    if uppercase_check:
        os_sepa_m_or_OS_sepa_M = OS_sepa_M
    else:
        os_sepa_m_or_OS_sepa_M = os_sepa_m
    āñ_sepa_h = os_sepa_m_or_OS_sepa_M.replace("ā"+sepa+"ñ"+sepa+"h", "ā"+"ñ"+sepa+"h")
    īñ_sepa_h = āñ_sepa_h.replace("ī"+sepa+"ñ"+sepa+"h", "ī"+"ñ"+sepa+"h")
    ūñ_sepa_h = īñ_sepa_h.replace("ū"+sepa+"ñ"+sepa+"h", "ū"+"ñ"+sepa+"h")
    eñ_sepa_h = ūñ_sepa_h.replace("e"+sepa+"ñ"+sepa+"h", "e"+"ñ"+sepa+"h")
    oñ_sepa_h = eñ_sepa_h.replace("o"+sepa+"ñ"+sepa+"h", "o"+"ñ"+sepa+"h")

    āṇ_sepa_h = oñ_sepa_h.replace("ā"+sepa+"ṇ"+sepa+"h", "ā"+"ṇ"+sepa+"h")
    īṇ_sepa_h = āṇ_sepa_h.replace("ī"+sepa+"ṇ"+sepa+"h", "ī"+"ṇ"+sepa+"h")
    ūṇ_sepa_h = īṇ_sepa_h.replace("ū"+sepa+"ṇ"+sepa+"h", "ū"+"ṇ"+sepa+"h")
    eṇ_sepa_h = ūṇ_sepa_h.replace("e"+sepa+"ṇ"+sepa+"h", "e"+"ṇ"+sepa+"h")
    oṇ_sepa_h = eṇ_sepa_h.replace("o"+sepa+"ṇ"+sepa+"h", "o"+"ṇ"+sepa+"h")

    ān_sepa_h = oṇ_sepa_h.replace("ā"+sepa+"n"+sepa+"h", "ā"+"n"+sepa+"h")
    īn_sepa_h = ān_sepa_h.replace("ī"+sepa+"n"+sepa+"h", "ī"+"n"+sepa+"h")
    ūn_sepa_h = īn_sepa_h.replace("ū"+sepa+"n"+sepa+"h", "ū"+"n"+sepa+"h")
    en_sepa_h = ūn_sepa_h.replace("e"+sepa+"n"+sepa+"h", "e"+"n"+sepa+"h")
    on_sepa_h = en_sepa_h.replace("o"+sepa+"n"+sepa+"h", "o"+"n"+sepa+"h")

    ām_sepa_h = on_sepa_h.replace("ā"+sepa+"m"+sepa+"h", "ā"+"m"+sepa+"h")
    īm_sepa_h = ām_sepa_h.replace("ī"+sepa+"m"+sepa+"h", "ī"+"m"+sepa+"h")
    ūm_sepa_h = īm_sepa_h.replace("ū"+sepa+"m"+sepa+"h", "ū"+"m"+sepa+"h")
    em_sepa_h = ūm_sepa_h.replace("e"+sepa+"m"+sepa+"h", "e"+"m"+sepa+"h")
    om_sepa_h = em_sepa_h.replace("o"+sepa+"m"+sepa+"h", "o"+"m"+sepa+"h")

    āy_sepa_h = om_sepa_h.replace("ā"+sepa+"y"+sepa+"h", "ā"+"y"+sepa+"h")
    īy_sepa_h = āy_sepa_h.replace("ī"+sepa+"y"+sepa+"h", "ī"+"y"+sepa+"h")
    ūy_sepa_h = īy_sepa_h.replace("ū"+sepa+"y"+sepa+"h", "ū"+"y"+sepa+"h")
    ey_sepa_h = ūy_sepa_h.replace("e"+sepa+"y"+sepa+"h", "e"+"y"+sepa+"h")
    oy_sepa_h = ey_sepa_h.replace("o"+sepa+"y"+sepa+"h", "o"+"y"+sepa+"h")

    āḷ_sepa_h = oy_sepa_h.replace("ā"+sepa+"ḷ"+sepa+"h", "ā"+"ḷ"+sepa+"h")
    īḷ_sepa_h = āḷ_sepa_h.replace("ī"+sepa+"ḷ"+sepa+"h", "ī"+"ḷ"+sepa+"h")
    ūḷ_sepa_h = īḷ_sepa_h.replace("ū"+sepa+"ḷ"+sepa+"h", "ū"+"ḷ"+sepa+"h")
    eḷ_sepa_h = ūḷ_sepa_h.replace("e"+sepa+"ḷ"+sepa+"h", "e"+"ḷ"+sepa+"h")
    oḷ_sepa_h = eḷ_sepa_h.replace("o"+sepa+"ḷ"+sepa+"h", "o"+"ḷ"+sepa+"h")

    āl_sepa_h = oḷ_sepa_h.replace("ā"+sepa+"l"+sepa+"h", "ā"+"l"+sepa+"h")
    īl_sepa_h = āl_sepa_h.replace("ī"+sepa+"l"+sepa+"h", "ī"+"l"+sepa+"h")
    ūl_sepa_h = īl_sepa_h.replace("ū"+sepa+"l"+sepa+"h", "ū"+"l"+sepa+"h")
    el_sepa_h = ūl_sepa_h.replace("e"+sepa+"l"+sepa+"h", "e"+"l"+sepa+"h")
    ol_sepa_h = el_sepa_h.replace("o"+sepa+"l"+sepa+"h", "o"+"l"+sepa+"h")

    āv_sepa_h = ol_sepa_h.replace("ā"+sepa+"v"+sepa+"h", "ā"+"v"+sepa+"h")
    īv_sepa_h = āv_sepa_h.replace("ī"+sepa+"v"+sepa+"h", "ī"+"v"+sepa+"h")
    ūv_sepa_h = īv_sepa_h.replace("ū"+sepa+"v"+sepa+"h", "ū"+"v"+sepa+"h")
    ev_sepa_h = ūv_sepa_h.replace("e"+sepa+"v"+sepa+"h", "e"+"v"+sepa+"h")
    ov_sepa_h = ev_sepa_h.replace("o"+sepa+"v"+sepa+"h", "o"+"v"+sepa+"h")
    #UPPERCASE
    ĀÑ_sepa_H = ov_sepa_h.replace("Ā"+sepa+"Ñ"+sepa+"H", "Ā"+"Ñ"+sepa+"H")
    ĪÑ_sepa_H = ĀÑ_sepa_H.replace("Ī"+sepa+"Ñ"+sepa+"H", "Ī"+"Ñ"+sepa+"H")
    ŪÑ_sepa_H = ĪÑ_sepa_H.replace("Ū"+sepa+"Ñ"+sepa+"H", "Ū"+"Ñ"+sepa+"H")
    EÑ_sepa_H = ŪÑ_sepa_H.replace("E"+sepa+"Ñ"+sepa+"H", "E"+"Ñ"+sepa+"H")
    OÑ_sepa_H = EÑ_sepa_H.replace("O"+sepa+"Ñ"+sepa+"H", "O"+"Ñ"+sepa+"H")

    ĀṆ_sepa_H = OÑ_sepa_H.replace("Ā"+sepa+"Ṇ"+sepa+"H", "Ā"+"Ṇ"+sepa+"H")
    ĪṆ_sepa_H = ĀṆ_sepa_H.replace("Ī"+sepa+"Ṇ"+sepa+"H", "Ī"+"Ṇ"+sepa+"H")
    ŪṆ_sepa_H = ĪṆ_sepa_H.replace("Ū"+sepa+"Ṇ"+sepa+"H", "Ū"+"Ṇ"+sepa+"H")
    EṆ_sepa_H = ŪṆ_sepa_H.replace("E"+sepa+"Ṇ"+sepa+"H", "E"+"Ṇ"+sepa+"H")
    OṆ_sepa_H = EṆ_sepa_H.replace("O"+sepa+"Ṇ"+sepa+"H", "O"+"Ṇ"+sepa+"H")

    ĀN_sepa_H = OṆ_sepa_H.replace("Ā"+sepa+"N"+sepa+"H", "Ā"+"N"+sepa+"H")
    ĪN_sepa_H = ĀN_sepa_H.replace("Ī"+sepa+"N"+sepa+"H", "Ī"+"N"+sepa+"H")
    ŪN_sepa_H = ĪN_sepa_H.replace("Ū"+sepa+"N"+sepa+"H", "Ū"+"N"+sepa+"H")
    EN_sepa_H = ŪN_sepa_H.replace("E"+sepa+"N"+sepa+"H", "E"+"N"+sepa+"H")
    ON_sepa_H = EN_sepa_H.replace("O"+sepa+"N"+sepa+"H", "O"+"N"+sepa+"H")

    ĀM_sepa_H = ON_sepa_H.replace("Ā"+sepa+"M"+sepa+"H", "Ā"+"M"+sepa+"H")
    ĪM_sepa_H = ĀM_sepa_H.replace("Ī"+sepa+"M"+sepa+"H", "Ī"+"M"+sepa+"H")
    ŪM_sepa_H = ĪM_sepa_H.replace("Ū"+sepa+"M"+sepa+"H", "Ū"+"M"+sepa+"H")
    EM_sepa_H = ŪM_sepa_H.replace("E"+sepa+"M"+sepa+"H", "E"+"M"+sepa+"H")
    OM_sepa_H = EM_sepa_H.replace("O"+sepa+"M"+sepa+"H", "O"+"M"+sepa+"H")

    ĀY_sepa_H = OM_sepa_H.replace("Ā"+sepa+"Y"+sepa+"H", "Ā"+"Y"+sepa+"H")
    ĪY_sepa_H = ĀY_sepa_H.replace("Ī"+sepa+"Y"+sepa+"H", "Ī"+"Y"+sepa+"H")
    ŪY_sepa_H = ĪY_sepa_H.replace("Ū"+sepa+"Y"+sepa+"H", "Ū"+"Y"+sepa+"H")
    EY_sepa_H = ŪY_sepa_H.replace("E"+sepa+"Y"+sepa+"H", "E"+"Y"+sepa+"H")
    OY_sepa_H = EY_sepa_H.replace("O"+sepa+"Y"+sepa+"H", "O"+"Y"+sepa+"H")

    ĀḶ_sepa_H = OY_sepa_H.replace("Ā"+sepa+"Ḷ"+sepa+"H", "Ā"+"Ḷ"+sepa+"H")
    ĪḶ_sepa_H = ĀḶ_sepa_H.replace("Ī"+sepa+"Ḷ"+sepa+"H", "Ī"+"Ḷ"+sepa+"H")
    ŪḶ_sepa_H = ĪḶ_sepa_H.replace("Ū"+sepa+"Ḷ"+sepa+"H", "Ū"+"Ḷ"+sepa+"H")
    EḶ_sepa_H = ŪḶ_sepa_H.replace("E"+sepa+"Ḷ"+sepa+"H", "E"+"Ḷ"+sepa+"H")
    OḶ_sepa_H = EḶ_sepa_H.replace("O"+sepa+"Ḷ"+sepa+"H", "O"+"Ḷ"+sepa+"H")

    ĀL_sepa_H = OḶ_sepa_H.replace("Ā"+sepa+"L"+sepa+"H", "Ā"+"L"+sepa+"H")
    ĪL_sepa_H = ĀL_sepa_H.replace("Ī"+sepa+"L"+sepa+"H", "Ī"+"L"+sepa+"H")
    ŪL_sepa_H = ĪL_sepa_H.replace("Ū"+sepa+"L"+sepa+"H", "Ū"+"L"+sepa+"H")
    EL_sepa_H = ŪL_sepa_H.replace("E"+sepa+"L"+sepa+"H", "E"+"L"+sepa+"H")
    OL_sepa_H = EL_sepa_H.replace("O"+sepa+"L"+sepa+"H", "O"+"L"+sepa+"H")

    ĀV_sepa_H = OL_sepa_H.replace("Ā"+sepa+"V"+sepa+"H", "Ā"+"V"+sepa+"H")
    ĪV_sepa_H = ĀV_sepa_H.replace("Ī"+sepa+"V"+sepa+"H", "Ī"+"V"+sepa+"H")
    ŪV_sepa_H = ĪV_sepa_H.replace("Ū"+sepa+"V"+sepa+"H", "Ū"+"V"+sepa+"H")
    EV_sepa_H = ŪV_sepa_H.replace("E"+sepa+"V"+sepa+"H", "E"+"V"+sepa+"H")
    OV_sepa_H = EV_sepa_H.replace("O"+sepa+"V"+sepa+"H", "O"+"V"+sepa+"H")

    # Remove juncture sign after long vowels (ā, ī, ū, e, o) followed by k_y, m_y, y_y, l_y, v_y
    # lowercase
    if uppercase_check:
        ov_sepa_h_or_OV_sepa_H = OV_sepa_H
    else:
        ov_sepa_h_or_OV_sepa_H = ov_sepa_h
    āk_sepa_y = ov_sepa_h_or_OV_sepa_H.replace("ā"+sepa+"k"+sepa+"y", "ā"+"k"+sepa+"y")
    īk_sepa_y = āk_sepa_y.replace("ī"+sepa+"k"+sepa+"y", "ī"+"k"+sepa+"y")
    ūk_sepa_y = īk_sepa_y.replace("ū"+sepa+"k"+sepa+"y", "ū"+"k"+sepa+"y")
    ek_sepa_y = ūk_sepa_y.replace("e"+sepa+"k"+sepa+"y", "e"+"k"+sepa+"y")
    ok_sepa_y = ek_sepa_y.replace("o"+sepa+"k"+sepa+"y", "o"+"k"+sepa+"y")

    ām_sepa_y = ok_sepa_y.replace("ā"+sepa+"m"+sepa+"y", "ā"+"m"+sepa+"y")
    īm_sepa_y = ām_sepa_y.replace("ī"+sepa+"m"+sepa+"y", "ī"+"m"+sepa+"y")
    ūm_sepa_y = īm_sepa_y.replace("ū"+sepa+"m"+sepa+"y", "ū"+"m"+sepa+"y")
    em_sepa_y = ūm_sepa_y.replace("e"+sepa+"m"+sepa+"y", "e"+"m"+sepa+"y")
    om_sepa_y = em_sepa_y.replace("o"+sepa+"m"+sepa+"y", "o"+"m"+sepa+"y")

    āy_sepa_y = om_sepa_y.replace("ā"+sepa+"y"+sepa+"y", "ā"+"y"+sepa+"y")
    īy_sepa_y = āy_sepa_y.replace("ī"+sepa+"y"+sepa+"y", "ī"+"y"+sepa+"y")
    ūy_sepa_y = īy_sepa_y.replace("ū"+sepa+"y"+sepa+"y", "ū"+"y"+sepa+"y")
    ey_sepa_y = ūy_sepa_y.replace("e"+sepa+"y"+sepa+"y", "e"+"y"+sepa+"y")
    oy_sepa_y = ey_sepa_y.replace("o"+sepa+"y"+sepa+"y", "o"+"y"+sepa+"y")

    āl_sepa_y = oy_sepa_y.replace("ā"+sepa+"l"+sepa+"y", "ā"+"l"+sepa+"y")
    īl_sepa_y = āl_sepa_y.replace("ī"+sepa+"l"+sepa+"y", "ī"+"l"+sepa+"y")
    ūl_sepa_y = īl_sepa_y.replace("ū"+sepa+"l"+sepa+"y", "ū"+"l"+sepa+"y")
    el_sepa_y = ūl_sepa_y.replace("e"+sepa+"l"+sepa+"y", "e"+"l"+sepa+"y")
    ol_sepa_y = el_sepa_y.replace("o"+sepa+"l"+sepa+"y", "o"+"l"+sepa+"y")

    āv_sepa_y = ol_sepa_y.replace("ā"+sepa+"v"+sepa+"y", "ā"+"v"+sepa+"y")
    īv_sepa_y = āv_sepa_y.replace("ī"+sepa+"v"+sepa+"y", "ī"+"v"+sepa+"y")
    ūv_sepa_y = īv_sepa_y.replace("ū"+sepa+"v"+sepa+"y", "ū"+"v"+sepa+"y")
    ev_sepa_y = ūv_sepa_y.replace("e"+sepa+"v"+sepa+"y", "e"+"v"+sepa+"y")
    ov_sepa_y = ev_sepa_y.replace("o"+sepa+"v"+sepa+"y", "o"+"v"+sepa+"y")
    # UPPERCASE
    ĀK_sepa_Y = OV_sepa_H.replace("Ā"+sepa+"K"+sepa+"Y", "Ā"+"K"+sepa+"Y")
    ĪK_sepa_Y = ĀK_sepa_Y.replace("Ī"+sepa+"K"+sepa+"Y", "Ī"+"K"+sepa+"Y")
    ŪK_sepa_Y = ĪK_sepa_Y.replace("Ū"+sepa+"K"+sepa+"Y", "Ū"+"K"+sepa+"Y")
    EK_sepa_Y = ŪK_sepa_Y.replace("E"+sepa+"K"+sepa+"Y", "E"+"K"+sepa+"Y")
    OK_sepa_Y = EK_sepa_Y.replace("O"+sepa+"K"+sepa+"Y", "O"+"K"+sepa+"Y")

    ĀM_sepa_Y = OK_sepa_Y.replace("Ā"+sepa+"M"+sepa+"Y", "Ā"+"M"+sepa+"Y")
    ĪM_sepa_Y = ĀM_sepa_Y.replace("Ī"+sepa+"M"+sepa+"Y", "Ī"+"M"+sepa+"Y")
    ŪM_sepa_Y = ĪM_sepa_Y.replace("Ū"+sepa+"M"+sepa+"Y", "Ū"+"M"+sepa+"Y")
    EM_sepa_Y = ŪM_sepa_Y.replace("E"+sepa+"M"+sepa+"Y", "E"+"M"+sepa+"Y")
    OM_sepa_Y = EM_sepa_Y.replace("O"+sepa+"M"+sepa+"Y", "O"+"M"+sepa+"Y")

    ĀY_sepa_Y = OM_sepa_Y.replace("Ā"+"Y"+sepa+"Y", "Ā"+"Y"+sepa+"Y")
    ĪY_sepa_Y = ĀY_sepa_Y.replace("Ī"+"Y"+sepa+"Y", "Ī"+"Y"+sepa+"Y")
    ŪY_sepa_Y = ĪY_sepa_Y.replace("Ū"+"Y"+sepa+"Y", "Ū"+"Y"+sepa+"Y")
    EY_sepa_Y = ŪY_sepa_Y.replace("E"+"Y"+sepa+"Y", "E"+"Y"+sepa+"Y")
    OY_sepa_Y = EY_sepa_Y.replace("O"+"Y"+sepa+"Y", "O"+"Y"+sepa+"Y")

    ĀL_sepa_Y = OY_sepa_Y.replace("Ā"+sepa+"L"+sepa+"Y", "Ā"+"L"+sepa+"Y")
    ĪL_sepa_Y = ĀL_sepa_Y.replace("Ī"+sepa+"L"+sepa+"Y", "Ī"+"L"+sepa+"Y")
    ŪL_sepa_Y = ĪL_sepa_Y.replace("Ū"+sepa+"L"+sepa+"Y", "Ū"+"L"+sepa+"Y")
    EL_sepa_Y = ŪL_sepa_Y.replace("E"+sepa+"L"+sepa+"Y", "E"+"L"+sepa+"Y")
    OL_sepa_Y = EL_sepa_Y.replace("O"+sepa+"L"+sepa+"Y", "O"+"L"+sepa+"Y")

    ĀV_sepa_Y = OL_sepa_Y.replace("Ā"+sepa+"V"+sepa+"Y", "Ā"+"V"+sepa+"Y")
    ĪV_sepa_Y = ĀV_sepa_Y.replace("Ī"+sepa+"V"+sepa+"Y", "Ī"+"V"+sepa+"Y")
    ŪV_sepa_Y = ĪV_sepa_Y.replace("Ū"+sepa+"V"+sepa+"Y", "Ū"+"V"+sepa+"Y")
    EV_sepa_Y = ŪV_sepa_Y.replace("E"+sepa+"V"+sepa+"Y", "E"+"V"+sepa+"Y")
    OV_sepa_Y = EV_sepa_Y.replace("O"+sepa+"V"+sepa+"Y", "O"+"V"+sepa+"Y")

    # Remove juncture sign after long vowels (ā, ī, ū, e, o) followed by l_l
    # lowercase
    if uppercase_check:
        ov_sepa_y_or_OV_sepa_Y = OV_sepa_Y
    else:
        ov_sepa_y_or_OV_sepa_Y = ov_sepa_y
    āl_sepa_l = ov_sepa_y_or_OV_sepa_Y.replace("ā"+sepa+"l"+sepa+"l", "ā"+"l"+sepa+"l")
    īl_sepa_l = āl_sepa_l.replace("ī"+sepa+"l"+sepa+"l", "ī"+"l"+sepa+"l")
    ūl_sepa_l = īl_sepa_l.replace("ū"+sepa+"l"+sepa+"l", "ū"+"l"+sepa+"l")
    el_sepa_l = ūl_sepa_l.replace("e"+sepa+"l"+sepa+"l", "e"+"l"+sepa+"l")
    ol_sepa_l = el_sepa_l.replace("o"+sepa+"l"+sepa+"l", "o"+"l"+sepa+"l")

    # UPPERCASE
    ĀL_sepa_L = ol_sepa_l.replace("Ā"+sepa+"L"+sepa+"L", "Ā"+"L"+sepa+"L")
    ĪL_sepa_L = ĀL_sepa_L.replace("Ī"+sepa+"L"+sepa+"L", "Ī"+"L"+sepa+"L")
    ŪL_sepa_L = ĪL_sepa_L.replace("Ū"+sepa+"L"+sepa+"L", "Ū"+"L"+sepa+"L")
    EL_sepa_L = ŪL_sepa_L.replace("E"+sepa+"L"+sepa+"L", "E"+"L"+sepa+"L")
    OL_sepa_L = EL_sepa_L.replace("O"+sepa+"L"+sepa+"L", "O"+"L"+sepa+"L")

    # Remove juncture sign after long vowels (ā, ī, ū, e, o) followed by m_s and s_s
    # lowercase
    if uppercase_check:
        ol_sepa_l_or_OL_sepa_L = OL_sepa_L
    else:
        ol_sepa_l_or_OL_sepa_L = ol_sepa_l
    ām_sepa_s = ol_sepa_l_or_OL_sepa_L.replace("ā"+sepa+"m"+sepa+"s", "ā"+"m"+sepa+"s")
    īm_sepa_s = ām_sepa_s.replace("ī"+sepa+"m"+sepa+"s", "ī"+"m"+sepa+"s")
    ūm_sepa_s = īm_sepa_s.replace("ū"+sepa+"m"+sepa+"s", "ū"+"m"+sepa+"s")
    em_sepa_s = ūm_sepa_s.replace("e"+sepa+"m"+sepa+"s", "e"+"m"+sepa+"s")
    om_sepa_s = em_sepa_s.replace("o"+sepa+"m"+sepa+"s", "o"+"m"+sepa+"s")

    ās_sepa_s = om_sepa_s.replace("ā"+sepa+"s"+sepa+"s", "ā"+"s"+sepa+"s")
    īs_sepa_s = ās_sepa_s.replace("ī"+sepa+"s"+sepa+"s", "ī"+"s"+sepa+"s")
    ūs_sepa_s = īs_sepa_s.replace("ū"+sepa+"s"+sepa+"s", "ū"+"s"+sepa+"s")
    es_sepa_s = ūs_sepa_s.replace("e"+sepa+"s"+sepa+"s", "e"+"s"+sepa+"s")
    os_sepa_s = es_sepa_s.replace("o"+sepa+"s"+sepa+"s", "o"+"s"+sepa+"s")
    # UPPERCASE
    ĀM_sepa_S = os_sepa_s.replace("Ā"+sepa+"M"+sepa+"S", "Ā"+"M"+sepa+"S")
    ĪM_sepa_S = ĀM_sepa_S.replace("Ī"+sepa+"M"+sepa+"S", "Ī"+"M"+sepa+"S")
    ŪM_sepa_S = ĪM_sepa_S.replace("Ū"+sepa+"M"+sepa+"S", "Ū"+"M"+sepa+"S")
    EM_sepa_S = ŪM_sepa_S.replace("E"+sepa+"M"+sepa+"S", "E"+"M"+sepa+"S")
    OM_sepa_S = EM_sepa_S.replace("O"+sepa+"M"+sepa+"S", "O"+"M"+sepa+"S")

    ĀS_sepa_S = OM_sepa_S.replace("Ā"+sepa+"S"+sepa+"S", "Ā"+"S"+sepa+"S")
    ĪS_sepa_S = ĀS_sepa_S.replace("Ī"+sepa+"S"+sepa+"S", "Ī"+"S"+sepa+"S")
    ŪS_sepa_S = ĪS_sepa_S.replace("Ū"+sepa+"S"+sepa+"S", "Ū"+"S"+sepa+"S")
    ES_sepa_S = ŪS_sepa_S.replace("E"+sepa+"S"+sepa+"S", "E"+"S"+sepa+"S")
    OS_sepa_S = ES_sepa_S.replace("O"+sepa+"S"+sepa+"S", "O"+"S"+sepa+"S")

    # Remove juncture sign after long vowels (ā, ī, ū, e, o) followed by t_v, d_v, y_v, s_v
    # lowercsae
    if uppercase_check:
        os_sepa_s_or_OS_sepa_S = OS_sepa_S
    else:
        os_sepa_s_or_OS_sepa_S = os_sepa_s
    āt_sepa_v = os_sepa_s_or_OS_sepa_S.replace("ā"+sepa+"t"+sepa+"v", "ā"+"t"+sepa+"v")
    īt_sepa_v = āt_sepa_v.replace("ī"+sepa+"t"+sepa+"v", "ī"+"t"+sepa+"v")
    ūt_sepa_v = īt_sepa_v.replace("ū"+sepa+"t"+sepa+"v", "ū"+"t"+sepa+"v")
    et_sepa_v = ūt_sepa_v.replace("e"+sepa+"t"+sepa+"v", "e"+"t"+sepa+"v")
    ot_sepa_v = et_sepa_v.replace("o"+sepa+"t"+sepa+"v", "o"+"t"+sepa+"v")

    ād_sepa_v = ot_sepa_v.replace("ā"+sepa+"d"+sepa+"v", "ā"+"d"+sepa+"v")
    īd_sepa_v = ād_sepa_v.replace("ī"+sepa+"d"+sepa+"v", "ī"+"d"+sepa+"v")
    ūd_sepa_v = īd_sepa_v.replace("ū"+sepa+"d"+sepa+"v", "ū"+"d"+sepa+"v")
    ed_sepa_v = ūd_sepa_v.replace("e"+sepa+"d"+sepa+"v", "e"+"d"+sepa+"v")
    od_sepa_v = ed_sepa_v.replace("o"+sepa+"d"+sepa+"v", "o"+"d"+sepa+"v")

    āy_sepa_v = od_sepa_v.replace("ā"+sepa+"y"+sepa+"v", "ā"+"y"+sepa+"v")
    īy_sepa_v = āy_sepa_v.replace("ī"+sepa+"y"+sepa+"v", "ī"+"y"+sepa+"v")
    ūy_sepa_v = īy_sepa_v.replace("ū"+sepa+"y"+sepa+"v", "ū"+"y"+sepa+"v")
    ey_sepa_v = ūy_sepa_v.replace("e"+sepa+"y"+sepa+"v", "e"+"y"+sepa+"v")
    oy_sepa_v = ey_sepa_v.replace("o"+sepa+"y"+sepa+"v", "o"+"y"+sepa+"v")

    ās_sepa_v = oy_sepa_v.replace("ā"+sepa+"s"+sepa+"v", "ā"+"s"+sepa+"v")
    īs_sepa_v = ās_sepa_v.replace("ī"+sepa+"s"+sepa+"v", "ī"+"s"+sepa+"v")
    ūs_sepa_v = īs_sepa_v.replace("ū"+sepa+"s"+sepa+"v", "ū"+"s"+sepa+"v")
    es_sepa_v = ūs_sepa_v.replace("e"+sepa+"s"+sepa+"v", "e"+"s"+sepa+"v")
    os_sepa_v = es_sepa_v.replace("o"+sepa+"s"+sepa+"v", "o"+"s"+sepa+"v")
    # UPPERCASE
    ĀT_sepa_V = os_sepa_v.replace("Ā"+sepa+"T"+sepa+"V", "Ā"+"T"+sepa+"V")
    ĪT_sepa_V = ĀT_sepa_V.replace("Ī"+sepa+"T"+sepa+"V", "Ī"+"T"+sepa+"V")
    ŪT_sepa_V = ĪT_sepa_V.replace("Ū"+sepa+"T"+sepa+"V", "Ū"+"T"+sepa+"V")
    ET_sepa_V = ŪT_sepa_V.replace("E"+sepa+"T"+sepa+"V", "E"+"T"+sepa+"V")
    OT_sepa_V = ET_sepa_V.replace("O"+sepa+"T"+sepa+"V", "O"+"T"+sepa+"V")

    ĀD_sepa_V = OT_sepa_V.replace("Ā"+sepa+"D"+sepa+"V", "Ā"+"D"+sepa+"V")
    ĪD_sepa_V = ĀD_sepa_V.replace("Ī"+sepa+"D"+sepa+"V", "Ī"+"D"+sepa+"V")
    ŪD_sepa_V = ĪD_sepa_V.replace("Ū"+sepa+"D"+sepa+"V", "Ū"+"D"+sepa+"V")
    ED_sepa_V = ŪD_sepa_V.replace("E"+sepa+"D"+sepa+"V", "E"+"D"+sepa+"V")
    OD_sepa_V = ED_sepa_V.replace("O"+sepa+"D"+sepa+"V", "O"+"D"+sepa+"V")

    ĀY_sepa_V = OD_sepa_V.replace("Ā"+sepa+"Y"+sepa+"V", "Ā"+"Y"+sepa+"V")
    ĪY_sepa_V = ĀY_sepa_V.replace("Ī"+sepa+"Y"+sepa+"V", "Ī"+"Y"+sepa+"V")
    ŪY_sepa_V = ĪY_sepa_V.replace("Ū"+sepa+"Y"+sepa+"V", "Ū"+"Y"+sepa+"V")
    EY_sepa_V = ŪY_sepa_V.replace("E"+sepa+"Y"+sepa+"V", "E"+"Y"+sepa+"V")
    OY_sepa_V = EY_sepa_V.replace("O"+sepa+"Y"+sepa+"V", "O"+"Y"+sepa+"V")

    ĀS_sepa_V = OY_sepa_V.replace("Ā"+sepa+"S"+sepa+"V", "Ā"+"S"+sepa+"V")
    ĪS_sepa_V = ĀS_sepa_V.replace("Ī"+sepa+"S"+sepa+"V", "Ī"+"S"+sepa+"V")
    ŪS_sepa_V = ĪS_sepa_V.replace("Ū"+sepa+"S"+sepa+"V", "Ū"+"S"+sepa+"V")
    ES_sepa_V = ŪS_sepa_V.replace("E"+sepa+"S"+sepa+"V", "E"+"S"+sepa+"V")
    OS_sepa_V = ES_sepa_V.replace("O"+sepa+"S"+sepa+"V", "O"+"S"+sepa+"V")

    # Remove juncture sign; "_" in certain double consonants if the syllables begin with a capitalized letter, preceeded by a space " ", or a line break / enter (char(10)
    #lowercase
    if uppercase_check:
        os_sepa_v_or_OS_sepa_V = OS_sepa_V
    else:
        os_sepa_v_or_OS_sepa_V = os_sepa_v
    Hm = os_sepa_v_or_OS_sepa_V.replace("H"+sepa+"m", "H"+"m")
    Sm = Hm.replace("S"+sepa+"m", "S"+"m")
    Ñh = Sm.replace("Ñ"+sepa+"h", "Ñ"+"h")
    Ṇh = Ñh.replace("Ṇ"+sepa+"h", "Ṇ"+"h")
    Nh = Ṇh.replace("N"+sepa+"h", "N"+"h")
    Mh = Nh.replace("M"+sepa+"h", "M"+"h")
    Yh = Mh.replace("Y"+sepa+"h", "Y"+"h")
    Ḷh = Yh.replace("Ḷ"+sepa+"h", "Ḷ"+"h")
    Lh = Ḷh.replace("L"+sepa+"h", "L"+"h")
    Vh = Lh.replace("V"+sepa+"h", "V"+"h")

    Ky = Vh.replace("K"+sepa+"y", "K"+"y")
    My = Ky.replace("M"+sepa+"y", "M"+"y")
    Yy = My.replace("Y"+sepa+"y", "Y"+"y")
    Ly = Yy.replace("L"+sepa+"y", "L"+"y")
    Vy = Ly.replace("V"+sepa+"y", "V"+"y")
    Ty = Vy.replace("T"+sepa+"y", "T"+"y")
    Dy = Ty.replace("D"+sepa+"y", "D"+"y")

    Ll = Dy.replace("L"+sepa+"l", "L"+"l")

    Ms = Ll.replace("M"+sepa+"s", "M"+"s")
    Ss = Ms.replace("S"+sepa+"s", "S"+"s")

    Tv = Ss.replace("T"+sepa+"v", "T"+"v")
    Dv = Tv.replace("D"+sepa+"v", "D"+"v")
    Yv = Dv.replace("Y"+sepa+"v", "Y"+"v")
    Sv = Yv.replace("S"+sepa+"v", "S"+"v")

    space_h_m = Sv.replace(" "+"h"+sepa+"m", " "+"h"+"m")
    space_s_m = space_h_m.replace(" "+"s"+sepa+"m", " "+"s"+"m")

    space_ñ_h = space_s_m.replace(" "+"ñ"+sepa+"h", " "+"ñ"+"h")
    space_ṇ_h = space_ñ_h.replace(" "+"ṇ"+sepa+"h", " "+"ṇ"+"h")
    space_n_h = space_ṇ_h.replace(" "+"n"+sepa+"h", " "+"n"+"h")
    space_m_h = space_n_h.replace(" "+"m"+sepa+"h", " "+"m"+"h")
    space_y_h = space_m_h.replace(" "+"y"+sepa+"h", " "+"y"+"h")
    space_ḷ_h = space_y_h.replace(" "+"ḷ"+sepa+"h", " "+"ḷ"+"h")
    space_l_h = space_ḷ_h.replace(" "+"l"+sepa+"h", " "+"l"+"h")
    space_v_h = space_l_h.replace(" "+"v"+sepa+"h", " "+"v"+"h")
    
    space_k_y = space_v_h.replace(" "+"k"+sepa+"y", " "+"k"+"y")
    space_m_y = space_k_y.replace(" "+"m"+sepa+"y", " "+"m"+"y")
    space_y_y = space_m_y.replace(" "+"y"+sepa+"y", " "+"y"+"y")
    space_l_y = space_y_y.replace(" "+"l"+sepa+"y", " "+"l"+"y")
    space_v_y = space_l_y.replace(" "+"v"+sepa+"y", " "+"v"+"y")
    space_t_y = space_v_y.replace(" "+"t"+sepa+"y", " "+"t"+"y")
    space_d_y = space_t_y.replace(" "+"d"+sepa+"y", " "+"d"+"y")

    space_l_l = space_d_y.replace(" "+"l"+sepa+"l", " "+"l"+"l")

    space_m_s = space_l_l.replace(" "+"m"+sepa+"s", " "+"m"+"s")
    space_s_s = space_m_s.replace(" "+"s"+sepa+"s", " "+"s"+"s")

    space_t_v = space_s_s.replace(" "+"t"+sepa+"v", " "+"t"+"v")
    space_d_v = space_t_v.replace(" "+"d"+sepa+"v", " "+"d"+"v")
    space_y_v = space_d_v.replace(" "+"y"+sepa+"v", " "+"y"+"v")
    space_s_v = space_y_v.replace(" "+"s"+sepa+"v", " "+"s"+"v")

    lbreak_h_m = space_s_v.replace("\n"+"h"+sepa+"m", "\n"+"h"+"m")
    lbreak_s_m = lbreak_h_m.replace("\n"+"s"+sepa+"m", "\n"+"s"+"m")
    
    lbreak_ñ_h = lbreak_s_m.replace("\n"+"ñ"+sepa+"h", "\n"+"ñ"+"h")
    lbreak_ṇ_h = lbreak_ñ_h.replace("\n"+"ṇ"+sepa+"h", "\n"+"ṇ"+"h")
    lbreak_n_h = lbreak_ṇ_h.replace("\n"+"n"+sepa+"h", "\n"+"n"+"h")
    lbreak_m_h = lbreak_n_h.replace("\n"+"m"+sepa+"h", "\n"+"m"+"h")
    lbreak_y_h = lbreak_m_h.replace("\n"+"y"+sepa+"h", "\n"+"y"+"h")
    lbreak_ḷ_h = lbreak_y_h.replace("\n"+"ḷ"+sepa+"h", "\n"+"ḷ"+"h")
    lbreak_l_h = lbreak_ḷ_h.replace("\n"+"l"+sepa+"h", "\n"+"l"+"h")
    lbreak_v_h = lbreak_l_h.replace("\n"+"v"+sepa+"h", "\n"+"v"+"h")

    lbreak_k_y = space_v_h.replace("\n"+"k"+sepa+"y", "\n"+"k"+"y")
    lbreak_m_y = lbreak_k_y.replace("\n"+"m"+sepa+"y", "\n"+"m"+"y")
    lbreak_y_y = lbreak_m_y.replace("\n"+"y"+sepa+"y", "\n"+"y"+"y")
    lbreak_l_y = lbreak_y_y.replace("\n"+"l"+sepa+"y", "\n"+"l"+"y")
    lbreak_v_y = lbreak_l_y.replace("\n"+"v"+sepa+"y", "\n"+"v"+"y")
    lbreak_t_y = lbreak_v_y.replace("\n"+"t"+sepa+"y", "\n"+"t"+"y")
    lbreak_d_y = lbreak_t_y.replace("\n"+"d"+sepa+"y", "\n"+"d"+"y")

    lbreak_l_l = lbreak_d_y.replace("\n"+"l"+sepa+"l", "\n"+"l"+"l")

    lbreak_m_s = lbreak_l_l.replace("\n"+"m"+sepa+"s", "\n"+"m"+"s")
    lbreak_s_s = lbreak_m_s.replace("\n"+"s"+sepa+"s", "\n"+"s"+"s")

    lbreak_t_v = lbreak_s_s.replace("\n"+"t"+sepa+"v", "\n"+"t"+"v")
    lbreak_d_v = lbreak_t_v.replace("\n"+"d"+sepa+"v", "\n"+"d"+"v")
    lbreak_y_v = lbreak_d_v.replace("\n"+"y"+sepa+"v", "\n"+"y"+"v")
    lbreak_s_v = lbreak_y_v.replace("\n"+"s"+sepa+"v", "\n"+"s"+"v")

    # UPPERCASE
    space_H_M = lbreak_s_v.replace(" "+"H"+sepa+"M", " "+"H"+"M")
    space_S_M = space_H_M.replace(" "+"S"+sepa+"M", " "+"S"+"M")

    space_Ñ_H = space_S_M.replace(" "+"Ñ"+sepa+"H", " "+"Ñ"+"H")
    space_Ṇ_H = space_Ñ_H.replace(" "+"Ṇ"+sepa+"H", " "+"Ṇ"+"H")
    space_N_H = space_Ṇ_H.replace(" "+"N"+sepa+"H", " "+"N"+"H")
    space_M_H = space_N_H.replace(" "+"M"+sepa+"H", " "+"M"+"H")
    space_Y_H = space_M_H.replace(" "+"Y"+sepa+"H", " "+"Y"+"H")
    space_Ḷ_H = space_Y_H.replace(" "+"Ḷ"+sepa+"H", " "+"Ḷ"+"H")
    space_L_H = space_Ḷ_H.replace(" "+"L"+sepa+"H", " "+"L"+"H")
    space_V_H = space_L_H.replace(" "+"V"+sepa+"H", " "+"V"+"H")
    
    space_K_Y = space_V_H.replace(" "+"K"+sepa+"Y", " "+"K"+"Y")
    space_M_Y = space_K_Y.replace(" "+"M"+sepa+"Y", " "+"M"+"Y")
    space_Y_Y = space_M_Y.replace(" "+"Y"+sepa+"Y", " "+"Y"+"Y")
    space_L_Y = space_Y_Y.replace(" "+"L"+sepa+"Y", " "+"L"+"Y")
    space_V_Y = space_L_Y.replace(" "+"V"+sepa+"Y", " "+"V"+"Y")
    space_T_Y = space_V_Y.replace(" "+"T"+sepa+"Y", " "+"T"+"Y")
    space_D_Y = space_T_Y.replace(" "+"D"+sepa+"Y", " "+"D"+"Y")

    space_L_L = space_D_Y.replace(" "+"L"+sepa+"L", " "+"L"+"L")

    space_M_S = space_L_L.replace(" "+"M"+sepa+"S", " "+"M"+"S")
    space_S_S = space_M_S.replace(" "+"S"+sepa+"S", " "+"S"+"S")

    space_T_V = space_S_S.replace(" "+"T"+sepa+"V", " "+"T"+"V")
    space_D_V = space_T_V.replace(" "+"D"+sepa+"V", " "+"D"+"V")
    space_Y_V = space_D_V.replace(" "+"Y"+sepa+"V", " "+"Y"+"V")
    space_S_V = space_Y_V.replace(" "+"S"+sepa+"V", " "+"S"+"V")

    lbreak_H_M = space_S_V.replace("\n"+"H"+sepa+"M", "\n"+"H"+"M")
    lbreak_S_M = lbreak_H_M.replace("\n"+"S"+sepa+"M", "\n"+"S"+"M")
    
    lbreak_Ñ_H = lbreak_S_M.replace("\n"+"Ñ"+sepa+"H", "\n"+"Ñ"+"H")
    lbreak_Ṇ_H = lbreak_Ñ_H.replace("\n"+"Ṇ"+sepa+"H", "\n"+"Ṇ"+"H")
    lbreak_N_H = lbreak_Ṇ_H.replace("\n"+"N"+sepa+"H", "\n"+"N"+"H")
    lbreak_M_H = lbreak_N_H.replace("\n"+"M"+sepa+"H", "\n"+"M"+"H")
    lbreak_Y_H = lbreak_M_H.replace("\n"+"Y"+sepa+"H", "\n"+"Y"+"H")
    lbreak_Ḷ_H = lbreak_Y_H.replace("\n"+"Ḷ"+sepa+"H", "\n"+"Ḷ"+"H")
    lbreak_L_H = lbreak_Ḷ_H.replace("\n"+"L"+sepa+"H", "\n"+"L"+"H")
    lbreak_V_H = lbreak_L_H.replace("\n"+"V"+sepa+"H", "\n"+"V"+"H")

    lbreak_K_Y = lbreak_V_H.replace("\n"+"K"+sepa+"Y", "\n"+"K"+"Y")
    lbreak_M_Y = lbreak_K_Y.replace("\n"+"M"+sepa+"Y", "\n"+"M"+"Y")
    lbreak_Y_Y = lbreak_M_Y.replace("\n"+"Y"+sepa+"Y", "\n"+"Y"+"Y")
    lbreak_L_Y = lbreak_Y_Y.replace("\n"+"L"+sepa+"Y", "\n"+"L"+"Y")
    lbreak_V_Y = lbreak_L_Y.replace("\n"+"V"+sepa+"Y", "\n"+"V"+"Y")
    lbreak_T_Y = lbreak_V_Y.replace("\n"+"T"+sepa+"Y", "\n"+"T"+"Y")
    lbreak_D_Y = lbreak_T_Y.replace("\n"+"D"+sepa+"Y", "\n"+"D"+"Y")

    lbreak_L_L = lbreak_D_Y.replace("\n"+"L"+sepa+"L", "\n"+"L"+"L")

    lbreak_M_S = lbreak_L_L.replace("\n"+"M"+sepa+"S", "\n"+"M"+"S")
    lbreak_S_S = lbreak_M_S.replace("\n"+"S"+sepa+"S", "\n"+"S"+"S")

    lbreak_T_V = lbreak_S_S.replace("\n"+"T"+sepa+"V", "\n"+"T"+"V")
    lbreak_D_V = lbreak_T_V.replace("\n"+"D"+sepa+"V", "\n"+"D"+"V")
    lbreak_Y_V = lbreak_D_V.replace("\n"+"Y"+sepa+"V", "\n"+"Y"+"V")
    lbreak_S_V = lbreak_Y_V.replace("\n"+"S"+sepa+"V", "\n"+"S"+"V")

    # Remove double juncture signs
    no_double_junctures = lbreak_S_V.replace(sepa+sepa,sepa)
    NO_DOUBLE_JUNCTURES = lbreak_S_V.replace(sepa+sepa,sepa)

    # Remove double juncture signs
    no_double_junctures2 = no_double_junctures.replace(sepa+sepa,sepa)
    NO_DOUBLE_JUNCTURES2 = NO_DOUBLE_JUNCTURES.replace(sepa+sepa,sepa)

    # (Optional) Anusvāra / niggahīta standard conversion
    if uppercase_check:
        no_double_junctures_or_NO_DOUBLE_JUNCTURES = NO_DOUBLE_JUNCTURES2
    else:
        no_double_junctures_or_NO_DOUBLE_JUNCTURES = no_double_junctures2
    if anusvara_select == "Change to ṃ - IAST (International Alphabet of Sanskrit Transliteration)":
        # lowercase
        convert_to_ṃ = no_double_junctures_or_NO_DOUBLE_JUNCTURES.replace("ṁ", "ṃ")
        # UPPERCASE
        convert_to_Ṁ_or_Ṃ = convert_to_ṃ.replace("Ṁ", "Ṃ")
    if anusvara_select == "Change to ṁ - ISO 15919: Pāḷi":
        # lowercase
        convert_to_ṁ = no_double_junctures_or_NO_DOUBLE_JUNCTURES.replace("ṃ", "ṁ")
        # UPPERCASE
        convert_to_Ṁ_or_Ṃ = convert_to_ṁ.replace("Ṃ", "Ṁ")
    else:
        convert_to_Ṁ_or_Ṃ = no_double_junctures_or_NO_DOUBLE_JUNCTURES

    # Fix the position of preposition pauses and junctions signs

    sepa_comma = convert_to_Ṁ_or_Ṃ.replace(sepa+",",","+sepa)
    sepa_period = sepa_comma.replace(sepa+".","."+sepa)
    sepa_scolon = sepa_period.replace(sepa+";",";"+sepa)
    sepa_colon = sepa_scolon.replace(sepa+":",":"+sepa)

    # (Optional) Saṃyoga Pauses; Breaks for short open syllables at the end of a phrase/sentence; Insert juncture sign after the short vowels a, i, and u if they preceed a line break, a double space (tab/indentations), a comma, a semi-colon, or a colon:
    # lowercase
    a_sepa_lbreak = sepa_colon.replace("a"+"  \n", "a"+sepa+"  \n")
    i_sepa_lbreak = a_sepa_lbreak.replace("i"+"  \n", "i"+sepa+"  \n")
    u_sepa_lbreak = i_sepa_lbreak.replace("u"+"  \n", "u"+sepa+"  \n")

    a_sepa_dspace = u_sepa_lbreak.replace("a"+"  ", "a"+sepa+"  ")
    i_sepa_dspace = a_sepa_dspace.replace("i"+"  ", "i"+sepa+"  ")
    u_sepa_dspace = i_sepa_dspace.replace("u"+"  ", "u"+sepa+"  ")

    a_comma_sepa = u_sepa_dspace.replace("a"+",", "a"+","+sepa)
    i_comma_sepa = a_comma_sepa.replace("i"+",", "i"+","+sepa)
    u_comma_sepa = i_comma_sepa.replace("u"+",", "u"+","+sepa)

    a_sepa_period = u_comma_sepa.replace("a"+".", "a"+"."+sepa)
    i_sepa_period = a_sepa_period.replace("i"+".", "i"+"."+sepa)
    u_sepa_period = i_sepa_period.replace("u"+".", "u"+"."+sepa)

    a_sepa_scolon = u_sepa_period.replace("a"+";", "a"+";"+sepa)
    i_sepa_scolon = a_sepa_scolon.replace("i"+";", "i"+";"+sepa)
    u_sepa_scolon = i_sepa_scolon.replace("u"+";", "u"+";"+sepa)

    a_sepa_colon = u_sepa_scolon.replace("a"+":","a"+":"+sepa)
    i_sepa_colon = a_sepa_colon.replace("i"+":","i"+":"+sepa)
    u_sepa_colon = i_sepa_colon.replace("u"+":","u"+":"+sepa)
    # UPPERCASE
    A_sepa_lbreak = u_sepa_colon.replace("A"+"  \n", "A"+sepa+"  \n")
    I_sepa_lbreak = A_sepa_lbreak.replace("I"+"  \n", "I"+sepa+"  \n")
    U_sepa_lbreak = I_sepa_lbreak.replace("U"+"  \n", "U"+sepa+"  \n")

    A_sepa_dspace = U_sepa_lbreak.replace("A"+"  ", "A"+sepa+"  ")
    I_sepa_dspace = A_sepa_dspace.replace("I"+"  ", "I"+sepa+"  ")
    U_sepa_dspace = I_sepa_dspace.replace("U"+"  ", "U"+sepa+"  ")

    A_comma_sepa = U_sepa_dspace.replace("A"+",", "A"+","+sepa)
    I_comma_sepa = A_comma_sepa.replace("I"+",", "I"+","+sepa)
    U_comma_sepa = I_comma_sepa.replace("U"+",", "U"+","+sepa)

    A_sepa_period = U_comma_sepa.replace("A"+".", "A"+"."+sepa)
    I_sepa_period = A_sepa_period.replace("I"+".", "I"+"."+sepa)
    U_sepa_period = I_sepa_period.replace("U"+".", "U"+"."+sepa)

    A_sepa_scolon = U_sepa_period.replace("A"+";", "A"+";"+sepa)
    I_sepa_scolon = A_sepa_scolon.replace("I"+";", "I"+";"+sepa)
    U_sepa_scolon = I_sepa_scolon.replace("U"+";", "U"+";"+sepa)

    A_sepa_colon = U_sepa_scolon.replace("A"+":","A"+":"+sepa)
    I_sepa_colon = A_sepa_colon.replace("I"+":","I"+":"+sepa)
    U_sepa_colon = I_sepa_colon.replace("U"+":","U"+":"+sepa)
        

    # (Optional) Saṃyoga Pauses; Breaks for short open syllables at the end of a phrase/sentence; Insert juncture sign after the short vowels a, i, and u if they preceed a line break, a double space (tab/indentations), a comma, a semi-colon, or a colon:
    # lowercase
    if uppercase_check:
        u_sepa_colon_or_U_sepa_colon = U_sepa_colon
    else:
        u_sepa_colon_or_U_sepa_colon = u_sepa_colon
    undo_a_sepa_lbreak = u_sepa_colon_or_U_sepa_colon.replace("a"+sepa+"  \n", "a"+"  \n")
    undo_i_sepa_lbreak = undo_a_sepa_lbreak.replace("i"+sepa+"  \n", "i"+"  \n")
    undo_u_sepa_lbreak = undo_i_sepa_lbreak.replace("u"+sepa+"  \n", "u"+"  \n")

    undo_a_sepa_dspace = undo_u_sepa_lbreak.replace("a"+sepa+"  ", "a"+"  ")
    undo_i_sepa_dspace = undo_a_sepa_dspace.replace("i"+sepa+"  ", "i"+"  ")
    undo_u_sepa_dspace = undo_i_sepa_dspace.replace("u"+sepa+"  ", "u"+"  ")

    undo_a_comma_sepa = undo_u_sepa_dspace.replace("a"+","+sepa, "a"+",")
    undo_i_comma_sepa = undo_a_comma_sepa.replace("i"+","+sepa, "i"+",")
    undo_u_comma_sepa = undo_i_comma_sepa.replace("u"+","+sepa, "u"+",")

    undo_a_sepa_period = undo_u_comma_sepa.replace("a"+"."+sepa, "a"+".")
    undo_i_sepa_period = undo_a_sepa_period.replace("i"+"."+sepa, "i"+".")
    undo_u_sepa_period = undo_i_sepa_period.replace("u"+"."+sepa, "u"+".")

    undo_a_sepa_scolon = undo_u_sepa_period.replace("a"+";"+sepa, "a"+";")
    undo_i_sepa_scolon = undo_a_sepa_scolon.replace("i"+";"+sepa, "i"+";")
    undo_u_sepa_scolon = undo_i_sepa_scolon.replace("u"+";"+sepa, "u"+";")

    undo_a_sepa_colon = undo_u_sepa_scolon.replace("a"+":"+sepa, "a"+":")
    undo_i_sepa_colon = undo_a_sepa_colon.replace("i"+":"+sepa, "i"+":")
    undo_u_sepa_colon = undo_i_sepa_colon.replace("u"+":"+sepa, "u"+":")
    # UPPERCASE
    undo_A_sepa_lbreak = undo_u_sepa_colon.replace("A"+sepa+"  \n", "A"+"  \n")
    undo_I_sepa_lbreak = undo_A_sepa_lbreak.replace("I"+sepa+"  \n", "I"+"  \n")
    undo_U_sepa_lbreak = undo_I_sepa_lbreak.replace("U"+sepa+"  \n", "U"+"  \n")

    undo_A_sepa_dspace = undo_U_sepa_lbreak.replace("A"+sepa+"  ", "A"+"  ")
    undo_I_sepa_dspace = undo_A_sepa_dspace.replace("I"+sepa+"  ", "I"+"  ")
    undo_U_sepa_dspace = undo_I_sepa_dspace.replace("U"+sepa+"  ", "U"+"  ")

    undo_A_comma_sepa = undo_U_sepa_dspace.replace("A"+","+sepa, "A"+",")
    undo_I_comma_sepa = undo_A_comma_sepa.replace("I"+","+sepa, "I"+",")
    undo_U_comma_sepa = undo_I_comma_sepa.replace("U"+","+sepa, "U"+",")

    undo_A_sepa_period = undo_U_comma_sepa.replace("A"+"."+sepa, "A"+".")
    undo_I_sepa_period = undo_A_sepa_period.replace("I"+"."+sepa, "I"+".")
    undo_U_sepa_period = undo_I_sepa_period.replace("U"+"."+sepa, "U"+".")

    undo_A_sepa_scolon = undo_U_sepa_period.replace("A"+";"+sepa, "A"+";")
    undo_I_sepa_scolon = undo_A_sepa_scolon.replace("I"+";"+sepa, "I"+";")
    undo_U_sepa_scolon = undo_I_sepa_scolon.replace("U"+";"+sepa, "U"+";")

    undo_A_sepa_colon = undo_U_sepa_scolon.replace("A"+":"+sepa, "A"+":")
    undo_I_sepa_colon = undo_A_sepa_colon.replace("I"+":"+sepa, "I"+":")
    undo_U_sepa_colon = undo_I_sepa_colon.replace("U"+":"+sepa, "U"+":")


    # (Optional) Medial anusvāra / niggahīta to nasal (gaṃgā → gaṅgā)
    if samyoga_pauses_check:
        u_sepa_colon_or_U_sepa_colon_OR_undo_U_sepa_colon = undo_U_sepa_colon
    else:
        u_sepa_colon_or_U_sepa_colon_OR_undo_U_sepa_colon = u_sepa_colon_or_U_sepa_colon
    ṃ_to_ṅ_g = u_sepa_colon_or_U_sepa_colon_OR_undo_U_sepa_colon.replace("ṃ"+"g", "ṅ"+"g")
    ṁ_to_ṅ_g = ṃ_to_ṅ_g.replace("ṁ"+"g", "ṅ"+"g")
    Ṃ_to_Ṅ_G = ṁ_to_ṅ_g.replace("Ṃ"+"G", "Ṅ"+"G")
    Ṁ_to_Ṅ_G = Ṃ_to_Ṅ_G.replace("Ṁ"+"G", "Ṅ"+"G")
    ṃ_to_ṅ_sepa_g = Ṁ_to_Ṅ_G.replace("ṃ"+sepa+"g", "ṅ"+sepa+"g")
    ṁ_to_ṅ_sepa_g = ṃ_to_ṅ_sepa_g.replace("ṁ"+sepa+"g", "ṅ"+sepa+"g")
    Ṃ_to_Ṅ_sepa_G = ṁ_to_ṅ_sepa_g.replace("Ṃ"+sepa+"G", "Ṅ"+sepa+"G")
    Ṁ_to_Ṅ_sepa_G = Ṃ_to_Ṅ_sepa_G.replace("Ṁ"+sepa+"G", "Ṅ"+sepa+"G") 

    st.divider()

    """
    **Split text:**
    """

    if insert_text == "":
        st.markdown('''
        :gray[The split text will be shown here.]''')
    if nasal_check:
        u_sepa_colon_or_U_sepa_colon_OR_undo_U_sepa_colon_OR_Ṁ_to_Ṅ_sepa_G = Ṁ_to_Ṅ_sepa_G
    else:
        u_sepa_colon_or_U_sepa_colon_OR_undo_U_sepa_colon_OR_Ṁ_to_Ṅ_sepa_G = u_sepa_colon_or_U_sepa_colon_OR_undo_U_sepa_colon

    # Nasal ññ → nñ
    ññ_to_nñ = u_sepa_colon_or_U_sepa_colon_OR_undo_U_sepa_colon_OR_Ṁ_to_Ṅ_sepa_G.replace ("ñ"+sepa+"ñ", "n"+sepa+"ñ")
    ÑÑ_to_NÑ = ññ_to_nñ.replace("Ñ"+sepa+"Ñ", "N"+sepa+"Ñ")
    Ññ_to_Nñ = ÑÑ_to_NÑ.replace("Ñ"+sepa+"ñ", "N"+sepa+"ñ")
    ñÑ_to_nÑ = Ññ_to_Nñ.replace("ñ"+sepa+"Ñ", "n"+sepa+"Ñ")

    if nñ_check:
        nasal_nñ = ñÑ_to_nÑ
    else:
        nasal_nñ = u_sepa_colon_or_U_sepa_colon_OR_undo_U_sepa_colon_OR_Ṁ_to_Ṅ_sepa_G

    # Nasal ṅ, ṃ, ṁ → ng
        #lowercase
    ṅ_to_ng = nasal_nñ.replace("ṅ", "ng")
    ṃ_to_ng = ṅ_to_ng.replace("ṃ", "ng")
    ṁ_to_ng = ṃ_to_ng.replace("ṁ", "ng")
    #UPPERCASE
    Ṅ_TO_NG = ṁ_to_ng.replace("Ṅ", "NG")
    Ṃ_TO_NG = Ṅ_TO_NG.replace("Ṃ", "NG")
    Ṁ_TO_NG = Ṃ_TO_NG.replace("Ṁ", "NG")

    if ng_check:
        nasal_ng = ṁ_to_ng
    else:
        nasal_ng = nasal_nñ

    if uppercase_check:
        NASAL_NG = Ṁ_TO_NG
    else:
        NASAL_NG = nasal_ng
    
    # Saṃyoga Consonants
    if samyoga_consonants_check:
        samyoga_ṭ = NASAL_NG.replace("ṭ", "t")
        samyoga_ḍ = samyoga_ṭ.replace("ḍ", "d")
        samyoga_ṇ = samyoga_ḍ.replace("ṇ", "n")
        samyoga_Ṭ = samyoga_ṇ.replace("Ṭ", "T")
        samyoga_Ḍ = samyoga_Ṭ.replace("Ḍ", "D")
        samyoga_Ṇ = samyoga_Ḍ.replace("Ṇ", "N")
        samyoga_bh = samyoga_Ṇ.replace("bh", "ph")
        samyoga_b = samyoga_bh.replace("b", "ph")
        samyoga_dh = samyoga_b.replace("dh", "th")
        samyoga_d = samyoga_dh.replace("d", "th")
        samyoga_gh = samyoga_d.replace("gh", "kh")
        samyoga_g = samyoga_gh.replace("g", "kh")
        samyoga_jh = samyoga_g.replace("jh", "ch")
        samyoga_j = samyoga_jh.replace("j", "ch")
        samyoga_ñ = samyoga_j.replace("ñ", "y")
        samyoga_Bh = samyoga_ñ.replace("Bh", "Ph")
        samyoga_B = samyoga_Bh.replace("B", "Ph")
        samyoga_Dh = samyoga_B.replace("Dh", "Th")
        samyoga_D = samyoga_Dh.replace("D", "Th")
        samyoga_Gh = samyoga_D.replace("Gh", "Kh")
        samyoga_G = samyoga_Gh.replace("G", "Kh")
        samyoga_Jh = samyoga_G.replace("Jh", "Ch")
        samyoga_J = samyoga_Jh.replace("J", "Ch")
        samyoga_Ñ = samyoga_J.replace("Ñ", "Y")
        samyoga_BH = samyoga_Ñ.replace("BH", "PH")
        samyoga_DH = samyoga_BH.replace("DH", "TH")
        samyoga_GH = samyoga_DH.replace("GH", "KH")
        samyoga_JH = samyoga_GH.replace("JH", "CH")
        samyoga_bH = samyoga_JH.replace("bH", "pH")
        samyoga_dH = samyoga_bH.replace("dH", "tH")
        samyoga_gH = samyoga_dH.replace("gH", "kH")
        samyoga_jH = samyoga_gH.replace("jH", "cH")
    else:
        samyoga_jH = NASAL_NG    

    if insert_text[:2] == "ñh":
        first_letters = samyoga_jH.replace("ñ"+sepa+"h", "ñ"+"h", 1)
    elif insert_text[:2] == "ñH":
        first_letters = samyoga_jH.replace("ñ"+sepa+"H", "ñ"+"H", 1)
    elif insert_text[:2] == "ÑH":
        first_letters = samyoga_jH.replace("Ñ"+sepa+"H", "Ñ"+"H", 1)
    elif insert_text[:2] == "ṇh":
        first_letters = samyoga_jH.replace("ṇ"+sepa+"h", "ṇ"+"h", 1)
    elif insert_text[:2] == "ṇH":
        first_letters = samyoga_jH.replace("ṇ"+sepa+"H", "ṇ"+"H", 1)
    elif insert_text[:2] == "ṆH":
        first_letters = samyoga_jH.replace("Ṇ"+sepa+"H", "Ṇ"+"H", 1)
    elif insert_text[:2] == "nh":
        first_letters = samyoga_jH.replace("n"+sepa+"h", "n"+"h", 1)
    elif insert_text[:2] == "nH":
        first_letters = samyoga_jH.replace("n"+sepa+"H", "n"+"H", 1)
    elif insert_text[:2] == "NH":
        first_letters = samyoga_jH.replace("N"+sepa+"H", "N"+"H", 1)
    elif insert_text[:2] == "mh":
        first_letters = samyoga_jH.replace("m"+sepa+"h", "m"+"h", 1)
    elif insert_text[:2] == "mH":
        first_letters = samyoga_jH.replace("m"+sepa+"H", "m"+"H", 1)
    elif insert_text[:2] == "MH":
        first_letters = samyoga_jH.replace("M"+sepa+"H", "M"+"H", 1)
    elif insert_text[:2] == "yh":
        first_letters = samyoga_jH.replace("y"+sepa+"h", "y"+"h", 1)
    elif insert_text[:2] == "yH":
        first_letters = samyoga_jH.replace("y"+sepa+"H", "y"+"H", 1)
    elif insert_text[:2] == "YH":
        first_letters = samyoga_jH.replace("Y"+sepa+"H", "Y"+"H", 1)
    elif insert_text[:2] == "ḷh":
        first_letters = samyoga_jH.replace("ḷ"+sepa+"h", "ḷ"+"h", 1)
    elif insert_text[:2] == "ḷH":
        first_letters = samyoga_jH.replace("ḷ"+sepa+"H", "ḷ"+"H", 1)
    elif insert_text[:2] == "ḶH":
        first_letters = samyoga_jH.replace("Ḷ"+sepa+"H", "Ḷ"+"H", 1)
    elif insert_text[:2] == "lh":
        first_letters = samyoga_jH.replace("l"+sepa+"h", "l"+"h", 1)
    elif insert_text[:2] == "lH":
        first_letters = samyoga_jH.replace("l"+sepa+"H", "l"+"H", 1)
    elif insert_text[:2] == "LH":
        first_letters = samyoga_jH.replace("L"+sepa+"H", "L"+"H", 1)
    elif insert_text[:2] == "vh":
        first_letters = samyoga_jH.replace("v"+sepa+"h", "v"+"h", 1)
    elif insert_text[:2] == "vH":
        first_letters = samyoga_jH.replace("v"+sepa+"H", "v"+"H", 1)
    elif insert_text[:2] == "VH":
        first_letters = samyoga_jH.replace("V"+sepa+"H", "V"+"H", 1)

    elif insert_text[:2] == "tv":
        first_letters = samyoga_jH.replace("t"+sepa+"v", "t"+"v", 1)
    elif insert_text[:2] == "tV":
        first_letters = samyoga_jH.replace("t"+sepa+"V", "t"+"V", 1)
    elif insert_text[:2] == "TV":
        first_letters = samyoga_jH.replace("T"+sepa+"V", "T"+"V", 1)
    elif insert_text[:2] == "dv":
        first_letters = samyoga_jH.replace("d"+sepa+"v", "d"+"v", 1)
    elif insert_text[:2] == "dV":
        first_letters = samyoga_jH.replace("d"+sepa+"V", "d"+"V", 1)
    elif insert_text[:2] == "DV":
        first_letters = samyoga_jH.replace("D"+sepa+"V", "D"+"V", 1)
    elif insert_text[:2] == "yv":
        first_letters = samyoga_jH.replace("y"+sepa+"v", "y"+"v", 1)
    elif insert_text[:2] == "yV":
        first_letters = samyoga_jH.replace("y"+sepa+"V", "y"+"V", 1)
    elif insert_text[:2] == "YV":
        first_letters = samyoga_jH.replace("Y"+sepa+"V", "Y"+"V", 1)
    elif insert_text[:2] == "sv":
        first_letters = samyoga_jH.replace("s"+sepa+"v", "s"+"v", 1)
    elif insert_text[:2] == "sV":
        first_letters = samyoga_jH.replace("s"+sepa+"V", "s"+"V", 1)
    elif insert_text[:2] == "SV":
        first_letters = samyoga_jH.replace("S"+sepa+"V", "S"+"V", 1)

    elif insert_text[:2] == "ky":
        first_letters = samyoga_jH.replace("k"+sepa+"y", "k"+"y", 1)
    elif insert_text[:2] == "kY":
        first_letters = samyoga_jH.replace("k"+sepa+"Y", "k"+"Y", 1)
    elif insert_text[:2] == "KY":
        first_letters = samyoga_jH.replace("K"+sepa+"Y", "K"+"Y", 1)    
    elif insert_text[:2] == "ly":
        first_letters = samyoga_jH.replace("l"+sepa+"y", "l"+"y", 1)
    elif insert_text[:2] == "lY":
        first_letters = samyoga_jH.replace("l"+sepa+"Y", "l"+"Y", 1)
    elif insert_text[:2] == "LY":
        first_letters = samyoga_jH.replace("L"+sepa+"Y", "L"+"Y", 1)
    elif insert_text[:2] == "my":
        first_letters = samyoga_jH.replace("m"+sepa+"y", "m"+"y", 1)
    elif insert_text[:2] == "mY":
        first_letters = samyoga_jH.replace("m"+sepa+"Y", "m"+"Y", 1)
    elif insert_text[:2] == "MY":
        first_letters = samyoga_jH.replace("M"+sepa+"Y", "M"+"Y", 1)
    elif insert_text[:2] == "vy":
        first_letters = samyoga_jH.replace("v"+sepa+"y", "v"+"y", 1)
    elif insert_text[:2] == "vY":
        first_letters = samyoga_jH.replace("v"+sepa+"Y", "v"+"Y", 1)
    elif insert_text[:2] == "VY":
        first_letters = samyoga_jH.replace("V"+sepa+"Y", "V"+"Y", 1)
    elif insert_text[:2] == "ty":
        first_letters = samyoga_jH.replace("t"+sepa+"y", "t"+"y", 1)
    elif insert_text[:2] == "tY":
        first_letters = samyoga_jH.replace("t"+sepa+"Y", "t"+"Y", 1)
    elif insert_text[:2] == "TY":
        first_letters = samyoga_jH.replace("T"+sepa+"Y", "T"+"Y", 1)
    elif insert_text[:2] == "dy":
        first_letters = samyoga_jH.replace("d"+sepa+"y", "d"+"y", 1)
    elif insert_text[:2] == "dY":
        first_letters = samyoga_jH.replace("d"+sepa+"Y", "d"+"Y", 1)
    elif insert_text[:2] == "DY":
        first_letters = samyoga_jH.replace("D"+sepa+"Y", "D"+"Y", 1)
    elif insert_text[:2] == "yy":
        first_letters = samyoga_jH.replace("y"+sepa+"y", "y"+"y", 1)
    elif insert_text[:2] == "yY":
        first_letters = samyoga_jH.replace("y"+sepa+"Y", "y"+"Y", 1)
    elif insert_text[:2] == "YY":
        first_letters = samyoga_jH.replace("Y"+sepa+"Y", "Y"+"Y", 1)

    elif insert_text[:2] == "hm":
        first_letters = samyoga_jH.replace("h"+sepa+"m", "h"+"m", 1)
    elif insert_text[:2] == "hM":
        first_letters = samyoga_jH.replace("h"+sepa+"M", "h"+"M", 1)
    elif insert_text[:2] == "HM":
        first_letters = samyoga_jH.replace("H"+sepa+"M", "H"+"M", 1)
    elif insert_text[:2] == "sm":
        first_letters = samyoga_jH.replace("s"+sepa+"m", "s"+"m", 1)
    elif insert_text[:2] == "sM":
        first_letters = samyoga_jH.replace("s"+sepa+"M", "s"+"M", 1)
    elif insert_text[:2] == "SM":
        first_letters = samyoga_jH.replace("S"+sepa+"M", "S"+"M", 1)
    
    elif insert_text[:2] == "ll":
        first_letters = samyoga_jH.replace("l"+sepa+"l", "l"+"l", 1)
    elif insert_text[:2] == "lL":
        first_letters = samyoga_jH.replace("l"+sepa+"L", "l"+"L", 1)
    elif insert_text[:2] == "LL":
        first_letters = samyoga_jH.replace("L"+sepa+"L", "L"+"L", 1)

    elif insert_text[:2] == "ms":
        first_letters = samyoga_jH.replace("m"+sepa+"s", "m"+"s", 1)
    elif insert_text[:2] == "mS":
        first_letters = samyoga_jH.replace("m"+sepa+"S", "m"+"S", 1)
    elif insert_text[:2] == "MS":
        first_letters = samyoga_jH.replace("M"+sepa+"S", "M"+"S", 1)
    elif insert_text[:2] == "ss":
        first_letters = samyoga_jH.replace("s"+sepa+"s", "s"+"s", 1)
    elif insert_text[:2] == "sS":
        first_letters = samyoga_jH.replace("s"+sepa+"S", "s"+"S", 1)
    elif insert_text[:2] == "SS":
        first_letters = samyoga_jH.replace("S"+sepa+"S", "S"+"S", 1)

    else:
        first_letters = samyoga_jH


    if show_unsplit:
        input_lines = insert_text.split('\n')
        output_lines = first_letters.split('\n')
        for i in range(len(input_lines)):
            unsplit_OR_split = input_lines[i]+'\n'+'\n'+output_lines[i]+'\n'
            st.write(unsplit_OR_split)
    else:
        unsplit_OR_split = first_letters
        st.write(unsplit_OR_split)
      
animation_demo()

st.divider()

st.markdown("<h6 style='text-align: center;'>How does it work?</h6>", unsafe_allow_html=True)
st.markdown("<p>It works by adding breaks or visual spacers after <em>every heavy syllable</em> (garu akkhara). The visual spacers act as temporal punctuations or juncture signs. You would then read the split text by dragging every syllable that is followed by a juncture sign.</p>", unsafe_allow_html=True)

st.markdown("<h6 style='text-align: center;'>What is a heavy syllable?</h6>", unsafe_allow_html=True)
st.markdown("<p>Syllables in Pāḷi are classified as <em>heavy</em> (garu) or <em>light</em> (lahu), whereas vowels are classified as either <em>long</em> (dīgha) or <em>short</em> (rassa). A syllable is heavy if the vowel is long, or followed by a consonant cluster (conjunct/double consonant), or an anusvāra/niggahīta (ṃ/ṁ). On the other hand, a syllable is light if it contains a short vowel [a, i, u] not followed by a consonant cluster or an anusvāra/niggahīta.</p>", unsafe_allow_html=True)

st.markdown("<h6 style='text-align: center;'>Long vowels:</h6>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>• [ā, ī, ū, e, o]</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>• [a, i, u] + ṃ</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>• [a, i, u] + Consonant + Consonant</p>", unsafe_allow_html=True)

st.markdown("<h6 style='text-align: center;'>Short vowels:</h6>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>[a, i, u] + Consonant + Vowel</p>", unsafe_allow_html=True)

#"""
#**Pāḷi Phonology**

#**Regional Variances**

#**Useful Links** \n
#Pāḷi Text Juncture Splitter Website \n
#View & download Parittā of the latest version with juncture signs:  \n
#Pāḷi Text Syllable Splitter: \n
#Pāḷi IPA pronunciation Generator: \n
#Pāḷi Scripts Converter (Roman, Brahmi, Sinhalese, Khom Thai, Thai, Khmer, and more): [Aksharamukha](https://aksharamukha.appspot.com/converter): Indic script converter by Vinodh Rajan\n
#Introduction to Pāḷi (pdf) \n
#Pāḷi Study & Parittā Chanting Forum (Discord) \n
#(YouTube Playlist) Pāḷi Pronunciation Guide \n

#**Roadmap**
#Give suggestions form \n
#Copy to clipboard button \n
#Download text \n
#Line by line conversion \n
#Indonesian page \n

#**References**

st.divider()

st.markdown("<p>We are looking for ways to improve this web tool. If you have any suggestions or ideas, please share them with us at samaneracalvin@gmail.com.</p>", unsafe_allow_html=True)
st.markdown("<p><em>This is an online, open-source and free website app for anyone to use, duplicate, distribute, edit and build upon in any medium or format.</em></p>", unsafe_allow_html=True)

st.divider()

"""
**Keywords:** \n
Pāḷi text heavy syllable separator, syllabification, syllabication, stressed syllable fragmentizer, syllable breaks visualizer, emphasized syllable, closed syllable, open syllable, long vowel, short vowel, double consonant, tempo, duration, pacer, easy chanting
"""

st.sidebar.divider()
show_app_code = st.sidebar.checkbox (label='Show app code')

if show_app_code:
    show_code(animation_demo)

st.sidebar.markdown("tessttett")

st.sidebar.markdown('View [GitHub repository](https://github.com/PaliJunctureSeparator/Pali-Juncture-Splitter.git)')
