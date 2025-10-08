import pandas as pd
import streamlit as st

data = pd.read_csv('data/Students.csv')

st.set_page_config(page_title="Te veel van het goede: Sociale media en mentale gezondheid", layout="centered")

st.title("Te veel van het goede: Sociale media en mentale gezondheid")

# Eerste alinea
st.markdown("""
<style>
.dropcap:first-letter {
    float: left;
    font-size: 4em;
    line-height: 0.8;
    padding-right: 8px;
    padding-top: 4px;
    font-weight: bold;
    color: #f63366; 
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<p class="dropcap">
Sociale media spelen een centrale rol in het leven van studenten. Ze bieden snelle communicatie, sociale verbinding en toegang tot informatie, maar diezelfde voordelen kennen een keerzijde. Steeds meer onderzoek wijst op risico’s van intensief gebruik, met name op het vlak van mentale gezondheid, slaap en schoolprestaties.
</p>
""", unsafe_allow_html=True)

# tweede alinea
st.header("Onderzoek en dataverantwoording") 
st.markdown(""" De onderstaande visualisaties zijn gebaseerd op data uit een online enquête uitgevoerd in het eerste kwartaal van 2025. In totaal namen 700 studenten deel, in de leeftijd van 16 tot 25 jaar, afkomstig uit Bangladesh, India, de Verenigde Staten, het Verenigd Koninkrijk, Canada, Australië, Duitsland, Brazilië, Japan en Zuid-Korea. De vragenlijst onderzocht onder meer dagelijkse schermtijd, slaapduur, mentale gezondheidsscores en studiegewoonten. """)

# derde alinea
st.header("Sociale media en mentale gezondheid")

st.markdown("""
De data laten een verontrustend patroon zien: studenten die dagelijks tot wel zeven uur op sociale media doorbrengen, scoren aanzienlijk lager op mentale gezondheid dan leeftijdsgenoten die minder tijd online besteden. Deze bevinding sluit aan bij internationale studies waarin langdurig socialemediagebruik wordt gekoppeld aan hogere niveaus van angst, depressie en stresssymptomen<sup><a href="#voetnoot1">1</a></sup>. Het ogenschijnlijk onschuldige scrollen blijkt vaak een bron van constante vergelijking, FOMO (fear of missing out) en cognitieve overbelasting<sup><a href="#voetnoot2">2</a></sup>.
""", unsafe_allow_html=True)

st.markdown("""
Een studie onder universiteitsstudenten toont aan dat de mate van socialmediagebruik significant samenhangt met scores op depressie- en angstschalen<sup><a href="#voetnoot3">3</a></sup>. Ook blijkt dat jongeren die sociale media als essentieel onderdeel van hun identiteit zien, kwetsbaarder zijn voor negatieve emoties wanneer ze geen toegang hebben tot hun accounts<sup><a href="#voetnoot4">4</a></sup>.
""", unsafe_allow_html=True)

# 4de alinea
st.subheader("Visualisatie A: Mentale gezondheid tegenover dagelijks gebruik van sociale media")
st.write('De data laat een alarmerend patroon zien: studenten die dagelijks tot wel 7 uur op sociale media zitten, scoren opvallend lager op mentale gezondheid dan hun leeftijdsgenoten die minder tijd online besteden. Scrollen op sociale media lijkt in eerste instantie onschuldig, maar kan doorgroeien tot grotere mentale problemen. ')
avg_data1 = data.groupby("Mental_Health_Score", as_index=False)["Avg_Daily_Usage_Hours"].mean()
st.bar_chart(data=avg_data1, x ="Mental_Health_Score", y ="Avg_Daily_Usage_Hours", color=["#f63366"],x_label="Mentale Gezondheidsscore", y_label="Gemiddelde dagelijkse schermtijd (uren)")
st.write('_Visualisatie A: mentale gezondheid tegenover sociale media gebruik_')

# 5de alinea
st.header("Sociale media en slaap")

