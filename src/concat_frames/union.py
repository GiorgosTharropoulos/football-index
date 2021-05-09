import pathlib

import pandas as pd
# from unidecode import unidecode

BASE_DIR = pathlib.Path(__file__).parent
FRAMES_DIR = BASE_DIR.joinpath('frames')

# STR_COLS = ['Player', 'Team', 'Team within selected timeframe', 'Position',
#             'Contract expires', 'Birth country', 'Passport country',
#             'Foot', 'On loan']

xlsx_files = FRAMES_DIR.glob('*.xlsx')

all_df = pd.DataFrame()

for file in xlsx_files:
    df = pd.read_excel(file)
    df['file'] = file.name
    all_df = pd.concat([all_df, df])


all_df.to_excel(BASE_DIR.joinpath('all_frames.xlsx'), encoding='utf-8')
