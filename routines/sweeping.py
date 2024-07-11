#!/usr/bin/env python3

import pandas as pd
import numpy as np
import argparse
import sys
import matplotlib.pyplot as plt
import os

def BARS():
    print(40*':=')
    
def changeSufixOutput( outfile ):
    print('-- inside --')
    print(outfile)
    ##tempoutput = outfile.split('/')[-1]
    tempoutput = os.path.basename(outfile)
    print('------------------------')
    print(tempoutput)
    print('------------------------')
    sufixword = tempoutput.split('_')[-2].split('.')[0]
    print(sufixword)
    print('------------------------')
    last = int(sufixword[-1])
    last+=1
    tempoutput = tempoutput.replace(sufixword[-1],str(last))
    return tempoutput

##########################################
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-fscan", "--file_scan" ,help="provide scan file")
    parser.add_argument("-fcali", "--file_cali" ,help="provide calibrated file")
    parser.add_argument("-sweeping","--RL",help="Sweeping Right(1) or Left(0)", required=False)
    args = parser.parse_args()

    if ( (str(args.file_scan)=='None') & (str(args.file_cali)=='None') ) :
        print("----------------------- >>>>>>>>>>>>>>>> Input files -- Mandatory   <<<<<<<<<<<<<<<<<<<-------------------------")
        print('Script not executed')
        exit()

    filescan = str(args.file_scan)
    filecali = str(args.file_cali)
    filedigi_par = '../files/allDigital_VRefN-SCAN_24May2024_digital.csv'
    filealias = '../files/newlistWays.csv'
    print('--------------------------')
    print('calibration:',filecali)
    print('--------------------------')
    print('scan:',filescan)
    print('---------------------------')
    #outputfile = changeSufixOutput(filecali.split('/')[-1])
    
    df_scan = pd.read_csv(filescan)
    df_cali = pd.read_csv(filecali)
    df_digi_par = pd.read_csv(filedigi_par)
    df_alias= pd.read_csv(filealias)
    
    BARS()
    
    scanList =  list(df_scan.select_dtypes(include=['float64']).columns)
    
    print('# of pixels to correct=',len(scanList))
    print('--List of pixels to correct--')
    print(scanList)


    ##exit()
    
    for i, pixel in enumerate(scanList):
        print('-->>', i, '--',pixel)
        ##print(df_cali[['VRefN','PPReg']][df_cali.Scan==pixel])
        index_cali = df_cali[['VRefN','PPReg']][df_cali.Scan==pixel].index
        
        if (len(index_cali)==0):
            continue
        idx_cali= index_cali[0]
        
        zval_cali = df_cali.PPReg[idx_cali]
        #xval_cali = df_cali.VRefN2[idx_cali]
        xval_cali = df_cali.VRefN[idx_cali]
        
        print('INDEX in calibration   =',idx_cali)
        print('PPREG  value calibration=',zval_cali)
        print('VREFN value calibration=',xval_cali)
        print('VREFN  value calibration=',wval_cali)
        
        min = 999.0
        idx_of_min = -1
        ppreg_of_min = -1
        vrefn_of_min = 999.0
        #vrefn2_of_min = 999.0
        
        df_temp = df_digi_par[['VRefN','PulsedReg','VRefN2']][ (df_digi_par.Scan==pixel) & (df_digi_par.VRefN2<249) ].sort_values(by='VRefN2',ascending=True)
      
        for j in df_temp.index :
            #wval = df_temp.VRefN[j]
            xval = df_temp.VRefN[j]
            zval = df_temp.PulsedReg[j]
           
            if ( (xval_cali - xval > 0 ) & ( abs(xval_cali-xval)<min  ) & ( zval_cali!=zval)  ) :
                min = xval_cali - xval
                idx_of_min = j
                ppreg_of_min = zval
                vrefn_of_min = xval 
        
        print('........')
        print('proposed PPReg =',ppreg_of_min)
        print('VRefN  of proposed PPReg =',vrefn_of_min)
        df_cali.loc[idx_cali,'PPReg'] = ppreg_of_min
        df_cali.loc[idx_cali,'rawIadj'] = ppreg_of_min
        df_cali.loc[idx_cali,'VRefN'] = vrefn_of_min
        df_cali.loc[idx_cali,'Delta'] = abs(df_cali.Mean[idx_cali] - vrefn_of_min)
        ##print('~~~~~~~~~~~~~~~~')
        ##print(df_cali[df_cali.Scan==pixel])
        ##print('--------------------------------------------')
    
    ##df_cali.to_csv('../files/'+outputfile,index=False)
    ##newdf = df_cali[['Row','Col','PPReg']]
    ##newdf.to_csv('../files/'+outputfile.split('.')[0]+'_reduced.csv',index=False)
    
    BARS()
    
    print('----- DONE --------------')
    exit()

##########################################    
if __name__ == "__main__":
    main()