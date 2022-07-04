import numpy as np
import matplotlib.pyplot as plt1
import pandas as pd
import pandas_datareader as web
import datetime as dt

from sklearn.preprocessing import MinMaxScaler
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Dropout, LSTM

def stockpre(company, epoch):

    #Load Data
    # company='FB'

    start= dt.datetime(2020,1,1)
    end=dt.datetime.now()

    data=web.DataReader(company, 'yahoo', start, end)
    print(data)

    #Prepare Data
    scalar= MinMaxScaler(feature_range=(0,1))
    scaled_data=scalar.fit_transform(data['Close'].values.reshape(-1,1))

    prediction_days=60

    x_train = []
    y_train= []

    for x in range(prediction_days, len(scaled_data)):
        x_train.append(scaled_data[x-prediction_days:x, 0])
        y_train.append(scaled_data[x, 0])

    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train=np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    #Build the model
    model = Sequential()

    model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))

    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x_train, y_train, epochs=epoch, batch_size=32)

    #Testiing the model.

    test_start= dt.datetime(2020,11, 1)
    test_end=dt.datetime.now()

    test_data = web.DataReader(company, 'yahoo', test_start, test_end)
    actual_prices = test_data['Close'].values

    total_dataset= pd.concat((data['Close'], test_data['Close']))

    model_inputs = total_dataset[len(total_dataset) - len(test_data) - prediction_days:].values
    model_inputs=model_inputs.reshape(-1,1)
    model_inputs=scalar.transform(model_inputs)

    #Make prediction on test data

    x_test = []

    for x in range(prediction_days, len(model_inputs)):
        x_test.append(model_inputs[x-prediction_days:x, 0])

    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

    predicted_prices=model.predict(x_test)
    predicted_prices=scalar.inverse_transform(predicted_prices)

    #Plot the test predictions
    plt1.plot(actual_prices, color='black', label=f"Actual {company} Price")
    plt1.plot(predicted_prices, color='green', label=f"Predicted {company} Price")
    plt1.title(f"{company} Share price")
    plt1.xlabel("Time")
    plt1.ylabel(f'{company} Share Price')
    plt1.legend()
    plt1.show()

    #Predict Next Day
    real_data = [model_inputs[len(model_inputs)+1-prediction_days:len(model_inputs+1), 0]]
    real_data = np.array(real_data)
    real_data=np.reshape(real_data, (real_data.shape[0], real_data.shape[1],1))

    prediction=model.predict(real_data)
    prediction= scalar.inverse_transform(prediction)
    # print(f"Prediction: {prediction}")
    return prediction

# print(stockpre('FB', 25))