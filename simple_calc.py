from os import error
from tkinter import *
root = Tk()
root.title("Simple Calculator")
root.minsize(300, 500)

operations = {1:'+',2:'-', 3:'*', 4:'/'}
next_op_allowed = FALSE
is_float = FALSE
next_expr = FALSE
error = FALSE

expr = Entry(root, 
            relief = SUNKEN, 
            bd = 5, 
            state = 'disabled', 
            bg = 'white', 
            fg = 'black', 
            justify = 'right')
expr.place(relheight=0.2,relwidth=0.8,relx=0, rely=0)

def btn_press(number):
    global next_op_allowed
    global is_float
    global next_expr
    expr.configure(state='normal')
    if next_expr == TRUE:
        next_expr = FALSE
        expr.delete(0, END)    
    current = expr.get()
    expr.delete(0, END)
    expr.insert(0, str(current) + str(number))
    if next_op_allowed == FALSE:
        next_op_allowed = TRUE
    expr.configure(state='disabled')      

def place_dot():
    global next_op_allowed
    global is_float
    global next_expr
    if next_expr == TRUE:
        expr.configure(state='normal')
        res = expr.get()
        expr.configure(state='disabled')
        try:
            res = int(res)
            next_expr = FALSE
        except ValueError:
            try:
                res = float(res)
                next_expr = FALSE
                return
            except ValueError:        
                return
    if (is_float == FALSE and next_op_allowed == TRUE):
        next_op_allowed = FALSE
        is_float = TRUE
        expr.configure(state='normal')
        current = expr.get()
        expr.delete(0, END)
        expr.insert(0, str(current) + '.')
        expr.configure(state='disabled')
    else:
        pass
   
def clear_expr():
    global next_op_allowed
    global is_float
    global next_expr
    global error
    next_op_allowed = FALSE
    is_float = FALSE
    next_expr = FALSE
    error = FALSE
    expr.configure(state='normal')
    expr.delete(0, END)
    expr.configure(state='disabled')

def set_op(operation):
    global next_op_allowed
    global is_float
    global error
    global next_expr
    if error == TRUE:
        error = FALSE
        expr.configure(state='normal')
        expr.delete(0, END)
        expr.configure(state='disabled')
        return
    if next_expr == TRUE:
        next_expr = FALSE
    expr.configure(state='normal')
    curr_expr = expr.get()
    is_float = FALSE
    if next_op_allowed == TRUE:     
        next_op_allowed = FALSE
        expr.delete(0, END)
        expr.insert(0, str(curr_expr) + str(operations[operation]))
    else:
        curr_expr = curr_expr[:len(curr_expr) - 1] + operations[operation]
        expr.delete(0, END)
        expr.insert(0, str(curr_expr))
    expr.configure(state='disabled')

def calculate():
    global next_expr
    global error
    global next_op_allowed
    expr.configure(state='normal')
    expression = expr.get()
    try:
        result = eval(expression)
        next_op_allowed = TRUE
    except ZeroDivisionError:
        result = "Cannot divide by zero"
        error = TRUE
    except NameError:
        result = "Bad syntaxes"
        error = TRUE
    except SyntaxError:
        result = "Bad syntaxes"
        error = TRUE
    next_expr = TRUE
    expr.delete(0, END)
    expr.insert(0, str(result))
    expr.configure(state='disabled')
       
btn_0 = Button(root, text='0',command=lambda: btn_press(0))
btn_1 = Button(root, text='1',command=lambda: btn_press(1))
btn_2 = Button(root, text='2',command=lambda: btn_press(2))
btn_3 = Button(root, text='3',command=lambda: btn_press(3))
btn_4 = Button(root, text='4',command=lambda: btn_press(4))
btn_5 = Button(root, text='5',command=lambda: btn_press(5))
btn_6 = Button(root, text='6',command=lambda: btn_press(6))
btn_7 = Button(root, text='7',command=lambda: btn_press(7))
btn_8 = Button(root, text='8',command=lambda: btn_press(8))
btn_9 = Button(root, text='9',command=lambda: btn_press(9))
btn_sum = Button(root, text='+',command=lambda: set_op(1))
btn_sub = Button(root, text='-',command=lambda: set_op(2))
btn_mul = Button(root, text='*',command=lambda: set_op(3))
btn_div = Button(root, text='/',command=lambda: set_op(4))
btn_clr = Button(root, text='C',command=clear_expr)
btn_dot = Button(root, text='.',command=place_dot)
btn_cnt = Button(root, text='=',command=calculate) 

btn_0.place(relheight=0.2,relwidth=0.25,relx=0, rely=0.8)
btn_1.place(relheight=0.2,relwidth=0.25,relx=0, rely=0.6)
btn_2.place(relheight=0.2,relwidth=0.25,relx=0.25, rely=0.6)
btn_3.place(relheight=0.2,relwidth=0.25,relx=0.5, rely=0.6)
btn_4.place(relheight=0.2,relwidth=0.25,relx=0, rely=0.4)
btn_5.place(relheight=0.2,relwidth=0.25,relx=0.25, rely=0.4)
btn_6.place(relheight=0.2,relwidth=0.25,relx=0.5, rely=0.4)
btn_7.place(relheight=0.2,relwidth=0.25,relx=0, rely=0.2)
btn_8.place(relheight=0.2,relwidth=0.25,relx=0.25, rely=0.2)
btn_9.place(relheight=0.2,relwidth=0.25,relx=0.5, rely=0.2)
btn_sum.place(relheight=0.2,relwidth=0.25,relx=0.75, rely=0.2)
btn_sub.place(relheight=0.2,relwidth=0.25,relx=0.75, rely=0.4)
btn_mul.place(relheight=0.2,relwidth=0.25,relx=0.75, rely=0.6)
btn_div.place(relheight=0.2,relwidth=0.25,relx=0.75, rely=0.8)
btn_clr.place(relheight=0.2,relwidth=0.2,relx=0.8, rely=0)
btn_dot.place(relheight=0.2,relwidth=0.25,relx=0.25, rely=0.8)
btn_cnt.place(relheight=0.2,relwidth=0.25,relx=0.5, rely=0.8)

root.mainloop()