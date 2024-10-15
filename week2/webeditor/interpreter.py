class Interpreter:
    def __init__(self,txt):
        self.mem = {}
        self.keyword = {'clear': self.clear,'incr':self.incr,'decr':self.decr}
        self.execute(self.parse(txt))
    def clear(self,var):
        self.mem[var] = 0
    def incr(self,var):
        self.mem[var]+=1
    def decr(self,var):
        self.mem[var]-=1

    def wale(self,var,val,il):
        while self.mem[var] != int(val):
            self.execute(il[:])
    def execute(self,il):
        for i,x in enumerate(il):
            if x[0] not in ['while','end']:
                self.keyword[x[0]](x[1])
            elif len(x)>1:
                self.wale(x[1],x[3],x[-1])
    def parse(self,instructionlist):
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
            
if __name__ == "__main__":
    with open('barebones.txt') as f:
        i = Interpreter([x.split() for x in f.read().replace(';','').splitlines()])
        print(i.mem)
       