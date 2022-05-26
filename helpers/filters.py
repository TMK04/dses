def filter_null(df):
  return df[df.isnull().any(axis=1)]

def filter_nonnull(df):
  return df[df.notnull().any(axis=1)]