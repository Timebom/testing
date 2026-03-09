def page_rank():
    print("Enter the Matrix:")
    array_input = []
    for i in range(3):
        array_input.append([float(y) for y in input().split()])
    print(array_input)

    final_mat = [1.0, 1.0, 1.0]
    itr = int(input("Number of Iteration: "))
    for loop in range(itr):
        print(f"Iteration : {loop + 1}")
        cnt = 0
        for row in range(len(array_input)):
            sum = 0
            for col in range(len(array_input[row])):
                if array_input[col][row] == 1:
                    # cnt = 0
                    for i in range(3):
                        if array_input[col][i] == 1:
                            cnt = cnt + 1
                    sum += final_mat[col] / cnt

            cnt = 0
            final_mat[row] = 0.5 + (0.5 * sum)
            # print(f"{final_mat[row]:.2f}", end='\t')
            print(final_mat[row])
        print()

page_rank()
