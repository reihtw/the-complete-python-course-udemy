# print(my_variable) # NameError: name 'my_variable' is not defined

'''
=====================================================================================
Traceback (most recent call last):
    File ".../app.py", line 53, in <module> menu()
    File ".../app.py", line 10, in menu show_movies()
    File ".../app.py", line 36, in show_movies show_movie_details(movie)'
    File ".../app.py", line 40, in show_movie_details print(f'Name: {movies['name']})
TypeError: list indices must be integers or slices, not str
=====================================================================================

1 - At the very bottom it gives you the error that was raised and a description.
2 - What line of your code raised the error;
3 - What function that line is in;
4 - What function called the function tha line is in;
5 - And so on... until you reach the file that you executed.
'''

# Tips to solve errors:
#
# 1 - Look at your code
# 2 - Put the error and message into Google, see if something comes up in StackOverflow
# 3 - Look at the code you've written again, this time more slowly, and run through it as
#     if you were a computer. Do you notice anything that could potentially be a source of
#     the error?
# 4 - Run only some parts of the code in isolation, that'll help identify which part of your
#     is giving you an error.
# 5 - Use a debugger.
# 6 - And of course, ask questions in the Course Q&A. We're here to help!