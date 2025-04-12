#yad_test ver.1.0

import pyxel
import random
import math

class App:
    def __init__(self):
        pyxel.init(200,200,fps=60)
        pyxel.cls(11)
        pyxel.load("yad.pyxres")
        self.yadx = 100
        self.yady = 0
        self.yadm = 0
        self.yadm_f = 0
        self.frame_count = 0
        self.flag1 =0
        self.flag2 =0
        self.yadn = 0
        self.count = 0
        self.cur = 0
        self.now = 0
        self.framenow = 0
        self.hour = 0
        self.min = 0
        self.sec =0
        self.timer = 0
        self.timer_down =1
        self.yadhp = 100
        self.yaddamage = 30
        self.yadlv = 20
        self.yada = 0
        self.yadh = 0
        self.yadb = 0
        self.yadc = 0
        self.yadd = 0
        self.yads = 0
        self.yad_now = 0
        self.yad_now_p = 0
        self.scene = 0 #0タイトル 1操作画面 2計測
        pyxel.playm(0,loop=True)
        pyxel.run(self.update,self.draw)
        
    def update(self):
        self.frame_count +=1
        if self.scene == 0:
            self.update_title_scene()
        elif self.scene == 1:
            self.update_play_scene()
        elif self.scene == 2:
            self.update_count_scene()

    def draw(self):
        if self.scene == 0:
            self.draw_title_scene()
        elif self.scene == 1:
            self.draw_play_scene()
        elif self.scene == 2:
            self.draw_count_scene()

    # タイトル画面の処理
    def update_title_scene(self):#タイトル画面で実行する処理です
        self.mouse= pyxel.mouse_x
        if pyxel.btnp(pyxel.KEY_RETURN) :
            self.yadx=100
            self.scene = 1
            self.yady = 70
            self.frame_count=0
        if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            self.yadx=100
            self.scene = 1
            self.yady = 70
            self.frame_count=0

    # タイトル画面の描画
    def draw_title_scene(self):
        #タイトル画面を表示しているときの表示です
        pyxel.cls(11)
        if self.frame_count % 120 == 0:
            self.yadn +=1
        if self.yadn ==1:
            pyxel.blt(89,69,0,0,0,24,24,6)
            self.yadn = 2
        elif self.yadn ==2:
            pyxel.blt(89,68,0,0,0,24,24,6)
            self.yadn = 3
        elif self.yadn ==3:
            pyxel.blt(89,65,0,0,0,24,24,6)
            self.yadn = 4
        elif self.yadn ==4:
            pyxel.blt(89,64,0,0,0,24,24,6)
            self.yadn = 5
        elif self.yadn ==5:
            pyxel.blt(89,65,0,0,0,24,24,6)
            self.yadn = 6
        elif self.yadn ==6:
            pyxel.blt(89,68,0,0,0,24,24,6)
            self.yadn = 7
        elif self.yadn ==7:
            pyxel.blt(89,69,0,0,0,24,24,6)
            self.yadn = 0 
        else:
            pyxel.blt(89,70,0,0,0,24,24,6)
        pyxel.text(85, 150,"YADON GAME",7)
        pyxel.text(70, 160,"Let's Go Slowpoke",7)
        pyxel.text(75, 170,"Put Your Phone!",7)

        if 0<=self.frame_count%50<=5:
            pyxel.text(75, 170,"Put Your Phone!",15)
        elif 6<=self.frame_count%50<=14:
            pyxel.text(75, 170,"Put Your Phone!",14)
        elif 15<=self.frame_count%50<=20:
            pyxel.text(75, 170,"Put Your Phone!",15)
            

        pyxel.text(87, 140,"--ENTER--",7)

    #操作画面について
    def update_play_scene(self):
        #動かし方について
        if self.yadm ==0:
            if self.frame_count%120 ==0:
                self.yadx -= 5
                self.yadm_f += 1
            if self.frame_count%600==0:
                self.yadm=1
        elif self.yadm ==1:
            if self.frame_count%120 ==0:
                self.yadx += 5
                self.yadm_f += 1
            if self.frame_count%1200==0:
                self.yadm=2
        elif self.yadm ==2:
            if self.frame_count%120 ==0:
                self.yadx -= 5
                self.yadm_f += 1
            if self.frame_count%600==0:
                self.yadm=0
        if self.frame_count%240==0:
            a = random.randint(5, 10)
            self.yady += a
        if self.frame_count%120==0:
            b = random.randint(2, 5)
            self.yady -= b

        if pyxel.btnp(pyxel.KEY_SPACE):#強制退場
            self.flag1=0

        if self.flag1 ==0:#待機画面
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.flag1 =1
                self.framenow = self.frame_count
            if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                self.flag1=1
                self.framenow = self.frame_count
       
        if self.flag1 ==1:#時間入力
            if pyxel.btnp(pyxel.KEY_D):
                self.cur+=1
            elif pyxel.btnp(pyxel.KEY_RIGHT):
                self.cur+=1
            if pyxel.btnp(pyxel.KEY_A):
                self.cur-=1
            elif pyxel.btnp(pyxel.KEY_LEFT):
                self.cur-=1
            if pyxel.btnp(pyxel.KEY_0):
                self.cur = 0
            elif pyxel.btnp(pyxel.KEY_1):
                self.cur = 1
            elif pyxel.btnp(pyxel.KEY_2):
                self.cur = 2
            elif pyxel.btnp(pyxel.KEY_3):
                self.cur = 3
            elif pyxel.btnp(pyxel.KEY_4):
                self.cur = 4
            elif pyxel.btnp(pyxel.KEY_5):
                self.cur = 5
            elif pyxel.btnp(pyxel.KEY_6):
                self.cur = 6
            elif pyxel.btnp(pyxel.KEY_7):
                self.cur = 7
            elif pyxel.btnp(pyxel.KEY_8):
                self.cur = 8
            elif pyxel.btnp(pyxel.KEY_9):
                self.cur = 9
            
            if self.cur <= 0:
                self.cur =0
            elif self.cur >= 9:
                self.cur = 9

            if pyxel.btnp(pyxel.KEY_RETURN):
                if self.frame_count -self.framenow >= 10:
                    self.flag1 = 2
                    self.framenow = self.frame_count
            if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                 if self.frame_count -self.framenow >= 10:
                    self.flag1=2
                    self.framenow = self.frame_count
            
        if self.flag1 ==2:#時間確認
            if pyxel.btn(pyxel.KEY_D):
                self.now=1
            elif pyxel.btn(pyxel.KEY_RIGHT):
                self.now=1
            if pyxel.btn(pyxel.KEY_A):
                self.now=0
            elif pyxel.btn(pyxel.KEY_LEFT):
                self.now=0
            
            if self.now == 1:
                if pyxel.btnp(pyxel.KEY_RETURN):
                    if self.frame_count -self.framenow >= 10:
                        self.flag1 = 1
                        self.framenow = self.frame_count
            elif self.now ==0:
                if pyxel.btnp(pyxel.KEY_RETURN):
                    if self.frame_count -self.framenow >= 10:
                        self.flag1 = 3
                        self.hour = self.cur
                        self.cur = 0
                        self.framenow = self.frame_count

        if self.flag1 ==3:#分入力
            if pyxel.btnp(pyxel.KEY_D):
                self.cur+=1
            elif pyxel.btnp(pyxel.KEY_RIGHT):
                self.cur+=1
            if pyxel.btnp(pyxel.KEY_A):
                self.cur-=1
            elif pyxel.btnp(pyxel.KEY_LEFT):
                self.cur-=1

            if self.cur<=0:
                self.cur=0
            elif self.cur >=10:
                self.cur=10

            if pyxel.btnp(pyxel.KEY_0):
                self.cur = 0
            elif pyxel.btnp(pyxel.KEY_1):
                self.cur = 1
            elif pyxel.btnp(pyxel.KEY_2):
                self.cur = 2
            elif pyxel.btnp(pyxel.KEY_3):
                self.cur = 3
            elif pyxel.btnp(pyxel.KEY_4):
                self.cur = 4
            elif pyxel.btnp(pyxel.KEY_5):
                self.cur = 5
            elif pyxel.btnp(pyxel.KEY_6):
                self.cur = 6
            elif pyxel.btnp(pyxel.KEY_7):
                self.cur = 7
            elif pyxel.btnp(pyxel.KEY_8):
                self.cur = 8
            elif pyxel.btnp(pyxel.KEY_9):
                self.cur = 9
            elif pyxel.btnp(pyxel.KEY_P):
                self.cur = 10

            if pyxel.btnp(pyxel.KEY_RETURN):
                if self.frame_count -self.framenow >= 10:
                    self.flag1 = 4
                    self.framenow = self.frame_count
            if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                 if self.frame_count -self.framenow >= 10:
                    self.flag1=4
                    self.framenow = self.frame_count

        if self.flag1 ==4:#分入力確認
            if pyxel.btn(pyxel.KEY_D):
                self.now=1
            elif pyxel.btn(pyxel.KEY_RIGHT):
                self.now=1
            if pyxel.btn(pyxel.KEY_A):
                self.now=0
            elif pyxel.btn(pyxel.KEY_LEFT):
                self.now=0
            
            if self.now == 1:
                if pyxel.btnp(pyxel.KEY_RETURN):
                    if self.frame_count -self.framenow >= 10:
                        self.flag1 = 3
                        self.framenow = self.frame_count
            elif self.now ==0:
                if pyxel.btnp(pyxel.KEY_RETURN):
                    if self.frame_count -self.framenow >= 10:
                        self.flag1 = 5
                        self.min = 5+5*self.cur
                        self.cur = 0
                        self.framenow = self.frame_count

        if self.flag1 ==5:#時間の確認
            if pyxel.btn(pyxel.KEY_D):
                self.now=1
            elif pyxel.btn(pyxel.KEY_RIGHT):
                self.now=1
            if pyxel.btn(pyxel.KEY_A):
                self.now=0
            elif pyxel.btn(pyxel.KEY_LEFT):
                self.now=0
            
            if self.now == 1:
                if pyxel.btnp(pyxel.KEY_RETURN):
                    if self.frame_count -self.framenow >= 10:
                        self.flag1 = 1
                        self.framenow = self.frame_count
            elif self.now ==0:
                if pyxel.btnp(pyxel.KEY_RETURN):
                    if self.frame_count -self.framenow >= 10:
                        self.flag1 = 6
                        self.cur = 0
                        self.framenow = self.frame_count
                        
        if self.flag1 ==6:#育成ステータス選択
            if pyxel.btnp(pyxel.KEY_D):
                self.cur+=1
            elif pyxel.btnp(pyxel.KEY_RIGHT):
                self.cur+=1
            if pyxel.btnp(pyxel.KEY_A):
                self.cur-=1
            elif pyxel.btnp(pyxel.KEY_LEFT):
                self.cur-=1

            if self.cur<=0:
                self.cur=0
            elif self.cur >=5:
                self.cur=5
            
            if pyxel.btnp(pyxel.KEY_0):
                self.cur = 0
            elif pyxel.btnp(pyxel.KEY_1):
                self.cur = 1
            elif pyxel.btnp(pyxel.KEY_2):
                self.cur = 2
            elif pyxel.btnp(pyxel.KEY_3):
                self.cur = 3
            elif pyxel.btnp(pyxel.KEY_4):
                self.cur = 4
            elif pyxel.btnp(pyxel.KEY_5):
                self.cur = 5
            
            if pyxel.btnp(pyxel.KEY_H):
                self.cur = 0
            elif pyxel.btnp(pyxel.KEY_A):
                self.cur = 1
            elif pyxel.btnp(pyxel.KEY_B):
                self.cur = 2
            elif pyxel.btnp(pyxel.KEY_C):
                self.cur = 3
            elif pyxel.btnp(pyxel.KEY_D):
                self.cur = 4
            elif pyxel.btnp(pyxel.KEY_S):
                self.cur = 5

            if pyxel.btnp(pyxel.KEY_RETURN):
                if self.frame_count -self.framenow >= 10:
                    self.flag1=7
                    self.framenow = self.frame_count
            if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                 if self.frame_count -self.framenow >= 10:
                    self.flag1=7
                    self.framenow = self.frame_count
        
        if self.flag1 ==7:#育成ステータス確認
            if pyxel.btn(pyxel.KEY_D):
                self.now=1
            elif pyxel.btn(pyxel.KEY_RIGHT):
                self.now=1
            if pyxel.btn(pyxel.KEY_A):
                self.now=0
            elif pyxel.btn(pyxel.KEY_LEFT):
                self.now=0
            
            if self.now == 1:
                if pyxel.btnp(pyxel.KEY_RETURN):
                    if self.frame_count -self.framenow >= 10:
                        self.flag1 = 6
                        self.framenow = self.frame_count
            elif self.now ==0:
                if pyxel.btnp(pyxel.KEY_RETURN):
                    if self.frame_count -self.framenow >= 10:
                        self.flag1 = 0
                        self.yad_now = self.cur
                        self.timer = 3600*self.min + 216000*self.hour
                        self.scene = 2
                        self.framenow = self.frame_count
                        self.cur = 0
            
    #操作画面の描画
    def draw_play_scene(self):
        pyxel.cls(11)
        pyxel.rect(50,15,self.yadhp-self.yaddamage,5,3)
        pyxel.rectb(50,15,self.yadhp,5,0)
        pyxel.text(50,7,str(self.yadhp-self.yaddamage)+ "/" + str(self.yadhp),0)
        pyxel.text(7,15,"YADON'S HP",0) #EXP?
        pyxel.text(7,22,"YADON'S LV. "+ str(self.yadlv),0)
        pyxel.rectb(10,30,180,100,0)
        pyxel.rect(5,120,40,40,0)
        pyxel.rect(6,121,38,38,7)
        pyxel.tri(7,131,42,131,25,121,0)
        pyxel.tri(7,148,42,148,25,158,0)
        pyxel.rect(7,131,36,17,0)
        pyxel.pset(25,140,7)
        #pyxel.line(25,140,25-math.cos(27.8)*self.yada/252*19,140-math.sin(27.8)*self.yada/252*19,7) #A
        #pyxel.line(25,140,25-math.cos(27.8)*self.yadb/252*19,140+math.sin(27.8)*self.yadb/252*19,7) #B
        #pyxel.line(25,140,25+math.cos(27.8)*self.yadc/252*19,140-math.sin(27.8)*self.yadc/252*19,7) #C
        #pyxel.line(25,140,25+math.cos(27.8)*self.yadd/252*19,140+math.sin(27.8)*self.yadd/252*19,7) #D
        #pyxel.line(25,140,25,140-self.yadh/252*19,7) #H
        #pyxel.line(25,140,25,140+self.yads/252*19,7) #S
        pyxel.line(25-math.cos(27.8)*self.yada/252*19,140-math.sin(27.8)*self.yada/252*19,25-math.cos(27.8)*self.yadb/252*19,140+math.sin(27.8)*self.yadb/252*19,7)#AB
        pyxel.line(25+math.cos(27.8)*self.yadc/252*19,140-math.sin(27.8)*self.yadc/252*19,25+math.cos(27.8)*self.yadb/252*19,140+math.sin(27.8)*self.yadb/252*19,7)#CD
        pyxel.line(25+math.cos(27.8)*self.yadd/252*19,140+math.sin(27.8)*self.yadd/252*19,25,140+self.yads/252*19,7) #DS
        pyxel.line(25-math.cos(27.8)*self.yadb/252*19,140+math.sin(27.8)*self.yadb/252*19,25,140+self.yads/252*19,7) #BS
        pyxel.line(25-math.cos(27.8)*self.yada/252*19,140-math.sin(27.8)*self.yada/252*19,25,140-self.yadh/252*19,7) #HA
        pyxel.line(25+math.cos(27.8)*self.yadc/252*19,140-math.sin(27.8)*self.yadc/252*19,25,140-self.yadh/252*19,7) #HC


        if self.yadm==0:#行って
            if self.yadm_f %2==0:
                pyxel.blt(self.yadx,self.yady,0,0,48,24,16,6)
            else:
                pyxel.blt(self.yadx,self.yady,0,0,64,24,16,6)
        elif self.yadm==1:#帰って
            if self.yadm_f %2==0:
                pyxel.blt(self.yadx,self.yady,0,0,48,-24,16,6)
            else:
                pyxel.blt(self.yadx,self.yady,0,0,64,-24,16,6)
        elif self.yadm==2:#元通り
            if self.yadm_f %2==0:
                pyxel.blt(self.yadx,self.yady,0,0,48,24,16,6)
            else:
                pyxel.blt(self.yadx,self.yady,0,0,64,24,16,6)
      
      
        if self.flag1 ==0:#文字の動かし方
            pyxel.text(75, 170,"Put Your Phone!",7)
            if 0<=self.frame_count%50<=5:
                pyxel.text(75, 170,"Put Your Phone!",15)
            elif 6<=self.frame_count%50<=14:
                pyxel.text(75, 170,"Put Your Phone!",14)
            elif 15<=self.frame_count%50<=20:
                pyxel.text(75, 170,"Put Your Phone!",15)
            pyxel.text(75, 150,"Enter to start",7)
        elif self.flag1 == 1:
            pyxel.text(75, 150,"How Long? (HOUR)",7)
            pyxel.text(75, 190,"ENTER to NEXT",7)
            pyxel.text(50, 170,"0",7)
            pyxel.text(60, 170,"1",7)
            pyxel.text(70, 170,"2",7)
            pyxel.text(80, 170,"3",7)
            pyxel.text(90, 170,"4",7)
            pyxel.text(100, 170,"5",7)
            pyxel.text(110, 170,"6",7)
            pyxel.text(120, 170,"7",7)
            pyxel.text(130, 170,"8",7)
            pyxel.text(140, 170,"9",7)
            pyxel.trib(51+self.cur*10,177,49+self.cur*10,181,53+self.cur*10,181,1)
        elif self.flag1 ==2:
            pyxel.text(80, 150, str(self.cur) + " H right?",7)
            pyxel.text(70, 170, "YES",7)
            pyxel.text(110, 170, "NO",7)
            if self.now ==0:
                pyxel.trib(73,177,71,181,75,181,1)
            elif self.now ==1:
                pyxel.trib(113,177,111,181,115,181,1)
        elif self.flag1 ==3:
            pyxel.text(75, 150,"How Long? (min)",7)
            pyxel.text(75, 190,"ENTER to NEXT",7)
            pyxel.text(50, 170,"0",7)
            pyxel.text(60, 170,"1",7)
            pyxel.text(70, 170,"2",7)
            pyxel.text(80, 170,"3",7)
            pyxel.text(90, 170,"4",7)
            pyxel.text(100, 170,"5",7)
            pyxel.text(110, 170,"6",7)
            pyxel.text(120, 170,"7",7)
            pyxel.text(130, 170,"8",7)
            pyxel.text(140, 170,"9",7)
            pyxel.text(150, 170,"P",7)
            pyxel.text(50, 160,"5",7)
            pyxel.text(60, 160,"10",7)
            pyxel.text(70, 160,"15",7)
            pyxel.text(80, 160,"20",7)
            pyxel.text(90, 160,"25",7)
            pyxel.text(100, 160,"30",7)
            pyxel.text(110, 160,"35",7)
            pyxel.text(120, 160,"40",7)
            pyxel.text(130, 160,"45",7)
            pyxel.text(140, 160,"50",7)
            pyxel.text(150, 160,"55",7)
            pyxel.trib(51+self.cur*10,177,49+self.cur*10,181,53+self.cur*10,181,1)
        elif self.flag1 ==4:
            pyxel.text(80, 150, str(5+5*self.cur) + " min Right?",7)
            pyxel.text(70, 170, "YES",7)
            pyxel.text(110, 170, "NO",7)
            if self.now ==0:
                pyxel.trib(73,177,71,181,75,181,1)
            elif self.now ==1:
                pyxel.trib(113,177,111,181,115,181,1)
        elif self.flag1 ==5:
            pyxel.text(60, 150, str(self.hour) + " H " + str(self.min) + " min Right?",7)
            pyxel.text(70, 170, "YES",7)
            pyxel.text(110, 170, "NO",7)
            if self.now ==0:
                pyxel.trib(73,177,71,181,75,181,1)
            elif self.now ==1:
                pyxel.trib(113,177,111,181,115,181,1)
        elif self.flag1 ==6:
            pyxel.text(75, 150,"Which Ability?",7)
            pyxel.text(75, 190,"ENTER to NEXT",7)
            pyxel.text(50, 170,"0",7)
            pyxel.text(60, 170,"1",7)
            pyxel.text(70, 170,"2",7)
            pyxel.text(80, 170,"3",7)
            pyxel.text(90, 170,"4",7)
            pyxel.text(100, 170,"5",7)
            pyxel.text(50, 160,"H",7)
            pyxel.text(60, 160,"A",7)
            pyxel.text(70, 160,"B",7)
            pyxel.text(80, 160,"C",7)
            pyxel.text(90, 160,"D",7)
            pyxel.text(100, 160,"S",7)
            pyxel.trib(51+self.cur*10,177,49+self.cur*10,181,53+self.cur*10,181,1)
        elif self.flag1 ==7:
            if self.cur ==0:
                pyxel.text(60, 150, " --HP--"+" Right?",7)
            elif self.cur ==1:
                pyxel.text(60, 150, " --ATK--"+" Right?",7)
            elif self.cur ==2:
                pyxel.text(60, 150, " --DEF--"+" Right?",7)
            elif self.cur ==3:
                pyxel.text(60, 150, " --SATK--"+" Right?",7)
            elif self.cur ==4:
                pyxel.text(60, 150, " --SDEF--"+" Right?",7)
            elif self.cur ==5:
                pyxel.text(60, 150, " --SPD--"+" Right?",7)
            pyxel.text(70, 170, "YES",7)
            pyxel.text(110, 170, "NO",7)
            if self.now ==0:
                pyxel.trib(73,177,71,181,75,181,1)
            elif self.now ==1:
                pyxel.trib(113,177,111,181,115,181,1)

    #カウントダウン画面の処理       
    def update_count_scene(self):
        pyxel.stop(0)
        pyxel.stop(1)
        if self.flag2 ==0:
            self.timer_down += 1
            self.timer -= self.timer_down
            if self.timer_down%60 ==0:
                self.sec +=1
            if self.sec ==60:
                    self.sec =0
                    self.min -=1
            if self.min ==0:
                if self.hour>=1:
                    self.hour-=1
                    self.min =59
                elif self.hour<=0:
                    self.hour-=1
                    self.min = -1
            
            if pyxel.btnp(pyxel.KEY_RETURN):
                if self.min > 0:
                    self.flag2 = 1
                elif self.min ==0:
                    if self.sec ==0:
                        self.flag2 = 2
                        if self.yad_now ==0:
                            self.yadh += 5
                        elif self.yad_now ==1:
                            self.yada += 5
                        elif self.yad_now ==2:
                            self.yadb += 5
                        elif self.yad_now ==3:
                            self.yadc += 5
                        elif self.yad_now ==4:
                            self.yadd += 5
                        elif self.yad_now ==5:
                            self.yads += 5
                        self.yad_now_p += 5
                elif self.min < 0:
                    if self.yad_now ==0:
                        self.yadh += 5
                    elif self.yad_now ==1:
                        self.yada += 5
                    elif self.yad_now ==2:
                        self.yadb += 5
                    elif self.yad_now ==3:
                        self.yadc += 5
                    elif self.yad_now ==4:
                        self.yadd += 5
                    elif self.yad_now ==5:
                        self.yads += 5
                    self.yad_now_p += 5
                    if self.timer ==0:
                        self.yadh += 200                        
                        self.yada += 200                       
                        self.yadb += 200                       
                        self.yadc += 200                        
                        self.yadd += 200                       
                        self.yads += 200
                        self.yad_now_p += 200
                    if self.timer <= -18000:
                        self.yadh += 10                        
                        self.yada += 10                       
                        self.yadb += 10                       
                        self.yadc += 10                        
                        self.yadd += 10                       
                        self.yads += 10
                        self.yad_now_p += 10
                    if self.timer <= -180000:
                        self.yadh += 10                        
                        self.yada += 10                       
                        self.yadb += 10                       
                        self.yadc += 10                        
                        self.yadd += 10                       
                        self.yads += 10
                        self.yad_now_p += 10
                    
                    self.flag2 = 2
        elif self.flag2 ==1:
            if pyxel.btnp(pyxel.KEY_RETURN):
                
                self.framenow = self.frame_count
                self.flag1 = 0
                self.flag2 = 0
                self.scene = 1
                self.timer = 0
                self.hour =0
                self.min =0
                self.sec =0
                self.timer_down = 0
                pyxel.playm(0,loop=True)
        elif self.flag2 ==2:
            if pyxel.btnp(pyxel.KEY_RETURN):
                
                self.framenow = self.frame_count
                self.yad_now_p=0
                self.yad_now=0
                self.flag1 = 0
                self.flag2 = 0
                self.scene = 1
                self.timer = 0
                self.hour =0
                self.min =0
                self.sec =0
                self.timer_down = 0
                pyxel.playm(0,loop=True)

    #カウントダウン画面の描画
    def draw_count_scene(self):
        if self.flag2 ==0:
            pyxel.cls(0)
            if self.frame_count % 120 == 0:
                self.yadn +=1
            if self.yadn ==1:
                pyxel.blt(self.yadx,self.yady-1,0,0,0,24,24,6)
                self.yadn = 2
            elif self.yadn ==2:
                pyxel.blt(self.yadx,self.yady-2,0,0,0,24,24,6)
                self.yadn = 3
            elif self.yadn ==3:
                pyxel.blt(self.yadx,self.yady-5,0,0,0,24,24,6)
                self.yadn = 4
            elif self.yadn ==4:
                pyxel.blt(self.yadx,self.yady-6,0,0,0,24,24,6)
                self.yadn = 5
            elif self.yadn ==5:
                pyxel.blt(self.yadx,self.yady-5,0,0,0,24,24,6)
                self.yadn = 6
            elif self.yadn ==6:
                pyxel.blt(self.yadx,self.yady-2,0,0,0,24,24,6)
                self.yadn = 7
            elif self.yadn ==7:
                pyxel.blt(self.yadx,self.yady-1,0,0,0,24,24,6)
                self.yadn = 0 
            else:
                pyxel.blt(self.yadx,self.yady,0,0,0,24,24,6)
            if self.min >0:
                pyxel.text(70, 160,str(self.hour)+" H " + str(self.min-1) + " M " + str(60-self.sec) + " S ",7)
            else:
                pyxel.text(70, 160,str(self.hour+1)+" H " + str(self.min+1) + " M " + str(self.sec) + " S ",7)
            pyxel.text(60, 180,"ENTER to TIMER STOP",7)
        elif self.flag2 ==1:
            pyxel.cls(0)
            pyxel.blt(self.yadx,self.yady,0,0,24,16,20,6)
            hour = math.floor(self.timer%216000)
            min = math.floor(self.timer%216000%60)
            sec = math.floor(self.timer%216000%3600)
            if self.min >0:
                pyxel.text(70, 160,str(self.hour)+" H " + str(self.min-1) + " M " + str(60-self.sec) + " S ",7)
            else:
                pyxel.text(70, 160,str(self.hour+1)+" H " + str(self.min+1) + " M " + str(self.sec) + " S ",7)
            pyxel.text(80,150,"YOU FAILED",7)
            pyxel.text(75, 190,"ENTER to NEXT",7)
        elif self.flag2 ==2:
            pyxel.cls(0)
            pyxel.blt(self.yadx,self.yady,0,0,24,16,20,6)
            if self.min >0:
                pyxel.text(70, 160,str(self.hour)+" H " + str(self.min-1) + " M " + str(60-self.sec) + " S ",7)
            else:
                pyxel.text(70, 160,str(self.hour+1)+" H " + str(self.min+1) + " M " + str(self.sec) + " S ",7)
            pyxel.text(80,150,"YOU SUCCESSED",7)
            pyxel.text(75, 190,"ENTER to NEXT",7)
            pyxel.text(80,175,"Your YADON got " + str(self.yad_now_p) +" POINTS!",7)


App()
