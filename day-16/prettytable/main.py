from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon","Type"]
table.add_rows(
    [
        ["Pikachu","Electric"],
        ["Squirtle","Warter"],
        ["Charmander","Fire"]
    ]
)
table.align = "l"
print(table)