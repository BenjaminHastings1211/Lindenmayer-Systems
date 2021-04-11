from ruleDeclaration import RuleSystem;
import turtle, random

t = turtle.Pen()
t.speed(1000000)

l = 5;

def teleport(t,pos):
    t.up()
    t.goto(pos[0],pos[1])
    t.down()

def push(stack):
    stack.append([t.pos(),t.heading()])

def pop(stack):
    data = stack[-1]
    del stack[-1]
    teleport(t,data[0])
    t.setheading(data[1])

def showSystem(system,n):
    plan = system.generate(n);
    print(plan);
    system.execute(plan);

koch = RuleSystem(
    { "F" : lambda : t.forward(l)},
    { "+" : lambda : t.left(90), "-" : lambda : t.right(90)},
    "F",
    { "F" : "F+F-F-F+F"}
)

tri = RuleSystem(
    {"F" : lambda : t.forward(l), "G" : lambda : t.forward(l)},
    {"+" : lambda : t.left(120), "-" : lambda : t.right(120)},
    "F-G-G",
    {"F" : "F-G+F+G-F", "G" : "GG"}
)

hex = RuleSystem(
    {"F" : lambda : t.forward(l), "G" : lambda : t.forward(l)},
    {"+" : lambda : t.left(60), "-" : lambda : t.right(60)},
    "F",
    {"F" : "G-F-G", "G" : "F+G+F"}
)

dragon = RuleSystem(
    {"F" : lambda : t.forward(l), "G" : lambda : t.forward(l)},
    {"+" : lambda : t.left(90), "-" : lambda : t.right(90)},
    "F",
    {"F" : "F+G", "G" : "F-G"}
)

binaryStack = []
ba = 30;
def fractalPush():
    push(binaryStack)
    t.left(ba);

def fractalPop():
    pop(binaryStack);
    t.right(ba)

fractal = RuleSystem(
    {"0" : lambda : t.forward(l), "1" : lambda : t.forward(l)},
    {"[" : fractalPush, "]" : fractalPop},
    "0",
    {"1" : "11", "0" : "1[0]0"}
)

def xfunction():
    t.right(random.randint(0,15))
    # t.forward(l*2)

plantStack = []

plant = RuleSystem(
    {"F" : lambda : t.forward(l), "X" : xfunction},
    {"+" : lambda : t.left(25), "-" : lambda : t.right(25) ,"[" : lambda : push(plantStack), "]" : lambda : pop(plantStack)},
    "X",
    {"X" : "F+[[X]-X]-F[-FX]+X", "F" : "FF"},
)

spiral = RuleSystem(
    {"F" : lambda : t.forward(l)},
    {"+" : lambda : t.left(72), "-" : lambda : t.right(72)},
    "F-F-F-F-F",
    {"F" : "F-F-F++F+F-F"}
)
# l=25
a = 90
hilbert = RuleSystem(
    {"A" : lambda : None, "B" : lambda : None, "X" : lambda : t.forward(l)},
    {"-" : lambda : t.left(a), "+" : lambda : t.right(a)},
    "A",
    {"A" : "-BX+AXA+XB-", "B" : "+AX-BXB-XA+"}
)

# RUNNER CODE
t.hideturtle()
# teleport(t,[0,-400])
t.setheading(90)
# t.speed(1)
l=10
showSystem(hilbert,6)
turtle.mainloop()
