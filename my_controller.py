# my_controller.py
def my_controller(x, v, t, eta10):
    """Simple damping controller example"""
    B_pto = 10e4

    F_pto = B_pto * v

    return F_pto