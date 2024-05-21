import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.title("*** Covid19 global total cases,deaths and recoverd by each continent analysis ***")

# Upload a .csv file on the website
uploaded_file = st.file_uploader("Upload the csv file", type=["csv"])

if uploaded_file is not None:
    st.success("فایل با موفقیت بارگزاری شده است")

    # Convert csv data to pandas dataframe
    df = pd.read_csv(uploaded_file)
    

    # Show dataframe in a table on the website
    st.header("10 records of global covid19 dataset")
    df_show = df.head(10)
    st.dataframe(df_show)

    # Write some information about your data science app in the website’s sidebar
    with st.sidebar:
        st.header("Information")
        country_num = df['country'].unique()
        st.write(f"This app shows some datas about covid19 cases and deaths in 226 countries around world in 2020 and 2021")
        #st.subheader("Countries are:")
        #st.write(f"{country_num}")


    df = df.dropna()


    # Percentage of continents in dataset
    #st.subheader("Percentage of continents in dataset")
    # by_continents = df.continent.value_counts()
    # st.write(by_continents)
    
    # total_confirmed,total_deaths,total_recovered

    continents = df['continent'].unique()


    total_cases_by_continents = df.groupby('continent')['total_confirmed'].sum().sort_values(ascending = False)
    
    fig, ax= plt.subplots()
    ax.bar(continents,total_cases_by_continents)

    plt.title("Total cases")
    plt.xlabel("Continents")
    plt.ylabel("Total cases by continents")
    st.pyplot(fig)

    total_deaths_by_continents = df.groupby('continent')['total_deaths'].sum().sort_values(ascending = False)

    fig, ax= plt.subplots()
    ax.bar(continents,total_deaths_by_continents )

    plt.title("Total deaths")
    plt.xlabel("Continents")
    plt.ylabel("Total deaths by continents ")
    st.pyplot(fig)
    

    total_recovered_by_continents = df.groupby('continent')['total_recovered'].sum().sort_values(ascending = False)
    fig, ax= plt.subplots()
    ax.bar(continents,total_recovered_by_continents)

    plt.title("Total recovereds")
    plt.xlabel("Continents")
    plt.ylabel("Total recovered by continents ")
    st.pyplot(fig)


else:
    st.warning("هنوز فایلی بارگزاری نشده است")



