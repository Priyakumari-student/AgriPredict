
import streamlit as st
import pickle

# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="AgriPredict",
    page_icon="🌾",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #f5f7f2;
}

.main-title {
    text-align: center;
    color: #355c3a;
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #68736a;
    font-size: 17px;
    margin-bottom: 30px;
}

h2, h3 {
    color: #355c3a !important;
}

.prediction-card {
    background-color: white;
    padding: 28px;
    border-radius: 14px;
    border: 1px solid #dfe5dc;
    text-align: center;
    min-height: 180px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.04);
}

.prediction-card h2 {
    color: #355c3a;
}

.prediction-card p {
    color: #68736a;
    font-size: 15px;
}

div.stButton > button {
    border-radius: 9px;
    border: 1px solid #668b6a;
    background-color: #557a5b;
    color: white;
    font-size: 16px;
    font-weight: 600;
    min-height: 48px;
}

div.stButton > button:hover {
    background-color: #426447;
    border-color: #426447;
    color: white;
}

div.stFormSubmitButton > button {
    border-radius: 9px;
    background-color: #557a5b;
    color: white;
    font-size: 16px;
    font-weight: 600;
    min-height: 48px;
}

div.stFormSubmitButton > button:hover {
    background-color: #426447;
    color: white;
}

.result-box {
    background-color: #edf3ed;
    border-left: 5px solid #557a5b;
    padding: 20px;
    border-radius: 10px;
    margin-top: 20px;
}

.result-box h1 {
    color: #355c3a;
}

.info-card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #e0e5df;
    text-align: center;
}

.info-card h3 {
    margin-bottom: 5px;
}

.info-card p {
    color: #68736a;
    margin: 0;
}

