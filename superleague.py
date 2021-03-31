# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np


# %%
file_path = 'C:/Users/githk/Projects/footballindex/Sample Data/raw stats/GRE1.xlsx'

gr_df = pd.read_excel(file_path)


# %%
def column_names_to_lower(df):
    df.columns = [col.lower() for col in gr_df.columns]
    return df


# %%
def per_90_to_absolute(df, min_cols='minutes played'):
    df = df.copy()
    per_90_cols = [col for col in df.columns if '90' in col]
    col_names = list(map(lambda x: x.replace(' per 90', '') + ' extrp', per_90_cols))
    for i, col in enumerate(per_90_cols):
        df[col_names[i]] = df[col] * df[min_cols] / 90
    return df


# %%
def successful_percentage_to_absolute(df, success_cols=['won', 'accurate', 'successful']):
    df = df.copy()
    percentage_cols = [col for col in df.columns if '%' in col]
    for col in percentage_cols:
        for keyword in success_cols:
            if keyword in col:
                col_name = col.replace(', %', '') + ' per 90'
                df[col_name] = gr_df[col.replace(keyword, '').replace(', %', '').strip() + ' per 90'] * df[col]
    return df


# %%
gr_df = column_names_to_lower(gr_df)
gr_df = successful_percentage_to_absolute(gr_df)
gr_df = per_90_to_absolute(gr_df)
gr_df.head()


# %%
camara = gr_df.iloc[0]
print(camara.goals, camara['goals extrp'])


# %%
positions_df = gr_df['position'].str.split(',', expand=True)
positions_df.columns = ['position' + str(col) for col in positions_df.columns]
positions_df


# %%

POS_DICT = {
    'Goalkeeper': ['GK'],
    'Full Back': ['LB', 'LB5', 'RB', 'RB5'],
    'Wing Back': ['LWB', 'RWB'],
    'Center Back': ['CB', 'CB3', 'RCB', 'LCB'],
    'Defensive Midfielder': ['DMF', 'RDMF', 'LDMF'],
    'Central Midfielder': ['LCMF', 'LCMF3', 'RCMF', 'RCMF3'],
    'Attacking Midfielder': ['AMF', 'LAMF', 'RAMF'],
    'Winger': ['LW', 'RW'],
    'Wing Forward': ['LWF', 'RWF'],
    'Striker': ['CF']
}

def map_pos(position):
    for key in POS_DICT:
        for values in POS_DICT[key]:
            if position in values:
                return key
    return -1

map_pos('AMF')

positions_df.position1.map(map_pos)

positions_df.applymap(map_pos, na_action='ignore')


# %%
positions_df.head()


# %%
positions_df.applymap(map_pos, na_action='ignore')


# %%
