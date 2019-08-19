_output = ''

def add_headers():
    global _output
    c_header = "{:^10}".format('Company')
    r_header = "{:^10}".format('Revenue')
    e_header = "{:^10}".format('Expenses')
    p_header = "{:^10}".format('Profit')
    _output += f'{c_header}\t{r_header}\t{e_header}\t{p_header}\n'
    
def add_row():
    global _output

    c = input("Company: ")
    r = float(input("Revenue: "))
    e = float(input("Expenses: "))
    p = r - e #profit

    c_str = "{:<10}".format(c)
    r_str = "${:>10,.2f}".format(r)
    e_str = "${:>10,.2f}".format(e)
    p_str = "${:>10,.2f}".format(p)

    new_row = f'{c_str}\t{r_str}\t{e_str}\t{p_str}\n'

    _output += new_row

    again = input("Again? Press ENTER to add a row or Q to quit. ")
    if again.lower() != 'q':
        add_row()
    else:
        print(_output)

def main():
    add_headers()
    add_row()

main()