def main():
    num = float(input("What do you weigh on Earth? "))
    mercury_weight = 0.38 * num
    jupiter_weight = 2.53 * num
    round_mercury = "%.2f" % mercury_weight
    round_jupiter = "%.2f" % jupiter_weight
    print("\n" + "On Mercury you would weigh " +
          f"{round_mercury}" + " pounds." + "\n" +
          "On Jupiter you would weigh " + f"{round_jupiter}" + " pounds.")


# NOTE: This means if the code is run as `python3 planets.py`, run the
# main function.  If the code is merely imported, don't do anything.

if __name__ == "__main__":
    main()
