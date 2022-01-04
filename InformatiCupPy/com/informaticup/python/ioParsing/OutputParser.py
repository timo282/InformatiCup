import sys

from InformatiCupPy.com.informaticup.python.objects.Passenger import Passenger
from InformatiCupPy.com.informaticup.python.objects.Train import Train
from InformatiCupPy.com.informaticup.python.algorithms.Errors import CannotSolveInput


class OutputParser:
    @staticmethod
    def parse_output_files(solvers: list, input):
        for solver in solvers:
            try:
                delay_accumulated = solver.solve()
            except CannotSolveInput:
                delay_accumulated = sys.maxsize
            output_str = ""

            # performance rating of the distinct algorithms used
            print(solver.get_name() + " - accumulated delay time: " + str(delay_accumulated))

            for i in solver.get_trains_and_passengers()[0]:
                if isinstance(i, Train):
                    output_str += i.to_output()

            for i in solver.get_trains_and_passengers()[1]:
                if isinstance(i, Passenger):
                    output_str += i.to_output()

            file = open("../input-output/output-" + solver.get_name() + ".txt", "w+")
            file.write(output_str)
            file.close()

    @staticmethod
    def prepare_output_file():
        # just an idea... maybe add general output file syntax here
        output_str = ""
        return output_str
