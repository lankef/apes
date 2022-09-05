from math import floor, ceil
from math_utilities import *
import chiphifunc
def eval_Z3_cp(X_coef_cp, Y_coef_cp, Z_coef_cp,             B_theta_coef_cp, B_psi_coef_cp,             B_alpha_coef,             kap_p, dl_p, tau_p, iota_coef):    
    
    out = -((2*X_coef_cp[1]*Y_coef_cp[2]-2*Y_coef_cp[1]*X_coef_cp[2])*dl_p*tau_p+(2*B_psi_coef_cp[0]*X_coef_cp[1]**2*diff(Y_coef_cp[1],'chi',1)-2*B_psi_coef_cp[0]*X_coef_cp[1]*Y_coef_cp[1]*diff(X_coef_cp[1],'chi',1)+2*X_coef_cp[1]*Z_coef_cp[2])*dl_p*kap_p+((-2*B_psi_coef_cp[0]*X_coef_cp[1]*diff(Y_coef_cp[2],'chi',1))+2*B_psi_coef_cp[0]*Y_coef_cp[1]*diff(X_coef_cp[2],'chi',1)-2*B_psi_coef_cp[1]*X_coef_cp[1]*diff(Y_coef_cp[1],'chi',1)+2*B_psi_coef_cp[1]*Y_coef_cp[1]*diff(X_coef_cp[1],'chi',1)+2*X_coef_cp[1]*B_theta_coef_cp[2]*Y_coef_cp[2]-2*Y_coef_cp[1]*B_theta_coef_cp[2]*X_coef_cp[2])*dl_p+(2*B_alpha_coef[0]*Y_coef_cp[1]*X_coef_cp[2]-2*B_alpha_coef[0]*X_coef_cp[1]*Y_coef_cp[2])*diff(Z_coef_cp[2],'chi',1)+2*Y_coef_cp[1]*diff(Y_coef_cp[2],'phi',1)+(2*B_alpha_coef[0]*X_coef_cp[1]*Z_coef_cp[2]+2*iota_coef[0]*Y_coef_cp[1])*diff(Y_coef_cp[2],'chi',1)+2*X_coef_cp[1]*diff(X_coef_cp[2],'phi',1)+(2*iota_coef[0]*X_coef_cp[1]-2*B_alpha_coef[0]*Y_coef_cp[1]*Z_coef_cp[2])*diff(X_coef_cp[2],'chi',1)+3*B_alpha_coef[0]*X_coef_cp[1]*Z_coef_cp[3]*diff(Y_coef_cp[1],'chi',1)-3*B_alpha_coef[0]*Y_coef_cp[1]*Z_coef_cp[3]*diff(X_coef_cp[1],'chi',1))/(6*dl_p)
    return(out)
