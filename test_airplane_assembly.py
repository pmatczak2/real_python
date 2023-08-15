import unittest
from airplane_assembly import Fuselage
fuselage = Fuselage()
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
    success = fuselage.attach_port_wing_to_fuselage(["bolt1", "bolt2", "bolt3", "bolt4", "bolt5"])
    assert success, "Wing should be attached using 5 bolt"



