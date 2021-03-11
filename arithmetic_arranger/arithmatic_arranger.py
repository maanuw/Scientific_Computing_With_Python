def arithmetic_arranger(problems, optional=None):
    if len(problems) > 5:
        return("Error: Too many problems.")
    for i in range(len(problems)):
        if '+' not in problems[i] and '-' not in problems[i]:
            return("Error: Operator must be '+' or '-'.")

    for i in range(len(problems)):
        if '+' in problems[i]:
            l = problems[i].split(" + ")
            #print(l)
            for j in range(len(l)):
                if l[j].isdigit():
                    if len(l[j]) > 4:
                        return("Error: Numbers cannot be more than four digits.")
                else:
                    return("Error: Numbers must only contain digits.")
        if '-' in problems[i]:
            l = problems[i].split(" - ")
            #print(l)
            for j in range(len(l)):
                if l[j].isdigit():
                    if len(l[j]) > 4:
                        return("Error: Numbers cannot be more than four digits.")
                else:
                    return("Error: Numbers must only contain digits.")

    solutions = []
    for i in range(len(problems)):
        if "+" in problems[i]:
            nums = problems[i].split(" + ")
            solution = int(nums[0])+int(nums[1])
            solutions.append(solution)
        elif "-" in problems[i]:
            nums = problems[i].split(" - ")
            solution = int(nums[0])-int(nums[1])
            solutions.append(solution)
    #print(solutions)
    arranged_problems = ""

    final_line1=""
    for i in range(len(problems)):
        l = problems[i].split(" ")
        #print(l)
        num1_len = len(l[0])
        num2_len = len(l[2])
        if num1_len > num2_len :
            line1 = " "*(2) + l[0]
        else:
            line1 = " "*((num2_len+2)-num1_len) + l[0]
        final_line1 = final_line1 + line1 + " "*4
    final_line1 = final_line1.rstrip()

    final_line2=""
    for i in range(len(problems)):
        l = problems[i].split(" ")
        num1_len = len(l[0])
        num2_len = len(l[2])
        if num1_len > num2_len :
            line2 = l[1]+" "*(1+(num1_len - num2_len))+l[2]
        else :
            line2 = l[1]+" "+l[2]
        final_line2 = final_line2+ line2 + " "*4
    final_line2 = final_line2.rstrip()

    final_dash=""
    for i in range(len(problems)):
        l = problems[i].split(" ")
        num1_len = len(l[0])
        num2_len = len(l[2])
        if num1_len > num2_len :
            dash = "-"*(num1_len+2)
        else :
            dash = "-"*(num2_len+2)
        final_dash = final_dash + dash + " "*4
    final_dash = final_dash.rstrip()

    final_sol=""
    for i in range(len(problems)):
        l = problems[i].split(" ")
        num1_len = len(l[0])
        num2_len = len(l[2])
        if num1_len > num2_len :
            sol =" "*((num1_len+2)-len(str(solutions[i]))) + str(solutions[i])
        else :
            sol =" "*((num2_len+2)-len(str(solutions[i]))) + str(solutions[i])
        final_sol = final_sol + sol + " "*4
    final_sol = final_sol.rstrip()

    if optional == True:
        arranged_problems = final_line1 + "\n" + final_line2 + "\n" + final_dash + "\n" + final_sol
    else:
        arranged_problems = final_line1 + "\n" + final_line2 + "\n" + final_dash

    arranged_problems = arranged_problems.rstrip()

    return arranged_problems
