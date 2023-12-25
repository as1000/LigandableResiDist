import pandas as pd

working_dir = "/path/to/working_dir/"

df = pd.read_excel(working_dir + "merged_rcsb_calls_ffilled_filtered_distance_annotated.xlsx")

new_method = df['Gene_Name'].tolist()

df3 = pd.read_csv(working_dir + "protein_class_Enzymes.tsv", sep="\t")
gene = df3['Gene'].tolist()
biol_process = df3['Biological process'].tolist()
mol_func = df3['Molecular function'].tolist()
pclass = df3['Protein class'].tolist()

biol_dict = dict(zip(gene,biol_process))
mol_dict = dict(zip(gene,mol_func))
pclass_dict = dict(zip(gene,pclass))

new_mol = []
new_biol = []
new_pclass = []

for a in new_method:
    temp_vals = a.split(", ")
    print(temp_vals)

    list1 = []
    list2 = []
    list3 = []

    for q in temp_vals:
        try:
            list1.append(mol_dict[q])
        except:
            list1.append("Not_Annotated")
        try:
            list2.append(biol_dict[q])
        except:
            list2.append("Not_Annotated")
        try:
            list3.append(pclass_dict[q])
        except:
            list3.append("Not_Annotated")
    
    new_mol.append(list1)
    new_biol.append(list2)
    new_pclass.append(list3)

df['Biological_Process'] = new_biol
df['Molecular_Function'] = new_mol
df['Protein_Class'] = new_pclass

val1 = df['Protein_Class'].tolist()
val2 = df['Molecular_Function'].tolist()
val3 = df['Biological_Process'].tolist()
val4 = df['Title'].tolist()

enzyme_val = []

q=0
while q<len(val1):
    string = str(val1[q]) + str(val2[q]) + str(val3[q]) + str(val4[q])
    if "Enzyme" in string:
        enzyme_val.append(1)
    else:
        enzyme_val.append(0)
    q=q+1

df['Enzyme'] = enzyme_val

df.to_excel(working_dir + "merged_rcsb_calls_ffilled_filtered_distance_annotated.xlsx", index=False)
