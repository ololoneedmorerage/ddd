a = open("ppoppa.txt")  
f= open("output.txt", "w")
c = list()   
cccp = ("+" + "=" * 24) * 3 + "+"  
print(cccp, file = f)
usa = "|            Число       |            Квадрат     |           Kуб          |"
print(usa, file = f)
for c in a: 
    while c:
        c = float(c)     
        d= c*c
        e= c *c *c
        v = "+" + "-" * 24 
        g= "+"
        h = v * 3 + g
        print(h, file = f)
        print("|%20.05f    | %20.05f   | %20.05f   | "%(c, d, e), file = f )
        break
a.close()
f.close()
