# 2023project
Final assignment for dlut open source course.

## 2023年大连理工大学开源软件基础课程大作业
## 开源软件svelte历史提交信息分析
### 成员信息
| 小组成员 | 学号 | GitHub用户名 |
| ----------- | ----------- | ----------- |
| 付天赐 | 20212241306 | sparklesheep |
| 侯欣桐 | 20212241322 | coderhooxi |
| 安真达 | 20212241460 | azd-ui |

### 文件说明
login.py：用于GitHub API进行身份认证

spider.py：爬虫脚本

commits.xlsx：爬虫获取的excel数据

Figure_1.png：作者-提交次数柱状图

Figure_2.png：作者编号，提交次数，平均评论量三维散点图

Figure_3.png：提交日期-提交量柱状图

Figure_4.png：提交日期-提交量柱状图

Figure_5.png：message词云图

Figure_6.png：message柱状图

Figure_7.png：一日内提交时间-提交量折线图

data_cleaning.py：清洗数据，按照作者首字母、提交日期、提交时间进行排序

update_commits.xlsx：清洗后的除message的数据

view1：对提交量超过三次的作者进行提交次数的统计分析

view2：对提交作者、提交次数和评论平均量绘制三维散点图分析

view3：对一年中提交时间和提交量绘制柱状图分析

view4：对一日内提交时间和提交量的折线分析

cleaned_message.txt：清洗后的message数据

message analyse.py：分析message数据的脚本

