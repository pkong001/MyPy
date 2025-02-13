import pandas as pd
import os
import sys

############### DEFINE OUTPUT FROM CMD ARGUMENT ###############
if len(sys.argv) > 1:
    output_name = sys.argv[1]  # Take the first argument as the output filename
else:
    output_name = "DefaultOutputName"  # Default name if no argument is given
# print(os.listdir("."))
############### Preparation ###############
with open("B2D.txt", "r", encoding="utf-8") as file:
    ecc_text = file.read()
with open("B4D.txt", "r", encoding="utf-8") as file:
    hana_text = file.read()

#Prepare Origin
df_ecc_text = pd.DataFrame(ecc_text.split("\n"))
df_hana_text = pd.DataFrame(hana_text.split("\n"))

def export_df(text):
        ls = [i.strip() for i in text.split("\n") 
                if 
                        ("Append structure " not in i) 
                        and ("Include structure " not in i)
                        and (".INCLUDE" not in i)
                        and (len(i) > 1)
                ]
        ls_ls = [i.split(" ") for i in ls]

        #####Define List
        set1 = set([i[-2] for i in ls_ls]) # set2 =  set([i.split(" ")[-3] for i in ls])    
        ls1 = [i for i in list(set1) if any(j.isalpha() for j in i)]
        ls1.extend(["QUAN", "DEC", "CURR"])
        type_ls = list(set(ls1)) 

        ls_name = [ i[0] for i in ls_ls]

        ls_type = []
        for i in ls_ls:
                if i[-2] in type_ls:
                        ls_type.append(f'{i[-2]} {i[-1]}')
                else:
                        ls_type.append(f'{i[-3]} {i[-2]},{i[-1]}')

        ls_combine = []
        for i in range(0,len(ls_ls)):
                ls_combine.append(f'{i} ' + ls_name[i]+" "+ls_type[i])
        ls_combine_ls = [i.split(" ") for i in ls_combine]
        
        return ls_combine_ls

############### Read files and apply def ###############
hana = export_df(hana_text)
ecc = export_df(ecc_text)

# Prepare Dataframe
df_ecc = pd.DataFrame(data=ecc,columns=["e_index","e_name","e_type","e_lgt"])
df_hana = pd.DataFrame(data=hana,columns=["h_index","h_name","h_type","h_lgt"])


############### Check Field Mismatch ###############
ecc_name = set([i[1] for i in ecc])
hana_name = set([i[1] for i in hana])

ecc_u = []
hana_u = []
if ecc_name == hana_name:
    print("Both DataFrames have the same columns.")
else:
    for i in ecc_name - hana_name:
        ecc_u.append(i)
    for i in hana_name - ecc_name:
        hana_u.append(i)

# Make same lenght
max_len = max(len(ecc_u), len(hana_u))
ecc_u += [""] * (max_len - len(ecc_u))  # Pad with empty string
hana_u += [""] * (max_len - len(hana_u))

# Prepare Dataframe
df_mismatched_fields = pd.DataFrame({"Only in HANA": hana_u,"Only in ECC": ecc_u})
# print(df_mismatched_fields.to_string(index=False))  # Properly formatted DataFrame output

############### Check Type Mismatch ###############
ecc_dict = {row[1]: row for row in ecc}  # {C1: [...], C3: [...]}
hana_dict = {row[1]: row for row in hana}  # {C1: [...], C3: [...]}
matching_keys = set(ecc_dict.keys()) & set(hana_dict.keys())

data = []
for i in matching_keys:
    e_row = ecc_dict[i]
    h_row = hana_dict[i]
    if (e_row[3] != h_row[3]) or (e_row[2] != h_row[2]):
        data.append({
            "e_name": e_row[1], "e_type": e_row[2], "e_lgt": e_row[3],
            "trans": ">>>",
            "h_name": h_row[1], "h_type": h_row[2], "h_lgt": h_row[3]
        })

# Convert to DataFrame
df_mismatched_types = pd.DataFrame(data)

# print(df.to_string(index=False))


############### Write Files ###############
excel_path = f"{output_name}.xlsx"

# Write to Excel with multiple sheets
with pd.ExcelWriter(excel_path, engine="xlsxwriter") as writer:
    df_ecc.to_excel(writer, sheet_name="ecc", index=False)
    df_hana.to_excel(writer, sheet_name="hana", index=False)
    df_mismatched_types.to_excel(writer, sheet_name="mismatched_types", index=False)
    df_mismatched_fields.to_excel(writer, sheet_name="mismatched_fields", index=False)
    df_ecc_text.to_excel(writer, sheet_name="ecc_origin", index=False)
    df_hana_text.to_excel(writer, sheet_name="hana_origin", index=False)
print(f"Excel file '{excel_path}'.")

