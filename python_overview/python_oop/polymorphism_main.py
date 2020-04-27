from python_oop.polymorphism_generic import Bird, sparrow, ostrich


if __name__ == "__main__":
    # we can instantiate the three objects because we are importing all of them up there
    obj_bird = Bird()
    obj_spr = sparrow()
    obj_ost = ostrich()

    obj_bird.intro()
    obj_bird.flight()

    obj_spr.intro()
    obj_spr.flight()

    obj_ost.intro()
    obj_ost.flight()