.footer {
    text-align: center;
    color: #7a837b;
    font-size: 13px;
    margin-top: 40px;
    padding: 15px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# PAGE STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "home"


# =========================================================
# LOAD PRODUCTION MODEL
# =========================================================

with open("Models/production_model.pkl", "rb") as file:
    production_model = pickle.load(file)

with open("Models/production_State_encoder.pkl", "rb") as file:
    production_state_encoder = pickle.load(file)

with open("Models/production_District_encoder.pkl", "rb") as file:
    production_district_encoder = pickle.load(file)

with open("Models/production_Crop_encoder.pkl", "rb") as file:
    production_crop_encoder = pickle.load(file)

with open("Models/production_Season_encoder.pkl", "rb") as file:
    production_season_encoder = pickle.load(file)

with open("Models/production_Irrigation_Method_encoder.pkl", "rb") as file:
    production_irrigation_encoder = pickle.load(file)


# =========================================================
# LOAD PROFIT MODEL
# =========================================================

with open("Models/linear_regression_model.pkl", "rb") as file:
    profit_model = pickle.load(file)

with open("Models/scaler.pkl", "rb") as file:
    profit_scaler = pickle.load(file)

with open("Models/Farm_ID_encoder.pkl", "rb") as file:
    farm_id_encoder = pickle.load(file)

with open("Models/State_encoder.pkl", "rb") as file:
    state_encoder = pickle.load(file)

with open("Models/District_encoder.pkl", "rb") as file:
    district_encoder = pickle.load(file)

with open("Models/Crop_encoder.pkl", "rb") as file:
    crop_encoder = pickle.load(file)

with open("Models/Season_encoder.pkl", "rb") as file:
    season_encoder = pickle.load(file)

with open("Models/Irrigation_Method_encoder.pkl", "rb") as file:
    irrigation_encoder = pickle.load(file)


# =========================================================
# HOME PAGE
# =========================================================

if st.session_state.page == "home":

    st.markdown(
        '<div class="main-title">🌾 AgriPredict</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Smart agricultural predictions powered by machine learning'
        '</div>',
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # INFORMATION CARDS
    # -----------------------------------------------------

    info1, info2, info3 = st.columns(3)

    with info1:
        st.markdown("""
        <div class="info-card">
            <h3>🌱 Crop Insights</h3>
            <p>Estimate crop production using farm conditions.</p>
        </div>
        """, unsafe_allow_html=True)

    with info2:
        st.markdown("""
        <div class="info-card">
            <h3>🌦️ Farm Conditions</h3>
            <p>Consider soil, weather and irrigation factors.</p>
        </div>
        """, unsafe_allow_html=True)

    with info3:
        st.markdown("""
        <div class="info-card">
            <h3>📈 ML Predictions</h3>
            <p>Generate production and profit estimates.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    st.subheader("Choose a Prediction")

    # -----------------------------------------------------
    # PREDICTION CARDS
    # -----------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="prediction-card">
            <h2>🌾 Production</h2>
            <p>
                Estimate expected agricultural production
                using farm, soil and environmental conditions.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        if st.button(
            "🌾 Predict Production",
            use_container_width=True
        ):
            st.session_state.page = "production"
            st.rerun()

    with col2:

        st.markdown("""
        <div class="prediction-card">
            <h2>💰 Profit</h2>
            <p>
                Estimate expected farm profit using
                production, market and cost information.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        if st.button(
            "💰 Predict Profit",
            use_container_width=True
        ):
            st.session_state.page = "profit"
            st.rerun()

    st.markdown("""
    <div class="footer">
        🌿 AgriPredict • Data-driven insights for smarter farming
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# PRODUCTION PAGE
# =========================================================

elif st.session_state.page == "production":

    st.markdown(
        '<div class="main-title">🌾 Production Prediction</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Enter the farm details to estimate expected production'
        '</div>',
        unsafe_allow_html=True
    )

    with st.form("production_form"):

        st.subheader("🌱 Farm Information")

        col1, col2 = st.columns(2)

        with col1:

            farm_area = st.number_input(
                "Farm Area (Hectares)",
                min_value=0.0,
                value=1.0
            )

            state = st.selectbox(
                "State",
                production_state_encoder.classes_
            )

            district = st.selectbox(
                "District",
                production_district_encoder.classes_
            )

            crop = st.selectbox(
                "Crop",
                production_crop_encoder.classes_
            )

            season = st.selectbox(
                "Season",
                production_season_encoder.classes_
            )

            irrigation = st.selectbox(
                "Irrigation Method",
                production_irrigation_encoder.classes_
            )

        with col2:

            rainfall = st.number_input(
                "Rainfall (mm)",
                min_value=0.0,
                value=100.0
            )

            avg_temperature = st.number_input(
                "Average Temperature (°C)",
                value=25.0
            )

            humidity = st.number_input(
                "Humidity (%)",
                min_value=0.0,
                max_value=100.0,
                value=60.0
            )

            sunlight = st.number_input(
                "Sunlight Hours per Day",
                min_value=0.0,
                value=6.0
            )

            soil_ph = st.number_input(
                "Soil pH",
                min_value=0.0,
                max_value=14.0,
                value=6.5
            )

            soil_moisture = st.number_input(
                "Soil Moisture (%)",
                min_value=0.0,
                max_value=100.0,
                value=40.0
            )

        st.subheader("🧪 Soil & Crop Factors")

        col1, col2, col3 = st.columns(3)

        with col1:

            nitrogen = st.number_input(
                "Nitrogen (kg/ha)",
                min_value=0.0,
                value=50.0
            )

            phosphorus = st.number_input(
                "Phosphorus (kg/ha)",
                min_value=0.0,
                value=30.0
            )

        with col2:

            potassium = st.number_input(
                "Potassium (kg/ha)",
                min_value=0.0,
                value=30.0
            )

            fertilizer = st.number_input(
                "Fertilizer (kg/ha)",
                min_value=0.0,
                value=50.0
            )

        with col3:

            pesticide = st.number_input(
                "Pesticide (Litre/ha)",
                min_value=0.0,
                value=2.0
            )

            seed_quality = st.number_input(
                "Seed Quality Score",
                min_value=0.0,
                max_value=100.0,
                value=75.0
            )

        disease_risk = st.number_input(
            "Disease/Pest Risk (%)",
            min_value=0.0,
            max_value=100.0,
            value=20.0
        )

        calculate_production = st.form_submit_button(
            "🔮 Calculate Production"
        )

    # -----------------------------------------------------
    # PRODUCTION RESULT
    # -----------------------------------------------------

    if calculate_production:

        state_encoded = production_state_encoder.transform([state])[0]
        district_encoded = production_district_encoder.transform([district])[0]
        crop_encoded = production_crop_encoder.transform([crop])[0]
        season_encoded = production_season_encoder.transform([season])[0]
        irrigation_encoded = production_irrigation_encoder.transform([irrigation])[0]

        production_input = [[
            state_encoded,
            district_encoded,
            crop_encoded,
            season_encoded,
            farm_area,
            rainfall,
            avg_temperature,
            humidity,
            sunlight,
            soil_ph,
            soil_moisture,
            nitrogen,
            phosphorus,
            potassium,
            irrigation_encoded,
            fertilizer,
            pesticide,
            seed_quality,
            disease_risk
        ]]

        production_prediction = production_model.predict(
            production_input
        )[0]

        st.markdown(
            f"""
            <div class="result-box">
                <h2>🌾 Production Estimate</h2>
                <h1>{production_prediction:.2f} Tonnes</h1>
                <p>
                    Estimated agricultural production based on
                    the entered farm conditions.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    if st.button("⬅️ Back to Home"):
        st.session_state.page = "home"
        st.rerun()


# =========================================================
# PROFIT PAGE
# =========================================================

elif st.session_state.page == "profit":

    st.markdown(
        '<div class="main-title">💰 Profit Prediction</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Enter the farm and market details to estimate expected profit'
        '</div>',
        unsafe_allow_html=True
    )

    with st.form("profit_form"):

        st.subheader("🌱 Farm Information")

        col1, col2 = st.columns(2)

        with col1:

            farm_id = st.selectbox(
                "Farm ID",
                farm_id_encoder.classes_
            )

            state = st.selectbox(
                "State",
                state_encoder.classes_
            )

            district = st.selectbox(
                "District",
                district_encoder.classes_
            )

            crop = st.selectbox(
                "Crop",
                crop_encoder.classes_
            )

            season = st.selectbox(
                "Season",
                season_encoder.classes_
            )

            irrigation = st.selectbox(
                "Irrigation Method",
                irrigation_encoder.classes_
            )

        with col2:

            farm_area = st.number_input(
                "Farm Area (Hectares)",
                min_value=0.0,
                value=1.0
            )

            rainfall = st.number_input(
                "Rainfall (mm)",
                min_value=0.0,
                value=100.0
            )

            avg_temperature = st.number_input(
                "Average Temperature (°C)",
                value=25.0
            )

            humidity = st.number_input(
                "Humidity (%)",
                min_value=0.0,
                max_value=100.0,
                value=60.0
            )

            sunlight = st.number_input(
                "Sunlight Hours per Day",
                min_value=0.0,
                value=6.0
            )

            soil_ph = st.number_input(
                "Soil pH",
                min_value=0.0,
                max_value=14.0,
                value=6.5
            )

        st.subheader("🧪 Soil & Crop Factors")

        col1, col2, col3 = st.columns(3)

        with col1:

            soil_moisture = st.number_input(
                "Soil Moisture (%)",
                min_value=0.0,
                max_value=100.0,
                value=40.0
            )

            nitrogen = st.number_input(
                "Nitrogen (kg/ha)",
                min_value=0.0,
                value=50.0
            )

            phosphorus = st.number_input(
                "Phosphorus (kg/ha)",
                min_value=0.0,
                value=30.0
            )

        with col2:

            potassium = st.number_input(
                "Potassium (kg/ha)",
                min_value=0.0,
                value=30.0
            )

            fertilizer = st.number_input(
                "Fertilizer (kg/ha)",
                min_value=0.0,
                value=50.0
            )

            pesticide = st.number_input(
                "Pesticide (Litre/ha)",
                min_value=0.0,
                value=2.0
            )

        with col3:

            seed_quality = st.number_input(
                "Seed Quality Score",
                min_value=0.0,
                max_value=100.0,
                value=75.0
            )

            yield_tonnes = st.number_input(
                "Yield (Tonnes/Ha)",
                min_value=0.0,
                value=5.0
            )

            production_tonnes = st.number_input(
                "Production (Tonnes)",
                min_value=0.0,
                value=5.0
            )

        st.subheader("💹 Market & Cost Information")

        col1, col2 = st.columns(2)

        with col1:

            market_price = st.number_input(
                "Market Price (INR/Tonne)",
                min_value=0.0,
                value=20000.0
            )

            total_cost = st.number_input(
                "Total Cost (INR)",
                min_value=0.0,
                value=50000.0
            )

            revenue = st.number_input(
                "Revenue (INR)",
                min_value=0.0,
                value=100000.0
            )

        with col2:

            water_used = st.number_input(
                "Water Used (m³)",
                value=1000.0
            )

            water_efficiency = st.number_input(
                "Water Efficiency (t/1000m³)",
                value=5.0
            )

            disease_risk = st.number_input(
                "Disease/Pest Risk (%)",
                min_value=0.0,
                max_value=100.0,
                value=20.0
            )

        calculate_profit = st.form_submit_button(
            "💰 Calculate Profit"
        )

    # -----------------------------------------------------
    # PROFIT RESULT
    # -----------------------------------------------------

    if calculate_profit:

        farm_id_encoded = farm_id_encoder.transform([farm_id])[0]
        state_encoded = state_encoder.transform([state])[0]
        district_encoded = district_encoder.transform([district])[0]
        crop_encoded = crop_encoder.transform([crop])[0]
        season_encoded = season_encoder.transform([season])[0]
        irrigation_encoded = irrigation_encoder.transform([irrigation])[0]

        numerical_input = [[
            farm_area,
            rainfall,
            avg_temperature,
            humidity,
            sunlight,
            soil_ph,
            soil_moisture,
            nitrogen,
            phosphorus,
            potassium,
            fertilizer,
            pesticide,
            seed_quality,
            yield_tonnes,
            production_tonnes,
            market_price,
            total_cost,
            revenue,
            water_used,
            water_efficiency,
            disease_risk
        ]]

        numerical_scaled = profit_scaler.transform(
            numerical_input
        )

        profit_input = [[
            *numerical_scaled[0],
            farm_id_encoded,
            state_encoded,
            district_encoded,
            crop_encoded,
            season_encoded,
            irrigation_encoded
        ]]

        profit_prediction = profit_model.predict(
            profit_input
        )[0]

        st.markdown(
            f"""
            <div class="result-box">
                <h2>💰 Profit Estimate</h2>
                <h1>₹{profit_prediction:,.2f}</h1>
                <p>
                    Estimated profit based on the entered
                    farm and market information.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    if st.button("⬅️ Back to Home"):
        st.session_state.page = "home"
        st.rerun()
