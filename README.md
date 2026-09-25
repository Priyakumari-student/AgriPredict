# 🌾 AgriPredict

### Smart Agricultural Predictions Powered by Machine Learning

AgriPredict is a **Streamlit-based machine learning application** designed to provide agricultural **production and profit estimates** using farm, soil, environmental, irrigation, crop, and market-related information.

The application provides two main prediction modules:

* 🌾 **Production Prediction** — estimates expected agricultural production in tonnes.
* 💰 **Profit Prediction** — estimates expected farm profit in Indian Rupees (₹).

---

## 📌 Project Overview

Agricultural production and profitability depend on several factors, including farm area, crop type, soil conditions, weather conditions, irrigation, crop quality, production, and market information.

AgriPredict uses trained machine learning models to process these factors and generate estimated production and profit values.

The application provides a simple web interface where users can enter farm-related information and receive predictions.

---

## ✨ Features

### 🌾 1. Production Prediction

The Production Prediction module estimates expected agricultural production in **tonnes**.

Users can provide information including:

* Farm Area
* State
* District
* Crop
* Season
* Irrigation Method
* Rainfall
* Average Temperature
* Humidity
* Sunlight Hours per Day
* Soil pH
* Soil Moisture
* Nitrogen
* Phosphorus
* Potassium
* Fertilizer
* Pesticide
* Seed Quality Score
* Disease/Pest Risk

The entered categorical values are encoded using trained encoders before being passed to the production model.

### 💰 2. Profit Prediction

The Profit Prediction module estimates expected farm profit in **Indian Rupees (₹)**.

Users can provide:

#### Farm Information

* Farm ID
* State
* District
* Crop
* Season
* Irrigation Method
* Farm Area

#### Environmental & Soil Information

* Rainfall
* Average Temperature
* Humidity
* Sunlight Hours per Day
* Soil pH
* Soil Moisture
* Nitrogen
* Phosphorus
* Potassium
* Fertilizer
* Pesticide
* Seed Quality Score

#### Production Information

* Yield
* Production

#### Market & Cost Information

* Market Price
* Total Cost
* Revenue
* Water Used
* Water Efficiency
* Disease/Pest Risk

The numerical values are scaled using a trained scaler and categorical values are encoded before prediction.

---

## 🖥️ Application Interface

The application contains three main pages:

### 🏠 Home

The home page provides:

* AgriPredict title and description
* Crop insights information
* Farm conditions information
* ML prediction information
* Production prediction option
* Profit prediction option

### 🌾 Production Prediction

Allows users to enter farm, soil, crop, irrigation, and environmental information and calculate estimated production.

### 💰 Profit Prediction

Allows users to enter farm, soil, production, market, cost, and environmental information and calculate estimated profit.

---

## 🔄 Application Workflow

```text
                  🌾 AgriPredict
                         │
                         ▼
                    🏠 Home Page
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
      🌾 Production            💰 Profit
       Prediction              Prediction
              │                     │
              ▼                     ▼
       Enter Farm Data       Enter Farm Data
              │                     │
              ▼                     ▼
      Encode Categories       Encode Categories
              │                     │
              │              Scale Numerical Data
              │                     │
              ▼                     ▼
      Production Model        Profit Model
              │                     │
              ▼                     ▼
      Production Estimate     Profit Estimate
         (Tonnes)                (₹)
```

---

## 🧠 Machine Learning Models

AgriPredict uses separate trained models for production and profit prediction.

### Production Model

The application loads:

```text
Models/production_model.pkl
```

The production model receives encoded categorical variables and numerical farm/environmental variables and predicts estimated agricultural production.

### Profit Model

The application loads:

```text
Models/linear_regression_model.pkl
```

The profit prediction workflow uses a scaler for numerical features:

```text
Models/scaler.pkl
```

The scaled numerical features are combined with encoded categorical variables and passed to the profit model.

The application therefore uses a **Linear Regression model for profit prediction**, based on the model filename and prediction implementation in `app.py`.

---

## 🔤 Categorical Encoding

AgriPredict uses saved encoders for categorical variables.

### Production Encoders

```text
production_State_encoder.pkl
production_District_encoder.pkl
production_Crop_encoder.pkl
production_Season_encoder.pkl
production_Irrigation_Method_encoder.pkl
```

