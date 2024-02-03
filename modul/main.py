from menu import choise_pizza
#from order import show_order
#from cost import show_cost
#from pay import show_pay
#from check import give_check
from cost import show_cost
from pay import pay
import time

def start():
    choise_pizza()
    time.sleep(2)
    show_cost()
    time.sleep(3)
    pay()
start()