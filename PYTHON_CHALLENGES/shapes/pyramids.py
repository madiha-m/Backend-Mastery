from validation import validate_input_num


def right_sided_pyramid(number):
    print('Right sided pyramid')
    for i in range(1, number+1):
        print('*'*i)


print('please enter a number for height for diamond:')
right_sided_pyramid(input())


def left_sided_pyramid(number):
    print('Left sided pyramid')
    for i in range(1, number):
        print('*'*number)
        number -= 1


print('please enter a number for height for diamond:', end='')
# user_input = input_validation(input())
left_sided_pyramid(validate_input_num(input()))


# 2 months basics conditions  language?js
# html > w3school, free codecamp
# , css , js
# 3 months basics conditions language?
# hard practice krni hy. with soft code.
# syntax error can do , but logical errors should not be there.

# twillio p app bnani hy ? chatbot hy yh?

# '''
# needs to craete api on twillio , like we receive msg, we reply as well. get+set
# ''' twillio p app bnani hy . how api craete in python.
# how we use api, deploy it, how uch we can perform using api using python on twillio.
# '''
