import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button


textbox1 = TextBox(plt.axes([0.3, 0.8, 0.5, 0.075]), 'number1')
textbox2 = TextBox(plt.axes([0.3, 0.7, 0.5, 0.075]), 'number2')
textbox3 = TextBox(plt.axes([0.3, 0.6, 0.5, 0.075]), 'number3')
button = Button(plt.axes([0.3, 0.5, 0.5, 0.075]), "submit")


def calculate(num1, num2):
    a = int(num1, 2)
    b = int(num2, 2)
    c = int('10000000000000000', 2)

    res = a + b
    if res >= c:
        res = res - c + 1

    return format(res, '#018b')


def flip(num):
    return bin(((1 << 16) + (~int(num, 2))))


def button_clicked(event):
    textbox4 = TextBox(plt.axes([0.3, 0.2, 0.5, 0.075]), "result",
                       initial=flip(calculate(calculate(textbox1.text, textbox2.text), textbox3.text)))
    plt.show()


button.on_clicked(button_clicked)
plt.show()



