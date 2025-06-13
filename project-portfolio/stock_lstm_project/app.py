import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import math

# ✅ Load predictions
actual_prices = np.load("actual.npy")
predicted_prices = np.load("predicted.npy")

# ✅ Calculate RMSE
rmse = math.sqrt(mean_squared_error(actual_prices, predicted_prices))

# ✅ Create DataFrame
df = pd.DataFrame({
    "Actual": actual_prices.flatten(),
    "Predicted": predicted_prices.flatten()
})

# ✅ Streamlit UI
st.set_page_config(page_title="Stock Prediction Dashboard", layout="centered")
st.title("📈 AAPL Stock Price Prediction Dashboard")
st.subheader("LSTM-Based Stock Price Prediction")
st.write(f"**📌 RMSE**: `{rmse:.2f}`")

# ✅ Line chart
st.line_chart(df)

# ✅ Matplotlib plot
st.subheader("📊 Actual vs Predicted (Graph)")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(actual_prices, label="Actual", color='blue')
ax.plot(predicted_prices, label="Predicted", color='orange')
ax.set_title("Actual vs Predicted Stock Prices")
ax.set_xlabel("Time")
ax.set_ylabel("Price (USD)")
ax.legend()
st.pyplot(fig)

st.markdown("---")
st.caption("🧠 Built with LSTM | 📊 Streamlit Dashboard | 💙 AAPL Stock")
