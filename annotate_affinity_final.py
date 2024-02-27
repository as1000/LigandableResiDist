import pandas as pd
import numpy as np

df = pd.read_csv("merged_rcsb_calls.csv")
df['Symbol'] = df['Symbol'].replace(np.nan, "EQUAL")
df = df[df['Ligand'].notna()]
df = df.fillna(method='ffill')

uq_types = list(set(df['Type'].tolist()))
df['Combined'] = df['Entry ID'].astype(str)
uq_types = sorted(list(set(df['Type'].tolist())))

df2 = pd.read_excel("merged_rcsb_calls_ffilled_filtered_distance_annotated.xlsx")
df2_combined_vals = df2['Entry ID'].tolist()

for a in uq_types:
    temp_df = df[df['Type']==a]

    symbols_min = []
    symbols_max = []
    min_val = []
    max_val = []
    units = []

    q=0
    for b in df2_combined_vals:
        q=q+1
        sub_df = temp_df[temp_df['Combined']==b]
    
        if len(sub_df.index.tolist())>0:
        
            min_val_temp = min(sub_df['Value'].tolist())
            max_val_temp = max(sub_df['Value'].tolist())

            wx=0
            while wx<len(sub_df['Value'].tolist()):
                if sub_df['Value'].tolist()[wx]==min_val_temp:
                    break
                wx=wx+1

            wy=0
            while wy<len(sub_df['Value'].tolist()):
                if sub_df['Value'].tolist()[wy]==max_val_temp:
                    break
                wy=wy+1

            symbols_min.append(sub_df['Symbol'].tolist()[wx])
            symbols_max.append(sub_df['Symbol'].tolist()[wy])
            min_val.append(min_val_temp)
            max_val.append(max_val_temp)
            units.append(sub_df['Unit'].tolist()[0])
        else:
            symbols_min.append(np.nan)
            symbols_max.append(np.nan)
            min_val.append(np.nan)
            max_val.append(np.nan)
            units.append(np.nan)
        if q%100==0:
            print(q)
    
    del df2[a+"_Symbol"]
    df2[a+"_MinValueSymbol"] = symbols_min
    df2[a+"_MaxValueSymbol"] = symbols_max
    df2[a+"_MinValue"] = min_val
    df2[a+"_MaxValue"] = max_val
    df2[a+"_Unit"] = units

    print(a)

df2.to_excel("merged_rcsb_calls_ffilled_filtered_distance_annotated_affinity_annotation.xlsx", index=False)
