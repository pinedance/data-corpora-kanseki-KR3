#%%
import os
import pandas as pd

#%%
PARENT_PATH = "의가류"
FILTER = "KR3e"
BRANCH = "master"
URL_FORMAT = "https://github.com/kanripo/{}.git"
DATAINFO = [
    ("자부_의가류", "KR3e", "https://www.kanripo.org/catalog?coll=KR3"),
]

OUTPUT_PATH = "META"
OUTPUT_CATALOG = os.path.join( OUTPUT_PATH, "Kanseki_Repository.catalog" )
OUTPUT_GITBATCH = os.path.join( "git_clone_Kanseki_Repository.sh" )

#%%
catalog_lst = list()
for info in DATAINFO:
    tables = pd.read_html( info[2], encoding="utf-8", extract_links="body" )
    table = tables[0]
    table.columns = ["serial", "name"]
    table["category"] = info[1]
    catalog_lst.append( table )

#%%
_df_catalog = pd.concat( catalog_lst )

#%%
df_catalog = _df_catalog.copy()
df_catalog["id"] = _df_catalog["serial"].apply( lambda x: x[0] )
df_catalog["serial"] = _df_catalog["serial"].apply( lambda x: x[1].split("/")[-2] )
df_catalog["name"] = _df_catalog["name"].apply( lambda x: x[0] )
df_catalog = df_catalog[ df_catalog['serial' ].str.contains( FILTER ) ]
df_catalog = df_catalog.reset_index()

#%%
df_catalog["path"] = PARENT_PATH + "/" \
                    + df_catalog["serial"] + "_" + df_catalog["name"]
df_catalog["url"] = df_catalog.apply( lambda r: URL_FORMAT.format( r["serial"] ), axis=1 )
# df_catalog["gitmodule_raw"] = df_catalog.apply( lambda r: "[submodule \"{}\"]\n\tpath = {}\n\turl = {}\n\tbranch = master".format( r["id"], r["path"], r["url"] ), axis=1 )
df_catalog["git_cmd"] = df_catalog.apply( lambda r: "git submodule add \"{}\" \"{}\" -b \"{}\" --depth 1 || true".format( r["url"], r["path"], BRANCH  ), axis=1 )

#%%
df_catalog.to_csv( OUTPUT_CATALOG, sep="\t", encoding="utf-8" )

#%%
with open( OUTPUT_GITBATCH, 'w', encoding="utf-8" ) as fl:
    fl.write( "\n\n".join( df_catalog["git_cmd"].to_list() ) )
    
# %%
