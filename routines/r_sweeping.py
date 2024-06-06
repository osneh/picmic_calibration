#!/usr/bin/env python3

import pandas as pd
import numpy as np
import argparse
import sys

def BARS():
    print(40*':=')

##########################################
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-fscan", "--file_scan" ,help="provide scan file")
    parser.add_argument("-fcali", "--file_cali" ,help="provide calibrated file")
    parser.add_argument("-sweeping","--RL",help="Sweeping Right(1) or Left(0)", action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    if ( (str(args.file_scan)=='None') & (str(args.file_cali)=='None') ) :
        print("----------------------- >>>>>>>>>>>>>>>> Input files -- Mandatory   <<<<<<<<<<<<<<<<<<<-------------------------")
        print('Script not executed')
        exit()

    filescan = str(args.file_scan)
    filecali = str(args.file_cali)
    print(filescan)
    print(filecali)
    
    df_scan = pd.read_csv(filescan)
    df_cali = pd.read_csv(filecali)
    ##df_comb = df_dig.copy()

    ##print(df_pul)
    BARS()
    
    exit()
    df_pul_filter = df_pul[df_pul.Delta<100]
    #pulse_list = df_pul_filter.Scan.tolist()
    digital_list = df_dig.Scan.tolist()
    
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