
---

## 1st meeting

- Question : Did you conduct any experiment to find the best hyperparameters used for the 3 networks ? 
	-> Answer : He used Ray Tune (which uses Optuna for Pytorch) to find the best hyperparameters. However he did not save any graphs or tables showing the obtained results. 

- Question : Did you save the models trained somewhere ?
	-> Answer : Yes, I will send them through WeTransfer. Still waiting for them (Wednesday 2pm)

- Question : How did you define the criterion "suitability for Federated Learning" ?
	-> Answer : Based on the model size and weight. 

- Question : How did you define the thresholds to rank SMAPE or Silhouette scores ?
	-> Answer : ..... Still waiting for papers or references. (Wednesday 2pm)

- Question : Did you find the best parameters via Ray with the data from only 1 building ?
	-> Answer : Yes because it was taking a lot of time. Clustering enables to select only 1 building from each cluster. 



## 2nd meeting

- Question : How did you assess if a model is good for short or long sequences ? 
	-> Answer : ..... No answer 

- Question : How did you draw the 2 t-SNE graphs ? Does the second one refers to the first cluster being divided into 4 smaller clusters ? If so, why the ranges of the plots does not match with the first plot ?
	-> Answer : Not the same information kept for the PCA reprojection, which explains the shape of the t-SNE plot.

- Question : Outlier removal done on the time series itself ? 
	-> Answer : Yes, he modified the data points of the time series and replace them by the average of the closest points. -> should not do that because it modifies the data themselves. Rather we can detect the outliers from the PCA or t-SNE decomposition and remove completely the time series from the cluster. 

- Question : What does the code for NBeats-label-0 do ? You go from 12000 lines in the dataframe to multiple millions of lines. What happened there ?
	-> Answer : He split the timeseries into chunks with a sliding window. The formula should show how the dataframe goes from thousand of lines to millions of lines.

- Question : Did you had the chance to look at the descriptive statistics to find the best parameters (like the lookback window, etc) ? It allows you to have an idea of the seasonality of the time series and which size of the data the network needs to catch this seasonality.
	-> Answer : No, I did not have the time to do that.  

