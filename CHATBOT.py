b_sts = ["1. Invictus Amarillo", "2. Guerreros", "3. Invictus Negro","4. Cocodrilos","5. ESBAR"]
b_3pt=["1. Santiago Tenjo(12)","2. Julián Sanchez(11)","3. Jeronimo Lozano(8)","4. Adrián Subaltrán(7)"]
b_mvp=["1. Adrián Subaltrán(INVB)","2. Julián Sanchez(GUE)","3. Santiago Tenjo(INVN)"]
v_sts=["1. Supernova","2. Mustangs","3. Vissel","4. BVS Sports","5. Kuppa"]
v_klss=["1. Juan Rodriguez(9)","2. Esteban Hernandez(8)","3. Felipe Fajardo(2)","4. Emilio Bonilla(1)"]
v_mvp=["1. Esteban Hernandez(MUS)","2. Santiago Estupiñan(SUP)","3. Sebastián Bahamon(MUS)",]
s_sts=["1. Caterpillar","2. Fortaleza FC","3. Santafe FC","4. Equidad FC","5. Juventus Bogotá"]
s_gls=["1. Andres Angulo(11)","2. Alejandro Heredia(11)","3. Mateo Martinez(10)","4. Nicolas Jimenez(8)"]
s_poty=["1. Mateo Martinez(CAT)","2. Camilo Rodriguez(EQU)","3. Alejandro Heredia(CAT)"]

while True:
    print("Welcome to Bogotá's male sub-16 basketball, soccer, and voleyball league")
    print("Select the league you want to see by typing its corresponding letter:")
    print("Basketball = B")
    print("Voleyball = V")
    print("Soccer = S")
    print("Exit = E")

    a=input("SELECT THE LEAGUE:")
    if  a=="B":
        print("Team standing = 1")
        print("Best 3-point shooters= 2")
        print("MVP ladder = 3")
        b2=int(input("Select the option to what to know about: "))
        if b2==1:
            for stats in b_sts:
                print(stats)
            c=input("Do you want to back to the menu? Write Y=YES or N=NO")
            if c=="Y":
                 print("Going back to the menu...")
                 continue
            elif c=="N":
                 print("Closing chat..")
                 break
        elif b2==2:
            print("Best 3-point shooters:")
            for shooter in b_3pt:
                print(shooter)
            c=input("Do you want to back to the menu? Write Y=YES or N=NO") 
            if c=="Y":
                 print("Going back to the menu...")
                 continue
            elif c=="N":
                 print("Closing chat..")
                 break
        elif b2==3:
            print("MVP ladder:")
            for mvp in b_mvp:
                print(mvp)
            c=input("Do you want to back to the menu? Write Y=YES or N=NO") 
            if c=="Y":
                 print("Going back to the menu...")
                 continue
            elif c=="N":
                 print("Closing chat..")
                 break
    elif a=="S":
          print("Team standing = 1")
          print("Golden boot contenders= 2")
          print("POTY contenders = 3")
          s2=int(input("Select the option to what to know about:"))
          if s2==1:
               print("Team standings:")
               for stat in s_sts:
                    print(stat)
               c=input("Do you want to back to the menu? Write Y=YES or N=NO") 
               if c=="Y":
                    print("Going back to the menu...")
                    continue
               elif c=="N":
                    print("Closing chat..")
                    break
          elif s2==2:
               print("Golden boot contenders:")
               for contender in s_gls:
                    print(contender)
               c=input("Do you want to back to the menu? Write Y=YES or N=NO")
               if c=="Y":
                    print("Going back to the menu...")
                    continue
               elif c=="N":
                    print("Closing chat..")
                    break
          elif s2==3:
               print("POTY contenders:")
               for contender in s_poty:
                    print(contender)
               c=input("Do you want to back to the menu? Write Y=YES or N=NO")
               if c=="Y":
                    print("Going back to the menu...")
                    continue
               elif c=="N":
                    print("Closing chat..")
                    break
    elif  a=="V":
          print("Team standing = 1")
          print("Most kills = 2")
          print("MVP rankings = 3")
          v2=int(input("Select the option to what to know about: "))
          if v2==1:
               print("Team standings:")
               for stat in v_sts:
                    print(stat)
               c=input("Do you want to back to the menu? Write Y=YES or N=NO") 
               if c=="Y":
                    print("Going back to the menu...")
                    continue
               elif c=="N":
                    print("Closing chat..")
                    break
          elif v2==2:
               print("Most kills:")
               for kill in v_klss:
                    print(kill)
               c=input("Do you want to back to the menu? Write Y=YES or N=NO") 
               if c=="Y":
                    print("Going back to the menu...")
                    continue
               elif c=="N":
                    print("Closing chat..")
                    break
          elif v2==3:
               print("MVP rankings:")
               for mvp in v_mvp:
                    print(mvp)
               c=input("Do you want to back to the menu? Write Y=YES or N=NO") 
               if c=="Y":
                    print("Going back to the menu...")
                    continue
               elif c=="N":
                    print("Closing chat..")
                    break
    elif  a=="E":
        print("Exiting...")
        break
    else:
        print("Invalid option, please try again.")
        continue