### Profit Encoders

```text
Farm_ID_encoder.pkl
State_encoder.pkl
District_encoder.pkl
Crop_encoder.pkl
Season_encoder.pkl
Irrigation_Method_encoder.pkl
```

These encoders convert categorical inputs into numerical values that can be processed by the trained machine learning models.

---

## 📊 Production Prediction Inputs

The production model receives the following features:

| Feature             | Description                    |
| ------------------- | ------------------------------ |
| State               | Farm state                     |
| District            | Farm district                  |
| Crop                | Selected crop                  |
| Season              | Farming season                 |
| Farm Area           | Area of the farm in hectares   |
| Rainfall            | Rainfall in mm                 |
| Average Temperature | Average temperature in °C      |
| Humidity            | Humidity percentage            |
| Sunlight            | Sunlight hours per day         |
| Soil pH             | Soil pH value                  |
| Soil Moisture       | Soil moisture percentage       |
| Nitrogen            | Nitrogen in kg/ha              |
| Phosphorus          | Phosphorus in kg/ha            |
| Potassium           | Potassium in kg/ha             |
| Irrigation Method   | Selected irrigation method     |
| Fertilizer          | Fertilizer quantity in kg/ha   |
| Pesticide           | Pesticide quantity in litre/ha |
| Seed Quality        | Seed quality score             |
| Disease/Pest Risk   | Disease/pest risk percentage   |

### Output

```text
Estimated Production: XX.XX Tonnes
```

---

## 💰 Profit Prediction Inputs

The profit model uses numerical and categorical information.

### Numerical Features

```text
Farm Area
Rainfall
Average Temperature
Humidity
Sunlight
Soil pH
Soil Moisture
Nitrogen
Phosphorus
Potassium
Fertilizer
Pesticide
Seed Quality
Yield
Production
Market Price
Total Cost
Revenue
Water Used
Water Efficiency
Disease/Pest Risk
```

### Categorical Features

```text
Farm ID
State
District
Crop
Season
Irrigation Method
```

### Output

```text
Estimated Profit: ₹XX,XXX.XX
```

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Application Framework

* Streamlit

### Machine Learning

* Pickle-based trained machine learning models
* Linear Regression for profit prediction
* Saved preprocessing/scaling components

### Frontend Styling

* Streamlit
* Custom CSS
* HTML styling through Streamlit

---

## 📂 Project Structure

Based on the files referenced directly by `app.py`, the application requires the following structure:

```text
AgriPredict/
│
├── app.py
│
├── Models/
│   ├── production_model.pkl
│   ├── production_State_encoder.pkl
│   ├── production_District_encoder.pkl
│   ├── production_Crop_encoder.pkl
│   ├── production_Season_encoder.pkl
│   ├── production_Irrigation_Method_encoder.pkl
│   │
│   ├── linear_regression_model.pkl
│   ├── scaler.pkl
│   ├── Farm_ID_encoder.pkl
│   ├── State_encoder.pkl
│   ├── District_encoder.pkl
│   ├── Crop_encoder.pkl
│   ├── Season_encoder.pkl
│   └── Irrigation_Method_encoder.pkl
│
└── README.md
```

> **Note:** The exact contents of the repository may contain additional files that are not referenced in `app.py`.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/AgriPredict.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Open the Project

```bash
cd AgriPredict
```

### 3. Install Required Packages

Install Streamlit:

```bash
pip install streamlit
```

The application also requires the Python environment used to create/load the saved machine learning models.

If a `requirements.txt` file is included in the repository, install dependencies using:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Run the Streamlit application using:

```bash
streamlit run app.py
```

Streamlit will provide a local address where the application can be opened in a web browser.

---

## 🧪 Example Workflow

### Production Prediction

1. Open AgriPredict.
2. Select **🌾 Predict Production**.
3. Enter the farm information.
4. Enter environmental and soil conditions.
5. Enter crop-related factors.
6. Click **🔮 Calculate Production**.
7. View the estimated production in tonnes.

### Profit Prediction

1. Return to the home page.
2. Select **💰 Predict Profit**.
3. Enter farm information.
4. Enter environmental and soil information.
5. Enter yield and production information.
6. Enter market and cost information.
7. Click **💰 Calculate Profit**.
8. View the estimated profit in Indian Rupees.

---

