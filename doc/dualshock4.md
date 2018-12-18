# ツール
- pythonとsdl2を使ってPS4コントローラーの値を取り出す
- venvで仮想環境を作る（Raspberry pi用のAnacondaが無かった）
- デフォルトでインストールされているpython3.5.3を使う

# pythonの設定

- 仮想環境を作る

```
$ sudo apt-get install python3-venv
$ apt-get install python3-venv
$ source venv/bin/activate
```

- モジュールを追加する

```
$ pip install pysdl2
```