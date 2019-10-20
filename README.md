# Pythonでアルゴレイヴの世界に足を踏み入れる

PyCon mini Hiroshima 2019でお話させていただいた「Pythonでアルゴレイヴの世界に足を踏み入れる」のためのリポジトリです

### スライド

[Slides](https://www.slideshare.net/ksnt/python-181761996)


### 動画

[当日の配信映像の記録](https://youtu.be/w11ecjRRB_M?t=4377)

### ブログその１(裏話)

[講演の裏話](http://ksnt.hatenablog.com/archive/2019/10/18)  

### ブログその２(解説ブログ)

TBA

※FoxDotそのもののコードを少し書き換えています。同じようなことをしないとFoxDotとProcessingの通信を行うことはできません。詳しくはブログを書きますので(予定)、そちらを参考にしてみてください。

### ファイル構成

FoxDot/`livecoding_191012.py`: ライブコーディングの際に用いたFoxDot用のコードの原型です。たぶん当日のものとは少しだけ違うものになっています。

Processing/osc_0_7/`Algorave_logo.png`: Algoraveのロゴ画像です

Processing/osc_0_7/`LimitedParticle.pde`: `osc_0_7.pde`内で使っているLimitedParticleクラスためのファイルです

Processing/osc_0_7/`osc_0_7.pde`: 中心となるProcessingのコードです

Processing/osc_0_7/`Particle.pde`: `LimitedParticle.pde`内で使っているParticleクラスのためのファイルです
