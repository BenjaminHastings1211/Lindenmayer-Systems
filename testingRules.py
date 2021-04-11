from ruleDeclaration import RuleSystem;

cantor = RuleSystem(
    {"A" : lambda : print("draw forward"), "B" : lambda : print("move forward")},
    {},
    "A",
    {"A" : "ABA", "B" : "BBB"}
)

koch = RuleSystem(
    { "F" : lambda : print("draw forward")},
    { "+" : lambda : print("turn left 90"), "-" : lambda : print("turn right 90")},
    "F",
    { "F" : "F+F-F-F+F"}
)

# save = cantor.generate(9);
# # cantor.execute(save)
# print(len(save))

save = koch.generate(7);
print(len(save))
