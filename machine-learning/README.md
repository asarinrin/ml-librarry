# 可視化

# 特徴量エンジニアリング

**get_column_by_target_type(df, target_type) :**
df 内の任意の型の配列 target_type を含む column を返す

**one_hot_encoding_by_target_column(df, category_column) :**
df 内の任意の category_column を OneHotEncoder で dummy変数にして、そのdata frameおよび新たな column を返す

**make_column_by_category_and_numeric(df, category_column, numeric_column, operation) :**
df 内の任意の category_column と numeric_column を組み合わせた新たな特徴量を生成する。具体的には category_column をgroup化した時に得られる統計量を追加する。
