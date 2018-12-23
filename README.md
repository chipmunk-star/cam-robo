# やり方
- pythonとsdl2を使ってPS4コントローラーの値を取り出す
- venvで仮想環境を作る（Raspberry pi用のAnacondaが無かった）
- デフォルトでインストールされているpython3.5.3を使う
- macからraspberry piにsshでつなげる
- mac上のvisual studio codeでコードを書く

# python (raspbery pi)
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

# ssh
- sshの鍵はrsaで作る（下のssh fsがed25519に対応していない）

# visual studio code (mac)
- ssh fsをインストールする

```
{
    "label": "raspbery pi",
    "root": "raspbery pi上のつなげたいディレクトリ",
    "host": "raspbery piのアドレス",
    "port": 22,
    "username": "pi",
    "privateKeyPath": "mac上の秘密鍵のパス"
}
```