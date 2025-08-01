import sys
import os
import pytest

# Add parent path for import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from device_simulator import FlashDevice

# ---------- BASIC TESTS ----------

def test_write_and_read(flash_device):
    device = FlashDevice(fail_chance=0.0)
    success = flash_device.write(100, "data123")
    assert success is True
    assert flash_device.read(100) == "data123"


def test_erase(flash_device):
    flash_device.write(100, "data123")
    flash_device.erase(100)
    assert flash_device.read(100) is None


@pytest.mark.parametrize("address, data", [
    (1, "A"),
    (42, "hello"),
    (999, "test123"),
])
def test_write_multiple(flash_device, address, data):
    device = FlashDevice(fail_chance=0.0)
    success = flash_device.write(address, data)
    assert success is True
    assert flash_device.read(address) == data


@pytest.mark.parametrize("address, data", [
    ("abc", "valid_data"),    # invalid address
    (123, 999),               # invalid data
    (None, "data"),           # null address
])
def test_invalid_write_inputs(flash_device, address, data):
    device = FlashDevice(fail_chance=0.0)
    with pytest.raises(ValueError):
        flash_device.write(address, data)


def test_read_empty_address(flash_device):
    assert flash_device.read(1234) is None


def test_erase_empty_address(flash_device):
    assert flash_device.erase(9876) is False

# ---------- ADVANCED BEHAVIOR TESTS ----------

def test_max_capacity_limit():
    device = FlashDevice(max_blocks=5)
    success_count = 0
    for i in range(10):
        result = device.write(i, f"data{i}")
        if result:
            success_count += 1
    assert success_count == 5  # Only 5 writes should succeed


def test_random_failures_resilient():
    device = FlashDevice(max_blocks=25, fail_chance=0.1)  # larger capacity
    passed = failed = 0
    for i in range(20):
        result = device.write(i, f"test{i}")
        if result:
            passed += 1
        else:
            failed += 1
    assert passed + failed == 20
    assert passed >= 15  # Should usually pass now


def test_device_busy_flag_simulation(monkeypatch):
    device = FlashDevice()

    # Force device to busy state
    device.busy = True
    result = device.write(0, "should_fail")
    assert result is False

    # Reset busy flag and write again
    device.busy = False
    result = device.write(0, "should_pass")
    assert result is True
