import xlrd
import string

sq = 12  # 选取的开头结尾多少碱基为保守区域
data = xlrd.open_workbook(r'C:/Users/lenovo/Desktop/xulie.xls')  # 读取表格文件
table = data.sheets()[0]
cols_list0 = table.col_values(colx=0)  # 读取所有未知序列名称
cols_list1 = table.col_values(colx=1)  # 读取需要寻找的orf的名称

for j in range(0, len(cols_list1)):
    j_str = ''  # 清除j_str内字符串
    j_str = str(cols_list1[j])  # 读取当前orf名称
    filename = 'C:/Users/lenovo/Desktop/所需标准株orf/' + j_str + '.txt'  # 组成读取标准orf文件的路径
    filename1 = 'C:/Users/lenovo/Desktop/待查看/' + j_str + '.txt'  # 组成保存找到的orf的路径
    with open(filename, encoding='utf-8') as f1:
        str0 = f1.read()
        str1 = str0[str0.index('\n') + 1:len(str0)]
        str1 = str1.replace('\n', '')  # 得到纯碱基序列，去掉fasta格式>的内容
        str2 = str1[0:sq]  # 需要查寻的ORF的开头保守区域
        str3 = str1[len(str1) - sq:len(str1)]  # 需要查寻的ORF的结尾保守区域
    with open(filename1, "w") as d:  # 创建保存结果的txt
        a = str(len(str1))  # 标准orf的长度
        print(a)
        d.write('该orf的标准长度为' + a + '\n')  # 在最开头输入该标准orf的长度方便校对

        for i in range(0, 4):  
            i_str = ''  # 清除i_str内字符串
            i_str = str(cols_list0[i])  # 读取当前序列名称
            filename2 = 'C:/Users/lenovo/Desktop/对齐后新基因组/' + i_str + '.txt'  # 组成读取需要查找的位置序列的路径
            with open(filename2, encoding='utf-8') as f2:
                strd = f2.read()  # 全序列导入
                strd = strd.replace('\n', '')  # 得到无换行空格的字符串
                try:
                    print(strd.index(str2))  # 寻找的orf的开头位于第几位
                    strd1 = strd[strd.index(str2):len(strd)]  # 删去orf开头之前的数据防止找结尾找到开头之前
                    print(strd1.index(str3) + len(str3))  # 寻找的orf的结尾位于第几位
                except ValueError:  # 如果发生寻找不到开头或者结尾的情况的处理
                    print('error')
                    d.write('>' + i_str + '\n')  # 输入fasta结构的标头
                    d.write('error' + '\n')  # 在txt文档中提示报错
                else:
                    print(len(strd[strd.index(str2):strd.index(str3) + len(str3)]))  # 得出找到的orf的长度，用以初步验证找到的orf有没有问题
                    print(strd[strd.index(str2):strd.index(str3) + len(str3)])  # 寻找到的新全序列中对应的orf
                    c = str(strd.index(str2))  # 寻找的orf的开头位于第几位
                    D = str(strd1.index(str3) + len(str3))  # 寻找的orf的结尾位于第几位以及orf长度
                    c1 = int(c)
                    D1 = int(D)
                    D2 = c1+D1
                    D3 = str(D2)
                    d.write('>' + i_str)  # 输入fasta结构的标头
                    d.write('(' + D + ')')  # 输入寻找到的orf的长度
                    d.write('(' + c + ')')
                    d.write('(' + D3 + ')' + '\n')
                    d.write(strd[c1:D2] + '\n')  # 输入寻找到的新全序列中对应的orf
