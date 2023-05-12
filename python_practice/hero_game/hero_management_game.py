# 每个操作封装成一个函数
# 创建英雄：当前游戏中，创建英雄角色，定义好对应英雄的血量及其攻击力。
# 查看英雄信息：查看当前游戏中所有的英雄信息。
# 修改英雄信息：修改英雄的血量。
# 删除英雄：英雄太弱，不需要，删除掉。
# 退出系统：结束程序

class HeroManagement:
    def __init__(self):
        self.hero_list = []

    def create_hero(self, hero_name, hero_volume, hero_prower):
        if hero_volume <= 0 or hero_volume > 100:
            return False
        if hero_prower <= 0:
            return False
        hero ={'name':hero_name , 'volume':hero_volume , 'prower':hero_prower}
        self.hero_list.append(hero)

    def find_hero(self, name):
        for hero in self.hero_list:
            if hero['name'] == name:
                return hero
        return False

    def updata_hero(self, name, volume):
        for hero in self.hero_list:
            if hero['name'] == name:
                hero['volume'] = volume
        return False

    def delete_hero(self, name):
        for hero in self.hero_list:
            if hero['name'] == name:
                self.hero_list.remove(hero)
        return False

    def exit_game(self):
        print('游戏结束')
        exit(0)


if __name__ == "__main__":
    # 实例化一个HeroManagement对象
    my_hero = HeroManagement()
    # 创建英雄
    my_hero.create_hero('baiqi', 100, 33)
    # 查看英雄
    print(my_hero.find_hero('baiqi'))
    # 修改英雄的血量
    my_hero.updata_hero('baiqi', 98)
    # 检查该英雄血量是否修改成功
    print(my_hero.find_hero('baiqi'))
    # 删除该英雄
    my_hero.delete_hero('baiqi')
    # 检查该英雄是否删除成功
    print(my_hero.find_hero('baiqi'))
    # 退出游戏
    my_hero.exit_game()










