import unittest
from airplane_assembly import Fuselage
fuselage = Fuselage()
bolt_pattern = {
        1: "1st bottom left bolt",
        2: "2nd top center bolt",
        3: "3rd bottom right bolt",
        4: "4th mid left bolt",
        5: "5th mid right bolt"
    }

def test_is_fuselage_ready_for_attachment():
    is_ready, reason = fuselage.is_ready_for_attachment()
    assert not is_ready, reason

    fuselage.clean()
    is_ready, reason = fuselage.is_ready_for_attachment()
    assert not is_ready, reason


#  here i want to test that the attachment is ready
#  this requires the attachment to have 5 bolts bolted in to the fuselage.
#  i need to assure that the port wing is attached using exactly 5 bolts
def test_attach_port_wing_to_fuselage():
    port_assembly_wing = fuselage.attach_port_wing_to_fuselage(["bolt1", "bolt2", "bolt3", "bolt4", "bolt5"])
    assert port_assembly_wing, "Wing should be attached using 5 bolt"


def test_attach_starboard_wing_to_fuselage():
    starboard_assembly_wing = fuselage.attach_starbord_wing_to_fuselage(["bolt1", "bolt2", "bolt3", "bolt4", "bolt5"])
    assert starboard_assembly_wing, "Starboard wing is attached using 5 bolts"

# test the attachment to the fuselage was used the star pattern
# the star pattern should beggin wiht the 1st bottom bolt, 2nd top center bolt, 3rd bottom right bolt,
# 4th midleft bolt, 5th mid rigth bolt. In this order

def test_bolt_using_star_pattern():

    star = fuselage.bolt_using_star_pattern(bolt_pattern)
    assert star, "Wings were bolted to fuselage using the star pattern"


# now i need to attach port and starboard wing using the star pattern!
def test_attach_port_and_starboard_wing_to_fuselage_using_the_star_pattern():
    fuselage.bolt_prot_wing_using_star_pattern()