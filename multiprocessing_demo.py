import multiprocessing

from utils.logger_config import logger


def generate_report(intern_name):
    message = f"Report generated for {intern_name}"
    logger.info("Report generation: %s", message)
    return message


def run_multiprocessing():
    interns = ["Asha", "Rahul", "Meera", "Imran"]
    with multiprocessing.Pool(processes=2) as pool:
        return pool.map(generate_report, interns)


if __name__ == "__main__":
    for result in run_multiprocessing():
        print(result)
