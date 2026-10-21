b_sts = ["1. Invictus Amarillo", "2. Guerreross, 3. Invictus Negro","4.Cocodrilos","5.ESBAR"]
b_3pt=["1.Santiago Tenjo(12)","2.Julián Sanchez(11)","3.Jeronimo Lozano(8)","4.Adrián Subaltrán(7)"]
b_mvp=["1.Adrián Subaltrán(INVB)","2.Julián Sanchez(GUE)","3.Santiago Tenjo(INVN)"]
v_sts=["1.Supernova","2.Mustangs","3.Vissel","4.BVS Sports","5.Kuppa"]
v_klss=["1.Juan Rodriguez(9)","2.Esteban Hernandez(8)","3.Felipe Fajardo(2)","4.Emilio Bonilla(1)"]
v_mvp=["1.Esteban Hernandez(MUS)","2.Santiago Estupiñan(SUP)","3.Sebastián Bahamon(MUS)",]
s_sts=["1.Caterpillar","2.Fortaleza FC","3.Santafe FC","4.Equidad FC","5.Juventus Bogotá"]
s_gls=["1.Andres Angulo(11)","2.Alejandro Heredia(11)","3.Mateo Martinez(10)","4.Nicolas Jimenez(8)"]
s_poty=["1.Mateo Martinez(CAT)","2.Camilo Rodriguez(EQU)","3.Alejandro Heredia(CAT)",]

while True:
    print("Welcome to Bogotá's male sub-16 basketball, soccer, and voleyball league")
    print("Select the league you want to see by typing its corresponding letter:")
    print("Basketball = b")
    print("Voleyball = v")
    print("Soccer = s")
    print("Exit = e")

    a=input("SELECT THE LEAGUE:")
    if  a=="b":
        print("Team standing = 1")
        print("Best 3-point shooters= 2")
        print("MVP ladder = 3")
        b2=int(input("Select the standings"))
        if b2==1:
            print(b_sts)
            print("Y=YES")
            print("N=NO")
            c=input("Do you want to back to the menu?") 
            if c=="Y":
                 print("Going back to the menu...")
                 continue
            elif c=="N":
                 print("Closing chat..")
                 break
        elif b2==2:
            print("Best 3-point shooters:", b_3pt)
            print("Y=YES")
            print("N=NO")
            c=input("Do you want to back to the menu?") 
            if c=="Y":
                 print("Going back to the menu...")
                 continue
            elif c=="N":
                 print("Closing chat..")
                 break
            
        elif b2==3:
            print("MVP ladder:", b_mvp)
            print("Y=YES")
            print("N=NO")
            c=input("Do you want to back to the menu?") 
            if c=="Y":
                 print("Going back to the menu...")
                 continue
            elif c=="N":
                 print("Closing chat..")
                 break
    elif  a=="s":
            print("Team standing = 1")
            print("Golden boot contenders= 2")
            print("POTY contenders = 3")
            s2=int(input("Select the standings"))
            if s2==1:
                print(s_sts)
                print("Y=YES")
                print("N=NO")
            c=input("Do you want to back to the menu?") 
            if c=="Y":
                 print("Going back to the menu...")
                 continue
            elif c=="N":
                 print("Closing chat..")
                 break
            elif s2==2:
                print("Golden boot contenders:", s_gls)
            print("Y=YES")
            print("N=NO")
            c=input("Do you want to back to the menu?")
            if c=="Y":
                 print("Going back to the menu...")
                 continue
            elif c=="N":
                 print("Closing chat..")
                 break

            elif s2==3:
                print("POTY contenders:", s_poty)
    elif  a=="v":
            v2=int(input("Select the standings"))
            print("Team standing = 1")
            print("Mos Kills = 2")
            print("MVP rankings = 3")
            if v2==1:
                print(v_sts)
            print("Y=YES")
            print("N=NO")
            c=input("Do you want to back to the menu?") 
            if c=="Y":
                 print("Going back to the menu...")
                 continue
            elif c=="N":
                 print("Closing chat..")
                 break
            elif v2==2:
                print("Most kills:", v_klss)
            print("Y=YES")
            print("N=NO")
            c=input("Do you want to back to the menu?") 
            if c=="Y":
                 print("Going back to the menu...")
                 continue
            elif c=="N":
                 print("Closing chat..")
                 break
            elif v2==3:
                print("MVP rankings:", v_mvp)
    elif  a=="e":
        print("Closing chat...")
        break