# Black–Scholes European Call Option Pricing

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24+-orange.svg)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7+-green.svg)](https://matplotlib.org/)
[![SciPy](https://img.shields.io/badge/SciPy-1.11+-red.svg)](https://scipy.org/)

## 📋 Description

Ce projet implémente le modèle de Black–Scholes pour la valorisation d'options d'achat européennes (European call options). Il compare deux approches :

- **Solution analytique** : formule fermée de Black–Scholes
- **Méthode numérique** : résolution par différences finies (FDM - Finite Difference Method)

Le notebook explore également le calcul des **Greeks** (Delta, Gamma, Theta) qui mesurent la sensibilité du prix de l'option aux différents paramètres du marché.

## 🎯 Objectifs

- Comprendre le modèle Black–Scholes et ses hypothèses
- Implémenter la solution analytique pour le pricing d'options
- Développer un solveur numérique par différences finies
- Calculer et visualiser les Greeks pour l'analyse de risque
- Comparer les résultats analytiques et numériques

## 📊 Fonctionnalités

### 1. Solution Analytique
- Calcul du prix de l'option selon la formule de Black–Scholes
- Calcul analytique des Greeks (Delta, Gamma, Vega, Theta, Rho)

### 2. Méthode des Différences Finies
- Discrétisation de l'EDP de Black–Scholes
- Schéma implicite pour la stabilité numérique
- Surface de prix option en fonction du temps et du prix de l'actif

### 3. Visualisations
- Comparaison prix analytique vs numérique
- Évolution des Greeks en fonction du prix de l'actif
- Surface 3D du prix de l'option

## 🚀 Installation

### Prérequis

Python 3.11 ou supérieur

### Dépendances

```bash
pip install numpy matplotlib scipy
```

Ou utilisez le fichier `requirements.txt` :

```bash
pip install -r requirements.txt
```

## 💻 Utilisation

1. Clonez le dépôt :
```bash
git clone https://github.com/[votre-username]/black-scholes-option-pricing.git
cd black-scholes-option-pricing
```

2. Lancez Jupyter Notebook :
```bash
jupyter notebook companion.ipynb
```

3. Exécutez les cellules séquentiellement pour :
   - Définir les paramètres du modèle
   - Calculer les prix avec les deux méthodes
   - Visualiser les résultats et les Greeks

## 📐 Modèle Mathématique

### Paramètres

| Symbole | Description | Valeur par défaut |
|---------|-------------|-------------------|
| S | Prix de l'actif sous-jacent | 100 |
| K | Prix d'exercice (strike) | 100 |
| T | Maturité (années) | 1.0 |
| r | Taux d'intérêt sans risque | 0.05 |
| σ | Volatilité | 0.2 |

### Équation de Black–Scholes

L'EDP gouvernant le prix de l'option V(t,S) :

```
∂V/∂t + (1/2)σ²S² ∂²V/∂S² + rS ∂V/∂S - rV = 0
```

Avec condition terminale : V(T,S) = max(S-K, 0)

### Formule Analytique

```
V(t,S) = S·Φ(d₁) - K·e^(-r(T-t))·Φ(d₂)
```

Où :
- d₁ = [ln(S/K) + (r + σ²/2)(T-t)] / [σ√(T-t)]
- d₂ = d₁ - σ√(T-t)
- Φ : fonction de répartition de la loi normale standard

## 📈 Résultats

Le notebook génère plusieurs visualisations :

1. **Comparaison des méthodes** : graphique montrant la convergence entre solution analytique et FDM
2. **Greeks** : sensibilités du prix aux paramètres (Delta, Gamma, Theta)
3. **Surface de prix** : évolution du prix en fonction du temps et du prix de l'actif

## 🧪 Exemple de Code

```python
# Paramètres du modèle
S0 = 100      # Prix actuel de l'actif
K = 100       # Strike
T = 1.0       # Maturité (1 an)
r = 0.05      # Taux sans risque (5%)
sigma = 0.2   # Volatilité (20%)

# Calcul du prix analytique
price_bs = black_scholes_call(S0, K, T, r, sigma)
print(f"Prix Black-Scholes : {price_bs:.4f}")

# Calcul des Greeks
delta = compute_delta(S0, K, T, r, sigma)
gamma = compute_gamma(S0, K, T, r, sigma)
theta = compute_theta(S0, K, T, r, sigma)
```

## 📚 Concepts Clés

### Greeks

- **Delta (Δ)** : sensibilité au prix de l'actif sous-jacent
- **Gamma (Γ)** : sensibilité de Delta au prix de l'actif
- **Theta (Θ)** : sensibilité au passage du temps (time decay)
- **Vega (ν)** : sensibilité à la volatilité
- **Rho (ρ)** : sensibilité au taux d'intérêt

## 🔬 Méthode Numérique

La méthode des différences finies utilise :
- **Discrétisation spatiale** : grille uniforme pour S
- **Discrétisation temporelle** : pas de temps adaptatif
- **Schéma implicite** : stabilité inconditionnelle
- **Conditions aux limites** : 
  - S = 0 : V = 0
  - S → ∞ : V ≈ S - K·e^(-r·τ)

## 🎓 Références

- Black, F., & Scholes, M. (1973). "The Pricing of Options and Corporate Liabilities". *Journal of Political Economy*, 81(3), 637-654.
- Wilmott, P. (2006). *Paul Wilmott on Quantitative Finance*. John Wiley & Sons.

## 📝 Structure du Projet

```
black-scholes-option-pricing/
├── companion.ipynb          # Notebook principal
├── README.md               # Ce fichier
├── requirements.txt        # Dépendances Python
└── paper/                  # Documentation théorique (optionnel)
```

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer de nouvelles fonctionnalités
- Améliorer la documentation

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👤 Auteur

[Votre Nom] - [Votre Email/GitHub]

## 🙏 Remerciements

- Communauté Python scientifique (NumPy, SciPy, Matplotlib)
- Ressources pédagogiques en finance quantitative
