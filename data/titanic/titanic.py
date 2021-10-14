import csv

class TitanicData ():
    def __init__(self):
        file_path: str = "./titanic.csv"
        menu: str =   """
Please select one of the following options:

[1] Display the names of all passengers
[2] Display the number of passengers that survived
[3] Display the number of passengers per gender
[4] Display the number of passengers per age group
[5] Display the number of survivors per age group

Select an option
>>> """

        print("\nLoading data...")

        with open(file_path, "r") as file:
            self.records: list[list[str]] = list(csv.reader(file))
            headings: list[str] = self.records.pop(0)

        print(f"Successfully loaded {len(self.records)} self.records.\n")

        option = input(menu)
        print(f"\n** You have selected the option: {option} **\n")

        if option == "1": print(self.one())
        elif option == "2": print(self.two())
        elif option == "3": print(self.three())
        elif option == "4":
            children, adults, elderly = self.four()
            print(f"children: {children}, adults: {adults}, elderly: {elderly}\n")
        elif option == "5": print(self.five())

    def one (self):
        return "\n".join([name for name in [name[3] for name in self.records]])

    def two (self):
        return f"{len(list(filter(lambda psng: psng[1] == '1', self.records)))} passengers survived."

    def three (self):
        males = len(list(filter(lambda psng: psng[4] == "male", self.records)))
        females = len(self.records) - males
        return f"females: {females}, males: {males}"

    def four (self):
        self.records = list(filter(lambda psng: psng[5] != "", self.records))
        children = len(list(filter(lambda psng: float(psng[5]) < 18, self.records)))
        adults = len(list(filter(lambda psng: float(psng[5]) >= 18 and float(psng[5]) < 65, self.records)))
        elders = len(list(filter(lambda psng: float(psng[5]) >= 65, self.records)))
        return (children, adults, elders)
    def five (self):
        children, adults, elders = self.four()
        c_surv = len(list(filter(lambda psng: float(psng[5]) < 18 and psng[1] == "1", self.records)))
        a_surv = len(list(filter(lambda psng: float(psng[5]) >= 18 and float(psng[5]) < 65 and psng[1] == "1", self.records)))
        e_surv = len(list(filter(lambda psng: float(psng[5]) >= 65 and psng[1] == "1", self.records)))
        return f"children: {c_surv}/{children}, adults: {a_surv}/{adults}, elderly: {e_surv}/{elders}"

TitanicData()