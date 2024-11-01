# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 4: Stocks and Portfolios

### Problem Statement

Can we cluster stocks based on multiple financial metrics - including volatility, market capitalization, historical performance, and liquidity - to generate **tailored investment strategies** for investors with different risk profiles?


-----

### Datasets

There are two datasets available in the data folder.  One for user data, named `Comprehensive_Banking_Database.csv`; and one for stocks data, named `Stock_Data_Final.csv`.  These are the original datasets, which were subsequently cleaned up for data analysis and model fitting.  The final datasets are `users-clean-data.csv` and `stocks-clean-data-2.csv`.  Both of these datasets are located in the `clean_data` folder.<br>
The features listed below correspond to the clean versions of the datasets.


**Dataset**: `users-clean-data.csv`
|Feature|Type|Description|
|---|---|---|
|**Customer ID**|_integer_|Record ID. Integer format, no units.|
|**Age**|_integer_|User age. Integer format, unit in years.|
|**Gender**|_object_|User gender. String format, no units.|
|**City**|_object_|City where user is located. String format, no units.|
|**Account Type**|_object_|Type of account held by user. String format, no units.|
|**Account Balance**|_float_|Monetary amount in user account. Float format, unit in dollars.|
|**Account Balance After Transaction**|_float_|Monetary amount in user account after last transaction. Float format, unit in dollars.|
|**Credit Limit**|_float_|Monetary amount available to spend in user account. Float format, unit in dollars.|
|**Credit Card Balance**|_float_|Monetary amount charged by user. Float format, unit in dollars.|

**Dataset**: `stocks-clean-data-2.csv`
|Feature|Type|Description|
|---|---|---|
|**trading_volume**|_float_|The trading volume of the symbol in the given period of time. Float format, unit in stock trades.|
|**weighted_volume**|_float_|The volume weighted average price. Float format, unit in dollars.|
|**open_price**|_float_|The open price for the symbol in the given period of time. Float format, unit in dollars.|
|**close_price**|_float_|The close price for the symbol in the given period of time. Float format, unit in dollars.|
|**highest_price**|_float_|The highest price for the symbol in the given period of time. Float format, unit in dollars.|
|**lowest_price**|_float_|The lowest price for the symbol in the given period of time. Float format, unit in dollars.|
|**timestamp**|_integer_|The Unix Msec timestamp for the start of the aggregate window. Integer format, unit in milliseconds.|
|**transactions**|_integer_|The number of transactions in the aggregate window. Integer format, no units.|
|**symbol**|_object_|Ticker symbol for given stock. String format, no units.|
|**price_range**|_float_|Engineered feature: `highest_price` - `lowest_price` for the trading period. Float format, unit in dollars.|
|**volatility**|_float_|Engineered feature: `close_price` - `open_price` for the trading period. Float format, unit in dollars.|
|**price_change_percentage**|_float_|Engineered feature: `close_price` - `open_price` / `open_price` for the trading period.. Float format, unit in percent.|
|**date**|_object_|Actual transaction date derived from `timestamp` feature. String format, no units.|

---

### Summary

Fill in...


---

### Recommendation

* bullet 1
* bullet 2

---

### Technical Report

Complete and thorough analysis in various Jupyter notebooks are located below:<br> 
[01_Intro_and_Cleaning_Stocks.ipynb](./notebooks/01_Intro_and_Cleaning_Stocks.ipynb).<br>
[01_Intro_and_Cleaning_Users.ipynb](./notebooks/01_Intro_and_Cleaning_Users.ipynb).<br>
[02_EDA_and_Visualizations_Stocks.ipynb](./notebooks/02_EDA_and_Visualizations_Stocks.ipynb).<br>
[02_EDA_and_Visualizations_Users.ipynb](./notebooks/02_EDA_and_Visualizations_Users.ipynb).<br>
[03_Modeling_Stocks.ipynb](./notebooks/03_Modeling_Stocks.ipynb).<br>
[03_Modeling_Users.ipynb](./notebooks/03_Modeling_Users.ipynb).<br>

---


### Presentation

Accompanying presentation in PDF format is located [here](./presentation/).

