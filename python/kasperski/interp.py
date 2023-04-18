import sys
user_functions = {}
operations = {
    'add' : lambda a: a[0] + a[1],
    'sub' : lambda a : a[0] - a[1],
    'mul' : lambda a : a[0] * a[1],
    'div' : lambda a: a[0] // a[1],
    'init' : lambda a : a[1]
}

class Function:
    def __init__(self,args_name ):
        self.body = []
        self.args_name = args_name

    def add_line(self , line):
        self.body.append(line)

    def result(self, arguments = []):

        def var_to_meaning(args , vars):
            meanings = []
            for x in args:
                buff = vars.get(x,x)
                meanings.append(buff)
            return meanings

        global operations
        global user_functions
        vars = {}
        #init vars from arguments
        for i in range(len(self.args_name)):
            vars[self.args_name[i]] = arguments[i]

        for i in range(len(self.body)):
            line = self.body[i]

            #make operation
            if(line[0] in operations):
                operation = operations[line[0]]
                operation_args = var_to_meaning(line[1:],vars)
                vars.update({line[1] : operation(operation_args) })

            #call user function
            if(line[0] in user_functions):
                function = user_functions[line[0]]
                function_args = var_to_meaning(line[1::],vars)
                vars.update({ line[1] : function.result(function_args) })
            
            if(line[0] == "return"):
                return vars[line[1]]


def line_to_term(line):
    return [int(x) if x.isdigit() else x for x in line.rstrip().split(" ")]

def solution(f_in, f_out):

    global user_functions
    main_function = Function([])
    stack_write_fn = [main_function]

    for inp_line in f_in:
        line = line_to_term(inp_line)
        if(line[0] == ''):
            continue
        if(line[0] == 'end_program'):
            break

        #create function
        if(line[0] == 'function'):
            user_functions[line[1]] = Function(line[2:])
            stack_write_fn.append(user_functions[line[1]])
            continue

        stack_write_fn[-1].add_line(line)

        #end write function
        if(line[0] == 'return'):
            stack_write_fn.pop()

    f_out.write(str(main_function.result()))

if __name__ == "__main__":
    solution(sys.stdin, sys.stdout)
