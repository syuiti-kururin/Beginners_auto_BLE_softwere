# 技術仕様書

ROBO-ONE Beginners Auto BLE PC Controller

---

# 1. 概要

本ドキュメントは
**ROBO-ONE Beginners Auto BLE PC Controller** の
技術仕様およびシステム構成を説明するものです。

README.md ではプロジェクトの背景や基本的な使い方を説明していますが、
このドキュメントでは以下の内容について **より詳細に解説**します。

* システム構成
* BLE通信の仕組み
* コマンド通信仕様
* ソフトウェア構造
* 接続フロー
* 拡張可能な設計

この文書は主に **開発者や改造を行うユーザー向け**に作成されています。

---

# 2. システム構成

本システムは大きく分けて **2つの要素**で構成されています。

1. PC側コントローラ（Python）
2. ロボット側コントローラ（MicroPython / BLE）

PCは **BLE Central（接続する側）** として動作し、
ロボットは **BLE Peripheral（接続される側）** として動作します。

通信構成：

```
+-----------------------+
|          PC           |
|  Python BLE Program   |
|   (Central Device)    |
+-----------+-----------+
            |
            | Bluetooth Low Energy
            |
+-----------v-----------+
|        Robot          |
|  MicroPython BLE Node |
|   (Peripheral Device) |
+-----------------------+
```

PC側ソフトウェアはロボットへコマンドを送信し、
ロボット側プログラムがそれを受信してモーターやサーボの動作を制御します。

---

# 3. BLE通信モデル

BLE通信は **GATT（Generic Attribute Profile）** を利用して行われます。

主に使用される要素は以下の通りです。

* Service
* Characteristic
* UUID

ロボット側のBLE実装では、
多くの場合 **UART風の通信サービス** が使用されています。

代表例として **Nordic UART Service (NUS)** があります。

例：

Service UUID

```
6E400001-B5A3-F393-E0A9-E50E24DCCA9E
```

RX Characteristic（PC → Robot）

```
6E400002-B5A3-F393-E0A9-E50E24DCCA9E
```

TX Characteristic（Robot → PC）

```
6E400003-B5A3-F393-E0A9-E50E24DCCA9E
```

ただし、実際に使用されるUUIDは
ロボット側プログラムの実装によって異なる場合があります。

---

# 4. BLE接続フロー

PCとロボットのBLE接続は、一般的なBLE通信の手順に従います。

接続の流れ：

1. ロボットがBLE advertisingを開始
2. PC側プログラムがBLEデバイスをスキャン
3. 対象デバイスを検出
4. BLE接続を確立
5. GATTサービスを取得
6. 通信Characteristicを特定
7. コマンド送信を開始

---

# 5. コマンド通信仕様

PCとロボット間の通信は
**シンプルな文字列コマンド**で行われます。

基本フォーマット：

```
[ASCII文字列]
```

例：

```
F
B
L
R
X
```

PC側ソフトウェアはこれらのコマンドをBLE通信で送信します。

---

# 6. コマンド一覧

| コマンド | 動作      |
| ---- | ------- |
| F    | 前進      |
| B    | 後退      |
| L    | 左回転     |
| R    | 右回転     |
| X    | 停止      |
| A    | 自動制御モード |
| OP   | 手動操作モード |

※ 実際の動作はロボット側プログラムの実装に依存します。

---

# 7. ソフトウェア構造

本プロジェクトはシンプルな構造を採用しています。

```
ROBO-ONE_BLE_PC_Controller

ble_robot.py
main.py
README.md
Specifics_md.md
LICENSE
```

主な役割：

ble_robot.py

BLE通信処理を担当

* BLEスキャン
* デバイス接続
* コマンド送信

main.py

操作インターフェース

* ユーザー入力
* コマンド送信テスト
* 操作確認

---

# 8. Python BLEライブラリ

本プロジェクトでは
PythonのBLEライブラリ **bleak** を使用しています。

インストール：

```
pip install bleak
```

Bleakは以下の環境で動作します。

* Windows
* Linux
* macOS

---

# 9. コマンド送信例

BLE Characteristic に対してコマンドを書き込みます。

例：

```
await client.write_gatt_char(uuid, b"F")
```

このコードはロボットへ **前進コマンド** を送信します。

---

# 10. 拡張可能な機能

本システムは以下のような機能拡張を想定しています。

センサフィードバック

* IMU
* 距離センサ
* バッテリー情報

自律制御

* マッピング
* 自律移動
* 経路探索

操作インターフェース

* GUIコントローラ
* ジョイスティック入力

---

# 11. 安全に関する注意

ロボットを外部ソフトウェアで制御する場合、
予期しない動作をする可能性があります。

安全な環境でテストを行い、
人や機器に危険が及ばないよう注意してください。

---

# 12. ライセンス

本プロジェクトは

ROBO-ONE Educational Non-Commercial Software License v1.0

のもとで公開されています。

詳細は `LICENSE` ファイルを参照してください。
