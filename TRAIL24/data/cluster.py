"""Fill in a module description here"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/01_data.cluster.ipynb.

# %% auto 0
__all__ = ['resample_building_data', 'calculate_wcss', 'plot_elbow_method', 'compute_statistics', 'weekly_monthly_statistics',
           'revert_umap_projection_2D', 'revert_umap_projection_3D']

# %% ../../nbs/01_data.cluster.ipynb 4
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis
from scipy.fft import fft
from statsmodels.tsa.stattools import adfuller, acf, pacf
import numpy as np

# %% ../../nbs/01_data.cluster.ipynb 6
def resample_building_data(group):
    group = group.reset_index(level='ID')
    # Specify columns explicitly for summing
    resampled_group = group.resample('h').agg({'consumption': 'sum'})  # Example if 'consumption' is your numeric column
    resampled_group['ID'] = group['ID'].iloc[0]  # Handle non-numeric separately if needed
    resampled_group = resampled_group.set_index('ID', append=True)
    
    return resampled_group

# %% ../../nbs/01_data.cluster.ipynb 7
def calculate_wcss(data: list[float], # the input dataframe
                   max_k: int # the number of clusters
                  ) -> float:
    "compute the WCSS metric"
    wcss = []
    for k in range(1, max_k + 1):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(data)
        wcss.append(kmeans.inertia_)
    return wcss

# %% ../../nbs/01_data.cluster.ipynb 10
def plot_elbow_method(wcss:list[float], # the wcss metric to plot
                      max_k:int # the number of clusters
                     ):
    "plot the graph of the wcss metric as a function of the number of clusters"
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, max_k + 1), wcss, marker='o')
    plt.title('Elbow Method for Optimal k')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('WCSS')
    plt.grid(True)
    plt.show()

# %% ../../nbs/01_data.cluster.ipynb 11
def compute_statistics(data: list[float] # the input dataframe
                      ) -> tuple: # multiple outputs
    "compute multiple statistics like mean, std, skewness, kurtosis, etc"
    avg = data.mean()
    std = data.std()
    skw = skew(data)
    krt = kurtosis(data)
    
    # Compute energy (sum of squared values)
    energy = np.sum(data**2)
    
    # Compute periodicity using the dominant frequency from the Fourier Transform
    fft_values = fft(np.array(data))
    fft_magnitudes = np.abs(fft_values)
    periodicity = np.argmax(fft_magnitudes[1:len(fft_magnitudes)//2]) + 1  # Dominant frequency index
    
     # Trend (using linear regression)
    trend = np.polyfit(np.arange(len(data)), data, 1)[0]  # Slope of the trend

    # Seasonality (using Fourier Transform)
    seasonality = fft_magnitudes[1:len(fft_magnitudes)//2].max()  # Magnitude of the dominant frequency

    # Stationarity (using Augmented Dickey-Fuller test)
    adf_result = adfuller(data)
    stationarity = adf_result[0]  # ADF statistic (more negative means more likely stationary)

    # Autocorrelation (first lag)
    autocorr = acf(data, nlags=1)[1]  # ACF for the first lag

    # Partial Autocorrelation (first lag)
    partial_autocorr = pacf(data, nlags=1)[1]  # PACF for the first lag
    
    
    return avg, std, skw, krt, energy, periodicity, trend, seasonality, stationarity, autocorr, partial_autocorr


# %% ../../nbs/01_data.cluster.ipynb 12
def weekly_monthly_statistics(data: pd.Series
                             ) -> np.ndarray:
    "Compute some statistics (mean, std, skewness, kurtosis, energy, periodicity)"
    
    avgs, stds, skws, krts, energies, periodicities, trends, seasonalities, stationarities, autocorrs, partial_autocorrs = [], [], [], [], [], [], [], [], [], [], []
    
    weeklength = 168*4  # Weekly data length (assuming hourly data)
    
    for i in np.arange(0, len(data)-weeklength, weeklength):
        avg, std, skw, krt, energy, periodicity, trend, seasonality, stationarity, autocorr, partial_autocorr = compute_statistics(data[i:i+weeklength])
        
        avgs.append(avg)
        stds.append(std)
        skws.append(skw)
        krts.append(krt)
        energies.append(energy)
        periodicities.append(periodicity)
        trends.append(trend)
        seasonalities.append(seasonality)
        stationarities.append(stationarity)
        autocorrs.append(autocorrs)
        partial_autocorrs.append(partial_autocorr)
        
    # Combine the statistics into a single array
    weekly_stats = np.concatenate([avgs, stds, skws, krts, energies, periodicities, 
                                   trends, seasonalities, stationarities, autocorrs, partial_autocorrs])
    
    return weekly_stats

# %% ../../nbs/01_data.cluster.ipynb 13
def revert_umap_projection_2D(umap_value_1:float, # first umap coeff
                              umap_value_2:float, # second umap coeff
                              umap_df_2d:pd.DataFrame
                             ) -> int:
    "Find the data that corresponds to the UMAP projection in 2D"
    
    # Example: Find the original row corresponding to a specific UMAP projection
    # Let's say you're looking for the closest point to [UMAP1_value, UMAP2_value]
    UMAP1_value = umap_value_1
    UMAP2_value = umap_value_2

    # Calculate the Euclidean distance between the given UMAP values and all UMAP projections
    distances = np.sqrt((umap_df_2d['UMAP1'] - UMAP1_value)**2 + (umap_df_2d['UMAP2'] - UMAP2_value)**2)

    # Find the index of the minimum distance
    min_distance_index = distances.idxmin()

    return min_distance_index

# %% ../../nbs/01_data.cluster.ipynb 14
def revert_umap_projection_3D(umap_value_1, # first umap coeff
                              umap_value_2, # second umap coeff
                              umap_value_3, # third umap coeff
                              umap_df_3d:pd.DataFrame
                             ) -> int:
    "Find the data that corresponds to the UMAP projection in 3D"
    
    # Example: Find the original row corresponding to a specific UMAP projection
    # Let's say you're looking for the closest point to [UMAP1_value, UMAP2_value]
    UMAP1_value = umap_value_1
    UMAP2_value = umap_value_2
    UMAP3_value = umap_value_3

    # Calculate the Euclidean distance between the given UMAP values and all UMAP projections
    distances = np.sqrt(
                            (umap_df_3d['UMAP1'] - UMAP1_value)**2 + 
                            (umap_df_3d['UMAP2'] - UMAP2_value)**2 + 
                            (umap_df_3d['UMAP3'] - UMAP3_value)**2
                        )

    # Find the index of the minimum distance
    min_distance_index = distances.idxmin()

    return min_distance_index
