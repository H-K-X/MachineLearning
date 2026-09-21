import pandas as pd
import numpy as np

# 单周课表
schoolTimetableOdd = pd.DataFrame({
    'Monday' : ['异构数据融合', '异构数据融合', '数据结构与算法设计', '数据结构与算法设计', '体育-足球', '体育-足球', '概率论与数理统计', '概率论与数理统计', '', '', ''],
    'Tuesday' : ['毛概', '毛概', '毛概', '', '形策(7-10)', '形策(7-10)', '', '', '', '', ''],
    'Wednesday' : ['概率论与数理统计', '概率论与数理统计', '数据结构与算法设计', '数据结构与算法设计', '', '', '机器学习与大数据计算', '机器学习与大数据计算', '工程力学', '工程力学', '工程力学'],
    'Thursday' : ['', '', '', '', '异构数据融合', '异构数据融合', '异构数据融合', '异构数据融合', '博弈与社会', '博弈与社会', ''],
    'Friday' : ['工程力学', '工程力学', '电路与电子技术', '电路与电子技术', '电路与电子技术', '电路与电子技术', '经济学原理', '经济学原理', '', '', ''],
    'Saturday' : ['', '', '', '', '', '', '', '', '', '', ''],
    'Sunday' : ['', '', '', '', '', '', '', '', '', '', ''],},
    index = ['1-8:00-8:45', '2-8:50-9:35', '3-10:00-10:45', '4-10:50-11:35', '5-13:30-14:15', '6-14:20-15:05', '7-15:30-16:15', '8-16:20-17:05', '9-18:30-19:15', '10-19:20-20:05', '11-20:10-20:55'],
    )
# 双周课表
schoolTimetableEven = pd.DataFrame({
    'Monday' : ['异构数据融合', '异构数据融合', '数据结构与算法设计', '数据结构与算法设计', '体育-足球', '体育-足球', '概率论与数理统计', '概率论与数理统计', '', '', ''],
    'Tuesday' : ['毛概', '毛概', '毛概', '', '形策(7-10)', '形策(7-10)', '', '', '', '', ''],
    'Wednesday' : ['', '', '经济学原理', '经济学原理', '', '', '机器学习与大数据计算', '机器学习与大数据计算', '工程力学', '工程力学', '工程力学'],
    'Thursday' : ['', '', '', '', '异构数据融合', '异构数据融合', '异构数据融合', '异构数据融合', '博弈与社会', '博弈与社会', ''],
    'Friday' : ['工程力学', '工程力学', '电路与电子技术', '电路与电子技术', '电路与电子技术', '电路与电子技术', '经济学原理', '经济学原理', '', '', ''],
    'Saturday' : ['', '', '', '', '', '', '', '', '', '', ''],
    'Sunday' : ['', '', '', '', '', '', '', '', '', '', ''],},
    index = ['1-8:00-8:45', '2-8:50-9:35', '3-10:00-10:45', '4-10:50-11:35', '5-13:30-14:15', '6-14:20-15:05', '7-15:30-16:15', '8-16:20-17:05', '9-18:30-19:15', '10-19:20-20:05', '11-20:10-20:55'],
    )

# 格式化输出课表
# schoolTimetables = [schoolTimetableOdd, schoolTimetableEven]
# for timetable in schoolTimetables:
#     for lessons in timetable.values:
#         for i in range(len(lessons)):
#             lessons[i] = f'{lessons[i]:^20}'
#     for time in timetable.index:
#         timetable.rename(index={time: f'{time:^13}'}, inplace=True)

# 输出课表
print("Odd Week Timetable:")
print(schoolTimetableOdd)
print("\nEven Week Timetable:")
print(schoolTimetableEven)

# 周六课程
SaturdayLessons = pd.Series(['辅修', '辅修', '', '', '', '', '', '', '', '', ''], index=schoolTimetableOdd.index)
# 将周六课程添加到单周和双周课表中
for timetable in [schoolTimetableOdd, schoolTimetableEven]:
    timetable['Saturday'] = SaturdayLessons

# 输出课表
print("\nOdd Week Timetable:")
print(schoolTimetableOdd)
print("\nEven Week Timetable:")
print(schoolTimetableEven)