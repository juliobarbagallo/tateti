# Ta-Te-Ti
Python ta-te-ti board game.
Play
    To run it, from the terminal: (base) jbarbaga@M1:~/codes/python/nb$ python tateti.py 
Tests
    (base) jbarbaga@M1:~/codes/python/nb$ python first_test.py

    El repositorio debe tener un archivo readme con las instrucciones de como iniciarlo y comentarios de lo que creas que haya sido desafiante al desarrollarlo.
    
    What was challenging?
    -------------------------
      The most challenging thing on this was how to determine the machine plays. How to avoid a tottally random choose.
      Then tried to do somethings using list comprehension as it was a question during the first interview.
      And, the last thing was add the random init between player and computer.

First of all I will need a board, where be placed the game.
    board = [' ' for x in range(10)]
    Board will have each place of the main board game, as its a 3x3 matrix, it will be range(10) 0-9
    and it will be created using list comprenhension with a for.

    machine_move():

    Is there a move we can do to win? if there is, do it
    if we can't win with just 1 move, is there a move the player can do to win? if we find that move, we should block it.
    pick up a corner if its available, if not take the center, if not take the edges

    possibleMoves: the list wich stores the available positions
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
                           |      |
                     our index    actual value in the enumerate(board) -> enumerate gives us the indexes and the values of the board
    x = 0 and letter = ' ' , X or O
    and check if letter is blank ' ' and X !=0, we don't want the computer to move at index 0

    for this function we will make a copy of the board:

    It will go step by step.
    1. If there is a move that can win the game, move to it.
    2. If the player can win with his next move, then move to that position.
    3. Check for any available corners. If more than one is available call to pick_random() to move to it.
    4. Check if the center, board[5], is available and take it.
    5. Check the edges, board[2,4,6,8]. If more than one is available call to pick_random() to move to it.
    

