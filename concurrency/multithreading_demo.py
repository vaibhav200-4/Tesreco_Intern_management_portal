import threading
import time

from utils.logger_config import logger


def process_attendance():
    time.sleep(1)
    logger.info("Attendance Processing completed")
    print("Attendance Processing completed")


def generate_certificates():
    time.sleep(1)
    logger.info("Certificate Generation completed")
    print("Certificate Generation completed")


def run_threads():
    attendance_thread = threading.Thread(target=process_attendance)
    certificate_thread = threading.Thread(target=generate_certificates)

    attendance_thread.start()
    certificate_thread.start()

    attendance_thread.join()
    certificate_thread.join()

    return "Both threads completed"


if __name__ == "__main__":
    print(run_threads())
