import streamlit as st
import pandas as pd
import plotly_express as px

st.write("Olympics Medal Counts")

olympics_df = pd.read_csv('https://raw.githubusercontent.com/josephplpriest/streamlit_olympics/main/olympics_cleaned.csv')
olympics_df = olympics_df.drop(olympics_df.columns[0], axis=1)

season = st.sidebar.selectbox('Summer or Winter Olympics', ("Summer", "Winter"))

years = olympics_df[olympics_df['season'] == season].drop_duplicates()

year_possibilities = years['year'].unique()

start_year, end_year = st.sidebar.select_slider("Select a range of years", options = year_possibilities,
                                                value=(int(year_possibilities[0]), int(year_possibilities[-1])))

chart_type = st.sidebar.selectbox('Visualization type', ("Bar chart", "Line plot", "Histogram"))




if chart_type == "Bar chart":
    plot_df = olympics_df[(olympics_df['year'] >= int(start_year))
                          & (olympics_df['year'] <= int(end_year))
                          & (olympics_df['season'] == season)
                          & (olympics_df['Total'] >= 10)]
    if start_year == end_year:
        st.write(f"Host Country: {plot_df['host_country'].unique()[0]}")
    fig = px.bar(plot_df, x="Nation", y=["Bronze", "Silver", "Gold"],
             color_discrete_sequence=['brown', 'grey', 'yellow'],
             labels={"value": "Medals", "variable": "Medal type"})
    st.plotly_chart(fig)

    st.write("For readability, countries with medal totals of < 10 are ignored")

elif chart_type == "Line plot":
    plot_df = olympics_df[(olympics_df['year'] >= int(start_year))
                          & (olympics_df['year'] <= int(end_year))
                          & (olympics_df['season'] == season)
                          & (olympics_df['Total'] >= 10)]
    medals_to_plot = st.sidebar.selectbox("Medals:", ("Total", "Gold", "Silver", "Bronze"))
    fig = px.line(plot_df, x='year', y=medals_to_plot, color='Nation')

    st.plotly_chart(fig)

    st.write("For readability, countries with medal totals of < 10 are ignored")


else:
    #histogram
    plot_df = olympics_df[(olympics_df['year'] >= int(start_year))
                          & (olympics_df['year'] <= int(end_year))
                          & (olympics_df['season'] == season)]
    country = st.sidebar.radio(label="Pick a country", options=list(plot_df['Nation'].unique()))
    st.title(f"Medal Counts for {country}")
    fig = px.bar(plot_df[plot_df['Nation'] == country], x='year', y='Total')
    fig.update_layout(
        xaxis= dict(tickmode='linear',
                    tick0=start_year,
                    dtick=4)
        )
    st.plotly_chart(fig)

st.write("Note: Due to WWII, the olympics in 1940 and 1944 were cancelled.\n"
         "During the Cold War, the US boycotted the 1980 games while the USSR boycotted the 1984 games.")
#%%
