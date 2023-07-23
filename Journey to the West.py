import time

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

class Room:
    def __init__(self, name, description, items=None, monster=None, event=None, exit=False):
        self.name = name
        self.description = description
        self.items = items if items else []
        self.monster = monster
        self.event = event
        self.exit = exit

    def __str__(self):
        return self.name

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

class Event:
    def __init__(self, description):
        self.description = description

def show_inventory(player):
    print("你的背包：")
    for item in player.inventory:
        print(f"{item.name}: {item.description}")

def show_room(room):
    delay_print(f"\n你进入了{room.name}。")
    delay_print(room.description)

def choose_action():
    print("\n你可以做以下操作：")
    print("1. 探索房间")
    print("2. 查看背包")
    print("3. 前往其他房间")
    while True:
        try:
            choice = int(input("请输入你的选择（1/2/3）："))
            if 1 <= choice <= 3:
                return choice
            else:
                print("无效的选择，请重新输入。")
        except ValueError:
            print("无效的输入，请重新输入。")

def explore_room(player, room):
    show_room(room)

    if room.items:
        for item in room.items:
            player.add_item(item)
            delay_print(f"你在{room.name}发现了{item.name}。")
            delay_print(f"{item.description} 已添加到你的背包中。")

    if room.monster:
        delay_print(f"突然，一只凶恶的{room.monster.name}跳了出来！")
        battle(player, room.monster)

    if room.event:
        delay_print(room.event.description)

def battle(player, monster):
    while player.health > 0 and monster.health > 0:
        delay_print(f"\n你的生命值：{player.health}  {monster.name}的生命值：{monster.health}")
        choice = input("你要攻击（A）还是逃跑（E）？").lower()
        if choice == "a":
            player.attack(monster)
            monster.attack(player)
        elif choice == "e":
            delay_print("你逃跑了。")
            break
        else:
            delay_print("无效的选择，请重新输入。")

    if player.health <= 0:
        delay_print("你被击败了，游戏结束。")
        exit()

def play_game():
    player_name = input("请输入你的角色名字：")
    player = Player(player_name)

    room1 = Room("迷宫入口", "你来到了一个神秘的迷宫入口。", [Item("钥匙", "可以打开某些门")])
    room2 = Room("迷宫中部", "你来到了迷宫的中部。", [Item("草药", "恢复10点生命值")], Monster("恶龙", 50, 15))
    room3 = Room("迷宫深处", "你来到了迷宫的深处。", event=Event("你发现了宝藏，恭喜你获得胜利！"), exit=True)

    room1.connect(room2, "east")
    room2.connect(room1, "west")
    room2.connect(room3, "east")
    room3.connect(room2, "west")

    current_room = room1

    delay_print(f"欢迎来到《西游释厄传》游戏，{player_name}！")
    delay_print("你将在迷宫中寻找宝藏。")

    while True:
        show_room(current_room)
        action = choose_action()

        if action == 1:
            explore_room(player, current_room)
        elif action == 2:
            show_inventory(player)
        elif action == 3:
            direction = input("你要前往东边（E）还是西边（W）？").lower()
            next_room = current_room.get_adjacent_room(direction)
            if next_room:
                current_room = next_room
            else:
                delay_print("无效的方向，请重新输入。")

if __name__ == "__main__":
    play_game()
