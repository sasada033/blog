## はじめに
最近Documentを作成してみようみたいな話があったのでそれ勉強メモです。

ドキュメントは，共同でコードを書く時，それを引き継ぐとき等々，自分で書いていてもコードを忘れてしまうかなと思うので，ほかの人がみても，あとから見ても,分かりやすくまとめておくことに役立ちます

### 参考
https://qiita.com/kinpira/items/505bccacb2fba89c0ff0

これだけで作成まではたどり着けると思いますが正直rstとかいろいろ始めてだったのでその話もまとめます
ちなみに今回使うのはSphinxというツール

## sphinx
これはpython製のドキュメント生成ツールになりますと書かれています  
rstでドキュメントを作れると書いてあります

いやいやrstってなんですか

というわけです

rstは
reStructuredText記法です

大体こんな感じでいつも書かれます

~~~
===========================
Utilities related to math
===========================

Func_math
=======================

.. automodule:: utils.func_math
   :members:
~~~
これは，

http://d.hatena.ne.jp/kk_Ataka/20111202/1322839748

このあたりを参考にしていただければよいと思います

基本的にはmarkdownと似た形で書けることが知られています

つまり，rst記法で書かれたものを使って，sphinxで読み込むイメージですね

## sphinx-quickstart

参考の記事でも書かれていましたが，これを行うと

- conf.py
- make.bat
- Makefile

その他もろもろができます

ここも疑問に思ったので書いておきます

### conf.py
conf.pyはconfigurationファイルのことです

sphinxでドキュメントを作成するときの中身の設定をしてくれています

中をみると英語ではありますが，説明をしてくれています
困ったらconf.pyの中を見てみてください
```
html_theme = 'default'
```
これはよく使います
テーマを変えられるので

extentionの部分もよく使用されるみたいですね
拡張機能を追加する場合はここに

```
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [

]
```
数式とかの拡張，コードをハイライトしてくれる等々
さまざまな機能がありそうです

http://www.sphinx-doc.org/ja/stable/extensions.html

extしといた方がいいのは

'sphinx.ext.autodoc'

このあたりかと
これは，
http://sphinx.shibu.jp/ext/autodoc.html
にかいてあるように
コメントアウトをうまく行っておくと，関数等を勝手にdoc化してくれるという優れもの

なんかなしにしてもbuild通ったのでよくわかりませんがあったほうがいいと思います 後日確認します

また，githubpagesとの連携もできます
githubpagesの作り方は以下のサイトとかみてみました

http://tell-k.hatenablog.com/entry/2012/01/18/224126

extは

'sphinx.ext.githubpages'
言えるのはこの辺をいろいろいじれば，ドキュメントの形等々変えることができるということです

makefile系
非常に無知だったので，書くのも恥ずかしいですが
makefileとMakefileはwindows用，LINUX用にそれぞれ書かれているものです
実行用ファイルですね！！
この中にを見てみると
```
# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = Utils # プロジェクト名
SOURCEDIR     = . # rstが置いてある場所
BUILDDIR      = build # 作る場所

# Put it first so that "make" without argument is like "make help".
help:
    @$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
    @$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
```
こんなんなってます
よくわかりません

が

たぶんSP..あたりをいじる場合はいじればよいと思います

make htmlする
さきほどの

sphinx-quickstart
ではhtmlを作成できていないので
上記の設定をもろもろやります

そのあとに
例えばこのような形でmoduleを作成したとします
```
├── LICENSE
├── Makefile
├── README.md
├── docs
│   ├── Makefile
│   ├── conf.py
│   ├── index.rst
│   ├── func_math.rst
│   └── make.bat
├── utils
│   ├── __init__.py
│   └── func_math.py
├── setup.py
└── tests
    ├── __init__.py
```
ここで
func_mathというmoduleを作成しています

func_mathの中身の一部はこんなん
```python
# -*- coding: utf-8 -*-

import math
import numpy as np

def rad_to_deg(rad_angle):
    """
    Translate rad to deg

    Parameters
    -------
    angle : float or numpy.ndarray [rad]

    Returns
    -------
    deg_angle : float or numpy.ndarray [deg]
    """

    deg_angle = 180.0 * rad_angle / math.pi

    return deg_angle
```
これで関数を作成しています
rad_to_degというラジアンから角度への変換といういたって簡単なものです

ここでのポイントは
コメントの書き方

このようにかくことで先ほどいっていた
automoduleが使えます

ちなみにdocStringというそうです

https://qiita.com/simonritchie/items/49e0813508cad4876b5a

参考はこの辺

で

func_math.rstを作成します
```
===========================
Utilities related to math
===========================

Func_math
=======================

.. automodule:: utils.func_math
   :members:
```
こうしておけば後はうまくいくはずです
```
make html
```

とdocsに移動してから打ってみてください

## 忘れないこと
init.pyをわすれずに．．．
module化しないと呼んでくれない
conf.py内でpathを追加することを忘れないように

htmlの中身を見てみると

キャプチャ.PNG

こんな感じでできていると思います！！

すごい．．．

詳しいこととかはまだまだ分かっていないので，また調べたらあげます
