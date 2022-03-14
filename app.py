import streamlit as st
import pandas as pd
import plotly.express as px
from fuzzywuzzy import fuzz

def main():
    st.markdown("""
<style>
.big-font {
    font-size:30px !important;
}
</style>
""", unsafe_allow_html=True)
    st.markdown('<p class="big-font">Medicare and Medicaid Spending: 2012-2020</p>', unsafe_allow_html=True)


    med_df = pd.read_csv('data/cleaned.csv', header=0, index_col=0)     
    drug_info = pd.read_csv('data/drug_info.csv', header=0, index_col=0)
    med_df.sort_values('year', inplace=True)
    fig = px.scatter(med_df[med_df['coverage_type']=='medicaid'], x = "Total Dosage Units", y = "Total Spending", hover_name='Brand Name', facet_col='year', facet_col_wrap=3)

    st.write(med_df.head())

    st.plotly_chart(fig)
    
    selection = st.selectbox("Brand Name or Generic", ("Brand", "Generic"))
    text = st.text_area("Select a Drug Name")
    

    results = {}
    for i, name in enumerate(drug_info[selection]):
        if fuzz.partial_ratio(text, name) > 75:
            results[name] = i

    drug_name = st.selectbox("Pick the drug you'd like info about:", results.keys())
    
    st.write(drug_info[drug_info[selection]==drug_name].T)

if __name__ == "__main__":
    main()
