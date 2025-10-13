# my_controller.py
import numpy as np

def my_controller(x, v, t, eta10):

    """ NOTE: eta10 is only provided for the scoring interval (t >= T_0 = 30 s) """
    """ eta10 = nan for t < T_0 --> make sure to handle nan values gracefully when using eta10 """
    if not np.isnan(eta10):
        # Optional preview or estimation logic
        pass


    """ Simple damping controller example """
    B_pto = 10e4

    F_pto = B_pto * v

    return F_pto