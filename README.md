# Pokemon TCG - Price Pub

### Overview

 A data-driven platform to analyze, visualize, and forecast Pokémon card prices, inspired by financial data pipeline management and analytical modeling requirements. This project mirrors asset management principles through the Pokemon Trading Card Game by tracking historical sales data, predicting card value trends, and providing insights for optimal card investments. 

### Use Cases

- Users can input specific cards they would like to track. Will be notified if a card drops below a certain price (or hits a relatively all-time low)

### Project Roadmap

- Store raw sales data in a SQL Server database, cleaned and normalized for analysis.
- Could use SQL Server Integration Services (SSIS) or other ETL tools like Apache NiFi or Luigi for database automation.
- Implement data validation rules (e.g., detecting missing prices, duplicate entries).
- Write SQL stored procedures for data transformation (e.g., price averaging, historical card trends).
- Build a time-series forecasting model (ARIMA, Prophet, or LSTM) to predict card price movements.
- Develop a basic portfolio optimization model, advising on profitable cards to "invest" in based on historical price fluctuations and rarity.
- Create a dashboard (Streamlit or PowerBI) showcasing:
    - Historical sales trends
    - Real-time price tracking
    - Forecasted price trends
    - Investment score for each card
- Implement a SQL-backed API that serves data to the front-end dashboard.

### Future Implementation

- Currently only applicable for Scarlet & Violet 151 set (a popular set that noticeably brought many collectors back into the hobby). Will expand to other sets once the base is finalized.
