---

---

--- 

# Observations

- [NVIDIA paper](https://arxiv.org/pdf/2312.17100) suggests NOT to choose a model based on a single metric. It is better to include MAE and RMSE error on top of SMAPE. Final model selection should take into account both metrics.

- NBEATS and NHITS show poor performances when context length (or lookback length is below 256 data points). This can explain why XGBoost is more suited to our case (10 data points) following the results obtained by Taher.

- XGBoost takes roughly twice more time to be trained according to the NVIDIA paper. Taher observed the reverse effect -> Is it due to the size of NBEATS and NHITS ?

- SMAPE values obtained by the NVIDIA team were around 8-10 % while Taher obtained values in the range 30-40%. May be it depends on the dataset OR on the implementation/architecture employed by Taher.
