# GUI_game

A simple "Link Game" (连连看) implemented as a learning assignment.  
作为学习作业制作的 **连连看** GUI 游戏  
学習課題として作成した **連連看ゲーム**

---

## How to Start / ゲームの起動方法 / 游戏启动方法

- :  
  Run the code 'GUI_game_v2.py'. The game window will appear.  
  From the menu bar, select `START` → `NEW` to begin the game and place icons.  

- :  
  'GUI_game_v2.py'コードを実行するとインスタンスが作成され、ゲームウィンドウが表示されます。  
  メニューバーの「START」から「NEW」を選択すると、ゲームが開始され、アイコンが配置されます。  

- :  
  运行'GUI_game_v2.py'代码，显示游戏窗口。  
  在菜单栏选择 `START` → `NEW` 即可开始游戏并生成图标。  

---

## Game Content, Goal / ゲームの内容・目的 / 游戏内容与目标

- :  
  - The game board is a 12×12 grid (144 cells).  
  - There are 36 types of icons, distributed randomly.  
  - Goal: Match pairs of the same icon. Icons can be linked directly or with one or two turns.  
  - Clear all icons to win.  

- :  
  - ゲームボードは 12×12 のグリッド (合計 144 マス)。  
  - アイコンの種類は 36 種類で、ランダムに配置されます。  
  - 目的: 同じアイコンをペアでマッチさせること。直線リンクまたは 1～2 回曲がるリンクで接続可能です。  
  - 全てのアイコンを消去すればゲームクリアです。  

- :  
  - 游戏棋盘为 12×12 的网格（共 144 格）。  
  - 包含 36 种不同的图标，随机分布。  
  - 目标：将相同图标配对连接，可以直线或拐弯 1～2 次连线。  
  - 清除所有图标即可通关。  

---

## Game Controls / ゲーム操作方法 / 游戏操作方法

- :  
  - **Click**: Select an icon on the board. The first clicked icon is stored.  
  - **Link Check**: Click a second icon to check if a valid link exists. If valid, both icons disappear.  
  - **End**: The game ends when all icons are matched.  

- :  
  - **クリック**: ボード上のアイコンをクリックして選択します。最初にクリックしたアイコンが記録されます。  
  - **リンク確認**: 2つ目のアイコンをクリックするとリンク可能かチェックされ、可能なら消去されます。  
  - **終了**: 全てのアイコンがペアで消去されるとゲーム終了です。  

- :  
  - **点击**：点击棋盘上的图标进行选择，第一点击的图标会被记录。  
  - **连线确认**：点击第二个图标后会检查是否可以连线，若可以则图标消除。  
  - **结束**：所有图标配对消除后，游戏结束。  

---

## ToDo / 今後の課題 / 后续计划

- :  
  Since the generation is purely random, some boards are unsolvable.  
  Future work: add a verification program or a smarter generation algorithm.  

- :  
  完全ランダム生成のため、クリアできない盤面が発生する場合があります。  
  今後の課題: 検証プログラムや生成アルゴリズムの追加。  

- :  
  由于采用纯随机生成，可能会出现无解的棋盘。  
  后续计划：增加验证程序或改进生成算法。  

---

![sample](sample.jpg)
