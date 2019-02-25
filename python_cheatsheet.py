
#import
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline
from sklearn.linear_model import LinearRegression as LR

#CSVデータ読み込み
train= pd.read_csv("train.csv")  #学習データ：目的変数・説明変数すべてを含むデータ
test=pd.read_csv("test.csv")     #テストデータ：目的変数が抜けているデータ
sample=pd.read_csv("sample.csv",header=None)

#データの表示：関数
train.head()
train.head(3)
train.tail()
train.shape      #行と列
train.describe() #基本統計量
train.info()     #データの型
train.isnull()   #各値が欠損値どうか判別
train.isnull().any() #欠損値が１つ以上あるか
train.isnull().sum() #各列に欠損値がいくつあるか
train[["y","temperature"]].corr() #相関係数を表示

#データの表示：カラムの条件
train["y"].mean()   #平均値
train["y"].median() #中央値
train[train["y"]>=150]
train[train["week"]=="火"].sort_values(by="y",ascending=False)
train[["datetime","y","temperature"]].head()
train["week"].value_counts() #各カラムの数

#グラフの描写
ax = train["y"].plot(figsize=(12,4),title="グラフ") #折れ線、軸付き
ax.set_xlabel("time")
ax.set_ylabel("y")

plt.axvline(x=train["y"].mean(),color="red")  #平均値の縦線、ヒストグラム
train["y"].plot.hist(figsize=(12,4),title="ヒストグラム")
plt.savefig("sample_fig.png")

train[["y","week"]].boxplot(by="week") #あごひげ図
train.plot.scatter(x="temperature",y="y",figsize=(5,5)) #散布図

#データの前処理
train.fillna(0)      #欠損値に0埋め
train.dropna(subset=["kcal"]) #kcalが欠損値である場合に行を削除
pd.get_dummies(train["week"]) #ダミー変数化
train["year"]=train["datetime"].apply(lambda x :x.split("-")[0] ) #データの分割取り出し
train["year"]=train["year"].astype(np.int)  #データの型を整数（int）に変換
#
#モデル作成：単回帰
#
trainX=train["temperature"]  #学  習：説明変数：気温
y=train["y"]                 #学  習：目的変数：お弁当の売り上げ数
testX=test["temperature"]    #テスト：説明変数
trainX=trainX.reshape(-1,1)  #おまじない
testX=testX.reshape(-1,1)    #おまじない

model1=LR() #モデルの箱
model1.fit(trainX,y) #単回帰モデル作成：学習の説明変数、目的変数

model1.coef_       #傾き
model1.intercept_  #切片

pred = model1.predict(testX) #モデルを使って予測

#
#モデル作成：重回帰
#
trainX=pd.get_dummies(train[["week","temperature"]]) #学習：ダミー変数化した曜日と、気温
y=train["y"] #学習：目的変数：売上数

model=LR() #回帰モデルの箱を用意
model.fit(trainX,y) #重回帰モデルの作成

model1.coef_       #傾き
model1.intercept_  #切片


