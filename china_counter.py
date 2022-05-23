class China:
    def __init__(self,num):
        self.num = num
        self.num_china = {
            0:'零',1:'一',2:'二',3:'三',
            4:'四',5:'五',6:'六',7:'七',
            8:'八',9:'九',10:'十',100:'百',
            1000:'千',10000:'万',100000:'十',
            1000000:'百',10000000:'千',100000000:'亿',
            1000000000:'十',
        }
        self.list_of_numbers = list(str(self.num)) #разбиваем на цифры исходное число
        self.zeros = [] #разряды для исходного числа в виде степеней числа 10
        self.chinaa = [] #
    def __str__(self):
        return ''.join(self.chinaa)
    def detec(self):
        count = len(self.list_of_numbers) #кол-во цифр исходного числа
        for i in self.list_of_numbers: #перебор цифр исходного
            if(count!=1):
                self.zeros.append(10**(count-1)) #заполнение разрядов
                count-=1
        #print(self.zeros)
        #print(self.list_of_numbers)
    def main(self):
        cc = -1 #счётчик для списка разрядов
        for i in self.list_of_numbers:
            if(i!='0'): #ноль в исходном числе не читается
                self.chinaa.append(self.num_china[int(i)])
                if(cc < len(self.zeros)-1):#разрядов на 1 меньше общей длинны исходного числа (единичный разряд не нужен)
                    cc += 1
                    self.chinaa.append(self.num_china[self.zeros[cc]])


print('Перевод цифр на китайские иероглифы:')
while True:
    try:
        cl = China(input('Введите число/цифру(или нажмите ENTER для выхода): '))
        cl.detec()
        cl.main()
        print(cl)
        break
    except:
        print('\nERROR!!\nЯ могу распознать только цифры до 10 МЛРД\n')
