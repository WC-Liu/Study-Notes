"""
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：
1. 添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
2. 修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
3. 删除学生成绩：根据输入的学生姓名，删除对应的学生成绩6
4. 查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
5. 展示全部学生成绩：展示出系统中所有学生的成绩

"""
class Student():
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    # "姓名：张三 | 语文：85 | 数学：90 | 英语：88 | 总分：263
    def __str__(self):
        total = self.chinese + self.math + self.english
        return (f"姓名：{self.name} | 语文：{self.chinese } | 数学：{self.math} | 英语：{self.english}"
                f"| 总分：{total}")

    #修改学生的成绩
    def update_score(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = [] #列表，记录在校学生的成绩

    # 添加学生成绩
    def add_student(self):
        name = input("请输入学生姓名: ")

        #判断学生姓名是否存在，如果存在，则添加失败（不能重复添加）
        for s in self.student_list:
            if s.name == name:
                print(f"该学生{name}已经存在，添加失败！")
                return

        #try:
        chinese = int(input("请输入学生语文成绩："))
        math = int(input("请输入学生数学成绩："))
        english = int(input("请输入学生英语成绩："))

        # 判断分数是否在0-100之中
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name, chinese, math, english)
            self.student_list.append(stu)
        else:
            print("各科成绩必须在 0 - 100 之间！")
            return
    # 修改学生成绩
    def update_student(self):
        name = input("请输入学生姓名: ")

        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩：{s}")
                chinese = int(input("请输入修改后学生语文成绩："))
                math = int(input("请输入修改后学生数学成绩："))
                english = int(input("请输入修改后学生英语成绩："))

                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese, math, english)
                    print("成绩修改成功")
                    print(f"修改后的成绩：{s}")
                    return
                else:
                    print("各科成绩必须在 0 - 100 之间！")
                    return
        print("未找到该学生，修改失败！")

    # 删除学生成绩
    def delete_student(self):
        name = input("请输入学生姓名: ")

        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("学生信息删除成功")
                return
        print("未找到该学生，删除失败！")

    # 查询指定学生成绩
    def query_student(self):
        name = input("请输入学生姓名: ")

        for s in self.student_list:
            if s.name == name:
                print(f"学生信息：{s}")
                return

        print("未找到该学生！")

    # 展示全部学生成绩
    def list_student(self):
        for s in self.student_list:
            print(s)

    # 运行系统
    def run(self):
        print("欢迎使用教务管理系统")

        while True:
            print()
            print("#" * 60)
            print("# 1.添加学生  2.修改学生  3.删除学生  4.查询指定学生  5.查询所有学生  6.退出系统 #")
            print("#" * 60)

            choice = input("\n请选择要执行的操作，输入1-6: ")

            try:
                match choice:
                    case "1":
                        self.add_student()
                    case "2":
                        self.update_student()
                    case "3":
                        self.delete_student()
                    case "4":
                        self.query_student()
                    case "5":
                        self.list_student()
                    case "6":
                        print("再见")
                        break
                    case _:
                        print("输入错误，请选择1-6之间的菜单功能")
            except ValueError:
                print("输入的数据有问题，请检查，然后重新输入")
            except Exception as e:
                print("程序运行出错了，请重新选择~")
#测试
if __name__ == '__main__':
    edu_management = EduManagement()
    edu_management.run()