from ruleDeclaration import RuleSystem
from tkinter import *
import turtle

class ShortEntry(Frame):
    def __init__(self,name,root,**kwargs):
        super().__init__(root,**kwargs)

        self['height']=25
        self['width']=300

        self.labelCon = Frame(self,width=100,height=self['height'],bg=self['bg'])
        self.labelCon.pack(side=LEFT,fill=BOTH)
        self.labelCon.pack_propagate(0)
        self.l = Label(self.labelCon,text="%s:"%name.title(),font=("Arial",12),bg=self['bg'],justify='left',anchor='w')
        self.l.pack(fill=BOTH)
        self.e = Entry(self,font=("Arial",12),bg=self['bg'], borderwidth = 1, relief = SUNKEN);
        self.e.pack(fill=BOTH,side=BOTTOM)

    def create(self):
        self.pack(pady=5)
        self.pack_propagate(0)

    def getValue(self):
        return self.e.get()

class App(Tk):
    def __init__(self,size,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.geometry("%sx%s+0+0"%(size[0],size[1]))
        self.Csize = min(size)
        self.size = size

        self.home = [0,0]
        self.stack = []

        self.angle = 0
        self.length = 0

        self.presets = {
            "A" : lambda : None,
            "B" : lambda : None,
            "X" : lambda : None,
            "Y" : lambda : None,
            "F" : lambda : self.turtle.forward(self.length),
            "f" : self.move,
            "G" : lambda : self.turtle.forward(self.length),
            "+" : lambda : self.turtle.left(self.angle),
            "-" : lambda : self.turtle.right(self.angle),
            "[" : self.push,
            "]" : self.pop,
            "|" : lambda : self.turtle.right(180)
        }
        self.system = RuleSystem(self.presets,{},"",{})

        self.createFrame()

        self.turtle = turtle.RawTurtle(self.turtleCnv)
        self.clear()

    def move(self):
        self.turtle.up()
        self.turtle.forward(int(self.lengthE.getValue()))
        self.turtle.down()

    def createFrame(self):
        self.control = Frame(self,width=self.size[0]-self.Csize,height=self.size[1])
        self.control.pack(side=LEFT)
        self.control.pack_propagate(0)
        Label(self.control,text="Lindenmayer System Generator",font=("Arial",18)).pack(side=TOP)
        self.form = Frame(self.control,width=0.8*self.control['width'],height=0.5*self.control['height'],bg='#fdfdfd')
        self.form.pack(pady=25)
        self.form.pack_propagate(0)
        Label(self.form,text="Edit Properties",font=("Arial",14),bg=self.form['bg']).pack(side=TOP,anchor='w',padx=10,pady=10)
        self.angleE = ShortEntry("Angle",self.form,bg=self.form['bg'],width=200)
        self.angleE.create()
        self.lengthE = ShortEntry("Length",self.form,bg=self.form['bg'],width=200)
        self.lengthE.create()
        self.iterationE = ShortEntry("Iterations",self.form,bg=self.form['bg'],width=200)
        self.iterationE.create()
        self.axiomE = ShortEntry("Axiom",self.form,bg=self.form['bg'],width=200)
        self.axiomE.create()
        Label(self.form,text="Rules",font=("Arial",12),bg=self.form['bg']).pack(side=TOP)
        self.rulesE = Text(self.form,width=int((0.8*self.form['width'])*0.125),height=10,relief=SOLID)
        self.rulesE.pack(padx=10,pady=10)
        self.submit = Button(self.form,text='Generate!',command=self.submit)
        self.submit.pack(side=BOTTOM,fill=BOTH,padx=15,pady=15)

        self.tForm = Frame(self.control,width=0.8*self.control['width'],height=0.5*self.control['height'],bg='#fdfdfd')
        self.tForm.pack(pady=25,fill=Y)
        self.tForm.pack_propagate(0)
        Label(self.tForm,text="Edit Drawer",font=("Arial",14),bg=self.tForm['bg']).pack(side=TOP,anchor='w',padx=10,pady=10)

        self.homeL = Label(self.tForm,text="Start Location:",font=("Arial",12),bg=self.tForm['bg'])
        self.homeL.pack(side=TOP,pady=10,padx=50,anchor='w')

        self.resetBtn = Button(self.tForm,text='Reset Drawer',command=self.clear)
        self.resetBtn.pack(side=BOTTOM,fill=BOTH,padx=15,pady=15)

        self.turtleCnv = Canvas(self,width=self.Csize,height=self.Csize,bd=0,highlightthickness=0)
        self.turtleCnv.pack(side=RIGHT)

    def submit(self):
        self.clear()
        self.length = int(self.lengthE.getValue())
        self.angle =  float(self.angleE.getValue())
        self.system.rules = self.formatRules(self.rulesE.get(0.0,END))
        self.system.axiom = self.axiomE.getValue().strip()
        plan = self.system.generate(int(self.iterationE.getValue()))
        self.system.execute(plan)

    def clear(self):
        self.turtle.reset()
        self.turtle.speed(1000000000)
        self.teleport(self.home)
        # self.turtle.setheading(90)
        self.turtle.hideturtle()
        self.turtleCnv.bind("<Button-1>",self.setHome)

    def formatRules(self,txt):
        ruleSet = {}
        for rule in txt.split('\n'):
            if rule.strip() == "":
                continue
            content = rule.split("=")
            ruleSet[content[0].strip()] = content[1].strip()
        return ruleSet;

    def teleport(self,pos):
        self.turtle.up()
        self.turtle.goto(pos[0],pos[1])
        self.turtle.down()

    def push(self):
        self.stack.append([self.turtle.pos(),self.turtle.heading()])

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        self.teleport(data[0])
        self.turtle.setheading(data[1])

    def setHome(self,e):
        self.home = [(e.x-self.Csize//2),(e.y-self.Csize//2)*-1]
        self.homeL.config(text="Start Location: %s"%self.home)

app = App((1600,1000))
# app =  App((1000,800))

app.title("Lindenmayer System Generator")
app.resizable(0,0)
app.wm_attributes("-topmost",1)
# app.wm_attributes("-fullscreen",1)


app.mainloop()
