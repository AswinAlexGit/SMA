from pandas_datareader import data
import matplotlib.pyplot as plt
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import make_pipeline
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.decomposition import PCA
# import datetime
import numpy as np
def clustering(companies, k):

    try:
        companies_dict = companies

        data_source='yahoo'
        start_date='2020-01-29'
        end_date='2022-02-27'


        df= data.DataReader(list(companies_dict.values()), data_source, start_date, end_date)


        stock_open = np.array(df['Open']).T # stock_open is numpy array of transpose of df['Open']
        stock_close = np.array(df['Close']).T # stock_close is numpy array of transpose of df['Close']

        movements = stock_close-stock_open
        sum_of_movement = np.sum(movements,1)



        for i in range(len(companies_dict)):
         print('company:{}, Change:{}'.format(df['High'].columns[i],sum_of_movement[i]))

        # plt.figure(figsize = (20,10))
        # plt.subplot(1,2,1)
        # plt.title("Company:Amazon",fontsize = 20)
        # plt.xticks(fontsize = 10)
        # plt.yticks(fontsize = 20)
        # plt.xlabel('Date',fontsize = 15)
        # plt.ylabel("Opening price",fontsize = 15)
        # plt.plot(df['Open']['AMZN'])
        # plt.subplot(1,2,2)
        # plt.title('Company:Apple',fontsize = 20)
        # plt.xticks(fontsize = 10)
        # plt.yticks(fontsize = 20)
        # plt.xlabel('Date',fontsize = 15)
        # plt.ylabel('Opening price',fontsize = 15)
        # plt.plot(df['Open']['AAPL'])

        normalizer= Normalizer()
        new = normalizer.fit_transform(movements)
        print(new.max())
        print(new.min())
        print(new.mean())

        # # create a K-means model with 10 clusters
        # kmeans = KMeans(n_clusters=10, max_iter=1000)
        #
        # # make a pipeline chaining normalizer and kmeans
        # pipeline = make_pipeline(normalizer,kmeans)
        # # fit pipeline to daily stock movements
        # pipeline.fit(movements)
        # print(kmeans.inertia_)
        #
        # # predict cluster labels
        # labels = pipeline.predict(movements)
        #
        # df1 = pd.DataFrame({'labels':labels,'companies':list(companies_dict)})
        # print(df1)

        # visualize the results
        reduced_data = PCA(n_components = 2).fit_transform(new)

        # run kmeans on reduced data Clusters
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(reduced_data)
        labels = kmeans.predict(reduced_data)

        # create DataFrame aligning labels & companies
        df1 = pd.DataFrame({'labels':labels,'companies':list(companies_dict)})

        # Display df sorted by cluster labels
        print(df1.sort_values('labels'))

        # Define step size of mesh
        h = 0.01

        # plot the decision boundary
        x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:,0].max() + 1
        y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:,1].max() + 1
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

        # Obtain labels for each point in the mesh using our trained model
        Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

        # Put the result into a color plot
        Z = Z.reshape(xx.shape)

        # define colorplot
        cmap = plt.cm.Paired

        # plot figure
        plt.clf()
        plt.figure(figsize=(10,10))
        plt.imshow(Z, interpolation='nearest',
         extent = (xx.min(), xx.max(), yy.min(), yy.max()),
         cmap = cmap,
         aspect = 'auto', origin='lower')
        plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=5)


        # plot the centroid of each cluster as a white X
        centroids = kmeans.cluster_centers_
        plt.scatter(centroids[:, 0], centroids[:, 1],
         marker='x', s=169, linewidth=3,
         color='w', zorder=10)

        plt.title('K-Means Clustering on Stock Market Movements (PCA-Reduced Data)')
        plt.xlim(x_min, x_max)
        plt.ylim(y_min, y_max)
        plt.show()
        return [1,df1.sort_values('labels')]

    except:
        print("Check your symbols again/Bad Network connection.")
        return [0]

# umu= {
#             'Amazon':'AMZN',
#             'Apple':'AAPL',
#             'Walgreen':'WBA',
#             'Northrop Grumman':'NOC',
#             'Boeing':'BA',
#             'Lockheed Martin':'LMT',
#             'McDonalds':'MCD',
#             'Intel':'INTC',
#             'IBM':'IBM',
#             'Texas Instruments':'TXN',
#             'MasterCard':'MA',
#             'Microsoft':'MSFT',
#             'General Electrics':'GE',
#             'American Express':'AXP',
#             'Pepsi':'PEP',
#             'Coca Cola':'KO',
#             'Johnson & Johnson':'JNJ',
#             'Toyota':'TM',
#             'Honda':'HMC',
#             'Exxon':'XOM',
#             'Chevron':'CVX',
#             'Valero Energy':'VLO',
#             'Ford':'F',
#             'Bank of America':'BAC'}
# Clustering(umu, 9)