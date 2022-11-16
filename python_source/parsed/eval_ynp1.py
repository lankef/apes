# Coefficient for Yn+1 - only X1 and Balpha0 needed
from math import floor, ceil
from math_utilities import *
import chiphifunc
def coef_a(n, B_alpha_coef, X_coef_cp):    
    
    out = (B_alpha_coef[0]*diff(X_coef_cp[1],'chi',1)*((-n)-1))/2
    return(out)


# Coefficient for dchi Yn+1  - only X1 and Balpha0 needed
def coef_b(B_alpha_coef, X_coef_cp):    
    
    out = (B_alpha_coef[0]*X_coef_cp[1])/2
    return(out)


# RHS - LHS 
# Used in (conv(a) + conv(b)@dchi)@Yn+1 = RHS - LHS(Yn+1 = 0) 
# Must run with Yn+1=0.# Depends on Xn+1, Yn, Zn, B_theta n, B_psi n-2
# iota (n-2)/2 or (n-3)/2, B_alpha n/2 or (n-1)/2.
def rhs_minus_lhs(n,
    X_coef_cp,
    Y_coef_cp,
    Z_coef_cp,
    B_psi_coef_cp,
    B_theta_coef_cp,
    B_alpha_coef,
    kap_p, dl_p, tau_p,
    iota_coef):    
    def sum_arg_31(i82):
        # Child args for sum_arg_31    
        def sum_arg_30(i80):
            # Child args for sum_arg_30
            return(B_theta_coef_cp[i80]*X_coef_cp[n-i82-i80+2])
        
        return(i82*X_coef_cp[i82]*py_sum(sum_arg_30,0,n-i82+2))
    
    def sum_arg_29(i78):
        # Child args for sum_arg_29    
        def sum_arg_28(i76):
            # Child args for sum_arg_28
            return(B_theta_coef_cp[i76]*Y_coef_cp[n-i78-i76+2])
        
        return(i78*Y_coef_cp[i78]*py_sum(sum_arg_28,0,n-i78+2))
    
    def sum_arg_27(i74):
        # Child args for sum_arg_27    
        def sum_arg_26(i72):
            # Child args for sum_arg_26
            return(B_psi_coef_cp[i72]*X_coef_cp[n-i74-i72])
        
        return(diff(X_coef_cp[i74],'chi',1)*py_sum(sum_arg_26,0,n-i74))
    
    def sum_arg_25(i70):
        # Child args for sum_arg_25    
        def sum_arg_24(i68):
            # Child args for sum_arg_24
            return(B_psi_coef_cp[i68]*Y_coef_cp[n-i70-i68])
        
        return(diff(Y_coef_cp[i70],'chi',1)*py_sum(sum_arg_24,0,n-i70))
    
    def sum_arg_23(i260):
        # Child args for sum_arg_23    
        def sum_arg_22(i96):
            # Child args for sum_arg_22
            return(B_psi_coef_cp[i96]*diff(X_coef_cp[n-i96-i260],'chi',1))
        
        return(diff(Y_coef_cp[i260],'phi',1)*py_sum(sum_arg_22,0,n-i260))
    
    def sum_arg_21(i264):
        # Child args for sum_arg_21    
        def sum_arg_20(i100):
            # Child args for sum_arg_20
            return(B_psi_coef_cp[i100]*diff(X_coef_cp[n-i264-i100],'phi',1))
        
        return(diff(Y_coef_cp[i264],'chi',1)*py_sum(sum_arg_20,0,n-i264))
    
    def sum_arg_19(i256):
        # Child args for sum_arg_19    
        def sum_arg_18(i98):
            # Child args for sum_arg_18
            return((B_theta_coef_cp[i98]*n+((-i98)-i256+2)*B_theta_coef_cp[i98])*X_coef_cp[n-i98-i256+2])
        
        return(diff(Y_coef_cp[i256],'phi',1)*py_sum(sum_arg_18,0,n-i256+2))
    
    def sum_arg_17(i90):
        # Child args for sum_arg_17    
        def sum_arg_16(i88):
            # Child args for sum_arg_16
            return((B_theta_coef_cp[i88]*n-B_theta_coef_cp[i88]*i90+(2-i88)*B_theta_coef_cp[i88])*Y_coef_cp[n-i90-i88+2])
        
        return(Z_coef_cp[i90]*py_sum(sum_arg_16,0,n-i90+2))
    
    def sum_arg_15(i86):
        # Child args for sum_arg_15    
        def sum_arg_14(i84):
            # Child args for sum_arg_14
            return(B_psi_coef_cp[i84]*Z_coef_cp[n-i86-i84])
        
        return(diff(Y_coef_cp[i86],'chi',1)*py_sum(sum_arg_14,0,n-i86))
    
    def sum_arg_13(i261):
        # Child args for sum_arg_13    
        def sum_arg_12(i262):
            # Child args for sum_arg_12
            return((((-i262)+2*i261-2)*diff(Y_coef_cp[i262],'chi',1)*X_coef_cp[(-n)-i262+2*i261-2]-diff(Y_coef_cp[i262],'chi',1)*X_coef_cp[(-n)-i262+2*i261-2]*n)*is_seq(n-i261+2,i261-i262))
        
        return(is_seq(0,n-i261+2)*B_alpha_coef[n-i261+2]*is_integer(n-i261+2)*py_sum(sum_arg_12,0,i261))
    
    def sum_arg_11(i109):
        # Child args for sum_arg_11    
        def sum_arg_10(i110):
            # Child args for sum_arg_10
            return((((-i110)+2*i109-2)*diff(X_coef_cp[i110],'chi',1)*Y_coef_cp[(-n)-i110+2*i109-2]-diff(X_coef_cp[i110],'chi',1)*Y_coef_cp[(-n)-i110+2*i109-2]*n)*is_seq(n-i109+2,i109-i110))
        
        return(is_seq(0,n-i109+2)*B_alpha_coef[n-i109+2]*is_integer(n-i109+2)*py_sum(sum_arg_10,0,i109))
    
    def sum_arg_9(i106):
        # Child args for sum_arg_9    
        def sum_arg_8(i104):
            # Child args for sum_arg_8
            return((B_theta_coef_cp[i104]*n-B_theta_coef_cp[i104]*i106+(2-i104)*B_theta_coef_cp[i104])*Y_coef_cp[n-i106-i104+2])
        
        return(diff(X_coef_cp[i106],'phi',1)*py_sum(sum_arg_8,0,n-i106+2))
    
    def sum_arg_7(i265):
        # Child args for sum_arg_7    
        def sum_arg_6(i266):
            # Child args for sum_arg_6    
            def sum_arg_5(i722):
                # Child args for sum_arg_5
                return(diff(X_coef_cp[(-i722)-i266+i265],'chi',1)*i722*Y_coef_cp[i722])
            
            return(is_seq(0,(-n)+i266+i265-2)*B_theta_coef_cp[(-n)+i266+i265-2]*is_integer((-n)+i266+i265-2)*is_seq((-n)+i266+i265-2,i266)*py_sum(sum_arg_5,0,i265-i266))
        
        return(iota_coef[n-i265+2]*py_sum(sum_arg_6,0,i265))
    
    def sum_arg_4(i257):
        # Child args for sum_arg_4    
        def sum_arg_3(i258):
            # Child args for sum_arg_3    
            def sum_arg_2(i706):
                # Child args for sum_arg_2
                return(diff(Y_coef_cp[(-i706)-i258+i257],'chi',1)*i706*X_coef_cp[i706])
            
            return(is_seq(0,(-n)+i258+i257-2)*B_theta_coef_cp[(-n)+i258+i257-2]*is_integer((-n)+i258+i257-2)*is_seq((-n)+i258+i257-2,i258)*py_sum(sum_arg_2,0,i257-i258))
        
        return(iota_coef[n-i257+2]*py_sum(sum_arg_3,0,i257))
    
    def sum_arg_1(i111):
        # Child args for sum_arg_1
        return(is_seq(0,n-i111)*diff(Z_coef_cp[2*i111-n],'chi',1)*iota_coef[n-i111]*is_integer(n-i111)*is_seq(n-i111,i111))
    
    
    out = -((is_seq(0,n+2)*dl_p*is_integer(n+2)*py_sum_parallel(sum_arg_31,0,n+2)+is_seq(0,n+2)*dl_p*is_integer(n+2)*py_sum_parallel(sum_arg_29,0,n+2)-2*is_seq(0,n)*dl_p*is_integer(n)*py_sum_parallel(sum_arg_27,0,n)-2*is_seq(0,n)*dl_p*is_integer(n)*py_sum_parallel(sum_arg_25,0,n))*tau_p+is_seq(0,n+2)*is_integer(n+2)*py_sum_parallel(sum_arg_9,0,n+2)+py_sum_parallel(sum_arg_7,ceil(n/2)+1,floor(n)+2)-py_sum_parallel(sum_arg_4,ceil(n/2)+1,floor(n)+2)+2*is_seq(0,n)*is_integer(n)*py_sum_parallel(sum_arg_23,0,n)-2*is_seq(0,n)*is_integer(n)*py_sum_parallel(sum_arg_21,0,n)-is_seq(0,n+2)*is_integer(n+2)*py_sum_parallel(sum_arg_19,0,n+2)+is_seq(0,n+2)*dl_p*kap_p*is_integer(n+2)*py_sum_parallel(sum_arg_17,0,n+2)-2*is_seq(0,n)*dl_p*kap_p*is_integer(n)*py_sum_parallel(sum_arg_15,0,n)+py_sum_parallel(sum_arg_13,ceil(n/2)+1,floor(n)+2)-py_sum_parallel(sum_arg_11,ceil(n/2)+1,floor(n)+2)-2*py_sum_parallel(sum_arg_1,ceil(n/2),floor(n))-2*is_seq(0,n)*is_integer(n)*diff(Z_coef_cp[n],'phi',1)+2*is_seq(0,n)*dl_p*kap_p*X_coef_cp[n]*is_integer(n))/2
    return(out)
