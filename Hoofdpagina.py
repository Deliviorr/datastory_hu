import pandas as pd
import streamlit as st
import pycountry_convert as pc
import altair as alt

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
De data laten een verontrustend patroon zien: studenten die dagelijks tot wel zeven uur op sociale media doorbrengen, scoren aanzienlijk lager op mentale gezondheid dan leeftijdsgenoten die minder tijd online besteden. Deze bevinding sluit aan bij internationale studies waarin langdurig socialemediagebruik wordt gekoppeld aan hogere niveaus van angst, depressie en stresssymptomen.<sup><a href="#voetnoot1">1</a></sup> Het ogenschijnlijk onschuldige scrollen blijkt vaak een bron van constante vergelijking, FOMO (fear of missing out) en cognitieve overbelasting.<sup><a href="#voetnoot2">2</a></sup>
""", unsafe_allow_html=True)

st.markdown("""
Een studie onder universiteitsstudenten toont aan dat de mate van socialmediagebruik significant samenhangt met scores op depressie- en angstschalen.<sup><a href="#voetnoot3">3</a></sup> Ook blijkt dat jongeren die sociale media als essentieel onderdeel van hun identiteit zien, kwetsbaarder zijn voor negatieve emoties wanneer ze geen toegang hebben tot hun accounts.<sup><a href="#voetnoot4">4</a></sup>
""", unsafe_allow_html=True)

# 4de alinea
st.subheader("Visualisatie A: Mentale gezondheid tegenover dagelijks gebruik van sociale media")
st.write('De data laat een alarmerend patroon zien: studenten die dagelijks tot wel 7 uur op sociale media zitten, scoren opvallend lager op mentale gezondheid dan hun leeftijdsgenoten die minder tijd online besteden. Scrollen op sociale media lijkt in eerste instantie onschuldig, maar kan doorgroeien tot grotere mentale problemen. ')
avg_data1 = data.groupby("Mental_Health_Score", as_index=False)["Avg_Daily_Usage_Hours"].mean()

def get_color(score):
    if score <= 5:
        return '#f63366'
    elif score <= 7:
        return '#ff884d'
    else:
        return '#33f6b0'


avg_data1['kleur'] = avg_data1['Mental_Health_Score'].apply(get_color)

chart = (
    alt.Chart(avg_data1)
    .mark_bar()
    .encode(
        x=alt.X("Mental_Health_Score:O", title="Mentale Gezondheidsscore"),
        y=alt.Y("Avg_Daily_Usage_Hours:Q", title="Gemiddelde dagelijkse schermtijd (uren)"),
        color=alt.Color("kleur:N", scale=None)  
    )
    .properties(width=600, height=400)
)
st.altair_chart(chart, use_container_width=True)

st.write('_Visualisatie A: mentale gezondheid tegenover sociale media gebruik_')

# 5de alinea
st.header("Sociale media en slaap")

st.markdown("""
Niet alleen de geest, ook het lichaam lijdt onder overmatig schermgebruik. Studenten die urenlang blijven scrollen, stelen letterlijk slaap van zichzelf. Chronisch slaaptekort door laat-nachtelijk gebruik verhoogt het risico op stress, angst en depressieve klachten.<sup><a href="#voetnoot5">5</a></sup> Studies tonen aan dat schermtijd, vooral vlak voor het slapengaan, de slaapkwaliteit verlaagt en de inslaaptijd verlengt.<sup><a href="#voetnoot6">6</a></sup>
""", unsafe_allow_html=True)

st.markdown("""
Uit een kwantitatief onderzoek met enquêtes bleek dat het verband tussen sociale mediagebruik en academische betrokkenheid gedeeltelijk wordt bepaald verklaard door slechtere slaapkwaliteit en meer vermoeidheid.<sup><a href="#voetnoot7">7</a></sup> Wanneer slaapduur afneemt, dalen concentratie, motivatie en academische betrokkenheid, met meetbare gevolgen voor cijfers en studiedruk.
""", unsafe_allow_html=True)

# 6de alinea
st.subheader("Visualisatie B: Slaapduur tegenover dagelijks gebruik van sociale media")

st.write('Studenten die urenlang door sociale media scrollen, stelen slaap van zichzelf. Nachten achter elkaar wordt hun lichaam uitgeput. Chronisch slaaptekort door eindeloos scrollen verhoogt het risico op stress, angst en depressie. Een gewoonte dat oorspronkelijk onschuldig lijkt, groeit toch tot een merkwaardige bedreiging voor welzijn.')
data['Sleep_Hours_Per_Night'] = data['Sleep_Hours_Per_Night'].round()

def get_color1(score):
    if score <= 5:
        return '#f63366'
    elif score <= 7:
        return '#ff884d'
    else:
        return '#33f6b0'

avg_data2 = data.groupby("Sleep_Hours_Per_Night", as_index=False)["Avg_Daily_Usage_Hours"].mean()

avg_data2['kleur'] = avg_data2['Sleep_Hours_Per_Night'].apply(get_color1)

chart = (
    alt.Chart(avg_data2)
    .mark_bar()
    .encode(
        x=alt.X("Sleep_Hours_Per_Night:O", title="Slaap duur"),
        y=alt.Y("Avg_Daily_Usage_Hours:Q", title="Gemiddelde dagelijkse schermtijd (uren)"),
        color=alt.Color("kleur:N", scale=None)
    )
)
st.altair_chart(chart, use_container_width=True)

st.write('_Visualisatie B: slaap duratie tegenover sociale media gebruik_')

st.subheader("Visualisatie C: Interactieve tabel")
st.write('Deze interactieve tabel toont hoe gemiddelde schermtijd, mentale gezondheid en academische prestaties')

# Subset en hernoemen
subset = data[['Country', 'Avg_Daily_Usage_Hours', 'Mental_Health_Score', 'Affects_Academic_Performance']]
df = subset.rename(
    columns={
        "Country": "Land",
        "Avg_Daily_Usage_Hours": "Gem. schermtijd (uren/dag)",
        "Mental_Health_Score": "Mentale gezondheidsscore (0–10)",
        "Affects_Academic_Performance": "Beïnvloedt schoolprestaties (%)",
    }
)

# Continent toevoegen
def get_continent(country):
    try:
        country_code = pc.country_name_to_country_alpha2(country, cn_name_format="default")
        continent_code = pc.country_alpha2_to_continent_code(country_code)
        continent_name = {
            "AF": "Afrika",
            "AS": "Azië",
            "EU": "Europa",
            "NA": "Noord-Amerika",
            "OC": "Oceanië",
            "SA": "Zuid-Amerika",
        }.get(continent_code, "Onbekend")
        return continent_name
    except Exception:
        return "Onbekend"

df["Continent"] = df["Land"].apply(get_continent)

# Numerieke kolommen
num_cols = ["Gem. schermtijd (uren/dag)", "Mentale gezondheidsscore (0–10)"]
for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Categorie kolom naar 0/1
df["Yes"] = df["Beïnvloedt schoolprestaties (%)"].astype(str).str.strip().str.lower().apply(lambda x: 1 if x == "yes" else 0)

# Filterlijst
continenten = sorted(df["Continent"].unique())
selectie = st.multiselect("Filter op continent", continenten, default=continenten)

# Filteren
filtered_df = df[df["Continent"].isin(selectie)]

# Groeperen per continent
grouped_df = filtered_df.groupby("Continent", as_index=False).agg({
    "Gem. schermtijd (uren/dag)": "mean",
    "Mentale gezondheidsscore (0–10)": "mean",
    "Yes": "mean"
})

# --- Functies voor kleurregels ---
def kleur_mentale_gezondheid(val):
    if val < 4:
        kleur = '#f63366'   
    elif 4 <= val < 7:
        kleur = '#ff884d'   
    else:
        kleur = '#33f6b0'   
    return f'background-color: {kleur}; color: black;'

def kleur_schermtijd(val):
    if val <= 4:
        kleur = '#33f6b0'   
    elif 5 <= val <= 6:
        kleur = '#ff884d'   
    else:
        kleur = '#f63366'   
    return f'background-color: {kleur}; color: black;'

def kleur_school(val):
    if val > 50:
        kleur = '#f63366'   
    else:
        kleur = '#33f6b0'   
    return f'background-color: {kleur}; color: black;'


# --- Berekeningen en afronden ---
grouped_df.loc[:, ['Mentale gezondheidsscore (0–10)', 'Gem. schermtijd (uren/dag)']] = (
    grouped_df[['Mentale gezondheidsscore (0–10)', 'Gem. schermtijd (uren/dag)']].round()
)

grouped_df["Beïnvloedt schoolprestaties (%)"] = (grouped_df["Yes"] * 100).round(1)
grouped_df = grouped_df.drop(columns="Yes")

# Sorteren op mentale score
grouped_df = grouped_df.sort_values("Mentale gezondheidsscore (0–10)", ascending=False)

# --- Styling toepassen ---
styled_df = (
    grouped_df.style
    .map(kleur_mentale_gezondheid, subset=['Mentale gezondheidsscore (0–10)'])
    .map(kleur_schermtijd, subset=['Gem. schermtijd (uren/dag)'])
    .map(kleur_school, subset=['Beïnvloedt schoolprestaties (%)'])
    .format({
        'Mentale gezondheidsscore (0–10)': "{:.1f}",
        'Gem. schermtijd (uren/dag)': "{:.1f}",
        'Beïnvloedt schoolprestaties (%)': "{:.1f}"
    })
    .set_table_styles([{'selector': 'table', 'props': [('width', '100%')]}]) 
)

# Tabel tonen
st.markdown(
    f'<div style="width:100%; overflow-x:auto;">{styled_df.to_html(escape=False, index=False)}</div>',
    unsafe_allow_html=True
)
st.header("Een groeiende bedreiging voor welzijn")

st.markdown("""
Hoewel sociale media voordelen aanbiedt, zoals sociale verbondenheid, informatie en ontspanning, tonen zowel data als literatuur dat te veel van het goede het welzijn van studenten ernstig kan aantasten. Wereldwijd geeft meer dan één op de tien jongeren aan problematisch socialemediagebruik te vertonen.<sup><a href="#voetnoot8">8</a></sup> En één op de vijf zegt dat sociale media hun mentale gezondheid negatief beïnvloeden.<sup><a href="#voetnoot9">9</a></sup>
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
