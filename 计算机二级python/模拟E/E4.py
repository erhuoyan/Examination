import turtle as t
for i in range(4):
    t.seth((i+1)*90)
    t.circle(200,90)
    t.seth(-90+i*90)
    t.circle(200,90)
