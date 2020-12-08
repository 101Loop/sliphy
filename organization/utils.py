import random
import string


def generate_slip_id() -> str:
    """Generate slip ID.
    :return:
    """
    random_string = string.digits
    new_id = "".join([random.SystemRandom().choice(random_string) for i in range(10)])
    generated_id = f"ID{new_id}"
    return generated_id
