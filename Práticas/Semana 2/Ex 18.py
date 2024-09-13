numero = input('Insere um número: ')

def ContarStreak():
    had_a_zero = False
    streak = 0
    highestStreak = 0
    for i in range(0, len(numero)):
        if numero[i] == '0':
            had_a_zero = True
            streak += 1
        else:
            if had_a_zero and highestStreak < streak:
                highestStreak = streak
                had_a_zero = False
            streak = 0
    return highestStreak

print(ContarStreak())