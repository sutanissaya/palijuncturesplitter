 "ly":
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
    # Replace 'v' with 'w' if preceded by a consonant in the same syllable
    # Frankfurter, O. (1883). Handbook of Pali. United Kingdom: Williams and Norgate. Retrieved from https://www.google.com/books/edition/Handbook_of_Pali/O7wOAAAAQAAJ?kptab=overview  
    if v_w_select == "if preceded by a consonant in the same syllable, 'v' → 'w'":
        tv_to_tw = first_letters.replace("tv", "tw")
        Tv_to_Tw = tv_to_tw.replace("Tv", "Tw")
        tV_to_tW = Tv_to_Tw.replace("tV", "tW") 
        TV_to_TW = tV_to_tW.replace("TV", "TW")
    
        dv_to_dw = TV_to_TW.replace("dv", "dw")
        Dv_to_Dw = dv_to_dw.replace("Dv", "Dw")
        dV_to_dW = Dv_to_Dw.replace("dV", "dW") 
        DV_to_DW = dV_to_dW.replace("DV", "DW")
    
        yv_to_yw = DV_to_DW.replace("yv", "yw")
        Yv_to_Yw = yv_to_yw.replace("Yv", "Yw")
        yV_to_yW = Yv_to_Yw.replace("yV", "yW") 
        YV_to_YW = yV_to_yW.replace("YV", "YW")
    
        sv_to_sw = YV_to_YW.replace("sv", "sw")
        Sv_to_Sw = sv_to_sw.replace("Sv", "Sw")
        sV_to_sW = Sv_to_Sw.replace("sV", "sW") 
        SV_to_SW = sV_to_sW.replace("SV", "SW")
        v_or_w = SV_to_SW
    else:
     
        # Replace 'v' with 'w'
        if v_w_select == "all 'v' → 'w'":
            all_v_to_w = first_letters.replace("v", "w")
            all_V_to_W = all_v_to_w.replace("V", "W")
            v_or_w = all_V_to_W
        else:
    
            # Replace 'w' with 'v'
            if v_w_select == "all 'w' → 'v'":    
                all_w_to_v = first_letters.replace("w", "v")
                all_W_to_V = all_w_to_v.replace("W", "V")    
                v_or_w = all_W_to_V
            else:
                v_or_w = first_letters
    # Extra juncture sign after a comma ",", a period ".", semi-colon";", colon ":", or a line break / double space / enter (char(10) or \n)
    comma_sepa = v_or_w.replace(",", ","+sepa)
    fix_comma_sepa = comma_sepa.replace(","+sepa+sepa+sepa, ","+sepa+sepa)
    period_sepa = fix_comma_sepa.replace(".", "."+sepa)
    fix_period_sepa = period_sepa.replace("."+sepa+sepa+sepa, "."+sepa+sepa)
    scolon_sepa = fix_period_sepa.replace(";", ";"+sepa)
    fix_scolon_sepa = scolon_sepa.replace(";"+sepa+sepa+sepa, ";"+sepa+sepa)
    colon_sepa = fix_scolon_sepa.replace(":", ":"+sepa)
    fix_colon_sepa = colon_sepa.replace(":"+sepa+sepa+sepa, ":"+sepa+sepa)
    a_sepa = fix_colon_sepa.replace("a"+sepa+"  ", "a"+sepa+sepa+"  ")
    i_sepa = a_sepa.replace("i"+sepa+"  ", "i"+sepa+sepa+"  ")
    u_sepa = i_sepa.replace("u"+sepa+"  ", "u"+sepa+sepa+"  ")
    e_sepa = u_sepa.replace("e"+sepa+"  ", "e"+sepa+sepa+"  ")
    o_sepa = e_sepa.replace("o"+sepa+"  ", "o"+sepa+sepa+"  ")
    ā_sepa = o_sepa.replace("ā"+sepa+"  ", "ā"+sepa+sepa+"  ")
    ī_sepa = ā_sepa.replace("ī"+sepa+"  ", "ī"+sepa+sepa+"  ")
    ū_sepa = ī_sepa.replace("ū"+sepa+"  ", "ū"+sepa+sepa+"  ")
    ṃ_sepa = ū_sepa.replace("ṃ"+sepa+"  ", "ṃ"+sepa+sepa+"  ")
    ṁ_sepa = ṃ_sepa.replace("ṁ"+sepa+"  ", "ṁ"+sepa+sepa+"  ")
    #UPPERCASE
    A_sepa = ṁ_sepa.replace("A"+sepa+"  ", "A"+sepa+sepa+"  ")
    I_sepa = A_sepa.replace("I"+sepa+"  ", "I"+sepa+sepa+"  ")
    U_sepa = I_sepa.replace("U"+sepa+"  ", "U"+sepa+sepa+"  ")
    E_sepa = U_sepa.replace("E"+sepa+"  ", "E"+sepa+sepa+"  ")
    O_sepa = E_sepa.replace("O"+sepa+"  ", "O"+sepa+sepa+"  ")
    Ā_sepa = O_sepa.replace("Ā"+sepa+"  ", "Ā"+sepa+sepa+"  ")
    Ī_sepa = Ā_sepa.replace("Ī"+sepa+"  ", "Ī"+sepa+sepa+"  ")
    Ū_sepa = Ī_sepa.replace("Ū"+sepa+"  ", "Ū"+sepa+sepa+"  ")
    Ṃ_sepa = Ū_sepa.replace("Ṃ"+sepa+"  ", "Ṃ"+sepa+sepa+"  ")
    Ṁ_sepa = Ṃ_sepa.replace("Ṁ"+sepa+"  ", "Ṁ"+sepa+sepa+"  ")
    if uppercase_check:
        ṁ_sepa_or_Ṁ_sepa = Ṁ_sepa
    else:
        ṁ_sepa_or_Ṁ_sepa = ṁ_sepa
    # Saṃyoga chanting style - Pauses
    if samyoga_pauses_check:
        saṃyoga_or_not = v_or_w
    else:
        saṃyoga_or_not = ṁ_sepa_or_Ṁ_sepa
 
    # Show Unsplit Line by Line
    if show_unsplit:
        input_lines = insert_text.split('\n')
        output_lines = saṃyoga_or_not.split('\n')
        for i in range(len(input_lines)):
            unsplit_OR_split = input_lines[i]+'\n'+'\n'+output_lines[i]+'\n'
            st.write(unsplit_OR_split)
    else:
        unsplit_OR_split = saṃyoga_or_not
        st.write(unsplit_OR_split)
      
