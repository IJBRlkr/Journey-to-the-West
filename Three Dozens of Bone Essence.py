import time

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0

    def attack(self, target):
        damage = self.attack_power
        target.take_damage(damage)
        return damage

class SunWukong(Character):
    def __init__(self):
        super().__init__("孙悟空", health=100, attack_power=30)

class BaiGuJing(Character):
    def __init__(self):
        super().__init__("白骨精", health=80, attack_power=25)

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def fight(player, enemy):
    delay_print(f"{player.name}遭遇了{enemy.name}！")
    while player.health > 0 and enemy.health > 0:
        player_damage = player.attack(enemy)
        enemy_damage = enemy.attack(player)
        delay_print(f"{player.name}对{enemy.name}造成了{player_damage}点伤害，{enemy.name}剩余{enemy.health}生命值。")
        delay_print(f"{enemy.name}对{player.name}造成了{enemy_damage}点伤害，{player.name}剩余{player.health}生命值。")
        if enemy.health <= 0:
            delay_print(f"{player.name}战胜了{enemy.name}！")
            break
        elif player.health <= 0:
            delay_print(f"{player.name}被{enemy.name}击败，游戏结束。")
            exit()

def main():
    player = SunWukong()
    bai_gu_jing = BaiGuJing()

    delay_print("欢迎来到《西游记》三打白骨精游戏！")
    delay_print("你将扮演孙悟空，与白骨精进行三次战斗。")

    for i in range(3):
        delay_print(f"第{i+1}次战斗：")
        fight(player, bai_gu_jing)
        if i < 2:
            bai_gu_jing.health = 80
            delay_print("白骨精逃走了，准备迎接下一次战斗！")

    delay_print("恭喜你，成功三打白骨精！游戏结束。")

if __name__ == "__main__":
    main()
