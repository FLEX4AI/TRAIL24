
---

# ROADMAP

#### 1) Create git repo
#### 2) Refactor Taher code and add comments
#### 3) Add dataset to DVC
#### 4) Check training results obtained by Taher
#### 5)


---

# TO-DO

- [x] Create Git repo for new pipeline
- [ ] Add docs to functions
- [ ] Add dataset to DVC
- [ ] Add MAE and RMSE metrics
- [ ] 




---

# Remarks

- [Nvidia paper](https://arxiv.org/pdf/2312.17100) suggests NOT to choose a model based on a single metric. It is better to include MAE and RMSE error on top of SMAPE. Final model selection should take into account both metrics.

- NBEATS and NHITS show poor performances when context length (or lookback length is below 256 data points). This can explain why XGBoost is more suited to our case (10 data points) following the results obtained by Taher.

- M

