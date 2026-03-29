# Black–Scholes European Call Option Pricing

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24+-orange.svg)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7+-green.svg)](https://matplotlib.org/)
[![SciPy](https://img.shields.io/badge/SciPy-1.11+-red.svg)](https://scipy.org/)


## 📋 Description
This project implements the Black–Scholes model for pricing European call options. It compares two approaches:

Analytical solution: closed-form Black–Scholes formula
Numerical method: Finite Difference Method (FDM) resolution

The notebook also explores the calculation of Greeks (Delta, Gamma, Theta), which measure the sensitivity of the option price to different market parameters.

## 🎯 Objectives

Understand the Black–Scholes model and its assumptions
Implement the analytical solution for option pricing
Develop a numerical solver using finite differences
Calculate and visualize Greeks for risk analysis
Compare analytical and numerical results

## 📊 Features

1. Analytical Solution

Option price calculation using the Black–Scholes formula
Analytical calculation of Greeks (Delta, Gamma, Vega, Theta, Rho)

2. Finite Difference Method

Discretization of the Black–Scholes PDE
Implicit scheme for numerical stability
Option price surface as a function of time and asset price

3. Visualizations

Comparison of analytical vs numerical prices
Greeks evolution as a function of asset price
3D surface plot of option price

## 💻 Usage

1. Clone the repository:

```
bashgit clone https://github.com/[your-username]/black-scholes-option-pricing.git
cd black-scholes-option-pricing
```
2. Launch Jupyter Notebook:
```
bashjupyter notebook companion.ipynb
```

3. Execute cells sequentially to:
   - Define model parameters
   - Calculate prices with both methods
   - Visualize results and Greeks

## 📐 Mathematical Model

## Parameters

| Symbol | Description | Default Value |
|---------|-------------|---------------|
| S | Underlying asset price | 100 |
| K | Strike price | 100 |
| T | Maturity time (years) | 1.0 |
| r | Risk-free interest rate | 0.05 |
| σ | Volatility | 0.2 |

### Black–Scholes Equation

The PDE governing the option price V(t,S):

```
∂V/∂t + (1/2)σ²S² ∂²V/∂S² + rS ∂V/∂S - rV = 0
```

With terminal condition: V(T,S) = max(S-K, 0)

### Analytical Formula
```
V(t,S) = S·Φ(d₁) - K·e^(-r(T-t))·Φ(d₂)
Where:

d₁ = [ln(S/K) + (r + σ²/2)(T-t)] / [σ√(T-t)]
d₂ = d₁ - σ√(T-t)
Φ : cumulative distribution function of the standard normal distribution
```

## 📈 Results
The notebook generates several visualizations:

Method comparison: chart showing convergence between analytical solution and FDM
Greeks: price sensitivities to parameters (Delta, Gamma, Theta)
Price surface: option price evolution as a function of time and asset price

## 🧪 Code Example
python# Model parameters
S0 = 100      # Current asset price
K = 100       # Strike
T = 1.0       # Maturity (1 year)
r = 0.05      # Risk-free rate (5%)
sigma = 0.2   # Volatility (20%)

## Calculate analytical price
price_bs = black_scholes_call(S0, K, T, r, sigma)
print(f"Black-Scholes Price: {price_bs:.4f}")

## Calculate Greeks
delta = compute_delta(S0, K, T, r, sigma)
gamma = compute_gamma(S0, K, T, r, sigma)
theta = compute_theta(S0, K, T, r, sigma)
📚 Key Concepts
Greeks

Delta (Δ): sensitivity to underlying asset price
Gamma (Γ): sensitivity of Delta to asset price
Theta (Θ): sensitivity to time passage (time decay)
Vega (ν): sensitivity to volatility
Rho (ρ): sensitivity to interest rate

## 🔬 Numerical Method
The finite difference method uses:

Spatial discretization: uniform grid for S
Time discretization: adaptive time step
Implicit scheme: unconditional stability
Boundary conditions:

S = 0 : V = 0
S → ∞ : V ≈ S - K·e^(-r·τ)



## 🎓 References

Black, F., & Scholes, M. (1973). "The Pricing of Options and Corporate Liabilities". Journal of Political Economy, 81(3), 637-654.
Wilmott, P. (2006). Paul Wilmott on Quantitative Finance. John Wiley & Sons.

👤 Author
Laura Cohen
