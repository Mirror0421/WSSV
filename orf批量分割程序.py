import xlrd
import string

sq = 12  
data = xlrd.open_workbook(r'C:/Users/lenovo/Desktop/xulie.xls')  
table = data.sheets()[0]
cols_list0 = table.col_values(colx=0)  
cols_list1 = table.col_values(colx=1)  

for j in range(0, len(cols_list1)):
    j_str = ''  
    j_str = str(cols_list1[j])  
    filename = 'C:/Users/lenovo/Desktop/所需标准株orf/' + j_str + '.txt'  
    filename1 = 'C:/Users/lenovo/Desktop/待查看/' + j_str + '.txt'  
    with open(filename, encoding='utf-8') as f1:
        str0 = f1.read()
        str1 = str0[str0.index('\n') + 1:len(str0)]
        str1 = str1.replace('\n', '')  
        str2 = str1[0:sq]  
        str3 = str1[len(str1) - sq:len(str1)]  
    with open(filename1, "w") as d:  
        a = str(len(str1))  
        print(a)
        d.write('该orf的标准长度为' + a + '\n')  

        for i in range(0, 4):  
            i_str = ''  
            i_str = str(cols_list0[i])  
            filename2 = 'C:/Users/lenovo/Desktop/对齐后新基因组/' + i_str + '.txt'  
            with open(filename2, encoding='utf-8') as f2:
                strd = f2.read()  
                strd = strd.replace('\n', '')  
                try:
                    print(strd.index(str2))  
                    strd1 = strd[strd.index(str2):len(strd)] 
                    print(strd1.index(str3) + len(str3))  
                except ValueError:  
                    print('error')
                    d.write('>' + i_str + '\n')  
                    d.write('error' + '\n')  
                else:
                    print(len(strd[strd.index(str2):strd.index(str3) + len(str3)]))  
                    print(strd[strd.index(str2):strd.index(str3) + len(str3)])  
                    c = str(strd.index(str2))  
                    D = str(strd1.index(str3) + len(str3))  
                    c1 = int(c)
                    D1 = int(D)
                    D2 = c1+D1
                    D3 = str(D2)
                    d.write('>' + i_str)  
                    d.write('(' + D + ')')  
                    d.write('(' + c + ')')
                    d.write('(' + D3 + ')' + '\n')
                    d.write(strd[c1:D2] + '\n')  
