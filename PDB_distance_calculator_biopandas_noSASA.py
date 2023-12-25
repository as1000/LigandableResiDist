import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist
import os
import re
from itertools import chain
from biopandas.pdb import PandasPdb
from Bio.PDB import PDBParser

#Run on High Affinity csv sent to Amit / Ellen

df = pd.read_excel("/Users/ananthansadagopan/Documents/ChoudharyLab/PTMs/merged_rcsb_calls_ffilled_filtered.xlsx")
#df = df[df['Entry ID']!="0003"]
all_pdbs = df['Entry ID'].tolist()
all_ligands = df['Ligand ID'].tolist()

ww=0
while ww<len(all_pdbs):

    p = PDBParser(QUIET=1)

    end = 0

    value = all_pdbs[ww]
    ligand = all_ligands[ww]
    
    """
    pdb = "/Users/ananthansadagopan/Downloads/" + str(value) + ".pdb"
    pdb_gz = "/Users/ananthansadagopan/Downloads/" + str(value) + ".pdb.gz"

    print(pdb_gz)

    pdb_download = "/Users/ananthansadagopan/Downloads/" + str(value) + "_download.txt"

    with open(pdb_download, 'a+') as the_file:
        the_file.write(value)

    os.system("chmod +x /Users/ananthansadagopan/Downloads/batch_download.sh")
    os.system("/Users/ananthansadagopan/Downloads/batch_download.sh -o /Users/ananthansadagopan/Downloads/ -f %s -p" % (pdb_download))
    os.system("gunzip -k %s" % pdb)

    try:
        struct = p.get_structure(value, pdb)
    except:
        ww=ww+1
        continue
    sr = ShrakeRupley()

    try:
        sr.compute(struct, level="S")
    except:
        ww=ww+1
        continue
    """

    #temp_ligand_coords = "/Users/ananthansadagopan/Downloads/" + str(value) + "_ligand_temp.txt"
    #ligand_coords = "/Users/ananthansadagopan/Downloads/" + str(value) + "_ligand.txt"

    #os.system("grep %s %s > %s" % (ligand,pdb,temp_ligand_coords)) #Need to choose the ligand
    #os.system("grep 'HETATM' %s > %s" % (temp_ligand_coords,ligand_coords))

    #file1 = open(ligand_coords, 'r')
    #lines = file1.readlines()

    #temp_vals = []
    #for q in lines:
    #    temp_vals.append(re.sub(' +', ' ', q).split(" "))
        
    #df = pd.DataFrame(temp_vals)

    print(value)
    ppdb = PandasPdb().fetch_pdb(value)
    df_temp = ppdb.df['HETATM']
    df_temp = df_temp[df_temp['residue_name']==ligand]

    xvals = df_temp['x_coord'].tolist()
    yvals = df_temp['y_coord'].tolist()
    zvals = df_temp['z_coord'].tolist()   

    s1 = []

    try:
        a=0
        while a<len(xvals):
            s1.append((float(xvals[a]),float(yvals[a]),float(zvals[a])))
            a=a+1
    except ValueError:
        ww=ww+1
        continue

    s1 = np.array(s1)

    residues_to_iterate = ['LYS', 'CYS', 'MET', 'TYR']
    xvals_ref = []
    yvals_ref = []
    zvals_ref = []
    atom_ref = []
    chain_ref = []
    resi_ref = []
    resi_type_ref = []

    for temp_residue in residues_to_iterate:

        """
        temp_coords = "/Users/ananthansadagopan/Downloads/" + str(value) + "_" + temp_residue + "_temp.txt"
        inter_coords = "/Users/ananthansadagopan/Downloads/" + str(value) + "_" + temp_residue + "_inter.txt"
        final_coords = "/Users/ananthansadagopan/Downloads/" + str(value) + "_" + temp_residue + ".txt"
        os.system("grep %s %s > %s" % (temp_residue,pdb,temp_coords))
        os.system("grep 'ATOM' %s > %s" % (temp_coords,inter_coords))
        
        if temp_residue == "LYS":
            os.system("grep 'NZ ' %s > %s" % (inter_coords,final_coords))
        elif temp_residue == "CYS":
            os.system("grep 'SG ' %s > %s" % (inter_coords,final_coords))
        elif temp_residue == "MET":
            os.system("grep 'SD ' %s > %s" % (inter_coords,final_coords))
        elif temp_residue == "TYR":
            os.system("grep 'OH ' %s > %s" % (inter_coords,final_coords))

        file1 = open(final_coords, 'r')
        lines = file1.readlines()

        temp_vals = []
        for q in lines:
            temp_vals.append(re.sub(' +', ' ', q).split(" "))

        df = pd.DataFrame(temp_vals)
        """

        df_temp = ppdb.df['ATOM']
        df_temp = df_temp[df_temp['residue_name']==temp_residue]

        if temp_residue == "LYS":
            df_temp = df_temp[df_temp['atom_name'].str.contains("NZ")]
        elif temp_residue == "CYS":
            df_temp = df_temp[df_temp['atom_name'].str.contains("SG")]
        elif temp_residue == "MET":
            df_temp = df_temp[df_temp['atom_name'].str.contains("SD")]
        elif temp_residue == "TYR":
            df_temp = df_temp[df_temp['atom_name'].str.contains("OH")]

        df = df_temp

        continue_val = 0

        try:
            chain_id_temp = df['chain_id'].tolist()
            resi_number_temp = df['residue_number'].tolist()
            atom_name_temp = df['atom_name'].tolist()
            xvals_ref.append(df['x_coord'].tolist())
            yvals_ref.append(df['y_coord'].tolist())
            zvals_ref.append(df['z_coord'].tolist())
            atom_ref.append(df['atom_number'].tolist())
            chain_ref.append(chain_id_temp)
            resi_ref.append(resi_number_temp)
            resi_type_ref.append(df['residue_name'].tolist())
            continue_val = 1
        except:
            print("NO RESIDUE")
            xvals_ref.append([])
            yvals_ref.append([])
            zvals_ref.append([])
            atom_ref.append([])
            chain_ref.append([])
            resi_ref.append([])
            resi_type_ref.append([])

    min_dist_list = []

    a=0
    while a<len(xvals_ref):
        ref_list = []
        try:
            b=0
            while b<len(xvals_ref[a]):
                ref_list.append((float(xvals_ref[a][b]),float(yvals_ref[a][b]),float(zvals_ref[a][b])))
                b=b+1
        except ValueError:
            end = 1
            break
        ref_list = np.array(ref_list)
        try:
            vals = cdist(ref_list, s1).min(axis=1).tolist()
        except ValueError:
            print("NO RESIDUE")
            vals = []
        min_dist_list.append(vals)
        #min_distance = min(vals)
        a=a+1
    
    if end == 1:
        ww=ww+1
        continue

    xvals_ref = list(chain.from_iterable(xvals_ref))
    yvals_ref = list(chain.from_iterable(yvals_ref))
    zvals_ref = list(chain.from_iterable(zvals_ref))
    atom_ref = list(chain.from_iterable(atom_ref))
    chain_ref = list(chain.from_iterable(chain_ref))
    resi_ref = list(chain.from_iterable(resi_ref))
    resi_type_ref = list(chain.from_iterable(resi_type_ref))
    min_dist_list = list(chain.from_iterable(min_dist_list))

    df_out = pd.DataFrame([resi_type_ref, chain_ref, resi_ref, min_dist_list, atom_ref, xvals_ref, yvals_ref, zvals_ref]).T
    df_out.columns = ['Residue_Type', 'Chain', 'Residue_Number', 'Min_Distance_from_Reactive_Atom_to_Ligand', 'Reactive_Atom_Reference', 'Reactive_Atom_X', 'Reactive_Atom_Y', 'Reactive_Atom_Z']

    df_out = df_out.sort_values(by=['Min_Distance_from_Reactive_Atom_to_Ligand'], ascending=True)

    df_out.to_csv("/Users/ananthansadagopan/Downloads/min_distance_from_" + str(value) + "_to_" + str(ligand) + ".csv", index=False)

    """
    os.system("rm -rf %s" % pdb)
    os.system("rm -rf %s" % pdb_gz)
    os.system("rm -rf %s" % pdb_download)
    """

    ww=ww+1

    print(ww)