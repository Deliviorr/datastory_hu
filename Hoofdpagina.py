import pandas as pd
import streamlit as st

green = "#27AE60"   # herstel
orange = "#F39C12"  # actie

data = pd.read_csv('data/Students.csv')
st.write("# Te veel van het goede: Sociale media en mentale gezondheid")


def intro():
    st.markdown(
        "<p style='font-size:22px;'>Sociale media spelen een grote rol in het leven van een student. Ze bieden verbinding onderling en informatie is makkelijk verkrijgbaar, maar wat zijn de risico’s achter deze sociale media met betrekking tot mentale gezondheid, slaap en schoolprestaties?</p>",
        unsafe_allow_html=True
    )

def grafieken(data):
    st.write('### Sociale media gebruik vs. Mentale gezondheid')
    st.write('De data laat een alarmerend patroon zien: studenten die dagelijks tot wel 7 uur op sociale media zitten, scoren opvallend lager op mentale gezondheid dan hun leeftijdsgenoten die minder tijd online besteden. Scrollen op sociale media lijkt in eerste instantie onschuldig, maar kan doorgroeien tot grotere mentale problemen. ')
    avg_data1 = data.groupby("Mental_Health_Score", as_index=False)["Avg_Daily_Usage_Hours"].mean()
    st.bar_chart(data=avg_data1, x ="Mental_Health_Score", y ="Avg_Daily_Usage_Hours", color=["#f63366"],x_label="Mentale Gezondheidsscore", y_label="Gemiddelde dagelijkse schermtijd (uren)")
    st.write('_Visualisatie A: mentale gezondheid tegenover sociale media gebruik_')

    st.write('###  Sociale media gebruik vs. Slaapduur')
    st.write('Studenten die urenlang door sociale media scrollen, stelen slaap van zichzelf. Nachten achter elkaar wordt hun lichaam uitgeput. Chronisch slaaptekort door eindeloos scrollen verhoogt het risico op stress, angst en depressie. Een gewoonte dat oorspronkelijk onschuldig lijkt, groeit toch tot een merkwaardige bedreiging voor welzijn.')
    data['Sleep_Hours_Per_Night'] = data['Sleep_Hours_Per_Night'].round()
    avg_data2 = data.groupby("Sleep_Hours_Per_Night", as_index=False)["Avg_Daily_Usage_Hours"].mean()
    st.bar_chart(data=avg_data2, x ="Sleep_Hours_Per_Night", y ="Avg_Daily_Usage_Hours", color=["#f63366"],x_label="Slaap duur", y_label="Gemiddelde dagelijkse schermtijd (uren)")
    st.write('_Visualisatie B: slaap duratie tegenover sociale media gebruik_')

intro()
grafieken(data)