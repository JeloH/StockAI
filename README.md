# Motivation
This notebook shows some steps to implenet a ML model to work on a huge stocks data. Regarding the size of dataset, I was trying to find a suitable model.I used XGBRegressor because it is more efficient than other machine-learning algorithms to handle large datasets easily. 

Bsicly, the rprogram run in the Kaggle platform, the public link is available here:
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
Example of 
https://7d4d-35-196-142-252.ngrok-free.app/predict?vol_moving_avg=12345&adj_close_rolling_med=25

![image](https://user-images.githubusercontent.com/11020050/235978329-5a03a8a4-8c59-41aa-a106-c5a073881d5c.png)

