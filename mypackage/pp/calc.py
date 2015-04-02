#!/usr/bin/python

# Paths
python_dir = '/home/jk125262/PythonDir_Cluster'
input_file_dir = '/home/jk125262/PythonDir_Cluster/exec/pp'

# Modules
import numpy as np
from numpy import linalg as la
from scipy import stats



def get_zsp_kalman(ip,dp,xs,ns,Gss_prior,zs_prior,Hy,R,zy,Gyy_prior,Gys_prior,Gssy):

    # -----------------------------------------
    # specific pilot point setup
    # -----------------------------------------
    jp       = np.arange(0,ip+1,dp) # position indices of pilot points up to position index ip
    mask = np.ones(len(xs),dtype=bool)
    mask[jp] = False
    jp_com   = np.arange(len(xs))[mask] # Complement of position indices
    xp       = xs[jp]           # positions of pilot points up to position index ip
    nploc     = xp.size          # number of first ip pilot points

    # pilot point matrices
    Xp        = np.ones([nploc,1])    # base function for uncertain mean
    Is        = np.eye(ns,ns)
    Hp        = Is[jp,:]
    Gsp_prior = Gss_prior[:,jp]        # cross-covariance s to p-locations
    Gps_prior = Gss_prior[jp,:]        # cross-covariance p-locations to s

    Grp_prior = Gsp_prior[jp_com,:]
    Gpr_prior = Gps_prior[:,jp_com]
    Gpp_prior = Gsp_prior[jp,:] 
    zp_prior  = zs_prior[jp]

    # Gpy_prior = np.dot( Gps_prior , Hy.T)
    Gyp_prior = np.dot( Hy , Gsp_prior )
    R_prior = R
    Hy_prior = Hy
    zy_prior = zy

    # -----------------------------------------
    # Pilot Point estimate
    # -----------------------------------------
    # # projection: s onto PP subspace of s: u = Ps*s
    Ps   = np.dot( np.dot(Gsp_prior,la.inv(Gpp_prior)) , Hp )
    N   = Is-Ps
    K         = np.dot( np.dot( Gps_prior , Hy_prior.T) , la.inv(Gyy_prior + R_prior)) # Kalman gain
    # zp_post = zp_prior + np.dot( K ,  zy_prior-np.dot(Hy_prior,zs_prior) )
    # step1_prior = np.dot( la.inv(Gyy_prior+R_prior), zy_prior-np.dot(Hy_prior,zs_prior))
    # step2_prior = np.dot(Hy_prior.T,step1_prior)
    # step3_prior = np.dot(Gps_prior,step2_prior)
    zp_post = zp_prior + np.dot( Gps_prior, np.dot( Hy_prior.T, np.dot( la.inv(Gyy_prior+R_prior), zy_prior-np.dot(Hy_prior,zs_prior))))
    # 
    Gps_post = Gps_prior - np.dot( K , Gys_prior )
    Gpp_post = Gps_post[:,jp].copy()
    Gsp_post = Gps_post.T.copy()
    Grp_post = Gsp_post[jp_com,:].copy()
    Gpr_post = Gps_post[:,jp_com].copy()

    zsp_post = np.dot( Gsp_prior, np.dot( la.inv(Gpp_prior), zp_post))


    zsp_post_j = zs_prior + np.dot(Ps,np.dot(Gss_prior,np.dot(Ps.T,np.dot(Hy_prior.T,np.dot(la.inv(Gyy_prior + R),zy_prior - np.dot(Hy_prior,zs_prior))))))
    Gss_post_j = Gss_prior - np.dot(Ps,np.dot(Gss_prior,np.dot(Ps.T,np.dot(Hy_prior.T,np.dot(la.inv(Gyy_prior + R),np.dot(Hy_prior,np.dot(Ps,np.dot(Gss_prior,Ps.T))))))))


    zp = zp_post
    zsp = zsp_post              # Output for plots
    
    estvar    = np.diag(Gssy).reshape(ns,1)   # estimation variance of s
    estvarp   = np.diag(Gss_post_j).reshape(ns,1)  # estimation variance of s plus error term

    return jp, zsp, estvar, estvarp, xp, zp, zsp_post_j, Gss_post_j
    # global zp_post, zsp_post, Gpp_prior, Gsp_prior, Gyy_prior, R_prior, Hy_prior,zy_prior
    # global step1_prior, step2_prior, step3_prior, Gps_prior, jp_com, K

    # return zsp_post_j, Gss_post_j, estvar, estvarp



#####################################################################################
#####################################################################################
#####################################################################################

