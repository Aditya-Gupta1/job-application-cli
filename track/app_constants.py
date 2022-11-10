from enum import Enum

DATE_FORMAT: str = "%Y-%m-%d"
PRECISION: int = 2


class Status(Enum):
    """Values for Status"""

    APPLIED = "APPLIED"
    OA = "ONLINE_ASSESSMENT"
    TECH_INTERVIEW = "TECH_INTERVIEW"
    HR_ROUND = "HR_ROUND"
    REJECTED = "REJECTED"

    @staticmethod
    def from_string(status: str):
        """Parse the given string to corresponding Enum value"""

        if status.upper() == "APPLIED":
            return Status.APPLIED
        elif status.upper() in [
            "ONLINE_ASSESSMENT",
            "ONLINE ASSESSMENT",
            "OA",
            "ONLINE-ASSESSMENT",
        ]:
            return Status.OA
        elif status.upper() in [
            "TECH_INTERVIEW",
            "TECH INTERVIEW",
            "TECH-INTERVIEW",
            "TECH ROUND",
            "TECH_ROUND",
            "TECH-ROUND",
            "TECH",
        ]:
            return Status.TECH_INTERVIEW
        elif status.upper() in ["HR_ROUND", "HR ROUND", "HR-ROUND"]:
            return Status.HR_ROUND
        elif status.upper() in ["REJECTED"]:
            return Status.REJECTED
        else:
            raise ValueError(f"'{status}' is not a Valid Status")
