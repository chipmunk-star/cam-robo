# こんな感じ
```
dualshock4（PS4コントローラー）] <-> [raspberry pi] <-> [cam-robot]
```

- pythonとsdl2を使ってdualshock4の値を取り出す
- venvで仮想環境を作る（Raspberry pi用のAnacondaが無かった）
- デフォルトでインストールされているpython3.5.3を使う
- mac上のvisual studio codeでコードを書く

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

# ssh (mac)
- sshの鍵はrsaで作る（下のssh fsがed25519に対応していない）

# ssh (raspberry pi)
- macで作成した公開鍵を~/.ssh/authorized_keysに追加する
- authorized_keysのパーミッションを600にする

# visual studio code (mac)
- ssh fsをインストールする
- SSH FILE SYSTEMSの下の空白をクリックして'Create a SSH FS Configuration'

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

# sdl2で、dualshock4のボタン割り当て

- button

|button  |assignment |
|---|---|
| 0 |× |
| 1 |○ |
| 2 |△ |
| 3 |□ |
| 4 |L1 |
| 5 |R1 |
| 6 |L2 |
| 7 |R2 |
| 8 |SHARE |
| 9 |OPTIONS |
|10 |PS |
|11 |L3 (Left stick) |
|12 |R3 (Right stick) |

- axis

|axis |assignment |value |
|---|---|---|
|0 | Left stick (left/right)  | -32768(left) <=> 32767(right) |
|1 | Left stick (up/down)     | -32768(up) <=> 32767(down) |
|2 | L2                       | -32768(release) <=> 32767(push) |
|3 | Right stick (left/right) | -32768(left) <=> 32767(right) |
|4 | Right stick (up/down)    | -32768(up) <=> 32767(down) |
|5 | R2                       | -32768(release) <=> 32767(push) |

- hat

|hat |assignment |value |
|---|---|---|
|0 | Directional buttons | up, rightup, right, rightdown, down, leftdown, left, leftup, centered|