# Function that outputs several arrays according to how many pilot points are in use
def get_zsp(ip,dp,xs,ns,Gss,beta_pri,Hy,Gyy,R,zy,Xy,Xs,Gssy,Gsy,Gys):
    # global jp, zsp, Gsspy, estvar, estvarp, xp, zp
    # global zsp_johannes, Gsspy_johannes, zp_johannes
    # global Ps, N, Gsp, Gps, Gpp, zp
    # 
    # -----------------------------------------
    # specific pilot point setup
    # -----------------------------------------
    jp       = range(0,ip+1,dp) # position indices of pilot points up to position index ip
    xp       = xs[jp]           # positions of pilot points up to position index ip
    nploc     = xp.size          # number of first ip pilot points

    # pilot point matrices
    Xp       = np.ones([nploc,1])    # base function for uncertain mean
    Is       = np.eye(ns,ns)
    Hp       = Is[jp,:]
    Gsp      = Gss[:,jp]        # cross-covariance s to p-locations
    Gps      = Gss[jp,:]        # cross-covariance p-locations to s
    Gpp      = Gsp[jp,:] 

    # -----------------------------------------
    # Pilot Point estimate
    # -----------------------------------------

    # projection: s onto PP subspace of s: u = Ps*s
    Ps   = np.dot( np.dot(Gsp,la.inv(Gpp)) , Hp )
    N   = Is-Ps

    zp = beta_pri*Xp + np.dot( Gps, np.dot( Hy.T, np.dot( la.inv(Gyy+R), zy-beta_pri*Xy)))
    zsp = beta_pri*Xs + np.dot( Gsp, np.dot( la.inv(Gpp), zp-beta_pri*Xp))
    #
    Gsspy = Gssy + np.dot( N, np.dot( Gsy, np.dot( la.inv(Gyy + R), np.dot( Gys, N.T))))
    # ATTENTION!!! THIS one would be WRONG:
    Gsspy2 = Gss - np.dot( Ps, np.dot( Gsy, np.dot( la.inv(Gyy + R), np.dot( Gys, Ps.T))))

    # Johannes updates
    zsp_johannes = beta_pri*Xs +np.dot(Ps, np.dot(Gss, np.dot(Ps.T, np.dot(Hy.T, np.dot(la.inv(Gyy + R), zy-beta_pri*Xy)))))
    zp_johannes = np.dot(Hp,zsp_johannes)
    Gsspy_johannes = Gss - np.dot( Ps , np.dot( Gss , np.dot(Ps.T, np.dot(Hy.T, np.dot( la.inv(Gyy + R), np.dot(Hy, np.dot(Ps, np.dot(Gss,Ps.T))))))))

    estvar    = np.diag(Gssy).reshape(ns,1)   # estimation variance of s
    estvarp   = np.diag(Gsspy).reshape(ns,1)  # estimation variance of s plus error term

    return jp, zsp, Gsspy, estvar, estvarp, xp, zp, zsp_johannes, Gsspy_johannes, zp_johannes
    # return zsp, Gsspy, estvar, estvarp



#####################################################################################
#####################################################################################
#####################################################################################


    # # -----------------------------------------
    # # OD criteria
    # # -----------------------------------------
    
    # estvar    = np.diag(Gssy).reshape(ns,1)   # estimation variance of s
    # estvarp   = np.diag(Gsspy).reshape(ns,1)  # estimation variance of s plus error term
    # aestvar   = np.mean(np.diag(Gssy)) # mean estmation variance of s
    # aestvarp  = np.mean(np.diag(Gsspy)) # mean estimation variance of s plus error term
    # adestvar  = np.mean(np.diag(np.dot(Hy,np.dot(Gssy,Hy.T)))) # mean estimation variance data
    # adestvarp = np.mean(np.diag(np.dot(Hy,np.dot(Gsspy,Hy.T)))) # mean estimation variance data plus error term
    # cestvar   = np.dot(c.T,np.dot(Gssy,c))                      # estimation variance of c
    # cestvarp  = np.dot(c.T,np.dot(Gsspy,c))                     # estimation variance of c
    # # destvar   = stats.gmean(la.eig(Gssy))                       # entropy
    # # destvarp  = stats.gmean(la.eig(Gsspy))                      # entropy

    # aestvar_record[ip]    = aestvar
    # aestvarp_record[ip]   = aestvarp
    # adestvar_record[ip]   = adestvar
    # adestvarp_record[ip]  = adestvarp
    # cestvar_record[ip]    = cestvar
    # cestvarp_record[ip]   = cestvarp
    # # destvar_record[ip]    = destvar
    # # destvarp_record[ip]   = destvarp


# #--------------------------------------------------
# # c - criterion
# #--------------------------------------------------

# c        = np.ones([ns,1])
# c        = c / np.sum(np.absolute(c))

# #--------------------------------------------------
# # OD criteria, prior stage
# #--------------------------------------------------

# prior_estvar   = np.diag(Gss)   # estimation variance
# prior_aestvar  = np.mean(np.diag(Gss)) # mean estimation variance
# prior_adestvar = np.mean(np.diag( np.dot( np.dot(Hy,Gss) , Hy.T ) )) # mean estimation variance of data
# prior_cestvar  = np.dot( np.dot(c.T,Gss) , c ) # estimation variance of c
# prior_cestvar = prior_cestvar[0,0]
# # prior_destvar  = stats.gmean(la.eig(Gss)[0][::-1])                # entropy of s

# # variables for recording
# aestvar_record    = np.zeros([ns,1]);
# aestvarp_record   = np.zeros([ns,1]);
# adestvar_record   = np.zeros([ns,1]);
# adestvarp_record  = np.zeros([ns,1]);
# cestvar_record    = np.zeros([ns,1]);
# cestvarp_record   = np.zeros([ns,1]);
# # destvar_record    = np.zeros(ns,1);
# # destvarp_record   = np.zeros(ns,1);
