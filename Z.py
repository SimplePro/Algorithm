N, r, c = map(int, input().split())

count = 0

def recursion(ro, co, depth):
    global count

    if depth == 0:
        if ro == r and co == c:
            print(count)

    else:
        step_gap = 2**(depth-1)
        if r < ro+step_gap:
            if c < co+step_gap:
                recursion(ro, co, depth-1)
            elif c >= co+step_gap:
                count += step_gap**2
                recursion(ro, co+step_gap, depth-1)

        elif r >= ro+step_gap:
            if c < co+step_gap:
                count += 2 * step_gap**2
                recursion(ro+step_gap, co, depth-1)
            elif c >= co+step_gap:
                count += 3 * step_gap**2
                recursion(ro+step_gap, co+step_gap, depth-1)

recursion(0, 0, N)