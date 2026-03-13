import joblib
import streamlit as st



model=joblib.load("vechile.joblib")
 
st.title("vechile price prediction")

year=st.number_input("manufacturing year",min_value=0)
present_price = st.number_input("Purchesing Price (in Lakhs)", min_value=0.0)
kms_driven = st.number_input("Kilometers Driven", min_value=0)
owner = st.selectbox("Owner Type", [0,1,2,3])

# fuel_type = st.selectbox("Fuel Type", ["Petrol","Diesel"])
# seller_type = st.selectbox("Seller Type", ["Individual","Dealer"])
# transmission = st.selectbox("Transmission", ["Manual","Automatic"])
# car_age = st.number_input("Car Age (years)", min_value=0)

if st.button("Predict Price"):
    result=model.predict([[year,present_price,kms_driven,owner]])
    print(f"predicted car price is : {result}")

    # st.success.success(f"Ridge Regression Prediction: {result}₹  Lakhs")
    st.success(f"Ridge Regression Prediction:{result}₹ Lakhs")
    
    

    # input_dict = {
    #     'Present_Price': present_price,
    #     'Kms_Driven': kms_driven,
    #     'Owner': owner,
    #     'Car_Age': car_age,
    #     'Fuel_Type_Diesel': 1 if fuel_type=="Diesel" else 0,
    #     'Seller_Type_Individual': 1 if seller_type=="Individual" else 0,
    #     'Transmission_Manual': 1 if transmission=="Manual" else 0
    # }