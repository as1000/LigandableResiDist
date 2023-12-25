# LigandableResiDist

Analysis steps to annotate distance of ligand to ligandable residue in PDB database:

(1) Query PDB database for structures; the query utilized in the manuscript is:
https://www.rcsb.org/search?request=%7B%22query%22%3A%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_entity_source_organism.ncbi_scientific_name%22%2C%22operator%22%3A%22exact_match%22%2C%22negation%22%3Afalse%2C%22value%22%3A%22Homo%20sapiens%22%7D%7D%2C%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22entity_poly.rcsb_entity_polymer_type%22%2C%22operator%22%3A%22exact_match%22%2C%22negation%22%3Afalse%2C%22value%22%3A%22Protein%22%7D%7D%2C%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_entry_info.resolution_combined%22%2C%22operator%22%3A%22range%22%2C%22negation%22%3Afalse%2C%22value%22%3A%7B%22from%22%3A0%2C%22to%22%3A3%2C%22include_lower%22%3Atrue%2C%22include_upper%22%3Afalse%7D%7D%7D%2C%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_binding_affinity.value%22%2C%22operator%22%3A%22exists%22%2C%22negation%22%3Afalse%7D%7D%2C%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_binding_affinity.type%22%2C%22operator%22%3A%22exact_match%22%2C%22value%22%3A%22IC50%22%2C%22negation%22%3Afalse%7D%7D%5D%2C%22label%22%3A%22nested-attribute%22%7D%2C%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_binding_affinity.value%22%2C%22operator%22%3A%22exists%22%2C%22negation%22%3Afalse%7D%7D%2C%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_binding_affinity.type%22%2C%22operator%22%3A%22exact_match%22%2C%22value%22%3A%22EC50%22%2C%22negation%22%3Afalse%7D%7D%5D%2C%22label%22%3A%22nested-attribute%22%7D%2C%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_binding_affinity.value%22%2C%22operator%22%3A%22exists%22%2C%22negation%22%3Afalse%7D%7D%2C%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_binding_affinity.type%22%2C%22operator%22%3A%22exact_match%22%2C%22value%22%3A%22Kd%22%2C%22negation%22%3Afalse%7D%7D%5D%2C%22label%22%3A%22nested-attribute%22%7D%2C%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_binding_affinity.value%22%2C%22operator%22%3A%22exists%22%2C%22negation%22%3Afalse%7D%7D%2C%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_binding_affinity.type%22%2C%22operator%22%3A%22exact_match%22%2C%22value%22%3A%22Ka%22%2C%22negation%22%3Afalse%7D%7D%5D%2C%22label%22%3A%22nested-attribute%22%7D%5D%2C%22logical_operator%22%3A%22or%22%7D%5D%2C%22logical_operator%22%3A%22and%22%7D%5D%2C%22label%22%3A%22text%22%7D%5D%7D%2C%22return_type%22%3A%22entry%22%2C%22request_options%22%3A%7B%22paginate%22%3A%7B%22start%22%3A0%2C%22rows%22%3A25%7D%2C%22results_content_type%22%3A%5B%22experimental%22%5D%2C%22sort%22%3A%5B%7B%22sort_by%22%3A%22score%22%2C%22direction%22%3A%22desc%22%7D%5D%2C%22scoring_strategy%22%3A%22combined%22%7D%2C%22request_info%22%3A%7B%22query_id%22%3A%226c2846b02fbf324a142330db3e0f84fb%22%7D%7D

(2) Click on "-- Tabular Report --" dropdown and select Create Custom Report.

(3) Select fields and press Run Report; it is good to include the following fields:
Entry ID, Ligand, Value, Symbol, Type, Unit, PDB ID, Resolution, Structure Title, Gene Name, Macromolecule Name, Ligand Formula, Ligand MW, Ligand ID, Ligand Name, Ligand SMILES, Ligand of Interest, and Entity ID. 

(4) Download the resulting records in batches of 2500 as .csv files, and concatenate them to yield a file: merged_rcsb_calls.csv.

(5) Run a short preprocessing script:

```
import pandas as pd
working_dir = "/path/to/working_dir/"
df = pd.read_csv(working_dir + "merged_rcsb_calls.csv")
df = df.dropna(subset=['Ligand ID'])
df = df.ffill()
df.to_csv(working_dir + "/merged_rcsb_calls_ffilled.csv", index=False)
```

Note: The affinity annotations on the resulting spreadsheet are essentially arbitrary (one experiment chosen at random from many experiments). This is corrected later in the workflow (step 10).

(6) Sort the resulting .csv by ligand formula and remove ligands with less than 10 carbons, inorganic ligands, and promiscuous organic ligands (e.g. ATP, GTP, etc.) to yield merged_rcsb_calls_ffilled_filtered.xlsx.

(7) Run PDB_distance_calculator_biopandas_noSASA.py on the resulting file to calculate the distance of ligand to ligandable residues for each PDB-ligand entry.

(8) Run annotate_min_distances.py on the output files generated in the previous step to annotate the minimum distances from ligand to ligandable residues on the master sheet: merged_rcsb_calls_ffilled_filtered.xlsx, to yield: merged_rcsb_calls_ffilled_filtered_distance_annotated.xlsx.

(9) Generate summary plots using: plot_distance_to_ligandable_res_histograms.py and/or ptm_plotting_CDFs.py

(10) Run annotate_affinity_final.py on merged_rcsb_calls_ffilled_filtered_distance_annotated.xlsx to annotate all available ligand affinity values for every PDB-ligand entry. This will yield a new file: merged_rcsb_calls_ffilled_filtered_distance_annotated_affinity_annotation.xlsx. Note: This script uses the file generated in step 4: merged_rcsb_calls.csv for the annotations.

(11) 

