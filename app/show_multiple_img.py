# 初期設定 -- ここから
category = ['飛行機', '自動車', '鳥', '猫', '鹿', '犬', 'カエル', '馬', '船', 'トラック']
nrows=10
ncols=5
# 初期設定 -- ここまで
 
# squeeze=Falseとしておけば、ncols=1でもaxes[i,j]と書ける。
fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(3.75, 6.25), dpi=96, squeeze=False)

for i in range(nrows):

    # ラベルi の画像のインデックスを取得する。
    label_i_index = np.where(y_train == i)[0]

    for j in range(ncols):
    
        # i+1 行目、j+1 列目に、
        # ラベルi の画像の中から、j+1 番目の画像を表示する。 
        axes[i,j].imshow(x_train[label_i_index[j], :, :, :])

        # 目盛りを非表示にする。
        axes[i, j].set_xticks([])
        axes[i, j].set_yticks([])

        # 1 列目の画像のみy軸ラベルをつける。
        if j == 0:
            axes[i,j].set_ylabel(f'ラベル{i}:{category[i]}', labelpad = 40, rotation="horizontal")

plt.show()
