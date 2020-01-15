
import pandas as pd
import numpy as np
from lightfm import LightFM
from lightfm.evaluation import precision_at_k

from sklearn.preprocessing import LabelEncoder 
from scipy.sparse import coo_matrix

games_df=pd.read_csv('steam-200k.csv',header=None)
games_df.columns=['user_id','title','action','hours','hz']

games_df=games_df[games_df['action']=='purchase']

le = LabelEncoder()
le.fit(games_df['title'])

games_df['title']=le.transform(games_df['title'])

games_df_pivot=games_df.pivot_table(columns=['title'],index=['user_id'],values=['hours'])
games_df_pivot.fillna(value=0,inplace=True)

games_df_pivot_train=games_df_pivot.sample(frac=0.8)
games_df_pivot_test=games_df_pivot.loc[games_df_pivot.index.difference(games_df_pivot_train.index)]

games_df_pivot_train_sparse=coo_matrix(games_df_pivot_train.values)
games_df_pivot_test_sparse=coo_matrix(games_df_pivot_test.values)

model = LightFM(loss='warp',random_state=42)
model.fit(games_df_pivot_train_sparse, epochs=150, num_threads=2)

return model.predict([3],[1])

# print("Train precision: %.2f" % precision_at_k(model, games_df_pivot_train_sparse, k=5).mean())
# print("Test precision: %.2f" % precision_at_k(model, games_df_pivot_test_sparse, k=5).mean())

# pickle.dump(model,open('model.pickle','wb'))
