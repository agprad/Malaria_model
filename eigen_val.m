#Parameter
alpha=3.64
gamma_A_mal=0.042
gamma_C_mal=0.047
gamma_T_mal=0.0047
gamma_natural=0.346
gamma_scd=0.5
ma=0.1
mt=0.2
#Fixed point
u=0
v=0.25338977070702223
w=0
x=0
y=0.1247500323491873
z=0
d=0
e=0
f=0.48403012551484664
n=1-(x+y+z+d+e+f+u+v+w)

J11=-mt
J12=0
J13=0
J14=mt+ma
J15=0
J16=0
J17=-ma
J18=0
J19=0
J21=0
J22=-mt-gamma_scd
J23=0
J24=ma
J25=mt
J26=0
J27=-ma
J28=0
J29=0
J31=0
J32 = 0
J33 = -mt-gamma_C_mal
J34 = ma
J35 = mt
J36 = 0
J37 = -ma
J38 = 0
J39 = 0
J41 = -(alpha/((x+y+z)*(x+y+z))) * (0.5*y*z+0.5*z*z)
J42 = -(alpha/((x+y+z)*(x+y+z))) * 0.25*z*z
J43 = -(alpha/((x+y+z)*(x+y+z)))*(y*y+0.5*y*z+0.25*z*z)
J44 = -ma
J45 = 0
J46 = 0
J47 = ma
J48 = 0
J49 = 0
J51 = 0
J52 = 0
J53 = 0
J54 = ma
J55 = -ma-gamma_scd
J56 = 0
J57 = -ma
J58 = ma
J59 = 0
J61 = 0
J62 = 0
J63 = 0
J64 = ma
J65 = 0
J66 = -ma-gamma_T_mal
J67 = -ma
J68 = 0
J69 = ma
J71 = (alpha*n/((x+y+z)*(x+y+z))) * (0.5*y+z) - (0.5*y*z + 0.5*z*z)
J72 = (alpha*n/((x+y+z)*(x+y+z)))*(0.5*z*(x+y+z)-0.25*z*z)
J73 =(alpha*n/((x+y+z)*(x+y+z)))*(0.5*(y+z)*(x+y+z)-(y*y+0.5*y*z+0.25*z*z))
J74 =ma
J75 = 0
J76 =0
J77 =-ma-gamma_T_mal
J78 =0
J79 =0
J81 =-(alpha*n/((x+y+z)*(x+y+z)))*(0.5*y*z+0.5*z*z)
J82 =(alpha*n/((x+y+z)*(x+y+z)))*(-0.25*z*z)
J83 =(alpha*n/((x+y+z)*(x+y+z)))*(y*y+0.5*y*z+0.25*z*z)
J84 =ma
J85 =0
J86 =0
J87 =-ma
J88 =-gamma_scd
J89 =0
J91 =(alpha*n/((x+y+z)*(x+y+z)))*((x+y+z)*0.5*z-(0.5*y*z+0.5*z*z))
J92 =(alpha*n/((x+y+z)*(x+y+z)))*(-0.25*z*z)
J93 =(alpha*n/((x+y+z)*(x+y+z)))*((x+y+z)*(2*y+0.5*z)-(y*y+0.5*y*z+0.25*z*z))
J94 =ma
J95 =0
J96 =0
J97 =-ma
J98 =0
J99 =-gamma_A_mal-gamma_natural
J = [J11 J12 J13 J14 J15 J16 J17 J18 J19;
J21 J22 J23 J24 J25 J26 J27 J28 J29;
J31 J32 J33 J34 J35 J36 J37 J38 J39;
J41 J42 J43 J44 J45 J46 J47 J48 J49;
J51 J52 J53 J54 J55 J56 J57 J58 J59;
J61 J62 J63 J64 J65 J66 J67 J68 J69;
J71 J72 J73 J74 J75 J76 J77 J78 J79;
J81 J82 J83 J84 J85 J86 J87 J88 J89;
J91 J92 J93 J94 J95 J96 J97 J98 J99]
lamda = eig(J)