st.markdown("""
Niet alleen de geest, ook het lichaam lijdt onder overmatig schermgebruik. Studenten die urenlang blijven scrollen, stelen letterlijk slaap van zichzelf. Chronisch slaaptekort door laat-nachtelijk gebruik verhoogt het risico op stress, angst en depressieve klachten<sup><a href="#voetnoot5">5</a></sup>. Studies tonen aan dat schermtijd, vooral vlak voor het slapengaan, de slaapkwaliteit verlaagt en de inslaaptijd verlengt<sup><a href="#voetnoot6">6</a></sup>.
""", unsafe_allow_html=True)

st.markdown("""
Uit een kwantitatief onderzoek met enquêtes bleek dat het verband tussen sociale mediagebruik en academische betrokkenheid gedeeltelijk wordt bepaald verklaard door slechtere slaapkwaliteit en meer vermoeidheid<sup><a href="#voetnoot7">7</a></sup>. Wanneer slaapduur afneemt, dalen concentratie, motivatie en academische betrokkenheid — met meetbare gevolgen voor cijfers en studiedruk.
""", unsafe_allow_html=True)

# 6de alinea
st.subheader("Visualisatie B: Slaapduur tegenover dagelijks gebruik van sociale media")

st.write('Studenten die urenlang door sociale media scrollen, stelen slaap van zichzelf. Nachten achter elkaar wordt hun lichaam uitgeput. Chronisch slaaptekort door eindeloos scrollen verhoogt het risico op stress, angst en depressie. Een gewoonte dat oorspronkelijk onschuldig lijkt, groeit toch tot een merkwaardige bedreiging voor welzijn.')
data['Sleep_Hours_Per_Night'] = data['Sleep_Hours_Per_Night'].round()
avg_data2 = data.groupby("Sleep_Hours_Per_Night", as_index=False)["Avg_Daily_Usage_Hours"].mean()
st.bar_chart(data=avg_data2, x ="Sleep_Hours_Per_Night", y ="Avg_Daily_Usage_Hours", color=["#f63366"],x_label="Slaap duur", y_label="Gemiddelde dagelijkse schermtijd (uren)")
st.write('_Visualisatie B: slaap duratie tegenover sociale media gebruik_')

st.header("Een groeiende bedreiging voor welzijn")

st.markdown("""
Hoewel sociale media voordelen aanbiedt, zoals sociale verbondenheid, informatie en ontspanning, tonen zowel data als literatuur dat te veel van het goede het welzijn van studenten ernstig kan aantasten. Wereldwijd geeft meer dan één op de tien jongeren aan problematisch socialemediagebruik te vertonen<sup><a href="#voetnoot8">8</a></sup>. En één op de vijf zegt dat sociale media hun mentale gezondheid negatief beïnvloeden<sup><a href="#voetnoot9">9</a></sup>.
""", unsafe_allow_html=True)

st.markdown("""
De uitdaging ligt dus niet in het volledig vermijden van sociale media, maar in het herstellen van balans. Een gezonde digitale leefstijl met bewust gebruik, vaste schermvrije momenten en meer belang voor slaap blijkt een krachtig middel om gezondheid en studieprestaties te beschermen.
""")

st.divider()

st.subheader("Voetnoten")
st.markdown("""
<ol>
<li id="voetnoot1">BMC Psychiatry (2023). <i>Social media and mental health in students: a cross-sectional study.</i></li>
<li id="voetnoot2">Pew Research Center (2025). <i>Teens, Social Media and Mental Health.</i></li>
<li id="voetnoot3">PMC (2024). <i>The Impact of Social Media on the Mental Health of Adolescents and Young Adults.</i></li>
<li id="voetnoot4">WHO Europe (2024). <i>Teens, screens and mental health.</i></li>
<li id="voetnoot5">PMC (2021). <i>Social Media Use and Sleep Disturbance among Adolescents.</i></li>
<li id="voetnoot6">PMC (2025). <i>The Impact of Social Media Use on Sleep and Mental Health in Youth.</i></li>
<li id="voetnoot7">Frontiers in Education (2025). <i>Social media addiction and academic engagement: the role of sleep.</i></li>
<li id="voetnoot8">WHO Europe (2024). <i>Teens, screens and mental health.</i></li>
<li id="voetnoot9">Pew Research Center (2025). <i>Teens, Social Media and Mental Health.</i></li>
</ol>
""", unsafe_allow_html=True)

