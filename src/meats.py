
class InputDetails:

    def get_meat_input(meat_selection):
        # Get input from user
        meat_choice = meat_selection
        time_per_kilo = 0

        # Calculate based on user input
        if meat_choice in ('Boeuf', 'boeuf'):
            time_per_kilo = 0.617


        elif meat_choice in {'Poulet', 'poulet'}:
            time_per_kilo = 1


        elif meat_choice in {'Porc' , 'porc'}:
            time_per_kilo = 1


        elif meat_choice in {'Agneau' , 'agneau'}:
            time_per_kilo = 0.4

        elif meat_choice in {'no meat selected'}:
            time_per_kilo = 0.0

        time = time_per_kilo
        return time