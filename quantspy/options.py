import math
import numpy as np
from scipy.stats import norm

class BlackScholesCall:
    
    def call_delta(self,
                   asset_price: float,
                   asset_volatility: float,
                   strike_price:float,
                   time_to_expiration:float,
                   risk_free_rate:float) -> float:
        b = np.exp(-risk_free_rate * time_to_expiration)