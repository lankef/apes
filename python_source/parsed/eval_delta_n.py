# (dphi + iota_coef[0] * dchi) Delta_n = inhomogenous 
# This method evaluates the inhomogenous component, which serves as 
# the input to solve_dphi_iota_dchi(iota, f).
# Uses B_denom_coef_cp[n], p_perp_coef_cp[n], iota[(n-1)/2 or n/2].
# Must be evaluated with Delta_n=0 
from math import floor, ceil
from math_utilities import *
import chiphifunc
def eval_inhomogenous_Delta_n_cp(n,
    B_denom_coef_c,
    p_perp_coef_cp, 
    Delta_coef_cp,
    iota_coef):    
    def sum_arg_10(i261):
        # Child args for sum_arg_10    
        def sum_arg_9(i262):
            # Child args for sum_arg_9    
            def sum_arg_8(i281):
                # Child args for sum_arg_8
                return(B_denom_coef_c[i262-i281]*B_denom_coef_c[i281])
            
            return(diff(p_perp_coef_cp[(-n)-i262+2*i261],'chi',1)*is_seq(n-i261,i261-i262)*py_sum(sum_arg_8,0,i262))
        
        return(is_seq(0,n-i261)*iota_coef[n-i261]*is_integer(n-i261)*py_sum(sum_arg_9,0,i261))
    
    def sum_arg_7(i260):
        # Child args for sum_arg_7    
        def sum_arg_6(i220):
            # Child args for sum_arg_6
            return(B_denom_coef_c[i220]*B_denom_coef_c[n-i260-i220])
        
        return(diff(p_perp_coef_cp[i260],'phi',1)*py_sum(sum_arg_6,0,n-i260))
    
    def sum_arg_5(i257):
        # Child args for sum_arg_5    
        def sum_arg_4(i258):
            # Child args for sum_arg_4
            return(B_denom_coef_c[i258]*diff(Delta_coef_cp[(-n)-i258+2*i257],'chi',1)*is_seq(n-i257,i257-i258))
        
        return(is_seq(0,n-i257)*iota_coef[n-i257]*is_integer(n-i257)*py_sum(sum_arg_4,0,i257))
    
    def sum_arg_3(i256):
        # Child args for sum_arg_3
        return(B_denom_coef_c[i256]*diff(Delta_coef_cp[n-i256],'phi',1))
    
    def sum_arg_2(i283):
        # Child args for sum_arg_2    
        def sum_arg_1(i224):
            # Child args for sum_arg_1
            return(Delta_coef_cp[i224]*diff(B_denom_coef_c[(-n)+2*i283-i224],'chi',1))
        
        return(is_seq(0,n-i283)*iota_coef[n-i283]*is_integer(n-i283)*is_seq(n-i283,i283)*py_sum(sum_arg_1,0,2*i283-n))
    
    
    out = -(2*is_seq(0,n)*is_integer(n)*py_sum_parallel(sum_arg_7,0,n)+2*py_sum_parallel(sum_arg_5,ceil(n/2),floor(n))+2*is_seq(0,n)*is_integer(n)*py_sum_parallel(sum_arg_3,0,n)-py_sum_parallel(sum_arg_2,ceil(n/2),floor(n))+2*py_sum_parallel(sum_arg_10,ceil(n/2),floor(n)))/(2*B_denom_coef_c[0])
    return(out)
