import random

def main():
    print("欢迎来到西游记打黑熊怪的游戏！")
    print("你是孙悟空，一位伟大的大圣。")
    print("一只凶恶的黑熊怪正袭击无辜的村民。")
    print("你必须阻止黑熊怪，保卫村庄！")

    health = 100  # 孙悟空的初始生命值
    bear_health = 80  # 黑熊怪的初始生命值

    while health > 0 and bear_health > 0:
        print("\n你的生命值：", health)
        print("黑熊怪的生命值：", bear_health)
        print("选择一个行动：")
        print("1. 使用金箍棒攻击黑熊怪")
        print("2. 使用筋斗云逃跑")
        
        choice = input("请输入选项的数字：")

        if choice == "1":
            player_damage = random.randint(10, 20)
            bear_damage = random.randint(5, 15)
            print(f"你对黑熊怪造成了 {player_damage} 点伤害！")
            print(f"黑熊怪对你造成了 {bear_damage} 点伤害！")
            health -= bear_damage
            bear_health -= player_damage
        elif choice == "2":
            print("你使用筋斗云逃跑了！")
            break
        else:
            print("无效的选项，请重新选择。")

    if health <= 0:
        print("你被黑熊怪击败了，村庄失去了保护！")
    elif bear_health <= 0:
        print("你成功击败了黑熊怪，村庄得以安全！")

if __name__ == "__main__":
    main()
