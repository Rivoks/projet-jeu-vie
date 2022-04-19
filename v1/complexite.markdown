## Mesure de la complexité à l'aide de McCabe Python

Mesure le nombre d'instruction générant une bifurcation (if, for, while...)
Plus ce nombre sera grand, plus il y aura de cas d'exécution différents,
et plus le code sera difficile à comprendre, mais également, de fait, à maintenir et à tester.

#### == main.py ==

13:4: 'MainGame.\_\_init\_\_' 1
23:4: 'MainGame.CreateCanvasBoardAndButtons' 1
35:4: 'MainGame.Setup' 1
46:4: 'MainGame.mainLoop' 2

#### == Board.py ==

20:4: 'Board.\_\_init\_\_' 1
28:4: 'Board.Init' 3
50:4: 'Board.CloneArrCells' 3
60:4: 'Board.Show' 4
71:4: 'Board.ConvertCoordonate' 5
82:4: 'Board.Update' 1
92:4: 'Board.Draw' 5

#### == Cell.py ==

9:4: 'Cell.SetColors' 1
17:4: 'Cell.\_\_init\_\_' 1
20:4: 'Cell.Clone' 1
23:4: 'Cell.GetColor' 1

#### == Graphics.py ==

5:4: 'GraphicsSetting.\_\_init\_\_' 1

#### == LTL2.py ==

12:4: 'LTL2.Init' 1
24:4: 'LTL2.GetNextState' 1
55:4: 'LTL2.GetSumNeighbours' 4
65:4: 'LTL2.Update' 3

#### == ButtonsManager ==

6:4: 'ButtonsManager.\_\_init\_\_' 1
9:4: 'ButtonsManager.Go' 1
16:4: 'ButtonsManager.Stop' 1
21:4: 'ButtonsManager.Change_vit' 1
25:4: 'ButtonsManager.Change_rayon' 1
29:4: 'ButtonsManager.CreateButtons' 1

#### == CustomRules1 ==

8:4: 'CustomRules1.Init' 1
14:4: 'CustomRules1.GetNextState' 7
73:4: 'CustomRules1.GetNeighbours' 4
83:4: 'CustomRules1.Update' 3

#### == LTL.py ==

8:4: 'LTL.Init' 1
12:4: 'LTL.GetNextState' 1
43:4: 'LTL.GetSumNeighbours' 4
53:4: 'LTL.Update' 3

#### == Useful.py ==

4:4: 'Useful.Lerp' 1
