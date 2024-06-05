import pandas as pd
import numpy as np
from os import listdir

def getPisteId(m_row,m_col):
    
    tempdf = pd.read_csv("/home/habreu/WORK/data_bin2ascii/listWays.csv")
    #print("Row-->",m_row,"Col-->",m_col)
    name =  tempdf['Name'][    (tempdf['Column']==m_col) &  (tempdf['Row']==m_row) ].to_list()  
    #print(name)
    #print('len name = ', name)
    #id = tempdf.Name.iloc[name].at(0)
    id = "R"+str(m_row)+"-C"+str(m_col)
    #print("id=",id)
    
    if ( len(name)>0 ) :
        id = name[0].strip()
    del tempdf
    return id

def getPisteIdRaw(m_row,m_col):
    id = "R"+str(m_row)+"-C"+str(m_col)
    return id

def cleanPandaPicmic(mypd, xAxis='VBN_adj') : 
    my_df = mypd.copy()
    my_df = my_df.dropna(axis=1)
    dim_data = len(my_df.columns)
    mylist = []
    mylist.append(xAxis)

    for i in range(1,dim_data) :
        ##my_pixel = 'R'+str(int(my_df.iloc[0].at[i]))+'-C'+str(int(my_df.iloc[1].at[i]))
        my_pixel = getPisteId(int(my_df.iloc[0].at[i]),int(my_df.iloc[1].at[i]))
        ##print('-------',my_pixel,i)
        temp = 'VBN_adj' if i == 0 else my_pixel
        mylist.append(temp)
        ##print(my_pixel,i,temp)

    ##print(mylist)  
    my_dict = {idx : mylist[idx] for idx in range(0,dim_data)}
    ##print(my_dict)
    
    my_df.rename(columns = my_dict, inplace=True) # rename columns 0 and 1
    #my_df = my_df.astype({0:'float',1:'float'})
    my_df = my_df.tail(-2) # to delete the two first rows
    #my_df = my_df.astype({'VBN_adj':'float','Eff_trig_'+my_way:'float'})
    my_df[xAxis] = my_df[xAxis].astype(int)
    my_df[mylist] = my_df[mylist].astype(float)
    return my_df

def dataframe_concat(var='VRefN',name='concat_scurves.csv'):
    
    mylist = [ x for x in listdir() if x.endswith(".txt") ]    
    dflist = [pd.read_csv(f) for f in mylist]
    
    pd_concat = pd.concat(dflist)
    pd_concat = pd_concat.fillna(0)
    pd_concat = pd_concat.sort_values(by=[var])
   
    pd_concat.reset_index(drop=True, inplace=True)
    pd_concat.sort_index(inplace=True)

    lastIndex = pd_concat.idxmax()[var]
    lastVal = pd_concat[var].min()

    zero = [0 for i in range(len(pd_concat.columns))]
   
    for i in range(lastVal):
        zero[0] = int(i)
        idx=lastIndex+i
        pd_concat.loc[idx] = zero 
  
    pd_concat = pd_concat.sort_values(by='VRefN')
    
    pd_concat.to_csv(name,index=False)
    
    
def dataframe_concat_standalone(mylist, var='VRefN',name='concat_scurves.csv'):
    
    ##if ( len(mylist)==0 ) :
    ##    break
    ##mylist = [ x for x in listdir() if x.endswith(pattern) ]    
    #mylist.sort()
    
    #for idx, i in enumerate(mylist) :
    #    print(idx, i)
    
    #print(10*'-')    
    ##exit()
        
    
    dflist = [pd.read_csv(f) for f in mylist]
    
    pd_concat = pd.concat(dflist)
    pd_concat = pd_concat.fillna(0)
    pd_concat = pd_concat.sort_values(by=[var])
   
    
    
    ##exit() 
     
    pd_concat.reset_index(drop=True, inplace=True)
    pd_concat.sort_index(inplace=True)
    
    #print(pd_concat)
    #print('------------------------------------')
    
    lastIndex = pd_concat.idxmax()[var]
    firstVal = pd_concat[var].min()

    #print('last Index = ', lastIndex)
    #print('fisrt Val   = ', firstVal)  
    
    ##print('------------------------------------')
    ##print(pd_concat)
    
    ##exit()
    ##print('----------------------------------------')
    
    zero = [0 for i in range(len(pd_concat.columns))]
    
    
    var_x = pd_concat[var].to_list()
    var_all = np.arange(0,251,1).tolist()
    
    
    for i in var_x:
        var_all.remove(i)
        
    index = len(var_all)
    
    for val in var_all :
        zero[0] = int(val)
        pd_concat.loc[index] = zero
        index+=1 
   
    ##exit() 
   
    ##for i in range(0,firstVal):
        #print(i)
    ##    zero[0] = int(i)
    ##    idx=lastIndex+i+1
    ##    pd_concat.loc[idx] = zero 
  
  
    #print(pd_concat)
    ##print('---------------------')
    ##print(pd_concat)
    #print(pd_concat[var].to_list())
  
    ##print('---------------------')
    
    
    
    
  
    pd_concat = pd_concat.sort_values(by=[var])
    ##print(pd_concat)
    
    ###exit()
    
    '''
    listOfColumns = pd_concat.select_dtypes(include=['float64']).columns.to_list()
    ##print(listOfColumns)
    ##print('.............................................')
    for i in listOfColumns:
        nums = i.split('-')
        ##print(nums,i)
        temp_alias = getPisteId(int(nums[0][1:]),int(nums[1][1:])).strip()
        ##print(i, temp_alias)
        pd_concat.rename(columns={i:temp_alias}, inplace=True)
    '''
    ##print(pd_concat)
    ##exit()
    #print(pd_concat)
    pd_concat.to_csv(name,index=False)
    
    
def dataframe_concat_standalone_digital(mylist, var='VRefN',name='concat_scurves.csv'):
    
    dflist = [pd.read_csv(f) for f in mylist]
    
    pd_concat = pd.concat(dflist)
    pd_concat = pd_concat.fillna(0)
    pd_concat = pd_concat.sort_values(by=[var])
   
    #print(pd_concat)
   
    pd_concat.reset_index(drop=True, inplace=True)
    pd_concat.sort_index(inplace=True)
    
    lastIndex = pd_concat.idxmax()[var]
    firstVal = pd_concat[var].min()
    #lastVal = pd_concat[var].min()
    
    zero = [0 for i in range(len(pd_concat.columns))]
   
    #print('HERE 01')
   
    #for i in range(lastVal):
    for i in range(0,firstVal):
        zero[0] = int(i)
        idx=lastIndex+i+1
        pd_concat.loc[idx] = zero 
    
    
    #print('HERE 02')
    #pd_concat = pd_concat.sort_values(by='VRefN')
    pd_concat = pd_concat.sort_values(by=[var])
    pd_concat.to_csv(name,index=False)
 
    #print('HERE 03')
