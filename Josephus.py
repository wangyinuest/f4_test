# Person 类：包含参与约瑟夫环每个人的基本信息（编号、名字和性别）。
class Person:
    def __init__(self, id_num, name, gender):
        self.id_num = id_num
        self.name = name
        self.gender = gender

    def __repr__(self):
        return f"编号: {self.id_num}, 名字: {self.name}, 性别: {self.gender}"
    
# JosephusCircle 类：处理约瑟夫环逻辑。
class JosephusCircle:
    def __init__(self):
        self.people = []
        self.total_people = int(input("请输入总人数: "))
        self.step = int(input("请输入步长: "))
        self.start_position = int(input("请输入开始数数的位置: "))
        self._create_people()

        
    def _create_people(self):
        """
        根据总人数创建参与人员列表，包含姓名、编号和性别信息。
        """
        for i in range(1, self.total_people + 1):
            name = input(f"请输入第 {i} 个人的名字: ")
            gender = input(f"请输入第 {i} 个人的性别 (M/F): ")
            self.people.append(Person(i, name, gender))

    def solve(self):
        """
        解决约瑟夫环问题，返回最后幸存者的信息。
        """
        index = (self.start_position - 1) % self.total_people  # 确定起始位置的索引
        while len(self.people) > 1:
            index = (index + self.step - 1) % len(self.people)
            eliminated_person = self.people.pop(index)  # 移除该位置的人员
            print(f"淘汰: {eliminated_person}")

        return self.people[0]  # 返回最后幸存者的信息

# 实例化 JosephusCircle 类，调用 solve 方法。
if __name__ == "__main__":
    circle = JosephusCircle()
    survivor = circle.solve()
    print(f"最后幸存者是: {survivor}")
