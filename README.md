# quanspy

A python package (library) for quantitative finance algorithms and models.

## Thanks

I want to thank Mr. Roman Paolucci <https://github.com/romanmichaelpaolucci> for teaching quantitative finance on YouTube and making a python library called Q-Fin, this package is inspired by his work.

## Functions Coverage

- Current scaffolding: Black-Scholes call/put stubs with price/Greeks hooks; Monte Carlo sketches for binary/vanilla/Asian/barrier/extendible options; GBM and stochastic-variance process interfaces; CVXPy optimization placeholder
- Equity & volatility pricing: Black-Scholes/Merton with dividends, implied vol solver, Greeks and scenario greeks; local vol (Dupire), stochastic vol (Heston, Bates, SABR), rough-vol placeholders; jump/Levy models (Merton, Kou, VG, NIG, CGMY); FFT/COS/FST pricing; binomial/trinomial/CRR/JR/JE lattices; American/Bermudan via trees and LSMC; exotics (barrier, Asian geo/arith, lookback, cliquet, TARN, digital/binary, rainbow, quanto, extendible, swing)
- Fixed income & rates: OIS/IRS/FRA curve bootstrapping, discount/forward curve construction, day-count/compounding, duration/convexity/key-rate; bond/FRN/swap/cap-floor/swaption/CMS helpers; multi-curve setup; short-rate models (Hull-White 1f/2f, CIR++), LMM/BGM, swaption smile (SABR), callable/putable bond lattices
- Credit & xVA: structural (Merton, Black-Cox) and reduced-form hazard/affine intensity models; CDS premium/protection leg PV, survival calibration; CVA/DVA/FVA/KVA skeletons with wrong-way risk hooks
- Portfolio & optimization: mean-variance, Black-Litterman (absolute/relative views), risk-parity/HRP/HCAA, min-var/min-CVaR, Kelly/log-utility sizing, robust optimization, factor exposures/tilts, turnover/TC/tax/lot/sector/leverage/box constraints, CVaR optimization with LP/SOCP
- Risk: VaR/ES (historical/parametric/Monte Carlo/EVT), stressed VaR, drawdown/Ulcer, tracking error/beta exposures, PCA risk decomposition, scenario and stress generators, liquidity and impact cost overlays
- Time series & signals: return prep/resampling, seasonality adjustments, unit-root/stationarity tests, ARIMA/SARIMA/VAR/VECM, GARCH family (GARCH/EGARCH/GJR/FIGARCH/APARCH/HEAVY), stochastic volatility, state-space/Kalman, HMM/regime switching, cointegration (Engle-Granger, Johansen), copula dependence modeling
- Forecasting & ML: linear/logistic/elastic-net baselines, SVMs, tree/forest/gradient boosting stacks, PCA/ICA and autoencoders, cross-sectional factor prediction, hyperparameter search hooks; sequence models (LSTM/GRU/Transformer/TFT stubs) for returns/vol/flow forecasting
- Stochastic processes: GBM, OU, Vasicek, CIR, Heston, SABR, Bates, jump diffusions (Merton/Kou), Levy classes (VG, NIG, CGMY), Hawkes/rough-vol placeholders, correlation via Cholesky and copulas
- Simulation: Monte Carlo (plain, antithetic, control variate, importance, stratified, moment matching), quasi-MC (Sobol/Halton), Brownian bridge for barriers, multivariate/Correlated paths, discretizations (Euler, Milstein, QE, exact GBM), pathwise and likelihood-ratio Greeks
- Calibration: vol surface building and smoothing (SVI, splines), local-vol calibration, SABR/Heston parameter fits, process MLE/GMM tools, smile arbitrage checks
- Performance & attribution: return/IR/Sharpe/Sortino/Calmar, drawdowns and turnover, Brinson allocation-selection, factor and style attribution, PnL decomposition
- Data & utilities: business-day calendars and holidays, trading-day shifts, resampling and alignment, forward/backward fills, currency/FX conversions, random seeds and reproducibility helpers
- Backtesting & execution: event-driven loop skeleton, order/portfolio/account objects, position and cash ledger, slippage/fee/impact models, PnL and risk tracking, walk-forward and cross-validation helpers, simple execution algos placeholders
