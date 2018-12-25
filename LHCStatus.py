import LHCStatusOptions

def main():
    print("What do you want to check?")
    i = 0
    
    options = list(LHCStatusOptions.StatusOptions)

    for Option in (LHCStatusOptions.StatusOptions):
        i += 1
        print('{}. {}'.format(i,Option.value))

    selection = input()

if __name__ == "__main__":
    main()