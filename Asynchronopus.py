class Asynchronous:
    def __init__(self, first_clk, second_clk):
        if(first_clk == second_clk):
            print("not Asynchronous")
        else:
            print("Asynchronous")

obj = Asynchronous(200, 300)
obj_1=Asynchronous(200, 200)