from prettytable import PrettyTable
import itertools


class IceCream(object):

    table = []
    males = ["Peter", "Jacob", "Carl"]
    females = ["Hannah", "Naomi", "Iris"]
    flavors = ["Chocolate", "Vanilla", "Strawberry"]
    preference = ["Dish", "Cone"]

    def __init__(self, firstnames, lastnames):
        self.firstnames = firstnames
        self.lastnames = lastnames

    # Builds an empty table where the first column of the table contains the first names
    def build_table(self):
        for i in range(len(self.firstnames)):
            self.table.append([""]*6)

        count = 0
        for row in self.table:
            row[0] = self.firstnames[count]
            count += 1

    # Prints the table in a pretty format
    def print_table(self):
        t = PrettyTable(["First Name", "Last Name", "First", "Second", "Third", "Cone/Dish"])
        print()
        print("+------------------------+--------------------------------------+-----------+")
        print("|                        |            Flavor Ranking            |           |")
        for row in self.table:
            t.add_row(row=row)
        print(t)
        print()

    def permute_table(self):
        # Generate all of the different table permutations until correct table is found
        table_index_permutations = list(itertools.permutations(range(0, 6)))
        lastname_index_permutations = list(itertools.permutations(range(0, 4)))
        flavor_indices_permutations = list(itertools.permutations(range(1, 6)))

        index = 0
        for indices in flavor_indices_permutations:
            flavor_indices_permutations[index] = (0,) + indices
            index += 1

        itercount = 0
        # Start by generating all last name permutations
        for lastname_indices in lastname_index_permutations:
            for table_indices in table_index_permutations:
                self.table[table_indices[0]][1] = self.lastnames[lastname_indices[0]]
                self.table[table_indices[1]][1] = self.lastnames[lastname_indices[0]]
                self.table[table_indices[2]][1] = self.lastnames[lastname_indices[1]]
                self.table[table_indices[3]][1] = self.lastnames[lastname_indices[1]]
                self.table[table_indices[4]][1] = self.lastnames[lastname_indices[2]]
                self.table[table_indices[5]][1] = self.lastnames[lastname_indices[3]]

                # We know that the first row and third column (i.e Peter) must be strawberry
                # Additionally, we know that atleast three of the flavors need to be chocolate
                # for flavor_indices in flavor_index_permutations:
                for flavor_table_indices in flavor_indices_permutations:

                    # self.table[flavor_table_indices[0]][2] = self.flavors[flavor_indices[2]]
                    self.table[flavor_table_indices[0]][2] = self.flavors[2]  # Always Peter and strawberry
                    self.table[flavor_table_indices[0]][3] = self.flavors[0]
                    self.table[flavor_table_indices[0]][4] = self.flavors[1]

                    # self.table[flavor_table_indices[1]][2] = self.flavors[flavor_indices[0]]
                    self.table[flavor_table_indices[1]][2] = self.flavors[0]
                    self.table[flavor_table_indices[1]][3] = self.flavors[1]
                    self.table[flavor_table_indices[1]][4] = self.flavors[2]

                    # self.table[flavor_table_indices[2]][2] = self.flavors[flavor_indices[0]]
                    self.table[flavor_table_indices[2]][2] = self.flavors[0]
                    self.table[flavor_table_indices[2]][3] = self.flavors[1]
                    self.table[flavor_table_indices[2]][4] = self.flavors[2]

                    # self.table[flavor_table_indices[3]][2] = self.flavors[flavor_indices[0]]
                    self.table[flavor_table_indices[3]][2] = self.flavors[0]
                    self.table[flavor_table_indices[3]][3] = self.flavors[2]
                    self.table[flavor_table_indices[3]][4] = self.flavors[1]

                    # self.table[flavor_table_indices[4]][2] = self.flavors[flavor_indices[1]]
                    self.table[flavor_table_indices[4]][2] = self.flavors[1]
                    self.table[flavor_table_indices[4]][3] = self.flavors[0]
                    self.table[flavor_table_indices[4]][4] = self.flavors[2]

                    # self.table[flavor_table_indices[5]][2] = self.flavors[flavor_indices[1]]
                    self.table[flavor_table_indices[5]][2] = self.flavors[1]
                    self.table[flavor_table_indices[5]][3] = self.flavors[2]
                    self.table[flavor_table_indices[5]][4] = self.flavors[0]

                    # Once we have generated each flavor permutation, we must also permute cone/dish options
                    self.table[0][5] = self.preference[1]
                    self.table[1][5] = self.preference[1]
                    self.table[2][5] = self.preference[1]
                    self.table[3][5] = self.preference[0]
                    self.table[4][5] = self.preference[0]
                    self.table[5][5] = self.preference[1]

                    itercount += 1
                    # Now that we have the table completely filled, check it against the problem statements
                    if self.check_table():  # That means we have found the correct names, flavors, and such
                        self.print_table()  # Show the resulting table
                        print(itercount)   
                        exit(0)             # And quit the program

    def check_table(self):
        # Checks that exactly two of the last names are Hillman and McNeal
        has_hillman = False
        has_mcneal = False
        hillman_count = 0
        mcneal_count = 0
        for row in self.table:
            if row[1] == "Hillman":
                has_hillman = True
                hillman_count += 1
            if row[1] == "McNeal":
                has_mcneal = True
                mcneal_count += 1
        two_last_names = has_hillman and has_mcneal and hillman_count == 1 and mcneal_count == 1

        # Checks that atleast three of the children ranked chocolate first
        num_chocolate_first = 0
        has_atleast_three_chocolate_ranked_first = False
        for row in self.table:
            if row[2] == "Chocolate":
                num_chocolate_first += 1
            if num_chocolate_first >= 3:
                has_atleast_three_chocolate_ranked_first = True
                break

        # Checks that none of the children that ranked chocolate first have sibling who also rank chocolate first
        has_siblings_that_ranked_chocolate_first = False
        for row in self.table:
            if row[2] == "Chocolate":
                firstname = row[0]
                lastname = row[1]
                for person in self.table:
                    if person[0] != firstname and person[1] == lastname:  # Means they are a sibling
                        if person[2] == "Chocolate":  # And means that they also ranked chocolate first
                            has_siblings_that_ranked_chocolate_first = True
                            break

        # Checks that Peter is the only child that ranked strawberry first
        peter_is_the_only_child_ranked_strawberry_first = False
        for row in self.table:
            if row[2] == "Strawberry":
                if row[0] == "Peter":
                    peter_is_the_only_child_ranked_strawberry_first = True
                else:  # Then we found a child other than Peter that ranked strawberry first, no good...
                    peter_is_the_only_child_ranked_strawberry_first = False
                    break

        # Checks that Jacob did not rank vanilla last
        jacob_ranked_vanilla_last = False
        for row in self.table:
            if row[0] == "Jacob" and row[4] == "Vanilla":
                jacob_ranked_vanilla_last = True
                break

        # Checks that Jacob's last name is not McNeal
        jacobs_last_name_is_mcneal = False
        for row in self.table:
            if row[0] == "Jacob" and row[1] == "McNeal":
                jacobs_last_name_is_mcneal = True
                break

        # Checks that Jacob's and a Harding child's flavor rankings are identical
        jacob = self.table[1]
        is_identical_flavors = False
        for row in self.table:
            if row[1] == "Harding":
                if jacob[1] == "Hillman" and jacob[2] == row[2] and jacob[3] == row[3] and jacob[4] == row[4]:
                    is_identical_flavors = True
                    break

        # Now check that they are the only children with identical flavor rankings
        is_other_identical_rankings = False
        for i in range(len(self.table)):
            child1 = self.table[i]
            if child1[0] == "Jacob" or child1[1] == "Harding":
                continue
            for j in range(i+1, len(self.table)):
                child2 = self.table[j]
                if child1[2] == child2[2] and child1[3] == child2[3] and child1[4] == child2[4]:
                    is_other_identical_rankings = True
                    break

        # Checks that Jacob and the Harding child do not both prefer a cone to a dish
        do_not_both_prefer_cone_to_dish = False
        for row in self.table:
            if row[1] == "Harding" and row[5] == "Dish" and jacob[5] == "Cone" or \
               row[1] == "Harding" and row[5] == "Cone" and jacob[5] == "Dish":
                do_not_both_prefer_cone_to_dish = True
                break

        # Checks that one child in each family prefers a cone, this also covers the only children case as well
        #
        #                Hillman, McNeal, Johnson, Harding
        # last_names = [   False,  False,   False,   False]
        #
        last_name_has_cone = [False, False, False, False]
        for row in self.table:
            if row[1] == "Hillman" and row[5] == "Cone":
                last_name_has_cone[0] = True
            elif row[1] == "McNeal" and row[5] == "Cone":
                last_name_has_cone[1] = True
            elif row[1] == "Johnson" and row[5] == "Cone":
                last_name_has_cone[2] = True
            elif row[1] == "Harding" and row[5] == "Cone":
                last_name_has_cone[3] = True
        one_child_in_each_family_prefers_cone = True
        for bool_val in last_name_has_cone:
            if not bool_val:
                one_child_in_each_family_prefers_cone = False
                break

        # Checks that only the Johnson children ranked vanilla last
        only_johnsons_ranked_vanilla_last = True
        for row in self.table:
            if (row[1] == "Johnson" and row[4] != "Vanilla") or (row[4] == "Vanilla" and row[1] != "Johnson"):
                only_johnsons_ranked_vanilla_last = False

        # Checks that Hannah prefers a dish to a cone
        hannah_prefers_dish = False
        for row in self.table:
            if row[0] == "Hannah" and row[5] == "Dish":
                hannah_prefers_dish = True
                break

        # Checks that Naomi's brother ranked chocolate last
        ranked_chocolate_last = False
        lastname = ""
        for row in self.table:
            if row[0] == "Naomi":
                lastname = row[1]
                break
        for row in self.table:
            if row[0] in self.males and row[1] == lastname and row[4] == "Chocolate":
                ranked_chocolate_last = True
                break

        # Returns if the table in self.table is correct or not
        return two_last_names and has_atleast_three_chocolate_ranked_first and not \
            has_siblings_that_ranked_chocolate_first and peter_is_the_only_child_ranked_strawberry_first \
            and not jacob_ranked_vanilla_last and not jacobs_last_name_is_mcneal and is_identical_flavors \
            and not is_other_identical_rankings and one_child_in_each_family_prefers_cone and hannah_prefers_dish \
            and ranked_chocolate_last and only_johnsons_ranked_vanilla_last and do_not_both_prefer_cone_to_dish


# Build an empty table that only has first names in it initially
ice = IceCream(firstnames=["Peter", "Jacob", "Carl", "Hannah", "Naomi", "Iris"],
               lastnames=["Hillman", "McNeal", "Johnson", "Harding"])
ice.build_table()
# Run the permutations filling the table with the rest of the info
ice.permute_table()
