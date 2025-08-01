import logging
import time
import random

logging.basicConfig(
    filename='flash_device.log',
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class FlashDevice:
    def __init__(self, max_blocks=5, fail_chance=0.1):
        self.storage = {}
        self.max_blocks = max_blocks
        self.busy = False
        self.fail_chance = fail_chance
        logging.info("FlashDevice initialized.")


    def simulate_delay(self):
        delay = round(random.uniform(0.1, 0.5), 2)  # 100ms–500ms delay
        logging.info(f"Simulating delay: {delay}s")
        time.sleep(delay)

    def simulate_failure(self):
        if random.random() < self.fail_chance:
            logging.error("Simulated random hardware failure!")
            return True
        return False


    def write(self, address, data):
        self.simulate_delay()
        if self.simulate_failure():
            return False

        if not isinstance(address, int) or not isinstance(data, str):
            logging.error(f"Invalid write attempt: address={address}, data={data}")
            raise ValueError("Invalid address or data")

        if self.busy:
            logging.warning("Write failed: Device is busy.")
            return False

        if len(self.storage) >= self.max_blocks and address not in self.storage:
            logging.warning("Write failed: Flash capacity reached.")
            return False

        self.busy = True
        self.storage[address] = data
        logging.info(f"WRITE: address={address}, data='{data}'")
        self.busy = False
        return True

    def read(self, address):
        self.simulate_delay()
        if address in self.storage:
            data = self.storage[address]
            logging.info(f"READ: address={address}, data='{data}'")
            return data
        else:
            logging.warning(f"READ EMPTY: address={address}")
            return None

    def erase(self, address):
        self.simulate_delay()
        if address in self.storage:
            del self.storage[address]
            logging.info(f"ERASE: address={address}")
            return True
        else:
            logging.warning(f"ERASE FAILED: address={address} not found")
            return False
