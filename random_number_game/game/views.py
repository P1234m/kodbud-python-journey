from django.shortcuts import render, redirect
import random
import time

def game_view(request):
    # Handle difficulty selection and start new game
    if request.method == 'GET' and 'difficulty' in request.GET:
        difficulty = request.GET.get('difficulty', 'medium').lower()
        ranges = {'easy': 50, 'medium': 100, 'hard': 150}
        max_val = ranges.get(difficulty, 100)

        request.session.clear()  # Clears previous game data safely

        request.session['number'] = random.randint(1, max_val)
        request.session['attempts'] = 0
        request.session['guesses'] = []
        request.session['difficulty'] = difficulty.capitalize()
        request.session['max_val'] = max_val
        request.session['start_time'] = time.time()

        return render(request, 'game.html', {
    'difficulty': difficulty.capitalize(),
    'max_val': max_val,
    'feedback': '',
    'guesses': [],
    'attempts': 0,
    'game_over': False
})

    # If game hasn't started yet
    if 'number' not in request.session:
        return render(request, 'game.html', {
            'feedback': '',
            'guesses': [],
            'attempts': 0,
            'difficulty': 'Medium',
            'max_val': 100,
            'game_over': False
        })

    # Game is active
    context = {
        'difficulty': request.session.get('difficulty', 'Medium'),
        'max_val': request.session.get('max_val', 100),
        'feedback': '',
        'guesses': request.session.get('guesses', []),
        'attempts': request.session.get('attempts', 0),
        'game_over': False
    }

    if request.method == 'POST':
        try:
            guess = int(request.POST.get('guess'))
            request.session['attempts'] += 1
            request.session['guesses'].append(guess)

            number = request.session['number']
            if guess < number:
                context['feedback'] = "Too Low! 🐭📉"
            elif guess > number:
                context['feedback'] = "Too High! 🚀📈"
            else:
                context['feedback'] = f"Perfect Guess! You cracked it in {request.session['attempts']} attempts! 🧠💥"
                context['game_over'] = True
                request.session.clear()
        except ValueError:
            context['feedback'] = "Please enter a valid number."

    return render(request, 'game.html', context)