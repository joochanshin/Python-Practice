# arr1 = ["A", "B", "C", "A", "B"]
#
# print(arr1)
#
#
# def first_recurring(arr):
#     counts = {}
#     for char in arr:
#         if char in counts:
#             return char
#         counts[char] = 1
#     return None
#
#
# print(first_recurring(arr1))
levels = {
        "Moon": {"G": -1.622, "Fuel": 150},
        "Earth": {"G": -9.81, "Fuel": 5000},
        "Pluto": {"G": -0.42, "Fuel": 1000},
        "Neptune": {"G": -14.07, "Fuel": 1000},
        "Uranus": {"G": -10.67, "Fuel": 1000},
        "Saturn": {"G": -11.08, "Fuel": 1000},
        "Jupiter": {"G": -25.95, "Fuel": 1000},
        "Mars": {"G": -3.77, "Fuel": 1000},
        "Venus": {"G": -8.87, "Fuel": 1000},
        "Mecury": {"G": -3.59, "Fuel": 1000},
        "Sun": {"G": -274.13, "Fuel": 50000}
    }
alt = 50
vel = 0.00
BUF = 0.10      # Burning Unit of Fuel
won = False


def ask_fuel(current_fuel):
    bool_ = True
    check = False
    while bool_:
        fuel = int(input("Enter units of fuel to use:"))
        if isinstance(fuel, int):
            if fuel >= 0:
                if fuel <= current_fuel:
                    check = True
        if check:
            # bool_ = False
            return fuel
        print("Enter a valid unit of fuel!")


def play_level(planet):
    p_fuel = levels[planet]["Fuel"]
    grav_ = levels[planet]["G"]
    print("Landing on the", planet, "\nGravity is ", grav_, "m/s^2\nInitial Altitude:", alt, "meters")
    print("Intial Velocity", vel, "m/s\nBurning a unit of fuel causes", BUF, "m/s slowdown.")
    print("Initial Fuel Level", p_fuel, "units\n\nGO")
    # print(planet, levels[planet]["G"], levels[planet]["Fuel"])
    count = 1
    vel2 = vel
    alt2 = alt
    c_fuel = 0
    run = True
    while run:
        vel2 = vel2 + grav_ + (c_fuel * BUF)
        alt2 = alt2 + vel2
        p_fuel = p_fuel - c_fuel
        # print("vel", vel2, "alt", alt2, "fuel", p_fuel)
        if alt2 < 0 and vel2 < -1:
            print("Crashed!")
            run = False
            return False
        elif alt2 == 0 or (vel2 > -1 and count > 1 and alt2 < 1):
            print("Landed Successfully.")
            run = False
            return True
        elif p_fuel <= 0:
            print("Ran out of fuel")
            run = False
            return False
        else:
            if count == 1:
                print("After", count, "second Altitude is", format(alt2, '.2f'), "meters, velocity is", format(vel2, '.2f') , "m/s.")
                print("Remaining Fuel:", p_fuel, "units.")
                c_fuel = ask_fuel(p_fuel)
            else:
                print("After", count, "seconds Altitude is", format(alt2, '.2f'), "meters, velocity is", format(vel2, '.2f'), "m/s.")
                print("Remaining Fuel:", p_fuel, "units.")
                c_fuel = ask_fuel(p_fuel)
        count += 1


def play_game():
    count = 1
    for planet in levels:
        won = play_level(planet)
        if won == False:
            print("Thanks for playing")
            break
        else:
            print("Do you want to play level", count, "?")
            inp = input("(yes/no)")
            if inp == "no":
                print("Thanks for playing")
                break
            elif inp == "yes":
                continue
            else:
                print("not a valid input. Exiting program...")
                break


play_game()


