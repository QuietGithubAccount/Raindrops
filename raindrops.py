#Raindrops.py
def raindrops(input):
    assert type(input) is int

    output = ''
    if input % 3 == 0:
        output = output + 'Pling'
    if input % 5 == 0:
        output = output + 'Plang'
    if input % 7 == 0:
        output = output + 'Plong'
    if len(output) == 0:
        output = str(input)

    return output
