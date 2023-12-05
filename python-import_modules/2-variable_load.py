variables = {}
exec(open('variable_load_2.py').read(), variables)

a_value = variables.get('a')

print(a_value)