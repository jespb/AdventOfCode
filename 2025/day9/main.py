
filenames = ["input1.txt", "input2.txt"]


# part 1
if False:
    for filename in filenames[2:]:

        m = [ [int(x) for x in line.strip().split(",")] for line in open(filename)]

        pwd = []
        for p1 in m:
            pwd.append( [ (abs(p1[0]-p2[0])+1) * (abs(p1[1]-p2[1])+1)  for p2 in m] )

        ma = 0
        for line in pwd:
            ma =max(ma, max(line))

        print(ma)



# part 2
if False:
    def allowed(points, x,y):
        valid = [0,0,0,0]
        for py, px in points:
            if py>=y and px>=x:
                valid[0] = 1
            if py>=y and px<=x:
                valid[1] = 1
            if py<=y and px>=x:
                valid[2] = 1
            if py<=y and px<=x:
                valid[3] = 1
            if sum(valid) == 4:
                return True
        return False

    for filename in filenames[1:]:

        m = [ [int(x) for x in line.strip().split(",")] for line in open(filename)]

        #tmp = [[0]*13 for _ in range(13)]
        #for y in range(13):
        #    for x in range(13):
        #        tmp[y][x] = "#" if allowed(m, y, x) else " "
        #for line in tmp:
        #    print(line)


        pwd = []
        for p1 in range(len(m)):
            print(p1/len(m))
            p1 = m[p1]
            tmp = [] 
            for p2 in m:
                valid = True
                yii, yia = min(p1[1], p2[1]), max(p1[1], p2[1])
                xii, xia = min(p1[0], p2[0]), max(p1[0], p2[0])
                yi = yii
                while valid and yi < yia:
                    valid &= allowed(m, yi, xii)
                    valid &= allowed(m, yi, xia)
                    yi +=1
                xi = xii
                while valid and xi < xia:
                    valid &= allowed(m, yii, xi)
                    valid &= allowed(m, yia, xi)
                    xi +=1
                if valid:
                    tmp.append( (abs(p1[0]-p2[0])+1) * (abs(p1[1]-p2[1])+1))
                else:
                    tmp.append(0)
            pwd.append(tmp)

        ma = 0
        for line in pwd:
            ma =max(ma, max(line))

        print(ma)




# part 2 teste
def getInfo(p1,p2):
    x1,y1 =p1
    x2,y2 =p2
    if y1==y2:
        dir = "D" if x2>x1 else "U"
        z = y1 
        mi = min(x1, x2)
        ma = max(x1, x2)
    else:
        dir = "L" if y2>y1 else "R"
        z = x1 
        mi = min(y1, y2)
        ma = max(y1, y2)
    return dir, z, mi, ma

def passed(limits, x, y):
    ceiling = -1
    for z, mi, ma in limits["D"]: 
        if z <= y and x >= mi and x <= ma:
            ceiling = max(ceiling, z)
    if ceiling == -1:

        return False
    for z, mi, ma in limits["U"]: 
        if x >= mi and x <= ma:
            if z>ceiling and z<y:
                return False
    
    ceiling = -1
    for z, mi, ma in limits["R"]: 
        if z <= x and y >= mi and y <= ma:
            ceiling = max(ceiling, z)
    if ceiling == -1:
        return False
    for z, mi, ma in limits["L"]: 
        if y >= mi and y <= ma:
            if z>ceiling and z<x:
                return False
    return True


def evaluate(p1, p2, limits):
    U = limits["U"]
    D = limits["D"]
    L = limits["L"]
    R = limits["R"]
    xi, xf = min(p1[0], p2[0]), max(p1[0], p2[0])
    yi, yf = min(p1[1], p2[1]), max(p1[1], p2[1]) 
    x_interest = sorted([v[0] for v in L]+[v[0] for v in R])
    x_interest = [x for x in x_interest if x >= xi and x <= xf]
    y_interest = sorted([v[0] for v in U]+[v[0] for v in D])
    y_interest = [y for y in y_interest if y >= yi and y <= yf]
    
    if len(x_interest) == 0 or len(y_interest)==0:
        return False
    
    for x_ in x_interest:
        for y_ in y_interest:
            if x_-1 >= xi and y_-1 >= yi and not passed(limits, x_-1, y_-1):
                #print("Failed:", x_-1, y_)
                return False
            if x_-1 >= xi and y_+1 <= yf and not passed(limits, x_-1, y_+1):
                #print("Failed:", x_-1, y_)
                return False
            if x_+1 <= xf and y_-1 >= yi and not passed(limits, x_+1, y_-1):
                #print("Failed:", x_-1, y_)
                return False
            if x_+1 <= xf and y_+1 <= yf and not passed(limits, x_+1, y_+1):
                #print("Failed:", x_-1, y_)
                return False

    return True



for filename in filenames[1:]:

    m = [ [int(x) for x in line.strip().split(",")] for line in open(filename)]

    limits = {"U":[],"D":[],"L":[],"R":[]}

    p1 = m[-1]
    p2 = m[0]
    dir, z, mi, ma = getInfo(p1, p2)
    limits[dir].append( (z, mi, ma) )
    for i in range(len(m)-1):
        dir, z, mi, ma = getInfo(m[i], m[i+1])
        limits[dir].append( (z, mi, ma) )
    
    for key in "UDLR":
        limits[key].sort(reverse= key in "UL")

    print(limits)

    evaluate([9,5],[2,3],limits)

    #assert(False)
    dist = 0
    for p1 in range(len(m)):
        print(p1/len(m))
        p1 = m[p1]
        for p2 in m:
            d = (abs(p1[0]-p2[0])+1) * (abs(p1[1]-p2[1])+1)
            if d < 2116295688 and d > 1506688 and evaluate(p1,p2,limits):
                #print(p1,p2)
                if d > dist:
                    dist = d 
                    print(dist)
    
    




# 1506688 too low

# 4638696212 too high
# 2116295688 too high