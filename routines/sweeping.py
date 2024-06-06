#!/usr/bin/env python3

import pandas as pd
import numpy as np
import argparse
import sys
import matplotlib.pyplot as plt

def BARS():
    print(40*':=')

##########################################
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-fscan", "--file_scan" ,help="provide scan file")
    parser.add_argument("-fcali", "--file_cali" ,help="provide calibrated file")
    parser.add_argument("-sweeping","--RL",help="Sweeping Right(1) or Left(0)", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args()

    if ( (str(args.file_scan)=='None') & (str(args.file_cali)=='None') ) :
        print("----------------------- >>>>>>>>>>>>>>>> Input files -- Mandatory   <<<<<<<<<<<<<<<<<<<-------------------------")
        print('Script not executed')
        exit()

    filescan = str(args.file_scan)
    filecali = str(args.file_cali)
    filedigi_par = '../files/allDigital_VRefN-SCAN_24May2024_digital.csv'
    filealias = '../files/newlistWays.csv'
    ##print(filescan)
    print(filecali)
    ##print(args.RL)
    ##print(filedigi)
    
    df_scan = pd.read_csv(filescan)
    df_cali = pd.read_csv(filecali)
    df_digi_par = pd.read_csv(filedigi_par)
    df_alias= pd.read_csv(filealias)
    ##df_comb = df_dig.copy()

    ##print(df_pul)
    BARS()
    
    ##exit()
    ##print(df_digi)
    ##exit()
    ##df_pul_filter = df_pul[df_pul.Delta<100]
    #pulse_list = df_pul_filter.Scan.tolist()
    ##digital_list = df_dig.Scan.tolist()
    
    scanList =  list(df_scan.select_dtypes(include=['float64']).columns)
    
    print(scanList)
    
    
    
    
    
    
    
    BARS()
    
    print('dimension =',len(scanList))
    ##print('Unique dimension =',len(list(set(scanList))))
    
    #print(df_digi_par)
    
    #exit()
    
    ##vrefn1 = []
    ##vrefn2 = []
    ##ppreg = []
    
    
    
    
    
    for i, pixel in enumerate(scanList):
        print('-->>', i, '--',pixel)
        ##print('calibrated value: PPReg=',df_scan.PPReg[df_scan.Scan==pixel]) ## ,', VRefN2=',)
        ##print(df_cali[['VRefN','PPReg','PPReg']][df_cali.Scan==pixel])
        index_cali = df_cali[['VRefN','PPReg','PPReg']][df_cali.Scan==pixel].index
        
        if (len(index_cali)==0):
            continue
        idx_cali= index_cali[0]
        
        ##print('index==',idx_cali)
        
        zval_cali = df_cali.PPReg[idx_cali]
        xval_cali = df_cali.VRefN[idx_cali]
        
        print('PPREG value calibration=',xval_cali)
        print('VREFN value calibration=',zval_cali)
        
 
        min = 999.0
        idx_of_min = -1
        ppreg_of_min = -1
        vrefn_of_min = 999.0
        
        ##print('......................')
        df_temp = df_digi_par[['VRefN','PulsedReg','VRefN2']][ (df_digi_par.Scan==pixel) & (df_digi_par.VRefN2<249) ].sort_values(by='VRefN2',ascending=True)
        #print(df_digi_par[['VRefN','PulsedReg','VRefN2']][ (df_digi_par.Scan==pixel) & (df_digi_par.VRefN2<249) ].sort_values(by='VRefN2',ascending=True))
        #print(df_temp)
        for j in df_temp.index :
            xval = df_temp.VRefN2[j]
            zval = df_temp.PulsedReg[j]
            #if ( (xval_cali - x_val > 0 ) & ( z_val != zval_cali) ) :
            if ( (xval_cali - xval > 0 ) & ( abs(xval_cali-xval)<min  ) ) :
                min = xval_cali - xval
                idx_of_min = j
                ppreg_of_min = zval
                vrefn_of_min = xval
                ##print('min=',min)
        
        ##print(pixe (l)
        ##print(df_a)lia(s.Name[df_alias.RC==pi) xel])
        ##print(df_alias[df_alias.RC==pixel])
        print('......................')
        print('proposed PPReg =',ppreg_of_min)
        print('VRefN of proposed PPReg =',vrefn_of_min)
        print('----------------------')
        ##plt.plot(df_scan.VRefN,df_scan[pixel], label=pixel)
    ##plt.legend()
    ##plt.show()
    
    
    
    
    exit()
    
    list_df = []
    
    
    
    #for ich, ch in enumerate(pulse_list) :
    for i, ch in enumerate(digital_list) :
        df_propo_dig = df_dig[ (df_dig.Scan==ch)]
        df_propo_pul = df_pul[ (df_pul.Scan==ch)&(df_pul.Delta<100)]
        
        idx_list = df_propo_pul.index.tolist()
        
        if len(idx_list)!=0 :
        
            print('----------> ',ch,' <------------')
            print('-->digi')
            print(df_propo_dig)
            print('-->Pulse')
            print(df_propo_pul)
        
            #print(40*'--------------------')
            print('list=',idx_list)
        
            for j in idx_list:
                index_inPulse_Channel = j
                index_inDigital_Channel = df_propo_dig.index.tolist()

                if (len(index_inDigital_Channel)==0):
                    continue
            
                print('index in Digital=',index_inDigital_Channel[0])
                print('index in Pulse  =',index_inPulse_Channel)
            
                df_propo_dig.loc[index_inDigital_Channel[0]] = df_propo_pul.loc[index_inPulse_Channel]
    
        list_df.append(df_propo_dig)
    
    new_df=pd.concat(list_df)
    new_df.to_csv('fullVersion.csv',index=False)
    
    newnewdf = new_df[['Row','Col','PPReg']]
    newnewdf.to_csv('fullVersion_reduced.csv',index=False)

    print('----- DONE --------------')
    exit()
    
##########################################    
if __name__ == "__main__":
    main()