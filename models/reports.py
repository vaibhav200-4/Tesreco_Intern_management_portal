from abc import ABC, abstractmethod

from utils.logger_config import logger


class Report(ABC):
    @abstractmethod
    def generate_report(self):
        pass


class AttendanceReport(Report):
    def __init__(self, records):
        self.records = records

    def generate_report(self):
        report = f"Attendance Report generated for {len(self.records)} records."
        logger.info("Report generation: %s", report)
        return report


class PerformanceReport(Report):
    def __init__(self, intern_name, score):
        self.intern_name = intern_name
        self.score = score

    def generate_report(self):
        report = f"Performance Report for {self.intern_name}: score {self.score}."
        logger.info("Report generation: %s", report)
        return report
