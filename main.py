from unit_converter import kg_to_g, g_to_kg, c_to_f, f_to_c, km_to_m, m_to_km

def main():
    print("\n====Welcome to unit converter====\n")
    print("What do uou want to convert?")
    print("1. Weight")
    print("2. Length")
    print("3. Temperature")
    choice1 = input("Choose your option: ")

    if choice1 == "1":
        print("1. kg -> g")
        print("2. g -> kg")
        choice2 = input("Choose option: ")
        if choice2 == "1":
            kg = float(input("Enter weight: "))
            print(kg_to_g(kg))
        elif choice2 == "2":
            g = float(input("Enter weight: "))
            print (g_to_kg(g))
        else:
            print ("Invalid choice")
        
    elif choice1 == "2":
        print("1. km -> m")
        print("2. m -> km")
        choice2 = input("Choose option: ")
        if choice2 == "1":
            km = float(input("Enter length: "))
            print (km_to_m(km))
        elif choice2 == "2":
            m = float(input("Enter length: "))
            print (m_to_km(m))
        else:
            print ("Invalid choice")
        
    elif choice1 == "3":
        print("1. celcius -> farenheit")
        print("2. farenheit -> celcius")
        choice2 = input("Choose option: ")
        if choice2 == "1":
            c = float(input("Enter temp: "))
            print(c_to_f(c))
        elif choice2 == "2":
            f = float(input("Enter temp: "))
            print(f_to_c(f))
        else:
            print ("Invalid choice")

    else:
        print ("Invalid Option!...try again")
    
if __name__ == "__main__":
    main()
        
        
