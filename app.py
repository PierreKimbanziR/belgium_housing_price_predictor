import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os
import webbrowser

cwd = os.getcwd()  # Get the current working directory (cwd)
model = pickle.load(open(cwd + "/estimator.pkl", "rb"))


data = pd.read_csv(
    "https://raw.githubusercontent.com/SamuelD005/challenge-regression/development/Data8.csv",
    sep=",",
)
x = data.drop(["Price", "PriceperMeter", "Unnamed: 0"], axis=1)
columns = x.columns

st.title("Estimate the price of your property")

st.subheader("A new approach to real-estate prices definition")


def main():
    st.write(
        """
        #### To evaluate the price of your property we will need a few infomations.  
        """
    )
    type_of_property = st.selectbox(
        "What type of property do you want to estimate ? ", ("--", "house", "apartment")
    )
    locality = st.number_input(
        "Please enter the property's postal code.", min_value=1000, max_value=9999
    )
    region = st.selectbox(
        "Select the region of the property", ("Flanders", "Wallonia", "Brussel")
    )
    province = st.selectbox(
        "Select the province of the property",
        options=[
            "------",
            "Flandre Occidental",
            "Flandre Oriental",
            "Hainaut",
            "Brussel",
            "Anvers",
            "Liège",
            "Brabant Flamand",
            "Brabant Wallon",
            "Limbourg",
            "Namur",
            "Luxembourg",
        ],
    )

    area = st.number_input(
        "Enter the size (in m²) of the property.", min_value=0, max_value=1000
    )
    number_of_room = st.select_slider(
        "How many rooms are there in the house ?",
        options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )
    state_of_building = st.select_slider(
        "What is the condition of the property ? ",
        options=["to renovate", "medium", "good", "new"],
    )
    st.write("_____________________________________________________")
    fully_equipped_kitchen = st.selectbox(
        "Is the kitchen fully equipped ?", ["No", "Yes"]
    )
    furnished = st.selectbox("Is the house is sell furnished ?", ["No", "Yes"])
    open_fire = st.selectbox("Does the house have an open fire ?", ["No", "Yes"])
    st.write("_____________________________________________________")

    terrace_area = st.number_input(
        "Enter the size of the terrace (in m²).", min_value=0, max_value=1000
    )
    garden_area = st.number_input(
        "Enter the area of your garden", min_value=0, max_value=100000000
    )
    number_of_facades = st.selectbox("How many facades does the property have ?", [2, 3, 4])
    swimming_pool = st.selectbox("Does the property have a swimming pool ?", ["No", "Yes"])
    surface_of_the_land = area + terrace_area + garden_area

    fully_equipped_kitchen = 1 if fully_equipped_kitchen == "Yes" else 0
    furnished = 1 if furnished == "Yes" else 0
    open_fire = 1 if open_fire == "Yes" else 0
    swimming_pool = 1 if swimming_pool == "Yes" else 0

    df = pd.DataFrame(
        [
            [
                locality,
                type_of_property,
                number_of_room,
                area,
                fully_equipped_kitchen,
                furnished,
                open_fire,
                terrace_area,
                garden_area,
                surface_of_the_land,
                number_of_facades,
                swimming_pool,
                state_of_building,
                province,
                region,
            ]
        ],
        columns=columns,
    )

    side_text = st.sidebar.write(
        """
        ## Get in touch  

        [Find me on Linkedin](https://www.linkedin.com/in/pierre-kimbanzi-ruganda/)  
        [Find me on Github](https://github.com/PierreKimbanziR)  
        [Take a look at the code behind this project](https://github.com/PierreKimbanziR/belgium_housing_price_predictor)


        """

    )

    if st.button("Estimate the property"):
        result = model.predict(df)
        st.success(f"The estimated price of the property is {round(result[0])} euros")


if __name__ == "__main__":
    main()
