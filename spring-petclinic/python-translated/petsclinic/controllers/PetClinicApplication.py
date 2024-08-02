from django.core.management import execute_from_command_line
import sys

class PetClinicApplication:
    @staticmethod
    def main():
        execute_from_command_line(sys.argv)

if __name__ == "__main__":
    PetClinicApplication.main()
