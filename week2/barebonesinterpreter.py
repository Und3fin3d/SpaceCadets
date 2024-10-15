mem = {}
def clear(var):
    mem[var] = 0
def incr(var):
    mem[var]+=1
def decr(var):
    mem[var]-=1
keyword = {'clear': clear,'incr':incr,'decr':decr}
def wale(var,val,il):
    while mem[var] != int(val):
        execute(il[:])
def execute(il):
    for i,x in enumerate(il):
        if x[0] not in ['while','end']:
            keyword[x[0]](x[1])
        elif len(x)>1:
            wale(x[1],x[3],x[-1])
def parse(instructionlist):
    whil = [i for i, x in enumerate(instructionlist) if x[0] == 'while']
    end = [i for i, x in enumerate(instructionlist) if x == ['end']]
    il = [x for x in instructionlist]
    for y in end:
        z =  max([x for x in whil if x < y])
        whil.remove(z)
        slic = il[z+1:y]
        il[z].append([x for x in slic if x not in [None, ['end']]])
        il[z+1:y] = [None] * len(slic)
    return [x for x in il if x not in [None, ['end']]]
            
        
with open('barebones.txt') as f:
    instructionlist = [x.split() for x in f.read().replace(';','').splitlines()]
    execute(parse(instructionlist))
    print(mem)