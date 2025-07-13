import re
import numpy as np
import sys

def genrate_config_base(nele):
    nele_try = 0
    config_try = ''
    flag = 1
    n_principle = 1
    n_angular = 0
    list_auger = ['s', 'p', 'd', 'f', 'g', 'h']
    while flag:
        nele_try += 1
        nshell_tot = 0
        for i in range(n_principle):
            nshell_tot += 2 * np.power(i, 2)
        nshell_tot_2 = 0
        for i in range(n_principle+1):
            nshell_tot_2 += 2*np.power(i,2)
        # print(nshell_tot)
        if nele_try > nshell_tot_2:
            n_principle += 1
            n_angular = 0
            nshell_tot = nshell_tot_2
            nshell_tot_2 = nshell_tot_2 + 2*np.power(n_principle, 2)
        nshell_nangular_tot = nshell_tot
        nshell_nangular_tot_2 = nshell_tot
        for i in range(n_angular):
            nshell_nangular_tot += 2*(2*i+1)
        for i in range(n_angular + 1):
            nshell_nangular_tot_2 += 2*(2*i+1)
        # print(nshell_nangular_tot)
        if nele_try - nshell_tot == 1:
            pass
        elif nshell_nangular_tot_2 < nele_try :
            n_angular += 1
            nshell_nangular_tot = nshell_nangular_tot_2
            nshell_nangular_tot_2 += 2*(2*n_angular+1)
        str_shell = str(n_principle) + list_auger[n_angular]
        # print('str_shell:{}'.format(str_shell))
        nele_try_sub = nele_try - nshell_tot
        for i in range(n_angular):
            nele_try_sub = nele_try_sub - 2*(2*i+1)
        # print(nele_try_sub)
        if re.search(str_shell, config_try):
            config_try = config_try[:-3]
            str_config_2 = str_shell+ str(nele_try_sub)
            config_try  = config_try + str_config_2
        else:
            str_config_2 = str_shell+ str(nele_try_sub)
            config_try = config_try + str_config_2
        # print(config_try)
        if nele_try == nele:
            flag = 0
    return config_try

if __name__ == '__main__':
  nele = 28
  config = generate_config_base(nele)
  print(config)
