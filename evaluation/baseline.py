# evaluation/baseline.py

def threshold_policy(state):
    """
    state = [lambda, instances, utilization, error_rate, response_time]
    """
    utilization = state[2]

    if utilization > 0.8:
        return 2  # scale up
    elif utilization < 0.3:
        return 0  # scale down
    else:
        return 1  # maintain