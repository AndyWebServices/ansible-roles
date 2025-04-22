#  Copyright (c) 2025. Andrew M. Zhang All rights reserved.
#  This work is protected by copyright law and international treaties. No part of this work may be copied, reproduced,
#  distributed, transmitted, stored in a retrieval system, or translated into any language, in any form or by any means,
#  without the prior written permission of the copyright holder. Unauthorized use, duplication, or distribution is
#  strictly prohibited and may result in civil and/or criminal penalties. For inquiries regarding licensing, usage,
#  or permissions, please open an issue on this repository: https://github.com/AndyWebServices/ansible-roles/issues

"""Tests for molecule scenarios."""

from __future__ import absolute_import, division, print_function

from pytest_ansible.molecule import MoleculeScenario


def test_integration(molecule_scenario: MoleculeScenario) -> None:
    """Run molecule for each scenario.

    :param molecule_scenario: The molecule scenario object
    """
    print(f'Scenario name: {molecule_scenario.name}')
    proc = molecule_scenario.test()
    assert proc.returncode == 0
