from sdtoolbox.postshock import CJspeed
from sdtoolbox.postshock import PostShock_eq
import cantera as ct
import matplotlib.pyplot as plt

mech = 'gri30.yaml'
gas = ct.Solution(mech)

# for one initial pressure and various initial temperatures

P1 = 100000    # 1 bar

for phi in range(50, 170, 20):
    T11 = []
    X1 = "O2:5, N2:18.8, C3H8:" + str(phi/100)
    cjs1 = []
    for T in range(250, 2500, 250):
        gas.TPX = T, P1, X1
        T11.append(T)
        U1 = CJspeed(P1, T, X1, mech)
        cjs1.append(U1)
    plt.plot(T11, cjs1, label="phi=%.2f" % (phi/100))

plt.legend()
plt.xlabel("Initial temperature [K]")
plt.ylabel("CJ speed [m/s]")
plt.title("CJ detonation speed of propane-air mixture", fontweight="bold")
plt.grid()
plt.savefig("propane_cjspeed(T11).png", dpi=1000)
plt.show()

for phi in range(50, 170, 20):
    T11 = []
    X1 = 'O2:5, N2:18.8, C3H8:' + str(phi/100)
    PostShock_T1 = []
    for T in range(250, 2500, 250):
        gas.TPX = T, P1, X1
        T11.append(T)
        U1 = CJspeed(P1, T, X1, mech)
        gas1 = PostShock_eq(U1, P1, T, X1, mech)
        PostShock_T1.append(gas1.T)
    plt.plot(T11, PostShock_T1, label="phi=%.2f" % (phi/100))

plt.legend()
plt.xlabel("Initial temperature [K]")
plt.ylabel("Post shock temperature [K]")
plt.title("Post shock temperature of propane-air mixture", fontweight="bold")
plt.grid()
plt.savefig("propane_T(T11).png", dpi=1000)
plt.show()

for phi in range(50, 170, 20):
    T11 = []
    X1 = "O2:5, N2:18.8, C3H8:" + str(phi/100)
    PostShock_P1 = []
    for T in range(250, 2500, 250):
        gas.TPX = T, P1, X1
        T11.append(T)
        U1 = CJspeed(P1, T, X1, mech)
        gas1 = PostShock_eq(U1, P1, T, X1, mech)
        PostShock_P1.append(gas1.P/100000)
    plt.plot(T11, PostShock_P1, label="phi=%.2f" % (phi/100))

plt.legend()
plt.xlabel("Initial temperature [K]")
plt.ylabel("Post shock pressure [bar]")
plt.title("Post shock pressure of propane-air mixture", fontweight="bold")
plt.grid()
plt.savefig("propane_P(T11).png", dpi=1000)
plt.show()

# for one initial temperature and various initial pressures

T1 = 298    # 25 dg celsius

for phi in range(50, 170, 20):
    P11 = []
    X2 = "O2:5, N2:18.8, C3H8:" + str(phi/100)
    cjs2 = []
    for P in range(100000, 1500000, 250000):
        gas.TPX = T1, P, X2
        P11.append(P)
        U2 = CJspeed(P, T1, X2, mech)
        cjs2.append(U2)
    plt.plot(P11, cjs2, label="phi=%.2f" % (phi/100))

plt.legend()
plt.xlabel("Initial pressure [K]")
plt.ylabel("CJ speed [m/s]")
plt.title("CJ detonation speed of propane-air mixture", fontweight="bold")
plt.grid()
plt.savefig("propane_cjspeed(P11).png", dpi=1000)
plt.show()

for phi in range(50, 170, 20):
    P11 = []
    X2 = 'O2:5, N2:18.8, C3H8:' + str(phi/100)
    PostShock_T2 = []
    for P in range(100000, 1500000, 250000):
        gas.TPX = T1, P, X2
        P11.append(P)
        U2 = CJspeed(P, T1, X2, mech)
        gas2 = PostShock_eq(U2, P, T1, X2, mech)
        PostShock_T2.append(gas2.T)
    plt.plot(P11, PostShock_T2, label="phi=%.2f" % (phi/100))

plt.legend()
plt.xlabel("Initial pressure [bar]")
plt.ylabel("Post shock temperature [K]")
plt.title("Post shock temperature of propane-air mixture", fontweight="bold")
plt.grid()
plt.savefig("propane_T(P11).png", dpi=1000)
plt.show()

for phi in range(50, 170, 20):
    P11 = []
    X2 = "O2:5, N2:18.8, C3H8:" + str(phi/100)
    PostShock_P2 = []
    for P in range(100000, 1500000, 250000):
        gas.TPX = T1, P, X2
        P11.append(P)
        U2 = CJspeed(P, T1, X2, mech)
        gas2 = PostShock_eq(U2, P, T1, X2, mech)
        PostShock_P2.append(gas2.P/100000)
    plt.plot(P11, PostShock_P2, label="phi=%.2f" % (phi/100))

plt.legend()
plt.xlabel("Initial pressure [bar]")
plt.ylabel("Post shock pressure [bar]")
plt.title("Post shock pressure of propane-air mixture", fontweight="bold")
plt.grid()
plt.savefig("propane_P(P11).png", dpi=1000)
plt.show()