## 📈 Prediction Outputs

### Production

The application displays:

```text
🌾 Production Estimate

XX.XX Tonnes
```

### Profit

The application displays:

```text
💰 Profit Estimate

₹XX,XXX.XX
```

---

## 🎨 User Interface

AgriPredict uses a clean agriculture-inspired interface with:

* 🌾 Agricultural theme
* 🌱 Green color palette
* 📊 Information cards
* 🧾 Structured input forms
* 🔮 Prediction buttons
* 💰 Profit estimation section
* 📱 Wide Streamlit layout
* Responsive Streamlit components

Custom CSS is used to style the application interface, buttons, cards, result sections, headings, and footer.

---

## 🔐 Model Files

The application loads pre-trained models and preprocessing objects from the `Models` directory using Python's `pickle` module.

The application cannot perform predictions if the required model or encoder files are missing.

Therefore, ensure that the required files remain in:

```text
Models/
```

with the filenames expected by `app.py`.

---

## ⚠️ Important Notes

AgriPredict provides **machine-learning-based estimates**. The predictions are based on the patterns learned by the trained models and the information supplied by the user.

The predictions should not be considered guaranteed agricultural outcomes.

Actual agricultural production and profit can be affected by many factors, including:

* Weather changes
* Soil characteristics
* Water availability
* Crop diseases
* Pest outbreaks
* Farming practices
* Input costs
* Market price changes
* Regional agricultural conditions

The application should therefore be considered a **decision-support and educational machine learning application**, rather than a guarantee of future production or profit.

---

## 🚀 Future Enhancements

The following features are **possible future improvements and are not currently implemented in the provided application**:

* 🌦️ Real-time weather API integration
* 📍 Location-based agricultural analysis
* 📊 Interactive prediction history
* 📈 Prediction visualization and analytics
* 🌱 Crop recommendation module
* 🧪 Fertilizer recommendation
* 🌾 Crop yield optimization
* 💹 Market price prediction
* 📱 Mobile application
* 🌐 Regional Indian language support
* 👤 User accounts and personalized dashboards
* ☁️ Cloud deployment and scalable model serving

---

## 🌐 Regional Language Support

Regional language support is **not currently implemented** in the provided application.

A future version could potentially support languages such as:

* Telugu
* Hindi
* Tamil
* Kannada
* Marathi
* Gujarati

This is listed only as a **future enhancement**.

---

## 🎓 Academic Project

AgriPredict demonstrates the application of **Machine Learning in Agriculture** through two prediction tasks:

```text
Agricultural Data
       │
       ├───────────────┐
       │               │
       ▼               ▼
Production Data    Profit Data
       │               │
       ▼               ▼
ML Prediction      ML Prediction
       │               │
       ▼               ▼
Production         Profit
Estimate           Estimate
```

The project demonstrates concepts including:

* Machine Learning
* Regression
* Feature preprocessing
* Categorical encoding
* Numerical scaling
* Streamlit application development
* Prediction systems
* Agricultural data analysis

---

## 🔮 Project Vision

AgriPredict aims to demonstrate how machine learning can be applied to agricultural data to provide useful estimates related to **farm production and profitability**.

By combining farm conditions, environmental factors, soil information, crop information, irrigation details, production data, and market information, the application provides a simple interface for generating data-driven estimates.

---

## 🤝 Contribution

Contributions and improvements are welcome.

To contribute:

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature/new-feature
```

3. Make your changes.
4. Commit your changes.

```bash
git commit -m "Add new feature"
```

5. Push your branch.

```bash
git push origin feature/new-feature
```

6. Create a Pull Request.

---

## 📜 License

No specific open-source license is currently specified in the provided `app.py`.

If this project is intended to be publicly distributed, an appropriate license can be added to the repository separately.

---

## 👩‍💻 Project

# 🌾 AgriPredict

**Smart agricultural predictions powered by machine learning.**

### Current Prediction Modules

🌾 **Production Prediction**
Estimate agricultural production in tonnes.

💰 **Profit Prediction**
Estimate farm profit in Indian Rupees.

---

### Built With

```text
🐍 Python
│
└── Streamlit
     │
     ├── 🌾 Production Model
     │
     └── 💰 Profit Model
```

**AgriPredict — Data-driven insights for smarter farming. 🌱**
