import numpy as np

def calculate(lists):
    max_amount = 9
    amount_in_list = len(lists)
    if amount_in_list < max_amount or amount_in_list > max_amount:
        print("List must contain nine numbers.")
        return

    else:
        lists = np.reshape(lists, (3,3))

        mean = []
        var = []
        std = []
        max = []
        min = []
        sum = []

        num_axis = [0,1]
        for num in num_axis:
            mean.append(lists.mean(axis = num).tolist())
            var.append(lists.var(axis = num).tolist())
            std.append(lists.std(axis = num).tolist())
            max.append(lists.max(axis = num).tolist())
            min.append(lists.min(axis = num).tolist())
            sum.append(lists.sum(axis = num).tolist())

        mean.append(lists.mean().tolist())
        var.append(lists.var().tolist())
        std.append(lists.std().tolist())
        max.append(lists.max().tolist())
        min.append(lists.min().tolist())
        sum.append(lists.sum().tolist())

        calculations = { 'mean': mean, 
                        'variance': var,
                        'standard deviation': std,
                        'max': max, 
                        'min': min,
                        'sum': sum}
        
        return calculations
