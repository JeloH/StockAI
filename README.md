# Motivation
This notebook shows some steps to implement a ML model to work on a huge stocks data. Regarding the size of dataset, I was trying to find a suitable model.I used XGBRegressor because it is more efficient than other machine-learning algorithms to handle large datasets easily. 

Basically, the program implemented in the Kaggle platform, the public link is available here:
https://www.kaggle.com/code/reko21/notebook503e15eeba

# Requirements
The packages used in this notebook :  

* os
* numpy
* pandas
* joblib
* sklearn
* xgboost
* flask
* threading
* pyngrok


# Model Serving:

By using heroku server:
https://aistock.herokuapp.com/predict?vol_moving_avg=12345&adj_close_rolling_med=25
![image](https://github.com/JeloH/StockAI/assets/11020050/237aa71b-8da4-472d-9ddb-c5499e570151)

![image](https://github.com/JeloH/StockAI/assets/11020050/2c14b2f6-757d-45ac-8a7b-7d26edebcb1d)



By using ngrok server:

![image](https://user-images.githubusercontent.com/11020050/235978329-5a03a8a4-8c59-41aa-a106-c5a073881d5c.png)

