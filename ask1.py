#Atur cara pengiraan untungan bazar Ramadan

print("***ATUR CARA PENGIRAAN KEUNTUNGAN HARIAN BAZAR RAMADAN***")

#Hasil jualan
h_harian=float(input("Sila masuk hasil jualan harian:RM "))

#Kos untuk membeli barangan bagi gerai bazar
kos_barangan=float(input("Sila mausk kos barangan:RM "))

#kira untungan bersih
u_bersih=float(h_harian-kos_barangan)
print("Untungan ialah RM",u_bersih)

#kira peratusan untungan bersih
peratus=((u_bersih/kos_barangan)*100)
peratus=round(peratus,2) #Bundarkan kepada 2 digit

if peratus > 0:
    print("Keuntungan ialah:", peratus,"%")
elif peratus == 0:
    print ("Tiada keuntungan")
else:
    print("Kerugian ialah:", abs(peratus), "%")
