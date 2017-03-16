#-*-coding:utf-8-*-

class Rabbit(object):
    "This is a rabiit"

    # 属性
    color = 'white'
    legs = 4
    longEars = 2

    # 方法
    def run(self):
        print '跑的嗖嗖快~~'

    def eat_carrot(self):
        print '恩，我最喜欢胡萝卜！！！'

    def bite(self):
        print '憋惹我，会咬人……'

    def playing_cute(self):
        print '可撒娇，会卖萌n(*≧▽≦*)n'


ra = Rabbit()
Rabbit()

# 调用其中的方法
ra.run()
ra.eat_carrot()
ra.bite()
ra.playing_cute()

# 类是对象的模板，像是玩具的模具，对象是根据模具所生产出来的玩具
