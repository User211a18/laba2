rost=1.80
ves=70
sagi=10000
time=90 #minut
dlina_shaga=rost/4+0.37
dlina=sagi*dlina_shaga
score=dlina/time
kkal=0.035*ves+(score**2/rost)*0.029*ves
print("Дистанция в метрах: "+str(dlina)+"; Количество сожжённых килокалорий: "+str(kkal))
print("Дистанция в км: "+str(dlina/1000))
if dlina/1000<2:
    print("Хорошая работа, но ты мжешь и лучше")
if dlina/1000<4 and dlina/1000>2:
    print("Осталось немного до цели")
if dlina/1000>4:
    print("Отлично, ты достиг цели")