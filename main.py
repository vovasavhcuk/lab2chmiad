from Bus import Bus


class main:
    print("Явное :")
    bus = Bus("gae", 24, 1)
    bus.show()
    print("Неявное")
    bus.set_name("goof")
    bus.set_number(2)
    bus.set_numSeats(24)
    bus.show()
