import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from device_simulator import FlashDevice

import pytest

@pytest.fixture
def flash_device():
    return FlashDevice()
