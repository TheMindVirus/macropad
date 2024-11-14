# VaryingBitness - TheMindVirus
# A collection of various oddities encountered when building with rotors and differentials
# When there is only one state per unit it is unary, when there are two it is binary, three is ternary

print("\n# Number with Varying Bitness #\n")

#1->1, 2->2, 3->6, 4->24, 5->120, 6->720, 7->5040, 8->40320
#1x1=1, 1x2=2, 2x3=6, 6x4=24,
#24x5=120, 120x6=360x2=720, 720x7=4900+140=5040, 5040x8=40320

b = 4 #8
x = [0] * b
n = 1 #200 # ((b + 1) * (b + 1)) - 1
for i in range(1, b + 1):
    n *= i
for i in range(0, n):
    print(i + 1, "\t", "".join([str(x[k]) for k in range(b-1,-1,-1)]))
    for j in range(0, b):
        x[j] += 1
        if x[j] > j:
            x[j] = 0
        else:
            break

print("\n# Sequential Bitstream Clutching #\n")

K = 16
I = 2
R = 10
B = 8
Y = [0] * B

for i in range(0, K):
    Y[-1] += 1
    for j in range(0, B):
        if Y[(j%2) % B] > 0:
            Y[(j+1) % B] += I
    for j in range(0, B):
        Y[j] %= R
    print(Y)
    Y[(-i-1) % B] = Y[-i % B]
    Y[-i % B] = 0

print("\n# Communication Bridge Differential #\n")

def make_matrix(n = 4, b = 4):
    ret = []
    for i in range(0, n):
        tmp = [[0] * b]
        ret += tmp[:]
    return ret

LHS = make_matrix(4, 4)[:]
MHS = make_matrix(1, 2)[0]
RHS = make_matrix(4, 4)[:]

N = 4
S = 4
step = 64 #10
states = [0]
for h in range(0, step):
    
    for i in range(0, S-1):
        if LHS[S-i-1][-1] == 1:
            LHS[S-i-1][-1] = 0
    
    for i in range(0, S-1):
        if RHS[S-i-1][-1] == 1:
            RHS[S-i-1][-1] = 0
        
    for j in range(0, S):
        
        for i in range(1, N-1):
            LHS[j][i] += LHS[j][i-1]
            if LHS[j][i] > 1:
                LHS[j][i] = 0
                LHS[j][i+1] += 1
                if LHS[j][-1] > 1:
                    LHS[j][-1] = 0
            else:
                break
        
        for i in range(1, N-1):
            RHS[j][i] += RHS[j][i-1]
            if RHS[j][i] > 1:
                RHS[j][i] = 0
                RHS[j][i+1] += 1
                if RHS[j][-1] > 1:
                    RHS[j][-1] = 0
            else:
                break
    
    for i in range(1, S):
        RHS[S-i][0] = RHS[S-i-1][0]
    RHS[0][0] = MHS[0]
    MHS[0] = LHS[-1][0]   
    for i in range(1, S):
        LHS[S-i][0] = LHS[S-i-1][0]
    LHS[0][0] = 1 - LHS[0][0]
    
    MHS[1] = 0
    for i in range(0, N):
        MHS[1] += (LHS[i][N-1] << i)
        MHS[1] -= (RHS[i][N-1] << i)
    MHS[1] = 1 if MHS[1] != 0 else 0

    states.append(MHS[1])

print("\n".join([str(i) for i in LHS]),
      " " + (" " * 8).join([str(i) for i in MHS]),
      "\n".join([str(i) for i in RHS]), sep = "\n")

print("\n" + str(states))