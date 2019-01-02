#
# show train and test data
#
import pandas as pd
import numpy as np

TRAIN_DATA = '../input/train.csv'
TEST_DATA = '../input/test.csv'

train = pd.read_csv(TRAIN_DATA)
test = pd.read_csv(TEST_DATA)

#dataframeの欠損データをisnull()で探して、カラムごとに返す
def kesson_table(df):
	null_val = df.isnull().sum()
	percent = 100 * df.isnull().sum()/len(df)
	kesson_table = pd.concat([null_val, percent], axis=1)
	kesson_table_ren_columns = kesson_table.rename(
	columns = {0 : '欠損数', 1: '%'})
	return kesson_table_ren_columns

#show train data
print('=== train ============================================================')
print('columnの確認==>\n', train.columns)
print('headの確認==>\n', train.head())
print('shapeの確認==>\n', train.shape)
print('describeの確認==>\n', train.describe())
print('kesson_tableの確認==>\n', kesson_table(train))

#show test data
print('=== test ============================================================')
print('columnの確認==>\n', test.columns)
print('headの確認==>\n', test.head())
print('describeの確認==>\n', test.describe())
print('kesson_tableの確認==>\n', kesson_table(test))
