# 【研究①】cifar10 における各ラベルに対応する画像表示について

## 研究内容
### １. あるラベルの特定の画像を表示
・**ラベル i の n 枚目の画像を表示**するには、次のようなコードで表せる。
```python
plt.imshow(x_train[label_i_idnex[n - 1], :, :, :])
```

ここで、 
```python
label_i_idnex ＝ np.where(y_train == i)[0]
```
であり、**ラベル i のインデックスが複数格納された 1 次元配列**を表す。
___
### ２. 複数の画像を表示する際のプロット
・**画像を複数表示する際のプロット**には、
```python
plt.subplots()
``` 
の戻り値である、Axesオブジェクトが複数格納された配列
``` python
axes
``` 
と、
二重for文のループ変数 `i, j `を用いて 、
``` python
axes[i, j]
``` 
のように、**行列の成分指定のように分かりやすく簡潔に記述**。

## 画像資料
### １. 各ラベルに対応する画像を複数表示
<img src="images/cifar10_show.png" width="600" height="auto">

### ２. x_train、y_train における画像とラベルの対応
<img src="images/relation_img_label.png" width="auto" height="auto">

### ３. ラベル i のインデックスを取得
<img src="images/get_label_index.png" width="auto" height="auto">


## 開発環境
Google Colaboratory  
<p>&nbsp;</p>

## ライセンス
"cifar10 におけるラベルに対応する画像表示について" is licenced under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
