import numpy as np

# Constantes et incertitudes
N = 1000000  
lambda_val = 633e-9  
delta_lambda = 1e-9  
D = 1.00  
delta_D = 0.01 
d = 0.013  
delta_d = 0.001  

# Tirages aléatoires 
lambda_sim = np.random.uniform(lambda_val - delta_lambda, lambda_val + delta_lambda, N)
D_sim = np.random.uniform(D - delta_D, D + delta_D, N)
d_sim = np.random.uniform(d - delta_d, d + delta_d, N)

# Calcul de a_sim
a_sim = (2 * lambda_sim * D_sim) / d_sim

# incertitude-type
u_a_MT = np.std(a_sim, ddof=1)

# Résultats
print("################## a ##################")
print("Incertitude-type u(a) :", u_a_MT)
