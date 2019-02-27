#!/usr/bin/env python3
from copy import copy, deepcopy
from answer_html import print_answer
import cgi


form = cgi.FieldStorage()

m = 3
n = 4



Cik = []
Lik = []
for i in range(m):
    Cikk = []
    Likk = []
    for j in range(n):
        Cikk.append(float(form.getfirst("C_"+str(i+1)+str(j+1), 0)))
        Likk.append(float(form.getfirst("L_"+str(i+1)+str(j+1), 0)))
    Cik.append(Cikk)
    Lik.append(Likk)

Bk = []
Rk = []
for i in range(m):
    Bk.append(float(form.getfirst("B_"+str(i+1), 0)))
    Rk.append(float(form.getfirst("R_"+str(i+1), 0)))


Gi = []
Di = []
Cip = []
Si = [] 
Lip = []
for i in range(n):
	Gi.append(float(form.getfirst("G_"+str(i+1), 0)))
	Di.append(float(form.getfirst("D_"+str(i+1), 0)))
	Cip.append(float(form.getfirst("C_"+str(i+1), 0)))
	Si.append(float(form.getfirst("S_"+str(i+1), 0)))
	Lip.append(float(form.getfirst("L_"+str(i+1), 0)))

pen = float(form.getfirst("Pen"))
if pen > 1:
    b = 2
    p = 2
else:
    b = 10
    p = 5


def Q (xx, i):
    Wi = 0.0
    for k in range(m):
        Wi += Lik[k][i]*xx[k][i]

    res = 0.0

    if ((Gi[i]+Di[i])/2 - Wi > 0):
        res = ((int(((Gi[i]+Di[i])/2 - Wi + 1)/Lip[i])  + 1) * Cip[i]) + Si[i]
    else:
        for k in range(m):
            res += Rk[k] * xx[k][i]
    return res


# In[199]:


def f(xx):
    sum1 = 0
    for j in range(m):
        for i in range(n):
            sum1 += xx[j][i] * Cik[j][i]
    for i in range(n):
        sum1 += Q(xx,i) 
    return sum1

def g1(xx, i):
    sum1 = 0.0
    for k in range(m):
        sum1 += Lik[k][i]*xx[k][i]

    return sum1 - (Gi[i] + Di[i]) / 2

def g2(xx, j):
    sum1 = 0.0
    for i in range(n):
        sum1 += xx[j][i]
    return Bk[j] - sum1

def g3(xx, j, i):
    return xx[j][i]


# In[200]:


def Alfa (xx):
    d1 = 0.0
    for i in range(n):
        d1 += max(0, -g1(xx,i))**p

    d2 = 0.0
    for j in range(m):
        d2 += max(0, -g2(xx,j))**p

    d3 = 0.0
    for j in range(m):
        for i in range(n):
            d3 += max(0, -g3(xx, j, i))**p
    return d1+d2+d3

def MainFunc(xx, rk):
    return f(xx) + rk*Alfa(xx)


# In[201]:


def Possible_Directions (xx, rk):
    found = 0
    is_sample = 0  # Индикатор поиска по образцу
    iter_n = 0
    x = xx
    q = deepcopy(xx)
    bb = deepcopy(xx)
    f_x = 0.0
    
    
    h = [[0.1, 0.1, 0.1, 0.1],
        [ 0.1, 0.1, 0.1, 0.1],
        [ 0.1, 0.1, 0.1, 0.1]]

    while (h[0][0] > 0.00001 and (iter_n < 10)):
        iter_n += 1
        for j in range(m):
            for i in range(n):
                f_x = MainFunc(x, rk)
                c = deepcopy(x)
                c[j][i] += h[j][i]             #шаг в положит. направлении j,i-ой коорд.
                if (MainFunc(c, rk) < f_x):
                    x = c
                    found = 1
                else:
                    c[j][i] -= 2 * h[j][i]     #шаг в отриц. напр. j,i-ой коорд.
                    if (MainFunc(c, rk) < f_x):
                        x = c
                        found = 1
                    else:
                        found = 0
                                                        
        if (is_sample == 1):
            if (found == 0 | (MainFunc(x, rk) >= MainFunc(q, rk))):            
                x = deepcopy(q)               #вернуться к базовой точке
                bb = deepcopy(q)
                is_sample = 0
                continue
            else:    
                bb = deepcopy(q)                #запомнить новую базовую точку
        else:
            if (found == 0):
                for j in range(m):
                    for i in range(n):
                        h[j][i] *= 0.1         #если исслед. поиск законч. неудачей - уменьшить шаг
                continue
    
        q = deepcopy(x)                       #поиск по образцу 

        for j in range(m):
            for i in range(n):
                x[j][i] = 2 * q[j][i] - bb[j][i]
        is_sample = 1
    return deepcopy(x)


# In[202]:


def PenaltyFunction(rk, be):
    count = 0
    eps = 0.0001
    #file = open(r"C:\Users\ASUSa\Desktop\Results.txt")
    x = [[.0, .0, .0, .0],
         [.0, .0, .0, .0],
         [.0, .0, .0, .0]]
    while (rk * Alfa(x) >= eps and count < 1000):
        count += 1
        x = Possible_Directions(x, rk)
        rk = rk*be
    
    return x


# In[203]:


x_1 = PenaltyFunction(pen, b)


x = []
for i in [elem for elem in x_1]:
    xx = [round(j) if j>0 else 0 for j in i ]
    x.append(xx)
resultValue = f(x)

# y = []
# for i in range(m):
#     xx = []
#     for j in range(n):
#         xx.append(Lik[i][j]* x[i][j])
#     y.append(xx)
print_answer(x,resultValue)