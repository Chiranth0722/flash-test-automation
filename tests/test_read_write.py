import sys
import os
import pytest

# Add parent path for import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flash_device.core import FlashDevice

# ---------- BASIC TESTS ----------

def test_write_and_read():
    device = FlashDevice(fail_chance=0.0)
    success = device.write(100, "data123")
    assert success is True
    assert device.read(100) == "data123"


def test_erase():
    device = FlashDevice(fail_chance=0.0)
    device.write(100, "data123")
    device.erase(100)
    assert device.read(100) is None


@pytest.mark.parametrize("address, data", [
    (1, "A"),
    (42, "hello"),
    (999, "test123"),
])
def test_write_multiple(address, data):
    device = FlashDevice(fail_chance=0.0)
    success = device.write(address, data)
    assert success is True
    assert device.read(address) == data


@pytest.mark.parametrize("address, data", [
    ("abc", "valid_data"),    # invalid address
    (123, 999),               # invalid data
    (None, "data"),           # null address
])
def test_invalid_write_inputs(address, data):
    device = FlashDevice(fail_chance=0.0)
    with pytest.raises(ValueError):
        device.write(address, data)


def test_read_empty_address():
    device = FlashDevice(fail_chance=0.0)
    assert device.read(1234) is None


def test_erase_empty_address():
    device = FlashDevice(fail_chance=0.0)
    assert device.erase(9876) is False

# ---------- ADVANCED BEHAVIOR TESTS ----------

def test_max_capacity_limit():
    device = FlashDevice(max_blocks=5, fail_chance=0.0)
    success_count = 0
    for i in range(10):
        result = device.write(i, f"data{i}")
        if result:
            success_count += 1
    assert success_count == 5  # Only 5 writes should succeed


def test_random_failures_resilient():
    device = FlashDevice(max_blocks=25, fail_chance=0.1)  # Allow some failure
    passed = failed = 0
    for i in range(20):
        result = device.write(i, f"test{i}")
        if result:
            passed += 1
        else:
            failed += 1
    assert passed + failed == 20
    assert passed >= 15  # Ensure most writes succeed


def test_device_busy_flag_simulation():
    device = FlashDevice(fail_chance=0.0)

    # Force device to busy state
    device.busy = True
    result = device.write(0, "should_fail")
    assert result is False

    # Reset busy flag and write again
    device.busy = False
    result = device.write(0, "should_pass")
    assert result is True
