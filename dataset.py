import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

st.set_page_config(page_title="Battery Life Predictor", layout="centered")

st.title("🔋 Battery Life Prediction using Random Forest")

# Upload CSV
uploaded_file = st.file_uploader("Upload your battery dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)

        st.subheader("📊 Preview of Uploaded Data")
        st.dataframe(data.head())

        target_col = st.selectbox("Select the target column (Battery Life)", data.columns)

        feature_cols = st.multiselect("Select feature columns", [col for col in data.columns if col != target_col])

        if feature_cols and target_col:
            X = data[feature_cols]
            y = data[target_col]

            # Train-test split
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Train Random Forest model
            model = RandomForestClassifier(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)

            st.success("✅ Model trained successfully!")

            st.subheader("📈 Model Evaluation")
            st.text(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
            st.text("Classification Report:")
            st.text(classification_report(y_test, y_pred))

            st.subheader("🔍 Try Predicting Battery Life")
            input_data = []
            for col in feature_cols:
                val = st.number_input(f"Enter value for {col}", value=float(X[col].mean()))
                input_data.append(val)

            if st.button("Predict"):
                prediction = model.predict([input_data])[0]
                st.success(f"🔋 Predicted Battery Life: {prediction}")

    except Exception as e:
        st.error(f"❌ Error loading file: {e}")
else:
    st.info("Please upload a CSV file to begin.")
