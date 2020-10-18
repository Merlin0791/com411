import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.escape_characters as escape_characters
import basics.output.ascii_art as ascii_art
import basics.input.ascii_robot as ascii_robot
import basics.input.data_type as data_type
import basics.input.string_operators as string_operators
import basics.input.user_input as user_input
import basics.decisions.and_operator as and_operator
import basics.decisions.or_operator as or_operator
import basics.decisions.nested_decisions.nestception as nestception
import basics.decisions.nested_decisions.nested_decision as nested_decision
import basics.decisions.simple_decisions.comparison_operator as comparison_operator
import basics.decisions.simple_decisions.counter as counter
import basics.decisions.simple_decisions.if_elif_else as if_elif_else
import basics.decisions.simple_decisions.if_else as if_else
import basics.decisions.simple_decisions.if_code as if_code
import basics.decisions.simple_decisions.modulo_operator as modulo_operator
import basics.functions.ascii_reverse as ascii_reverse
import basics.functions.ascii_function as ascii_function
import basics.functions.function_call as function_call
import basics.functions.function_with_loop as function_with_loop
import basics.functions.function_with_nesting as function_with_nesting
import basics.functions.function_with_parameter as function_with_parameter
import basics.functions.function_with_parameters as function_with_parameters
import basics.functions.multiple_functions as multiple_functions
import basics.functions.return_values as return_values
import basics.functions.simple_function as simple_function
import basics.repetitions.for_loop.characters as characters
import basics.repetitions.for_loop.countdown as countdown
import basics.repetitions.for_loop.membership_operators as membership_operators
import basics.repetitions.for_loop.ranged as ranged
import basics.repetitions.for_loop.reverse as reverse
import basics.repetitions.for_loop.for_simple as for_simple
import basics.repetitions.nested_loop.nested as nested
import basics.repetitions.nested_loop.nesting as nesting
import basics.repetitions.while_loop.while_ascii as while_ascii
import basics.repetitions.while_loop.count as count
import basics.repetitions.while_loop.factorial as factorial
import basics.repetitions.while_loop.lenloop as lenloop
import basics.repetitions.while_loop.simple as simple
import basics.repetitions.while_loop.sum_100 as sum_100
import basics.repetitions.while_loop.sum_of_user as sum_of_user
import basics.modules.guess_the_numnber as guess_the_numnber



def run_block_a():

    print("Which program in 'Block A: Basics' do you wish to run?")
    response = input()

    if (response == "simple_message"):
        simple_message.run()
    elif (response == "multiline_message"):
        multiline_message.run()
    elif (response == "escape_characters"):
        escape_characters.run()    
    elif (response == "ascii_art"):
        ascii_art.run()
    elif (response == "ascii_robot"):
        ascii_robot.run()
    elif (response == "data_type"):
        data_type.run()
    elif (response == "string_operators"):
        string_operators.run()
    elif (response == "user_input"):
        user_input.run()
    elif (response == "and_operator"):
        and_operator.run()
    elif (response == "or_operator"):
        or_operator.run()
    elif (response == "nestception"):
        nestception.run()
    elif (response == "nested_decision"):
        nested_decision.run()
    elif (response == "comparison_operator"):
        comparison_operator.run()
    elif (response == "counter"):
        counter.run()
    elif (response == "if_elif_else"):
        if_elif_else.run()
    elif (response == "if_else"):
        if_else.run()
    elif (response == "if_code"):
        if_code.run()
    elif (response == "modulo_operator"):
        modulo_operator.run()
    elif (response == "ascii_reverse"):
        ascii_reverse.run()
    elif (response == "ascii_function"):
        ascii_function.run()
    elif (response == "function_call"):
        function_call.run()
    elif (response == "function_with_loop"):
        function_with_loop.run()
    elif (response == "function_with_nesting"):
        function_with_nesting.run()
    elif (response == "function_with_parameter"):
        function_with_parameter.run()
    elif (response == "function_with_parameters"):
        function_with_parameters.run()
    elif (response == "multiple_functions"):
        multiple_functions.run()
    elif (response == "return_values"):
        return_values.run()
    elif (response == "simple_function"):
        simple_function.run()
    elif (response == "characters"):
        characters.run()
    elif (response == "countdown"):
        countdown.run()
    elif (response == "membership_operators"):
        membership_operators.run()
    elif (response == "ranged"):
        ranged.run()
    elif (response == "reverse"):
        reverse.run()
    elif (response == "for_simple"):
        for_simple.run()
    elif (response == "nested"):
        nested.run()
    elif (response == "nesting"):
        nesting.run()
    elif (response == "while_ascii"):
        while_ascii.run()
    elif (response == "count"):
        count.run()
    elif (response == "factorial"):
        factorial.run()
    elif (response == "lenloop"):
        lenloop.run()
    elif (response == "simple"):
        simple.run()
    elif (response == "sum_100"):
        sum_100.run()
    elif (response == "sum_of_user"):
        sum_of_user.run()
    elif (response == "guess_the_numnber"):
        guess_the_numnber.run()
    else:
      print("\nError!!!")


def run():
    is_running = True

    while(is_running):
        print("What would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if (response == "a"):
            run_block_a()
        elif (response == "q"):
            break
        else:
            print("Invalid option! Please try again.")

run()