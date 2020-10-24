from turtle import Turtle, Screen

wn = Screen()

def tree(length,t):
    if length > 5:
        t.forward(length) # ileri git
        t.right(40)       # sağa dön
        tree(length-15,t) # daha küçük bir ağaç çiz
        t.left(80)        # sola dön
        tree(length-15,t) # daha küçük bir ağaç çiz
        t.right(40)       # Başladığın açıya geri dön
        t.backward(length)# Başladığın noktaya geri dön


t = Turtle()
t.left(90) # Yukarıya doğru çizmek için
t.speed(0) # en hızlı animasyon

tree(100,t)

wn.exitonclick()
