# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, greeting_template = 'Hello, <name>!'):
    name == '<name>'
    return greeting_template.replace('<name>', name)

print(greet('Doc'))
print(greet('Bob', "What's up, <name>!"))

surface_gravity = {
        "sun" : 274,
        "jupiter" : 24.92,
        "neptune" : 11.15,
        "saturn" : 10.44,
        "earth" : 9.798,
        "uranus": 8.87,
        "venus" : 8.87,
        "mars" : 3.71,
        "mercury" : 3.7,
        "moon" : 1.62,
        "pluto" : 0.58
}
def force(mass, body = 'earth'):
    body == 'body'
    gravity = round((surface_gravity[body]), 1)
    print('the gravity of'+' '+ body + ' ' + 'becomes' + ' ' + str(gravity))
    calculation_gravity = (mass * gravity)
    return calculation_gravity

print(force(100,'venus'))

def pull(m1, m2, d):
    G = (6.674*(10**-11))
    calculate_pull = round((G * ((m1 * m2)/d**2)), 2)
    
    return calculate_pull

print (pull(0.1, (5.972*(10**24)), 6.371*(10**6)))
