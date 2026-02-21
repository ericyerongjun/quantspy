import numpy as np
from scipy.stats import norm
from typing import Union, Optional

class BlackScholesCall:
    
# Black Scholes European Call Option Pricing (Allowing for Vectorized Inputs and Optional Inputs)
    def call_delta(self,
                   asset_price: Union[float, np.ndarray],
                   asset_volatility: Union[float, np.ndarray],
                   strike_price:Union[float, np.ndarray],
                   time_to_expiration:Union[float, np.ndarray],
                   risk_free_rate:Union[float, np.ndarray],
                   dividend_yield: Optional[Union[float, np.ndarray]] = 0.0
                   ) -> Union[float, np.ndarray]:
        
        """
        Parameters explanation (Annualized):
        asset_price: Current price of the underlying asset (S)
        asset_volatility: Volatility of the underlying asset (σ)
        strike_price: Strike price of the option (K)
        time_to_expiration: Time to expiration in years (T)
        risk_free_rate: Risk-free interest rate (r)
        dividend_yield: Dividend yield of the underlying asset (q), default is 0.0
        """
        
        # Convert inputs to numpy arrays for vectorized operations and ensure consistent shapes (Set their data type to float64 for numerical stability)
        S = np.asarray(asset_price, dtype=np.float64)
        sigma = np.asarray(asset_volatility, dtype=np.float64)
        K = np.asarray(strike_price, dtype=np.float64)
        T = np.asarray(time_to_expiration, dtype=np.float64)
        r = np.asarray(risk_free_rate, dtype=np.float64)
        q = np.asarray(dividend_yield, dtype=np.float64)
        