animation_demo()
st.divider()
st.markdown("<h6 style='text-align: center;'>Browse Pāḷi text to split:</h6>", unsafe_allow_html=True)
st.markdown('<p>• <a href="https://tipitaka.app/"><strong>Chaṭṭha Saṅgāyanā Tipiṭaka</strong></a>, Vipassana Research Institute (VRI), 1956, license: <a href="https://creativecommons.org/licenses/by-nc-nd/3.0/">CC BY-NC-ND 3.0 Deed</a>.</p>', unsafe_allow_html=True)
st.markdown('<p>• <a href="https://tipitaka.app/"><strong>Tipiṭaka—the Three Baskets of the Buddhist Canon</strong></a>, SuttaCentral, license: <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0 Deed</a>.</p>', unsafe_allow_html=True)
st.markdown('<p>• <a href="https://bhikkhu-manual.github.io/essential-chants.html"><strong>Bhikkhu Manual: Essential Chants</strong></a>, Amaravati Publications, 2020, license: <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/">CC BY-NC-ND 4.0 Deed</a>.</p>', unsafe_allow_html=True)
st.divider()
st.markdown("<h6 style='text-align: center;'>How does it work?</h6>", unsafe_allow_html=True)
st.markdown("<p>It works by adding breaks or visual spacers after <em>every heavy syllable</em> (garu akkhara). The visual spacers act as temporal punctuations or juncture signs. The split text would then be read by dragging every syllable that is followed by a juncture sign.</p>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>What is a heavy syllable?</h6>", unsafe_allow_html=True)
st.markdown("<p>Syllables in Pāḷi are classified as <em>heavy</em> (garu) or <em>light</em> (lahu), whereas vowels are classified as either <em>long</em> (dīgha) or <em>short</em> (rassa). A syllable is heavy if i.) the vowel is long, ii.) followed by an anusvāra/niggahīta (ṃ/ṁ), or iii.) followed by a consonant cluster (conjunct/double consonant). On the other hand, a syllable is light if it contains a short vowel [a, i, u] not followed by a consonant cluster or an anusvāra/niggahīta.</p>", unsafe_allow_html=True)
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
#Pages in other languages \n
#**References**
st.divider()
st.markdown('<p>We are looking for ways to improve this web tool. If you have any suggestions or ideas, please share them with us via <a href="mailto:sutanissaya@gmail.com">email</a>.</p>', unsafe_allow_html=True)
st.markdown('<p><em>This web tool is licensed under <a href="https://github.com/sutanissaya/palijuncturesplitter/blob/main/LICENSE">CC0-1.0 Universal</a>.  Anyone may build upon, modify, incorporate in other works, reuse and redistribute as freely as possible in any form whatsoever and for any purposes, including without limitation commercial purposes.</em></p>', unsafe_allow_html=True)
st.divider()
"""
**Keywords:** \n
Pāḷi text heavy syllable separator, syllabification, syllabication, stressed syllable fragmentizer, syllable breaks visualizer, emphasized syllable, closed syllable, open syllable, long vowel, short vowel, double consonant, tempo, duration, pacer, easy chanting
"""
st.sidebar.divider()
show_app_code = st.sidebar.checkbox (label='Show app code')
if show_app_code:
    show_code(animation_demo)
st.sidebar.markdown('View [GitHub repository](https://github.com/sutanissaya/palijuncturesplitter.git)')
st.sidebar.markdown('Read [CC0-1.0 License](https://github.com/sutanissaya/palijuncturesplitter/blob/main/LICENSE)')
